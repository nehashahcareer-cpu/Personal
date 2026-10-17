
"""
Search in Rotated Sorted Array
==============================

Problem:
    Given an ascending sorted array rotated at an unknown pivot,
    return the index of target if it exists; otherwise, return -1.

Approach:
    Modified Binary Search

    1. Initialize left and right pointers.
    2. Calculate the middle index.
    3. If the middle element equals the target, return its index.
    4. Determine which half of the array is sorted.
    5. Check whether the target belongs to the sorted half.
       - If yes, continue searching that half.
       - Otherwise, search the other half.
    6. If the search space becomes empty, return -1.

Key Insight:
    With no duplicate elements, at least one half of the
    current search interval is always sorted.

Time Complexity:
    O(log n) - The search space is halved in each iteration.

Auxiliary Space Complexity:
    O(1) - Only a constant number of variables are used.

Assumption:
    The input contains distinct integers.
"""


def target_value_search(rotated_input: list[int], target_value: int) -> int:
    """
    Find a target in a rotated sorted array using binary search.

    Args:
        rotated_input: A rotated ascending array with no duplicates.
        target_value: The value to search for.

    Returns:
        The target's index if found; otherwise, -1.

    Time Complexity:
        O(log n)

    Auxiliary Space Complexity:
        O(1)
    """
    left = 0
    right = len(rotated_input) - 1

    while left <= right:
        # Find the middle index of the current search range.
        mid = (left + right) // 2

        # Return immediately if the target is found.
        if rotated_input[mid] == target_value:
            return mid

        # Case 1: The left half is sorted.
        if rotated_input[left] <= rotated_input[mid]:

            # Check whether the target lies within the sorted left half.
            if rotated_input[left] <= target_value < rotated_input[mid]:
                right = mid - 1
            else:
                # Target must be in the right half.
                left = mid + 1

        # Case 2: The right half is sorted.
        else:

            # Check whether the target lies within the sorted right half.
            if rotated_input[mid] < target_value <= rotated_input[right]:
                left = mid + 1
            else:
                # Target must be in the left half.
                right = mid - 1

    # Target was not found.
    return -1


if __name__ == "__main__":
    # Target exists.
    assert target_value_search([4, 5, 6, 7, 0, 1, 2], 6) == 2

    # Target does not exist.
    assert target_value_search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # Rotation occurs earlier in the array.
    assert target_value_search([6, 7, 0, 1, 2, 4, 5], 2) == 4

    # Single-element arrays.
    assert target_value_search([1], 1) == 0
    assert target_value_search([1], 0) == -1

    # Empty array.
    assert target_value_search([], 5) == -1

    print("All test cases passed!")
