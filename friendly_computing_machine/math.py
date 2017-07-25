"""
A small set of functions for doing math operations.
"""

# Write a function named add that adds two values.
def add(a, b):
    """
    Adds two values together.
    Params:
      a - First value to add
      b - Second value to add
    Returns:
      Sum of a and b
    """
    return a+b

# Write a function named mult that multiplies two values.
def mult(a, b):
    """
    Multiplies two values together.
    Params:
      a - First value to multiply
      b - Second value to multiply
    Returns:
      Product of a and b
    """
    return a*b

# Write a function that finds a/b
def div(a, b):
    return a/b

# Write a function that finds a^b
def pow(a, b):
    if(type(b) != int):
      print("ERROR: pow() not callable with doubles!")
      return 0
    if(b == 0):
      return 1
    else:
      return a * pow(a, b-1)

