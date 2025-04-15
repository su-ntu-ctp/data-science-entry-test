def find_first_negative(lst):
    """
    Finds the first negative number in a given list using a while loop.
    
    Parameters:
        lst (list): The list of numbers to search through.
    
    Returns:
        int or str: The first negative number if found, otherwise "No negatives".
    """
    # Initialize index for while loop
    index = 0

    # Loop through the list until the end
    while index < len(lst):
        # Check if current element is negative
        if lst[index] < 0:
            return lst[index]  # Return the first negative number
        index += 1  # Move to the next element

    # If no negative number is found
    return "No negatives"
# Test Case 1: List with negatives
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("First negative:", result1)  # Expected: -1

# Test Case 2: List without negatives
result2 = find_first_negative([2, 10, 7, 0])
print("First negative:", result2)  # Expected: "No negatives"
