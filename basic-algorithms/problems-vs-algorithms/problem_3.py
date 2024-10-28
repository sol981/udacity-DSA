"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    sorted = mergeSort(input_list)
    ret = [0, 0]
    even = True 
    for item in reversed(sorted):
        if even:
            ret[0] = ret[0] * 10 + item
            even = False 
        else:
            ret[1] = ret[1] * 10 + item
            even = True 

    return (ret[0], ret[1])

def mergeSort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst 

    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]
    merge_left = mergeSort(left)
    merge_right = mergeSort(right)

    merged_lst = merge(merge_left, merge_right)

    return merged_lst

# merge 2 sorted list
def merge(lst_1: list[int], lst_2: list[int]) -> list[int]:
    lst = []
    i = j = 0

    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            lst.append(lst_1[i])
            i+=1
        else:
            lst.append(lst_2[j])
            j += 1
    
    if i >= len(lst_1):
        lst = lst + lst_2[j:]
    if j >= len(lst_2):
        lst = lst + lst_1[i:]

    return lst

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':

    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    test_function(([3, 2, 1, 4, 5], [542, 31]))  
    test_function(([3, 2, 1, 4, 5], [531, 42]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    test_function(([1, 2, 9, 7, 5], [951, 72]))
