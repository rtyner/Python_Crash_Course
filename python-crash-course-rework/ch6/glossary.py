glossary = {
    'string': 'a simple string of text',
    'int': 'an integer',
    'float': 'a floating point number',
    'dictionary': 'a set of key values',
    'library': 'modules that can be imported to add functionality'
}

for name, text in glossary.items():
    if name in glossary != 'int':
        print("A " + name.title() + " is: " + text)