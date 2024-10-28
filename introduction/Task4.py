"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

texts = []
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    marketer = []

    for row in calls:
        check = True
        for text in texts:
            if row[0] == text[0] or row[0] == text[1]:
                check = False

        for item in calls:
            if row[0] == item[1]:
                check = False

        if check == True:
            marketer.append(row[0])
    
    mylist = list(dict.fromkeys(marketer))

    print("These numbers could be telemarketers: ")
    for item in sorted(mylist):
        print(item)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

