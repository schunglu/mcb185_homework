# 10demo.py by schunglu

import math 

print('hello, again') # greeting
print(1.5e-2)
print(1 + 1)
print(6 / 3)
print(math.pow(7, 9))
print(math.sqrt(4))
print(4 ** 9)


a = 3       # assign a the value 3
b = 4       # assign b the value 4   
c = (a**2 + b**2) ** 0.5  # pythagoras

print(type(a), type(b), type(c)) 

c = math.sqrt(a**2 + b**2)
print(c)


def rectangle_area(w, h):
    return w * h 
print(rectangle_area(2, 5))

def triangle_area(w, h):
    return rectangle_area(w, h) / 2
print(triangle_area(10, 20))