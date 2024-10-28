<!--
Problem 2: Search in a Rotated Sorted Array

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

1) Find the min element and separate list into 2 sorted array

2) Do Binary Search in a Sorted Subarray

If the given key is same as minimum, we return
If min index is 0, then the whole array is sorted, we call binary search for the whole array.
Now how do we decide the subarray in other cases. One simple idea can be to call binary search for both sides. This will keep the overall time complexity as O(Log n) only, but we can save one binary search. The idea is to compare the given key with the first element.

## Time complexity
- avg binary_search(): O(log n). we cacluate mid = low + (high - low) // 2 every time and change value
- avg find_min(): O(log n). similar mid = (low + high) // 2
- rotated_array_search(): 4log(n)
    - 1 find_min()
    - 3 binary_search()
-> Time complexity is O(log n), with n is length of array

## Space complexity
there is no more space for recusion so space complexity is O(1)
