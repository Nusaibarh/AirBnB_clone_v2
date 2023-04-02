#!/usr/bin/python3
"""Read some Binary Code"""

with open("file.txt") as code:
    bincode = code.readline()

split = bincode.split()
for coded in split:
    intcode = int(coded, 2)
    print(intcode, end=' ')
print()
