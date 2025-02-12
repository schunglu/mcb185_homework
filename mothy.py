import random 

x = random.random()
y = random.random()

print(x, y)

dis = (x ** 2 + y ** 2) ** (0.5)
print(dis)

in_circle = dis <= 1
print(in_circle)

pi_appr = 0
ins = 0
out = 0 

while True: 
    x = random.random()
    y = random.random()
    dis = (x ** 2 + y ** 2) ** (0.5)
    in_circle = dis <= 1 
    if in_circle:
        ins += 1
    else: out += 1
    pi_appr = ins / (ins + out) * 4
    print(x, y, dis, ins, out, pi_appr)
    