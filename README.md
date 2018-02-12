# Insight Data Engineering - Coding Challenge

This is the solution to the coding challenge for Insight Data Engineering. It reads an input file with individual campaign contributions, determines which ones came from repeat donors, and outputs a file with the following information:

- Total dollars received
- Total number of contributions received
- Donation amount in a given percentage.

Complete instructions of challenge found in this repository: https://github.com/InsightDataScience/donation-analytics	

## Getting Started

File structure is as follows:
./input/itcont.txt <-- input file containing campaign contribution information
./input/percentile.txt <-- file containing percentile to calculate
./output/repeat_donors.txt <-- output file containing information for repeat recipients by zip code and year.
./run.sh <-- run this file to run python script
./src/donation-analytics.py <-- Python code to read input and generate output file.
./insight_testsuite/run_tests.sh <-- run this to run tests on this folder

### Prerequisites

This code was written for Python version 3. Specifically 3.6, but should be able to run in later versions. 

The following libraries are use:

```
from collections import namedtuple
from collections import defaultdict
import logging
import math
import sys
import time
```

### Running it

Input files ./input/itcont.txt and ./input/percentile.txt must be present.

Run the ./run.sh shell command.

The ./run.sh shell command passes three parameters to the Python program: the input file, the percentile file, and the outuput file as follows:

```
python ./src/donation-analytics.py ./input/itcont.txt ./input/percentile.txt ./output/repeat_donors.txt
```

This produces the ./output/repeat_donors.txt file
```
$ tail output/repeat_donors.txt 
C00401224|95136|2017|1|2|2
C00401224|95136|2017|1|3|3
C00401224|95136|2017|1|4|4
C00501197|79831|2017|2400|2400|1
C00501197|78751|2017|1300|1300|1
C00501197|75023|2017|150|150|1
C00501197|75220|2017|500|3200|2
C00501197|78704|2017|200|200|1
C00501197|78704|2017|200|850|2
C00501197|78704|2017|200|2200|3
```

## Running the tests

The ./insight_testsuite contains test_n folders that house the 'input' and 'output' folders and run the Python code.  Each input folder contains the input file, 'itcont.txt' that generates the output file 'repeat_donors.txt'.  If after running the code, the file generates the same file as repead_donors.txt (it has the same number of lines), the test passes, otherwise, the test fails. 

To run the tests, call the ./run_test.sh shell command. Last line will indicate number of tests ran and who many passed.

```
$ cd insights_testsuites
$ ./run_tests.sh
...
[PASS]: test_4 repeat_donors.txt
[Sun Feb 11 09:03:49 CST 2018] 4 of 4 tests passed
```
## Author

* **Ariel Gamiño** - *Initial work* - [PurpleBooth](https://github.com/arielgamino/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
