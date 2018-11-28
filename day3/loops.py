magicians = ['merlin', 'morgana', 'gaius']

for magician in magicians:
    print(magician)

for val in range(1, 5, 2):
    print(val)

even_numbers = list(range(0, 5, 2))

print(even_numbers)

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))

print(max(digits))

print(sum(digits))

cubes = [val**3 for val in range(1, 11)]

print(cubes)

print('First two magicians')
for magician in magicians[:2]:
    print(magician)
