pizzas = ['mushroom', 'pepperoni', 'cheese']
friend_pizzas = ['sausage', 'meatball', 'pepper']

for pizza in pizzas:
    print("I like " + pizza + " pizza.") 

pizzas.append('buffalo chicken')
friend_pizzas.append('pineapple')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friends favotite pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza.title())