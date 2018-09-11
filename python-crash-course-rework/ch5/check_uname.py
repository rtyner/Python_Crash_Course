current_users = ['mike', 'bob', 'sara', 'kelly', 'sam', 'dave']
new_users = ['dale', 'dave', 'kevin', 'cindy', 'kate']

for user in new_users:
    if user in current_users:
        print("Username " + user + " is taken.")
    else:
        print("Username " + user +  " is available.")