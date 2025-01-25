def tm(a, c, g, t):
    total = a + c + g + t 
    if total <= 13:
        tm = (a + t) * 2 + (g + c) * 4
    else: 
        tm = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
    return tm
    
print(tm(5, 7, 3, 4))
