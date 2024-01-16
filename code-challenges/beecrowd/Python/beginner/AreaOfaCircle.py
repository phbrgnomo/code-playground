
"""
Calculates the area of a circle based on the given radius.

This function takes the radius of a circle as input, calculates the area using the 
formula A = π * R^2, and returns the result rounded to 4 decimal places.

Args:
    None

Returns:
    None

Examples:
    >>> main()
    2.0
    A=12.5664
"""
def main():
    R = float(input())
    A = round((3.14159 * (R ** 2)), 4)
    A = "{:.4f}".format(A)
    print(f"A={A}",)

main()