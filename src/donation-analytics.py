from collections import namedtuple
from collections import defaultdict
import logging
import math
import sys
import time

def print_elapsed_time_up_to_this_point(msg,start):
    """Returns elapsed time from start.
    Returns time from start until now to determine how long
    it took to run a particular piece of code.
    hh:mm:ss - msg
    """

    end = time.time()
    elapsed = end - start
    m, s = divmod(elapsed, 60)
    h, m = divmod(m, 60)
    formatted_elapsed = "%d:%02d:%02d" % (h,m,s)
    return formatted_elapsed+" -- "+msg

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


def calculate_percentile_value(percentile, list):
    """Returns percentile value of list
    It uses the nearest-rank method to calculate percentile value
    given a percentile and a list.
    Example: list = [15,20,35,40,50], percentile= 30
    It returns:
    """
    #List needs to be sorted
    list = sorted(list)
    n = len(list)
    ordinal_rank = math.ceil((percentile/100) * n)

    return list[int(ordinal_rank)-1]

def main(argv):
    start = time.time()
    #set filepaths
    contributions_input_filepath = argv[1]
    percentile_filepath          = argv[2]
    repeatdonors_output_filepath = argv[3]
    # Read percentile number
    percentile = int(open(percentile_filepath).read().strip())

    contribution_counter = 0
    all_input_records    = 0

    results_file = open(repeatdonors_output_filepath, "w")

    #keep track of all donors in this set
    donors = set()
    #keep track of repeat recipients (recipient,zipcode, year) and amounts
    contributions_dict = defaultdict(list)

    #open contributions file and process one line at a time
    with open(contributions_input_filepath) as input_file:
        for line in input_file:
            all_input_records += 1
            contribution = get_valid_fields(line)
            # print(contribution)
            if(contribution is not None):
                contribution_counter += 1
                # results_file.write(line)
                if(contribution.donor_id not in donors):
                    #donor was not found in list, add to set
                    donors.add(contribution.donor_id)
                else:
                    #donor already donated, this is a repeat contributor
                    #create a record_id to keep track of this recipient, zip_code, and year
                    record_id = contribution.cmte_id+"|"+contribution.zip_code+"|"+contribution.transaction_dt_year
                    contributions_dict[record_id].append(float(contribution.transaction_amt))
                    #perform calculations and round up, typecast to int in case is run with Python 3
                    contributions_sum        = round(sum(contributions_dict[record_id]))
                    number_of_contributions  = len(contributions_dict[record_id])
                    contributions_percentile = round(calculate_percentile_value(percentile,contributions_dict[record_id]))
                    #create output_line to used on output file
                    output_line = record_id+"|"+str(contributions_percentile)+"|"+str(contributions_sum)+"|"+str(number_of_contributions)
                    logger.debug(output_line)
                    results_file.write(output_line+"\n")

    results_file.close()
    logger.info("Number of records in input file:{0}".format(all_input_records))
    logger.info("Records in output file: {0}".format(contribution_counter))
    #Display time it took to process
    logger.info(print_elapsed_time_up_to_this_point("Completed Processing contributions",start))

if __name__ == "__main__":
    #Set logger configuration
    logging.basicConfig(level=logging.INFO)
    # Check correct number of arguments were passed
    # use logger to output program information
    logger = logging.getLogger()

    Contribution = namedtuple('Contribution',
                              'cmte_id, name, zip_code, transaction_dt_month, transaction_dt_day, transaction_dt_year, transaction_amt, donor_id')

    if(len(sys.argv)!=4):
        logger.error("Usage: python donation-analytics.py [input file path] [percentile file path] [output file path]")
    else:
        main(sys.argv)