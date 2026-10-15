
def missing_number(nums):
    """
    Find the missing number in an array containing distinct integers
    from 0 to n, with exactly one number missing.

    Args:
        nums (list[int]): List of integers from 0 to n with one missing.

    Returns:
        int: The missing number.

    Time Complexity: O(n)
        We iterate through the array once using sum(nums).

    Auxiliary Space Complexity: O(1)
        We use a fixed number of variables and no additional
        data structures that grow with the input size.
    """

    # The array contains n elements.
    # Therefore, the complete range should be from 0 to n.
    n = len(nums)

    # Calculate the expected sum of all integers from 0 to n.
    # Formula: n * (n + 1) / 2
    # Use // to get an integer result in Python.
    expected_sum = n * (n + 1) // 2

    # Calculate the sum of all numbers present in the array.
    # This operation takes O(n) time.
    actual_sum = sum(nums)

    # Subtract the actual sum from the expected sum.
    # The difference is the missing number.
    return expected_sum - actual_sum


if __name__ == "__main__":

    # Test case 1: A number in the middle is missing.
    nums = [0, 1, 2, 4, 5]
    print(missing_number(nums))  # Expected output: 3

    # Test case 2: The largest number n is missing.
    nums = [0, 1, 2, 3]
    print(missing_number(nums))  # Expected output: 4

    # Test case 3: Zero is missing.
    nums = [1, 2, 3, 4]
    print(missing_number(nums))  # Expected output: 0



# First approach it also have O(n) 
# def missing_number(nums):
#     num_set = set(nums)
#     n = len(nums) + 1
#     for number in range(n):
#         if number not in num_set:
#             return number  
