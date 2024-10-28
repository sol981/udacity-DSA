"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def getPrefix(str):
    ret = ""
    if str[0] == '(':
        i = 0
        while str[i] != ')':
            ret += str[i]
            i+=1
        ret += ')'
           
    else:
        if str[0:3] == '140': # marketer start 140
          ret = '140'
        else: # mobile start 7,8,9 
          for i in range(4):
             ret += str[i] 
    return ret

with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    lst = []
    count = 0
    for row in calls:
        if row[0][0:5] == "(080)":
          # get prefix of number (row[10] then add to list 
          lst.append(getPrefix(row[1]))
          if row[1][0:5] == "(080)":
            count+=1

    mylist = list(dict.fromkeys(lst))
    print("The numbers called by people in Bangalore have codes:")
    for item in sorted(mylist):
       print(item)
    
    print(str(round(count * 100 / len(lst), 2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
