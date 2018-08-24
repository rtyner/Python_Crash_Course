guests = ['bob', 'mike', 'carl']

for guest in guests:
    print("Welcome to dinner " + guest.title())

print("Looks like " + guests[-1].title() + " can't make it.")

del guests[-1]

guests.insert(-1, 'david')

for guest in guests:
    print("Welcome to dinner " + guest.title())

print("We just found a bigger table, three more guests wull be joinig us.")

guests.insert(0, 'frank')
guests.append('nancy')
guests.insert(2, 'yasin')

for guest in guests:
    print("Welcome to dinner " + guest.title())

print("Only two people can come to dinner")

print("Sorry " + guests.pop(0) + " no dinner for you")
guests.pop(1)
guests.pop(-1)
guests.pop(-2)
print(guests)

del guests[0]
del guests[-1]

print(len(guests))