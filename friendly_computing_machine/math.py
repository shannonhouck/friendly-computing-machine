"""
A small set of functions for doing math operations.
"""


# Write a function named add that adds two values.
def add(a, b):
    """
    Adds two values together.
    Params:
      a (float) - First value to add
      b (float) - Second value to add
    Returns:
      Sum of a and b (float)
    """
    return a+b


# Write a function named mult that multiplies two values.
def mult(a, b):
    """
    Multiplies two values together.
    Params:
      a (float) - First value to multiply
      b (float) - Second value to multiply
    Returns:
      Product of a and b (float)
    """
    return a*b


# Write a function that finds a/b
def div(a, b):
    """ 
    Divides two values.
    Params:
      a (float) - First value to divide
      b (float) - Second value to divide
    Returns:
      Value a divided by b (float)
    """
    return float(a)/float(b)


# Write a function that finds a^b
def pow(a, b):
    """ 
    Finds a^b using recursion.
    Params:
      a (float) - Base
      b (int) - Exponent
    Returns:
      Value of a^b (float)
    """
    if(type(b) != int):
      print("ERROR: pow() not callable with doubles!")
      return 0
    if(b == 0):
      return 1
    else:
      return a * pow(a, b-1)

# Write a function to integrate from limit1 to limit2
def integral(limit1, limit2, function):
    pass

