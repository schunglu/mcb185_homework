import random 

def deathsaves():
    success = 0
    fail = 0

    while success < 3 and failure < 3:
        roll = random.randint(1, 20)

        if roll == 1:
            failure += 2
        elif roll == 20:
            return "Revived"
        elif roll >= 10:
            success += 1
        else:
            failure += 1
        
        if success >= 3:
            return "Stable"
        else:
            return "Dead"

"""
Probability that one dies: 40.5%
Probability that one is stable: 41.5%
Probability that one revives: 18.5%
"""