#ENUM
#creating an Enum
from enum import Enum
class Color(Enum):
    red=1
    green=2
    blue=3
print(Color.red)
print(Color(1))
print(Color['red'])
print([c for c in Color])

#iteration
#Enums are iterable
