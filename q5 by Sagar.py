def check_divisibility(num, divisor):
    """
    Checks if num is divisible by divisor.
    - Validates that both num and divisor are numeric (int or float).
    - Returns True if divisible, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Error: Both inputs must be numeric."

    if divisor == 0:
        return "Error: Division by zero is not allowed."

    return num % divisor == 0
# Test Case 1
print(check_divisibility(10, 2))  # Expected: True

# Test Case 2
print(check_divisibility(7, 3))   # Expected: False
