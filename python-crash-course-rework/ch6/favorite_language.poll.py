favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['jen', 'sarah', 'steven', 'mike', 'tony']

for name in people:
    if name in favorite_languages:
        print("Thanks, " + name.title() + " you have already taken the poll")
    else:
        print(name.title() + ", Please take the language poll.")
