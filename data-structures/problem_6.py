from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    unique_ = set()
    if llist_1 is not None:
        current1 = llist_1.head
        while current1 is not None:
            unique_.add(current1.value)
            current1 = current1.next

    if llist_2 is not None:
        current2 = llist_2.head
        while current2 is not None:
            unique_.add(current2.value)
            current2 = current2.next
    
    # Create a new linked list to store the union
    llist = LinkedList()
    unique_ = sorted(unique_)
    
    for item in unique_:
        llist.append(item)
    
    return llist
    

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    set1 = set()
    set2 = set()
    if llist_1 is not None:
        current1 = llist_1.head
        while current1 is not None:
            set1.add(current1.value)
            current1 = current1.next

    if llist_2 is not None:
        current2 = llist_2.head
        while current2 is not None:
            set2.add(current2.value)
            current2 = current2.next

    # Find the intersection of both sets
    lst = []
    for item in set1:
        if item in set2:
            lst.append(item)
    lst = sorted(lst)

    # Create a new linked list to store the intersection
    llist = LinkedList()
    for item in lst:
        llist.append(item)
    
    return llist

if __name__ == "__main__":
    ## Test case 1: basic testcase
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2: 2 link list have same element
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_3 = [1, 2, 3, 4, 5, 6, 7, 8, 3]
    element_4 = [1, 2, 3, 4, 5, 6, 7, 8, 3]

    for i in element_3:
        linked_list_3.append(i)

    for i in element_4:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 

    ## Test case 3: 2 empty linklist
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6)) # Expected: empty
    print("Intersection:", intersection(linked_list_5, linked_list_6)) # Expected: empty

    ## Test case 4: check if pass a empty/None ll
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_7 = [1, 2, 3, 4, 5, 6, 7, 8, 3, 9, 10]

    for i in element_7:
        linked_list_7.append(i)

    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8)) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 
    print("Intersection:", intersection(linked_list_7, linked_list_8)) # Expected: empty
    print("Intersection:", intersection(linked_list_8, linked_list_7)) # Expected: empty
    print("Intersection:", intersection(linked_list_8, None)) # Expected: empty
    print("Intersection:", intersection(None, None)) # Expected: empty
    print("Intersection:", intersection(None, linked_list_7)) # Expected: empty
