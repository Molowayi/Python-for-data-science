numbers = [4, 7, 24, 42, 37]
print(numbers)

numbers.append(12)
print(numbers)
print(len(numbers))

numbers.insert(2,0)
print(numbers)

while 24 in numbers:
    numbers.remove(24)
removed = numbers.pop(2)
