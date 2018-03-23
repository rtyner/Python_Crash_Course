people = ['albert einstein', 'inigo montoya', 'bugs bunny']
print("Welcome to dinner " + people[0].title())
print("Welcome to dinner " + people[1].title())
print("Welcome to dinner " + people[2].title())
unable = people.pop(0)
print("Unfortunate news, " + unable.title() + " is unable to make it.")
people.insert(0, 'Bart Simpson')
print(
    "Welcome to dinner " + people[0].title() + ", " + people[1].title()
    + ", and " + people[2].title() + "."
    )
