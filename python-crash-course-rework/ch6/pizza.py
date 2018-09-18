pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza" + 
    " with the following topppings:")

for topping in pizza['toppings']:
    print("\t" + topping)