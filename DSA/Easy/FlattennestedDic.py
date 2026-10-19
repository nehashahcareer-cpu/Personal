
def flatten_config(config, prefix=""):
    """
    Flatten a nested dictionary into dot-separated keys.

    Preserve empty dictionaries as values.

    Args:
        config (dict): The nested dictionary to flatten.
        prefix (str): Prefix for nested keys.

    Returns:
        dict: A flattened dictionary with dot-separated keys.

    Example:
        Input:
            {"config": {"a": {}, "b": {"c": {}}}}

        Output:
            {"config.a": {}, "config.b.c": {}}

    Time Complexity:
        O(n), where n is the total number of dictionary entries.

    Auxiliary Space Complexity:
        O(d), excluding the output dictionary, where d is the
        maximum nesting depth due to recursive function calls.
    """
    result = {}

    for key, value in config.items():
        # Build the key using the existing prefix, if any.
        new_key = f"{prefix}.{key}" if prefix else key

        # Recurse only into non-empty dictionaries.
        if isinstance(value, dict) and value:
            nested_result = flatten_config(value, new_key)
            result.update(nested_result)
        else:
            # Store regular values and empty dictionaries.
            result[new_key] = value

    return result
