
## Reasoning Behind Decisions:
- follow instruction on Udacity page
1. encoding: calculate_frequencies -> build_huffman_tree -> generate_huffman_codes
+ calculate_frequencies: go through element then cound time appear
+ build_huffman_tree: 
    - initialize a heap base on frequencies data
    - create a tree by pop 2 node then combine them until the heap remained 1 node.
    - return root node of tree
+ generate_huffman_codes: input huffman_root, data, huffman_code
use dfs to find code for each character (code is the edge so I use dfs), then append code in return string

2. decoding
- traver all decode data, if it's 0 of huffman_tree then go go left otherwise go right

## Time Efficiency:
encoding:
    calculate_frequencies: O(n)
    build_huffman_tree: an interator (n-1): heap push/pop takes O(log n) time -> O(nlog(n))
    generate_huffman_codes: because need use dfs -> O(nlog n)
decoding: O(n)

-> O(nlog(n))
## Space Efficiency:
encoding: O(nlog(n))
decoding: O(n)
