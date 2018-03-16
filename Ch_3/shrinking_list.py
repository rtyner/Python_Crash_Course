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