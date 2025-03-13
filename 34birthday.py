import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for times in range(trials):
    calendar = [0] * days

    for ppl in range(people):
        birth = random.randint(0, days - 1)
        calendar[birthday] += 1
        if calendar[birthday] > 1:
            matches += 1
            break 

probability = matches / trials
print('probability of at least one shared birthday:', probability)