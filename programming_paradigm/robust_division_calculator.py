def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for:
    - Non-numeric inputs
    - Division by zero
    """

    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
