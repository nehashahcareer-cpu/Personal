
def rectangle_overlap(a, b):
    """
    Determine whether two axis-aligned rectangles overlap or touch.

    Each rectangle is represented by four (x, y) corner coordinates.
    The corners can be provided in any order.

    Args:
        a (list[tuple[int, int]]): Four corners of rectangle A.
        b (list[tuple[int, int]]): Four corners of rectangle B.

    Returns:
        bool: True if the rectangles overlap or touch;
              False if they are completely separate.

    Time Complexity:
        O(1), because each rectangle has exactly four corners.

    Auxiliary Space Complexity:
        O(1), because only a fixed number of boundary variables are stored.
    """

    # Step 1: Find the boundaries of rectangle A.
    a_left = min(point[0] for point in a)
    a_right = max(point[0] for point in a)
    a_bottom = min(point[1] for point in a)
    a_top = max(point[1] for point in a)

    # Step 2: Find the boundaries of rectangle B.
    b_left = min(point[0] for point in b)
    b_right = max(point[0] for point in b)
    b_bottom = min(point[1] for point in b)
    b_top = max(point[1] for point in b)

    # Step 3: Check whether the rectangles are completely separate.
    # Use OR because any one condition is sufficient.
    if (
        a_right < b_left       # A is left of B
        or a_left > b_right    # A is right of B
        or a_bottom > b_top    # A is above B
        or a_top < b_bottom    # A is below B
    ):
        return False

    # Step 4: If they are not separate, they overlap or touch.
    return True


if __name__ == "__main__":
    # Test 1: Rectangles overlap.
    a = [(-3, 5), (-3, 2), (0, 5), (0, 2)]
    b = [(-1, 4), (3, 4), (3, 1), (-1, 1)]
    assert rectangle_overlap(a, b) is True

    # Test 2: Rectangles are completely separate.
    a = [(0, 4), (0, 2), (2, 4), (2, 2)]
    b = [(3, 4), (3, 2), (5, 4), (5, 2)]
    assert rectangle_overlap(a, b) is False

    # Test 3: Rectangles share an edge.
    a = [(0, 2), (0, 0), (2, 2), (2, 0)]
    b = [(2, 2), (2, 0), (4, 2), (4, 0)]
    assert rectangle_overlap(a, b) is True

    # Test 4: Rectangles share only a corner.
    a = [(0, 2), (0, 0), (2, 2), (2, 0)]
    b = [(2, 0), (2, -2), (4, 0), (4, -2)]
    assert rectangle_overlap(a, b) is True

    print("All tests passed!")



# Interview revision notes
# - Approach: Find each rectangle's left, right, top, and bottom boundaries using min() and max().
# - Key insight: Check whether the rectangles are separated horizontally or vertically.
# - Why or? Any one separation condition means there is no overlap.
# - Why strict comparisons? Using < and > allows edges and corners to touch while still counting as overlap.
# - Time complexity: \(O(1)\), because each rectangle always has four corners.
# - Auxiliary space complexity: \(O(1)\).
# Interview tip: This is a version of the separating axis principle for axis-aligned rectangles. Instead of directly checking whether they overlap, check whether they are separated.
