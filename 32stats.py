import sys
import math

numbers = []

for arg in sys.argv[1:]:
    numbers.append(float(arg))

count = len(numbers)
print('number of values:', count)

smallest = numbers[0]
biggest = numbers[0]
for nums in numbers[1:]:
    if nums < smallest: smallest = nums
    if nums > biggest: biggest = nums
print('minimum number:', smallest)
print('maximum number:', biggest)

total = 0
for nums in numbers: 
    total += nums
mean = total / len(numbers)
print('mean: ', mean)

var = 0
for nums in numbers:
    var += (nums - mean)**2
var = var / len(numbers)
print('std:', math.sqrt(var))

numbers.sort()
mid = len(numbers) // 2
n = len(numbers)
if n % 2 == 0:
    median = (numbers[mid - 1] + numbers[mid]) / 2
else:
    median = numbers[mid] 
print('median:', median)

cumulativelength = 0
half = sum(numbers) / 2
n50 = 0
for i in numbers:
    cumulativelength += i
    if cumulativelength >= half:
        n50 = i
        break
print('n50:', n50)
