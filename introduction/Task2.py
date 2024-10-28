"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

phone_dict = {}

with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    for row in calls:
        phone_dict[row[0]] = phone_dict.get(row[0], 0) + int(row[3])
        phone_dict[row[1]] = phone_dict.get(row[1], 0) + int(row[3])

    number = max(phone_dict, key = lambda k: phone_dict[k])

    print(str(number) + " spent the longest time, " +  str(phone_dict[number]) + " seconds, on the phone during September 2016")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

