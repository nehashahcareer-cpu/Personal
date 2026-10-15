# Approach 1: Frequency dictionary
# This approach counts each number and adds it to the result when its frequency reaches exactly 2. This ensures each duplicate appears only once in the output.

def find_duplicates(nums):
    """
    Find all duplicate numbers using a frequency dictionary.

    A number is considered a duplicate if it appears more than once.
    Each duplicate is returned only once.

    Args:
        nums (list[int]): A list of positive, negative, or zero integers.

    Returns:
        list[int]: A list of unique duplicate numbers.

    Time Complexity:
        O(n), where n is the length of nums.
        Each number is processed once with average O(1) dictionary operations.

    Auxiliary Space Complexity:
        O(n), for the frequency dictionary and result list.
    """

    # Step 1: Create a dictionary to count occurrences.
    counts = {}

    # Step 2: Store duplicate numbers found.
    result = []

    # Step 3: Iterate through each number.
    for num in nums:

        # Step 4: Increase the number's frequency.
        counts[num] = counts.get(num, 0) + 1

        # Step 5: Add the number only when its count reaches 2.
        if counts[num] == 2:
            result.append(num)

    # Step 6: Return all unique duplicate numbers.
    return result


if __name__ == "__main__":
    # Test 1: Every number appears twice.
    assert find_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]

    # Test 2: Positive and negative duplicates.
    assert find_duplicates([1, -1, 2, 3, 3, -1]) == [-1, 3]

    # Test 3: No duplicates.
    assert find_duplicates([1, 2, 3, 4, 5]) == []

    # Test 4: A number appears more than twice.
    assert find_duplicates([1, 1, 1, 2, 2]) == [1, 2]

    # Test 5: Empty list.
    assert find_duplicates([]) == []

    print("All tests passed!")


# Approach 2: Two sets
# This approach uses one set to track previously seen numbers and another set to track which duplicates have already been collected.

def find_duplicates(nums):
    """
    Find all duplicate numbers using sets.

    A number is considered a duplicate if it appears more than once.
    Each duplicate is returned only once.

    Args:
        nums (list[int]): A list of positive, negative, or zero integers.

    Returns:
        list[int]: A list of unique duplicate numbers.

    Time Complexity:
        O(n) expected, where n is the length of nums.
        Set membership and insertion take average O(1) time.

    Auxiliary Space Complexity:
        O(n), for the seen set, duplicates set, and result list.
    """

    # Step 1: Track all numbers encountered.
    seen = set()

    # Step 2: Track duplicate numbers already collected.
    duplicates = set()

    # Step 3: Store duplicate numbers in the output list.
    result = []

    # Step 4: Iterate through each number.
    for num in nums:

        # Step 5: Check whether this number has appeared before.
        if num in seen:

            # Step 6: Add it only if it has not been recorded as a duplicate.
            if num not in duplicates:
                result.append(num)
                duplicates.add(num)

        # Step 7: Record the number the first time it is encountered.
        else:
            seen.add(num)

    # Step 8: Return the unique duplicates.
    return result


if __name__ == "__main__":
    # Test 1: Every number appears twice.
    assert find_duplicates([1, 2, 3, 1, 2, 3]) == [1, 2, 3]

    # Test 2: Positive and negative duplicates.
    assert find_duplicates([1, -1, 2, 3, 3, -1]) == [-1, 3]

    # Test 3: No duplicates.
    assert find_duplicates([1, 2, 3, 4, 5]) == []

    # Test 4: A number appears more than twice.
    assert find_duplicates([1, 1, 1, 2, 2]) == [1, 2]

    # Test 5: Empty list.
    assert find_duplicates([]) == []

    print("All tests passed!")

