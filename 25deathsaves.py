import random 

times = 10000 
revive = 0 
death = 0 
stable = 0 

for i in range(times): 
    success = 0
    failure = 0
    for turn in range(6):
        roll = random.randint(1, 20)

        if roll == 1:
            failure += 2
        elif roll == 20:
            revive += 1 
            break
        elif roll >= 10:
            success += 1
        else:
            failure += 1
        
        if success >= 3:
            stable += 1
            break
        elif failure >= 3:
            death += 1
            break

print("probability of revive", revive/times)
print("probability of death", death/times)
print("probability of stable", stable/times)

"""
Probability that one dies: 40.5%
Probability that one is stable: 41.5%
Probability that one revives: 18.5%
"""