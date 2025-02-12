import random 
import math
countin = 0 
countout = 0

for 1 in range(10): 
    x = random.random()
    y = random.random()
    dist = math.sqrt((x ** 2) + (y ** 2))

    if dist >= 1: countin += 1
    if dist > 1: countout += 1
    print(dist)

pi = (4 * (countin / (countin + countout))) 


import random 
import math 

ins = 0
tot = 0
while True: 
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2) 
        if d <= 1: ins += 1
        else 
for i in range(10): 
        x = random.random()
        y = random.random()
        d = (x**2 + y**2)**0.5
        print(x, y, d)
        if (random.random()**2 + random.random()**2)**0.5 <= 1: ins += 1
        tot += 1
        print(4 * ins/tot)

import random 

n = 10
total = 0 
for i in range(10):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    r3 = random.randint(1, 6)
    total = r1, r2, r3
    print(r1, r2, r3, total)
print(total/n)