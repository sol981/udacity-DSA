"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_tele_nums = set()

with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    for row in texts:
       unique_tele_nums.add(row[0])
       unique_tele_nums.add(row[1])

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for row in calls:
       unique_tele_nums.add(row[0])
       unique_tele_nums.add(row[1])
    print("There are " + str(len(unique_tele_nums)) + " different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
