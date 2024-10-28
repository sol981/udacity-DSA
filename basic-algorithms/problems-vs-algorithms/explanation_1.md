<!--
Problem 1: Square Root of an Integer

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
The idea is we start think value = 1 is answer, try to compare value * value with `number` which need to calculate square,
increase value if the condition is not satisfied. 
however the time complexity is O(n), to improve performance, I think value * value is too small compare with `number`, then can double it and continue recheck. 

## Time complexity
O(log(n)): n is input number we need to get sqrt.

## Space complexity
We need some space for some variables, however those variables are independent with input, so overall space complexity:
O(1)