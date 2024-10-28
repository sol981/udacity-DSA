<!--
Problem 3: Rearrange Array Digits

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
1. To form two numbers such that their sum is maximized, the first step is sort the array.
To satify to condition of time complexity I decided to use merge sort to rearrange digits
2. After I have sorted array pick number from array to have 2 number that their sum is maximized
(Take 2 numbers alternating from the beginning to the end of the array)

## Time complexity
- rearrange_digits(): take O(n)
- mergeSort() take O(nlog(n))
-> time complexity is O(nlog(n)), n is length of array 

## Space complexity
While merging two arrays, we require an auxillary space to temporarily store the merged array, before we plug this partially sorted array into the main array. Hence space complexity of Merge Sort is O(n) - n: length of array 