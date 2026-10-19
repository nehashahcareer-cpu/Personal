
def flatten_config(config, prefix=""):
    """
    Flatten a nested dictionary into dot-separated keys.

    Empty dictionaries are preserved as values.

    Args:
        config (dict): The nested dictionary to flatten.
        prefix (str): Prefix used to build nested keys.

    Returns:
        dict: A flattened dictionary with dot-separated keys.

    Time Complexity:
        O(n), where n is the total number of dictionary entries.

    Auxiliary Space Complexity:
        O(d), where d is the maximum nesting depth for the
        recursion stack, excluding the output and intermediate
        dictionaries.
    """

    result = {}

    # Step 1: Iterate through each key-value pair.
    for key, value in config.items():

        # Step 2: Build the full key using the current prefix.
        new_key = f"{prefix}.{key}" if prefix else key

        # Step 3: Recurse only into non-empty dictionaries.
        if isinstance(value, dict) and value:
            nested_result = flatten_config(value, new_key)

            # Step 4: Merge the flattened nested dictionary.
            result.update(nested_result)

        else:
            # Step 5: Store leaf values and empty dictionaries.
            result[new_key] = value

    return result


if __name__ == "__main__":
    # Test 1: Basic nested dictionary.
    config = {"a": {"b": 1}, "c": 2}
    assert flatten_config(config) == {"a.b": 1, "c": 2}

    # Test 2: Multiple nesting levels.
    config = {"a": {"b": {"c": 10}}}
    assert flatten_config(config) == {"a.b.c": 10}

    # Test 3: Preserve empty dictionaries.
    config = {"config": {"a": {}, "b": {"c": {}}}}
    assert flatten_config(config) == {
        "config.a": {},
        "config.b.c": {}
    }

    # Test 4: Empty input.
    assert flatten_config({}) == {}

    # Test 5: Non-dictionary values.
    config = {"name": "Alice", "active": True, "count": 5}
    assert flatten_config(config) == {
        "name": "Alice",
        "active": True,
        "count": 5
    }

    print("All tests passed!")


# Interview revision notes
# - Approach: Recursively traverse nested dictionaries and build dot-separated keys.
# - Key insight: Use a prefix to maintain the full path of each nested key.
# - Why recursion? The nesting depth can vary, so the same logic handles every level.
# - Why `isinstance(value, dict) and value`?
#   Recurse into non-empty dictionaries but preserve empty dictionaries as values.
# - Why `result.update()`? Merge the recursively flattened entries into the current result.
# - Time complexity: O(n), where n is the total number of dictionary entries.
# - Auxiliary space complexity: O(d) for the recursion stack, excluding output and intermediate dictionaries.
# - Edge cases: Empty input, empty nested dictionaries, deeply nested dictionaries, and non-dictionary values.
# - Interview tip: Clarify whether empty dictionaries should be preserved and whether lists or keys containing dots require special handling.
