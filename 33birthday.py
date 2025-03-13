import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matches = 0

for times in range(trials):
    birthdays = []

    for ppl in range(people):
        birth = random.randint(0, days - 1)
        if birth in birthdays:
            matches += 1
            break 

        birthdays.append(birth)

probability = matches / trials
print('probability of at least one shared birthday:', probability)