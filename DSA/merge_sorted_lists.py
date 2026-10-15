"""
Problem: Merge Two Sorted Lists

Given two sorted lists, merge them into one sorted list
in ascending order.

Example:
Input:  [1, 2, 5], [2, 4, 6]
Output: [1, 2, 2, 4, 5, 6]

Approach:
Use two pointers to compare elements from both lists.
Append the smaller element to the result, then move
the corresponding pointer. Append any remaining elements
after one list is exhausted.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""


def merge_list(list1, list2):
    result = []
    i = 0
    j = 0

    # Compare elements while both lists have elements remaining
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Append any remaining elements
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


# Test the function
if __name__ == "__main__":
    list1 = [1, 2, 5]
    list2 = [2, 4, 6]

    print(merge_list(list1, list2))
    # Expected output: [1, 2, 2, 4, 5, 6]
