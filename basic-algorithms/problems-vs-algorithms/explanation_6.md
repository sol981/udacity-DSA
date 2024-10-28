<!--
Problem 6: Unsorted Integer Array

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
This is a unsorted list of integer, just go through all elements then compare min, max with each element
if max, min still itself, go to next element
otherwise, set max/min again equal the element.
the value of max, min at start is the first element

## Time complexity
go through all elements so time complexity is O(n) - n is length of array.

## Space complexity
No need more auxillary space depent on array so space complexity is O(1)
