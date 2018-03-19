squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# this is called list comprehension, combines for loop and creation of elements
squares = [value**2 for value in range(1, 11)]
print(squares)
