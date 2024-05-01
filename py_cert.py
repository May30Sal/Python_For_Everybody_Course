#! Python Certification Training

#! Modules

# using the import * statement
from math import *
print(cos(10))

# using the value defined in the module and defining an alias for the entity
from math import pi as p
print(p)

# namespace example
import math
x = 75
cos = math.cos(x)
print(cos)

# Defining a different value for a pi variable, overriding the math.pi value
pi = 3.14
print(pi)

