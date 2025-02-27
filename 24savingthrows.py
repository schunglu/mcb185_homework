import random

def savingthrows(dc, mode):
    if mode == "Normal":
        roll = random.randint(1, 20)
    elif mode == "Advantage":
        roll = max(random.randint(1, 20), random.randint(1, 20))
    elif mode == "Disadvantage":
        roll = min(random.randint(1, 20), random.randint(1, 20))

    if roll >= dc:
        print("Success!")
    else: 
        print("Fail")


"""
           Normal   |   Advantage   | Disadvantage   
DC of 5:    80%            96%             64%
DC of 10:   55%           79.75%          30.25%
DC of 15:   30%            51%             9%
"""
