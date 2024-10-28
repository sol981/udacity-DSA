from collections import OrderedDict, deque
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.MAX_SIZE = capacity
        self.lru = {} # key - value
        self.q = deque() # key
        self.size = 0

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key in self.lru:
            self.q.remove(key)
            self.q.append(key)
            return self.lru[key]
        else:
            return -1

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        # key exist then update value
        if key in self.lru:
            self.q.remove(key)
            self.q.append(key)
            self.lru[key] = value
        # if stack is full then check least recently used element in cache then remove
        elif  self.size == self.MAX_SIZE:
            key_ = self.q.popleft()
            self.lru.pop(key_)
            
            # add new element
            self.lru[key] = value
            self.q.append(key)
        # new key-value
        else:
            self.lru[key] = value
            self.q.append(key)
            self.size += 1

if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    print("test 1")
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted
    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values

    # Test Case 2: add same key
    print("Test 2")
    our_cache.set(11, 87)
    our_cache.set(11, 88)
    assert our_cache.get(11) == 88

    # Test Case 3: add None/empty
    print("Test 3")
    our_cache.set(12, None)
    our_cache.set(11, '')
    assert our_cache.get(11) == ''
    assert our_cache.get(12) == None 

    # Test Case 4: Large value
    print("Test 4")
    str = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuururur"
    num = 123333333333333333333333333
    our_cache.set(13, str)
    our_cache.set(15, num)
    assert our_cache.get(13) == str
    assert our_cache.get(15) == num
