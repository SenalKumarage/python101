pizzas = ['bbq', 'pepperoni', 'meat delight', 'cheese pepperoni', 'magarita']

for pizza in pizzas:
    print('I like ' + pizza + ' pizza')

print('Pizza is good.. \nI love pizza!')

# print(sum(range(1, 10000001)))

for n in range(1, 21, 2):
    print(n)

for n in range(1, 11):
    print(n*3)

for n in range(1, 11):
    print(n**3)

cubes = [n**3 for n in range(1, 11)]

print(cubes)

print('The first 3 pizzas are: ')

for p in pizzas[:3]:
    print(p)

print('Three items from the pizzas are: ')

for p in pizzas[1:4]:
    print(p)


print('The last 3 items of pizzas are: ')

for p in pizzas[-3:]:
    print(p)

friends_pizzas = pizzas[:]

pizzas.append('Vegitable spice')

friends_pizzas.append('Sausage delight')


