odd = list(range(1, 21))
print(odd)
for odd in range(1, 21, 2):
    print(odd)

odd = [odd for odd in range(1, 21, 2)]
print(odd)
