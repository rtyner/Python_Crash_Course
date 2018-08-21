# functions to be used:
# del-
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

distros = ['gentoo', 'arch', 'centos', 'debian', 'void', 'kali', 'backtrack']

print("The following is a list of Linux distributions")
print(distros)

print("Some of the Linux distros I have used are " + distros[0].title() + ", " + distros[1].title() + ", " + distros[2].title() + ", " +
    distros[3].title() + ", " + distros[4].title() + distros[5].title() + ", and " + distros[6].title() + ".")

print("In alphabetical order that list would be " + str(sorted(distros)))

del distros[-1]
print(distros)

distros.sort()
print(distros)
distros.sort(reverse=True)
print(distros)

print("The length of the list is " + str(len(distros)) + " items.")
