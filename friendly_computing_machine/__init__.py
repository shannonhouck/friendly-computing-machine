"""
This is the base file of the friendly computing machine!
Initializes everything.
"""

# imports all things in math
# we can call functions as fcm.math.fn()
from . import math

# imports mult so we don't have to type fcm.math.mult() each time
# we can just call it as fcm.mult() now!!
from .math import mult

# imports EVERYTHING in .math as above
from .math import *

