"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array that has been rotated at a random min_index point. 
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

You are also given a target value to search for. If the target is found in the 
array, return its index; otherwise, return -1. Assume there are no duplicates 
in the array, and the runtime complexity of your algorithm must be O(log n).

You should implement the function body according to the rotated_array_search 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""
def binary_search(arr, low, high, num):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_min(arr, low, high):
    while low < high:
        # The current subarray is already sorted, the minimum is at the low index
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        # The right half is not sorted. So the minimum element must be in the right half.
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low

def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
    input_list (list[int]): Input array to search
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    n = len(input_list)
    min_index = find_min(input_list, 0, n - 1)

    # If the minimum element is present at index 0, then the whole array is sorted
    if min_index == 0:
        return binary_search(input_list, 0, n - 1, number)

    # If we found a min_index, then first compare with min_index and then search in two subarrays around min_index
    if input_list[min_index] == number:
        return min_index

    if input_list[0] <= number:
        return binary_search(input_list, 0, min_index - 1, number)
    return binary_search(input_list, min_index + 1, n - 1, number)

# Test function using provided test cases
def test_function(test_case: list[list[int], int]) -> None:
    """
    Test the rotated_array_search function with a given test case.

    Args:
    test_case (list[list[int], int]): A list containing two elements:
        - A list of integers representing the input array to search.
        - An integer representing the target number to find.

    Returns:
    None: Prints "Pass" if the rotated_array_search function returns the same 
    result as the linear_search function, otherwise prints "Fail".
    """
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def linear_search(input_list: list[int], number: int) -> int:
    """
    Perform a linear search for a target number in a list of integers.

    Args:
    input_list (list[int]): The list of integers to search through.
    number (int): The target number to find in the list.

    Returns:
    int: The index of the target number if found, otherwise -1.
    """
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

if __name__ == '__main__':
    # Edge case: Empty input list
    test_function([[], 5])
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected output: Pass

    test_function([[4, 5, 6, 7, 0, 1, 2], 1])

    test_function([[4, 5, 6, 7, 13, 14, 15, 18, 19, 34, 35, 36, 37, 0, 1, 2], 34])
    
    # Normal case: Number in the middle of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected output: Pass

    # Normal case: Number does not exist
    test_function([[4, 5, 6, 7, 0, 1, 2], 66])
    # Expected output: Pass
