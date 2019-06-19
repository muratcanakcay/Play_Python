"""
Convert to Binary.

This bit of code converts a decimal to binary
using a recursive function
"""


def convertToBinary(n):
    """Print binary number for the input decimal using recursion."""
    if n > 1:
        convertToBinary(n//2)
        print(n % 2, end='')
