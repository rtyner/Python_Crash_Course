pets = []

pet = {
    'name': 'lars',
    'animal_type': 'dog',
    'owner': 'steve',
}
pets.append(pet)

pet = {
    'name': 'petunia',
    'animal_type': 'cat',
    'owner': 'ashley',
}
pets.append(pet)

pet = {
    'name': 'doobie',
    'animal_type': 'bird',
    'owner': 'dave',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))