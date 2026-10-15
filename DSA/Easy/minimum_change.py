def minimum_change(cents):
    """
    Find the minimum number of coins needed to make the given
    amount of change using coin denominations 1, 5, 10, and 25 cents.

    Args:
        cents (int): The amount of change in cents.

    Returns:
        int: The minimum number of coins required.

    Time Complexity: O(1)
        We process exactly four fixed coin denominations.
        Each iteration uses constant-time division and modulo.

    Auxiliary Space Complexity: O(1)
        We use a fixed-size list of four denominations and a
        constant number of variables.
    """

    # Store coin denominations from largest to smallest.
    coins = [25, 10, 5, 1]

    # Track the total number of coins used.
    min_changes = 0

    # Process each denomination, starting with the largest coin.
    for coin in coins:

        # Calculate how many coins of this denomination fit
        # into the remaining amount and add them to the total.
        min_changes += cents // coin

        # Update cents to the amount remaining after using
        # as many coins of this denomination as possible.
        cents = cents % coin

    # Return the total number of coins needed.
    return min_changes


if __name__ == "__main__":

    # Test case 1: Amount requires multiple denominations.
    print(minimum_change(73))  # Expected output: 7

    # Test case 2: Exact multiple of 25.
    print(minimum_change(50))  # Expected output: 2

    # Test case 3: Amount smaller than the smallest larger coin.
    print(minimum_change(4))   # Expected output: 4

    # Test case 4: Amount is zero.
    print(minimum_change(0))   # Expected output: 0


# First approach: Repeated subtraction.
# Time Complexity: O(C) in the worst case, where C is the amount.
# Auxiliary Space Complexity: O(1).
#
# def minimum_change(cents):
#     coins = [25, 10, 5, 1]
#     min_changes = 0
#     i = 0
#
#     while cents != 0:
#         if cents >= coins[i]:
#             min_changes += 1
#             cents -= coins[i]
#         else:
#             i += 1
#
#     return min_changes
#
# The final approach is more efficient because it calculates
# the number of coins per denomination using // and % instead
# of subtracting one coin at a time.
#
# Note: The greedy approach gives the minimum for these
# specific denominations: 1, 5, 10, and 25 cents.
