<!--
Problem 5: Autocomplete with Tries

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
Trie:
TrieNode:
- define attribute dict children and a varible check is word or not
- insert(): if the char does not exist then insert it into trie with new Node
- suffix(): the idea is use Recursive function, when find a word from that node then append the return list - this call BFS.
Trie:
- constructor create a root node TrieNode
- insert(): with each character of word call TrieNode.insert(), then mark is a word by word atrribute
- find(): go through the trie from root, just go near the end of node. Check last element is prefix and return its children.

## Time complexity
TrieNode.insert(): O(1)
TriNode.suffix(): O(m*n) : m is number word, n is number of charater each word
trie.insert(): O(n): n is number of charater each word
trie.find(): O(n): n is number of charater each word
-> time complexity is O(m * n)
m is number word, n is number of charater each word

## Space complexity
O(m*n)
n is the total number of characters in all the words stored in the Trie.
m is the maximum length of a word in the Trie.