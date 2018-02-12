import math

def calculate_percentile_value(percentile, list):
    """Return percentile value

    It uses the nearest-rank method to calculate percentile value
    given a percentile and a list
    """
    list = sorted(list)
    n = len(list)
    ordinal_rank = math.ceil((percentile/100) * n)

    return list[ordinal_rank-1]

list = [15,20,35,40,50]
percentiles = [30]
for p in percentiles:
    print(calculate_percentile_value(p,list))

# list = [3, 6, 7, 8, 8, 10, 13, 15, 16, 20]
# percentiles = [25,50,75,100]
# for p in percentiles:
#     print(calculate_percentile_value(p,list))

# list =  [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
# percentiles = [25,50,75,100]
# for p in percentiles:
#     print(calculate_percentile_value(p,list))


# list = [89,33,104,33,145,59,125,111,33,72]
# percentiles = [30]
# for p in percentiles:
#     print(calculate_percentile_value(p,list))

