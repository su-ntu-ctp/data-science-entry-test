def update_dictionary(dct, key, value):
    """
    Updates a dictionary with a new key-value pair.
    - If the key already exists, prints the original value and then updates it.
    - Returns the updated dictionary.
    """
    if key in dct:
        print(f"Original value of '{key}': {dct[key]}")  # Print the original value
    dct[key] = value  # Update or add the key-value pair
    return dct
# Test Case 1: Empty dictionary, adding a new key-value pair
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Expected: {'name': 'Alice'}

# Test Case 2: Dictionary with existing key, updating its value
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)  # Expected: {'age': 26}
