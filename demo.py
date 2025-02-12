def tm(a, c, g, t):
    length = a + c + g + t
    if length <= 13: 
        temp = (a + t) * 2 + (g + c) * 4
        return temp
    else:
        temp = 64.9 + 41 * (g + c - 16.4) / length
        return temp

#(A+T)*2 + (G+C)*4
# 64.9 + 41*(G+C -16.4) ??forgot something here i think 

print('oligo1: ', tm(5, 3, 0, 2))
print('oligo2: ', tm(5, 3, 4, 2))



print(ord('A'))
print(ord('7'))
print(ord(','))
print(ord('>'))


"""
@mysequence
TACGATATCAT
+
A7,>

65 - 33 = 32 ---> 10**-3.2
55 - 33 = 22 ---> 10**-2.2
44 - 33 = 11 ---> 10**-1.1
62

"""
import math 

def symbol_to_prob(c):
    return 0.001

def prob_to_symbol(p):
    return '+' 

print(symbol_to_prob('9'))
print(prob_to_symbol(0.003))

p = 1 * 10 ** -3.2 
print(p)
pqv = -int(math.log10(p) * 10)  
symbol = chr(pqv+33)
print(symbol)


""" 

0.001

1 x 10^3

1e-3

1 * 10 ** -3 

"""


import math 
def dist2pt(x1, y1, x2, y2):
	x_dist = x2 - x1 
	y_dist = y2 - y1
	return math.sqrt(x_dist**2 + y_dist**2)

print(dist2pt(0, 0, 5, 5)) 
