# names = ['mike', 'bob', 'carol', 'sarah', 'admin']
names = []

for name in names:
    if name == 'admin':
        print("Hello admin, would you like a status report?")
    else:
        print("Hello " + name + ".")
else:
    print("No users")
