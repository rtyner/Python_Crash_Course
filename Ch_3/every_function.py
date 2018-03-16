# functions to be used:
# del 
# sort
# sorted
# reverse
# len
# title
# append
# insert
# X pop
# remove
# X place in list - ex - var_name[-1]
distro = ['ubuntu', 'red hat', 'centos', 'debian', 'arch', 
    'fedora', 'gentoo', 'antergos', 'kali', 'mint', 'backtrack']
print(distro)
print(
    "Some of the Linux distros I have used are: " + distro[0].title() + ", " + distro[1].title() + ", " 
    + distro[2].title() + ", " + distro[3].title() + ", " + distro[4].title() + ", " + distro[5].title() + ", " 
    + distro[6].title() + ", " + distro[7].title() + ", " + distro[8].title() + ", " + distro[9].title() + ", and " 
    + distro[10].title() + "."
    )

distro.pop(2).title()
distro.pop(1).title()
distro.pop(4).title()
distro.pop(5).title()

# I need to figure out a way to extract the values from the list, and be able to apply the title function to them.
print("Some of my favorites are: " + distro.pop(1).title() + ", " + distro.pop(1).title() + ", " 
    + distro.pop(2).title() + ", and " + distro.pop(1).title() + ".") 
distro.append('hannah montana linux')
# get this into the print statement
print(distro[-1])
print("I seem to have forgotten about the most important distro of all; " + ".")