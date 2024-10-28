
## Reasoning Behind Decisions:
- use stack to solve this problem: we need to go into each group then find user inside it, if it is existed return true
if inside that group exist another group -> extend the stack until traver every groups.

## Time Efficiency:
The time complexity of the provided code snippet is O(n + m), where:

n is the total number of groups in the hierarchy.
m is the maximum number of users in any group.

## Space Efficiency:
O(n)
n is the total number of groups in the hierarchy.