rivers = {
    'danube': 'germany',
    'nile': 'egypt',
    'tigris': 'iraq'
}

for name, location in rivers.items():
    print("The " + name.title() + " runs through " + location.title())

for name in rivers.keys():
    print(name.title())

for location in rivers.values():
    print(rivers)