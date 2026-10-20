
def first_timestamp_at_or_after(timestamps, target):
    """
    Find the first index where the timestamp is greater than
    or equal to the target.

    Args:
        timestamps: A sorted list of integers in non-decreasing order.
        target: The target timestamp to search for.

    Returns:
        The first index where timestamps[index] >= target.
        Returns len(timestamps) if no such timestamp exists.

    Time Complexity: O(log n)
    Auxiliary Space Complexity: O(1)
    """
    # Step 1: Initialize the search range.
    # right is exclusive, so it can equal len(timestamps).
    left = 0
    right = len(timestamps)

    # Step 2: Continue while candidate positions remain.
    while left < right:
        # Step 3: Find the middle index.
        mid = (left + right) // 2

        # Step 4: If the timestamp is too small,
        # the answer must be to the right of mid.
        if timestamps[mid] < target:
            left = mid + 1
        else:
            # Step 5: mid may be the answer.
            # Search left for an earlier valid index.
            right = mid

    # Step 6: Return the first valid index,
    # or len(timestamps) if no valid timestamp exists.
    return left


if __name__ == "__main__":
    timestamps = [1000, 1004, 1004, 1004, 1019, 1033]

    # Target falls between timestamps.
    assert first_timestamp_at_or_after(timestamps, 1005) == 4

    # Duplicate timestamps: return the first matching index.
    assert first_timestamp_at_or_after(timestamps, 1004) == 1

    # Target matches the final timestamp.
    assert first_timestamp_at_or_after(timestamps, 1033) == 5

    # Target exceeds every timestamp.
    assert first_timestamp_at_or_after(timestamps, 2000) == 6

    # Target is smaller than every timestamp.
    assert first_timestamp_at_or_after(timestamps, 900) == 0

    # Empty input.
    assert first_timestamp_at_or_after([], 1000) == 0

    print("All tests passed!")


# Interview revision notes
#  1. Approach
    #  Use binary search to find the first position where timestamps[index] >= target.
# 2. Key insight
    # - If timestamps[mid] < target, discard the left half, including mid.
    # - Otherwise, mid could be the answer, so keep searching to the left.
    # - Use right = len(timestamps) as an exclusive boundary.
# 3. Why use right = len(timestamps)?
    # The answer might be len(timestamps) when every timestamp is smaller than the target. This boundary also handles an empty list naturally.
# 4. Complexity
    # Complexity	Cost
    # Time	\(O(\log n)\)
    # Auxiliary space	\(O(1)\)
# 5. Common mistakes to remember
    # - Returning mid immediately can miss an earlier duplicate.
    # - Using right = mid - 1 can skip a valid candidate in this particular binary-search pattern.
    # - Returning mid after the loop can fail for empty lists or targets larger than all elements.
    # - A TypeError saying target is missing concerns the function call or platform's test harness, not the binary-search algorithm itself.
# Interview one-liner: “I use lower-bound binary search. When a value is smaller than the target, 
# I move right; otherwise, I preserve that candidate and search left for the first qualifying index. This runs in \(O(\log n)\) time and \(O(1)\) auxiliary space.”
