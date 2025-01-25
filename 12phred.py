import math

def char_to_prob(symbol):
    ascii_val = ord(symbol)
    quality = ascii_val - 33
    return 10 ** (-quality / 10)
 
print(char_to_prob('a'))\

def prob_to_char(prob):
    quality = -10 * math.log10(prob)
    ascii_val = int(round(quality)) + 33
    return chr(ascii_val)

print(prob_to_char(0.001))
