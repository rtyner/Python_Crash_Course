#unames = ['admin', 'alice', 'cindy', 'mike', 'karen']
unames = [] 

if unames:
    for uname in unames:
        if uname == 'admin':
            print("Administrator access granted.")
        else:
            print("Hello " + uname + ".")
else:
    print("Let's add some users.")