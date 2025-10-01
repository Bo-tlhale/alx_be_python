def safe_divide(numerator, denominator):
    try:
        the_numerator = float(numerator)
        the_denominator = float(denominator)
        try:
            division_result = the_numerator/the_denominator
            return f"The result of the division is {division_result}"
        except(ZeroDivisionError):
            return f"Error: Cannot divide by zero."
    except(ValueError):
       return f"Error: Please enter numeric values only."
    