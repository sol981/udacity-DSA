<!--
Problem 7: Request Routing in a Web Server with a Trie

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
- first thing I did that is I understand this problem, this problem is similar with problem 5
- We have node, trie of node and a router class which manage the trie
- follow the instruction I define a node, define attribute for trie, and router class.
- after that I start implement method in router class and test it, when they are all complete I move to implement method in trie.
- except split_path() other methods of router class call trie method so
+ trie.insert(path, handler)
if len(path) == 0: return None
To insert path and handler into a trie, I use a current_node to know where we are, go through all element(diectory) in paths, create a new Node + setup -> end of path: set handler for that node.

+ trie.find(paths)
the idea is with each directory in paths list, check the existen of it.
    - if it it exists -> point to next node until go end of path
    otherwise return None
    - when go to end node of trie, get handler and return it.

## Time complexity
both insert() and find() is O(n): n is lenght of path

## Space complexity
O(n) - n is lenght of path to save n nodes of data.