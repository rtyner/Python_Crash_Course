current_users = ['bob', 'mike', 'sara', 'ron', 'carol']
new_users = ['dan', 'steve', 'kayla', 'sara', 'becca']

for uname in current_users:
    if uname in new_users:
        print("The username " + uname + " is not unique.")
else:
    print(new_users[:] )
