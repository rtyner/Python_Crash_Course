people = ['rocko', 'inigo montoya', 'bugs bunny']
print("Welcome to dinner " + people[0].title())
print("Welcome to dinner " + people[1].title())
print("Welcome to dinner " + people[2].title())
unable = people.pop(0)
print("Unfortunate news, " + unable.title() + " is unable to make it.")
people.insert(0, 'bart simpson')
print("Welcome to dinner " + people[0].title() + ", " + people[1].title() +
    ", and " + people[2].title() + ".")
print("We've procured a larger table, and now have room for more guests.")
people.insert(0, 'daffy duck')
people.insert(2, 'morpheus')
people.append('freddy kruger')
print(people)
print("Welcome to dinner " + people[0].title() + ", " + people[1].title() +
    ", " + people[2].title() + ", " + people[3].title() + ", " + people[4].title() + ", and " + people[5].title() + ".")
print("Looks like we are only able to invite two people to dinner now.")
a = people.pop(0)
b = people.pop(0)
c = people.pop(2)
d = people.pop(2)
print("Sorry " + a.title() + ", " + b.title() + ", " + c.title() + 
    ", and " + d.title() + ". We do not have enough room at the table for you.")
print(people)
print("Hey, " + people[1].title() + " and " + people[0].title() + 
    ", you're the two remaining guests, let's have dinner.")
del people[0]
del people[0]
print(people)