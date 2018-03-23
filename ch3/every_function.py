# functions to be used:
# del
# sort
# sorted
# reverse
# len
# title
# append
# insert
# pop
# remove
# place in list - ex - var_name[-1]

# list of distros to be used throughout the exercise.
distro = [
    'ubuntu', 'red hat', 'centos', 'debian', 'arch',
    'fedora', 'gentoo', 'antergos', 'kali', 'mint', 'backtrack'
    ]
print(distro)

# crudely parse through the list and print the distros individually.
print(
    "Some of the Linux distros I have used are: "
    + distro[0].title() + ", " + distro[1].title() + ", "
    + distro[2].title() + ", " + distro[3].title() + ", "
    + distro[4].title() + ", " + distro[5].title() + ", "
    + distro[6].title() + ", " + distro[7].title() + ", "
    + distro[8].title() + ", " + distro[9].title() + ", and "
    + distro[10].title() + "."
    )

# pop out the items to be used below.
distro.pop(2).title()
distro.pop(1).title()
distro.pop(4).title()
distro.pop(5).title()

print(
    "Some of my favorites are: " + distro.pop(1).title() + ", "
    + distro.pop(1).title() + ", " + distro.pop(2).title() + ", and "
    + distro.pop(1).title() + "."
    )

# add and item to the end of the list.
distro.append('hannah montana linux')

# call the last distro in the list and print it.
print(
    "I seem to have forgotten about the most important distro of all: "
    + distro[-1].title() + "."
    )
print(
    "Let's just remove that actually."
    )

# delete the last distro in the list.
del distro[-1]
print(
    "Ok, with that gone, the distros left are: " + ', '.join(distro).title()
    )

print(
    "In alphabetical order: " + ', '.join(sorted(distro)).title()
    )
print(distro)

# sort list permanently.
distro.sort()
print(distro)

# sort list in reverse alphabetical order.
distro.reverse()
print(distro)

# insert and item into the list.
distro.insert(0, 'void')
print(distro)

# resort list to alphabetical order
distro.sort()
print(distro)

# determine length of list
print(
    "As it sits now, out list is "
    + str(len(distro)) + " characters long."
)
print(
    "Let's remove a deprecated distro."
)
distro.remove('backtrack')
print(distro)
