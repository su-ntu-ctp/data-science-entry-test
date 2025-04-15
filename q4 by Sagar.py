def string_reverse(s):
    """
    Reverses the given string.
    - Checks if s is a string.
    - Returns the reversed string.
    """
    if not isinstance(s, str):
        return "Error: Input must be a string."
    
    return s[::-1]  # Reverse using slicing




# Test Case 1
result1 = string_reverse("Hello World")
print(result1)  # Expected: "dlroW olleH"

# Test Case 2
result2 = string_reverse("Python")
print(result2)  # Expected: "nohtyP"
