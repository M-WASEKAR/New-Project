"""
Command needs to be executed as
python 2.py filename delimiter quotechar
delimiter and quote_char are optional
"""

import csv
import sys

filepath = sys.argv[1]
try:
    delimiter = sys.argv[2]
except IndexError:
    delimiter = ","
try:
    quote_char = sys.argv[3]
except IndexError:
    quote_char = '"'

# opening the CSV file
with open(filepath) as file:
    cr = csv.reader(file, delimiter=delimiter, quotechar=quote_char)
    for pos, row in enumerate(cr):
        if pos == 0:
            print("Name\t\tDOB(dd-mm-yy)\t\tSalary")
        else:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
