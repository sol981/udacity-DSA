"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""
import math

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """
    if number <= 1:
        return number 
    i = 1
    while i <= number // 2:
        if i * i == number:
            return i
        if i * i < number and (i + 1) * (i + 1) > number:
            return i 
        if i * i < (number // i):
            i *= 2
        else:
            i += 1

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 10 == sqrt(100) else "Fail")  # Expected Output: Pass
    print("Pass" if 10 == sqrt(101) else "Fail")  # Expected Output: Pass
    print("Pass" if 10 == sqrt(120) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(2) else "Fail")  # Expected Output: Pass
    print("Pass" if 1000 == sqrt(1000001) else "Fail")  # Expected Output: Pass
