people = []

person = {
    'first_name': 'trevor',
    'last_name': 'b',
    'age': 27,
    'city': 'lakeland',
}
people.append(person)

person = {
    'first_name': 'dale',
    'last_name': 'waters',
    'age': 31,
    'city': 'orlando'
}
people.append(person)

person = {
    'first_name': 'mark',
    'last_name': 'white',
    'age': 29,
    'city': 'miami',
}
people.append(person)

print(people)

for person in people:
    # name = person['first name'].title() + person['last name'].title()
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", of " + city + ", is " + age + " years old.")