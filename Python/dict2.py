numbers = [1, 2, 2, 3, 1, 2, 4, 3]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)