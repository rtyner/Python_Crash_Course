requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers.")
else:
    print("Adding " + requested_topping +".")