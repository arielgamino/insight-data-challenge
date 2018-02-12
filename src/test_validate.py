from collections import namedtuple

Contribution = namedtuple('Contribution',
                          'cmte_id, name, zip_code, transaction_dt_month, transaction_dt_day, transaction_dt_year, transaction_amt, donor_id')

def get_valid_fields(line):
    """Returns contribution fields.
    Returns None if line provided did not contain needed information
    or was incorrectly formatted.
    Returns nametupled Contribution with fields extracted from line:
    cmte_id, name, zip_code, transaction_dt_month, transaction_dt_day,
    transaction_dt_year, transaction_amt, donor_id
    """

    contribution = None
    #check it's a str in order to split
    if(isinstance(line, str)):
        #split and only return if records are useful
        fields = line.split("|")
        #Confirm there are at least the number of fields needed
        if(len(fields)>16):
            #check if other_id is empty, otherwise ignore
            other_id = fields[15]
            if(not other_id):
                cmte_id  = fields[0]
                #check recipient is not empty
                if(cmte_id):
                    name     = fields[7]
                    #check name is not empty
                    if(name):
                        zip_code = fields[10]
                        #Check length of zip_code and get only first 5 characters
                        if(len(zip_code)>=5):
                            zip_code = zip_code[:5]
                            transaction_dt  = fields[13]
                            #check transaction_dt is valid
                            if(len(transaction_dt)==8):
                                transaction_dt_month = transaction_dt[:2]
                                transaction_dt_day   = transaction_dt[2:4]
                                transaction_dt_year  = transaction_dt[4:]

                                transaction_amt = fields[14]

                                #create donor_id by combining name and zip
                                donor_id = name+'|'+zip_code
                                contribution = Contribution(cmte_id,name,zip_code,transaction_dt_month, transaction_dt_day, transaction_dt_year,transaction_amt, donor_id)

    return contribution

input_str = "C00042366|N|M3|P|201703200200085211|22Y|IND|WALDEN, DANIEL|ELKRKIDGE|MD|21075|||02282017|3||SB03221752117487|1153686|||2033120171392908983"

"""
0 - C00384516|
1 - N
2 - P
3 - 201702039042412112
4 - 15
5 - IND
6 - ABBOTT, JOSEPH
7 - WOONSOCKET
8 - RI
9 - 028956146
10 - CVS HEALTH
11 - EVP, HEAD OF RETAIL OPERATIONS
12 - 0112201
13 - 333|
14 - |
15 - 2017020211435-910
16 - 1147467
17 -
18 -
19 - 4020820171370030287"
"""

# print(get_valid_fields(33))
print(get_valid_fields(input_str))