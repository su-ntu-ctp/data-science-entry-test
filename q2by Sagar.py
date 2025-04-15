def find_and_replace(lst, find_val, replace_val):
    """
    Replaces all occurrences of find_val with replace_val in the list lst.
    Returns the modified list.
    """
    # Check if input is a list
    if not isinstance(lst, list):
        return "Error: First argument must be a list."
    
    # Replace all occurrences
    return [replace_val if item == find_val else item for item in lst]

# Test Case 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  # Expected: [1, 5, 3, 4, 5, 5]

# Test Case 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)  # Expected: ["orange", "banana", "orange"]
