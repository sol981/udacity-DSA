<!--
Problem 4: Dutch National Flag Problem

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
## Reasoning Behind Decisions:
1. Actually I don't know how to do it then search and found this explanation 
https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

2. As I understand I will separate the input_lists into 3 part respective 0,1,2
I use low(on the left side), high(on the right) to know the border between them, and an index when go through the input_lists
With each element, if the number is 0 or 2 move it to left/right, continue do it until we have sorted list.

## Time complexity
Because We need go through all element so the time complexity is
O(n): n is length of array

## Space complexity
No need more auxillary space depent on array so space complexity is
O(1)