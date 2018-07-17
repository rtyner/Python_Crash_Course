guests = ['john', 'mike', 'paul']

for guest in guests:
    print("Welcome to dinner " + guest.title() + ".")

print("Turns out " + guests[1].title() + " can't make it to dinner.")

guests.append('david')
print("We are going to replace " + guests[1].title() + " with " + guests[-1].title())
del guests[1]

for guest in guests:
    print('The final list is: ' + guest.title() + ".")