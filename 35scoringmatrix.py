import sys

nucleotides = sys.argv[1]
matched = sys.argv[2]
mismatched = sys.argv[3]

print('   ', end = '')

for nucleo in nucleotides:
    print(nucleo, end = '  ')
print()

for row in nucleotides:
    print(row, end = ' ')
    for i in nucleotides:
        if i == row:
            print(matched, end = ' ')
        else:
            print(mismatched, end = ' ')
    print()


