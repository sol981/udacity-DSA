import heapq
from collections import defaultdict
from typing import Optional, List, Dict


# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None 

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        lst = []

        return self.freq < other.freq
    
    
def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    freq_dict = {}
    for i in range(len(data)):
        if data[i] not in freq_dict.keys():
            freq_dict[data[i]] = 1
        else:
            freq_dict[data[i]] += 1
    
    return freq_dict

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    lst = []
   
    for item in frequency.items():
        node = HuffmanNode(item[0], item[1])
        lst.append(node)

    heapq.heapify(lst)
    
    while len(lst) > 1:
        node1 = heapq.heappop(lst)
        node2 = heapq.heappop(lst)
        node = HuffmanNode(None, node1.freq + node2.freq)
        if node1.freq < node2.freq:
            node.left = node1
            node.right = node2
        else:
            node.left = node2
            node.right = node1
        heapq.heappush(lst, node)

    return lst[0]

    
def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    # input rootNode, a string
    # output: dict [{char, bin_code}]
    # dfs - for each character until find it
    def dfs(node: Optional[HuffmanNode], char: str, found: bool, bin_code: str) -> str:
        if node is None:
            return ""

        if node.left is None and node.right is None and node.char == char:
            
            found = True
            return bin_code
        
        elif node.left is None and node.right is None and node.char != char:
            return ""
        else:
            left = dfs(node.left, char, found, bin_code + "0")
            right = dfs(node.right, char, found, bin_code + "1")

        if left:
            return left
        else:
            return right
        
    ret = ""
    for char in code:
        binary_code= ""
        ret += dfs(node, char, False, binary_code)
    huffman_codes[code] = ret
 
def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    freq_dict = calculate_frequencies(data)

    huffman_root = build_huffman_tree(freq_dict)
    huffman_code = {}
    encoded_data = generate_huffman_codes(huffman_root, data, huffman_code)
    return (huffman_code[data], huffman_root)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    current_node = tree
    # go to leaf -> add one more step
    encoded_data += " "
    data = ""
    for i in range(len(encoded_data)):
        if current_node.left is None and current_node.right is None:
            data += current_node.char
            current_node = tree 
        # if char == "1" go to right
        if encoded_data[i] == "1":
            current_node = current_node.right
        # if char == "0" go to left
        elif encoded_data[i] == "0":
            current_node = current_node.left
    return data
# Main Function
if __name__ == "__main__":
    # # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fundddddd            !   "

    print("string: " + sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    print("\nTest Case 2: empty")
    sentence2 = " "

    print("string: " + sentence2)
    encoded_data2, tree2 = huffman_encoding(sentence2)
    print("Encoded:", encoded_data2)
    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    print("Decoded:", decoded_data2)
    assert sentence2 == decoded_data2

    # Test Case 3
    print("\nTest Case 3: large data")
    sentence3 = " jfffffffffff djkdsj jdkd jdkdj  i like google, i like football, ddjkdks jjd; * somethins i dont !@#$%^&*()  know but i want to do it, this is interesting algorithm"

    print("string: " + sentence3)
    encoded_data3, tree3 = huffman_encoding(sentence3)
    print("Encoded:", encoded_data2)
    decoded_data3 = huffman_decoding(encoded_data3, tree3)
    print("Decoded:", decoded_data3)
    assert sentence3 == decoded_data3
