def swap_values(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap the values using tuple unpacking
    x, y = y, x

    # Print the swapped values
    print("Swapped values: x =", x, ", y =", y)

# ✅ Function call — this is what actually runs the code
swap_values(1, 50)
print(swap_values("abc", 20))  # This one will return -1 and print it

def swap_values(x, y):
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap the values using tuple unpacking
    x, y = y, x

    # Print the swapped values
    print("Swapped values: x =", x, ", y =", y)

# Task 2 test cases
print(swap_values("Apple", 10))  # Should return -1 (non-numeric input)
swap_values(9, 17)               # Should print swapped values: x = 17 , y = 9
