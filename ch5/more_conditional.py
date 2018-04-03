# testing for equality and inequality w/ strs
isps = ['spectrum', 'frontier', 'comcast']
for isp in isps:
    print(isp.title())

print('comcast' in isps)
print('spectrum' in isps)
print('frontier' in isps)
print('cox' in isps)

# use the lower function
computer = 'Dell' 
print(computer.lower() == 'dell')

# test for equality/inequality using numbers
first = 1
second = 2
third = 3
fourth = 4

print(first == second)
print(first < second)
print(first <= second)
print(first < second and fourth >= third)
print(first < second and fourth <= third or third > second)

# test whether an item is in a list
print("\n")
cars = ['audi', 'mercedes', 'volkswagen', 'tesla']
print('audi' in cars)

if 'tesla' in cars:
    print("Tesla is in this list of cars")

# This is my first ever if else statement
if 'ford' in cars:
    print("Ford is in this list of cars")
else:
    print("Ford is not in this list of cars")

cars.append('Porsche')
print(cars)

if 'porsche' in cars:
    print("Porsche is in this list.")
else:
    print("Porsche is not in this list.")

# just tried this on a whim and it worked!
if 'porsche'.title() in cars:
    print("Porsche is in this list.")

if 'toyota' not in cars:
    print("No Toyotas for you.")