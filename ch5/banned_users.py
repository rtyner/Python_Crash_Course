banned_users = ['drew', 'mark', 'cindy']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

banned_users.append('marie')

if user in banned_users:
    print(user.title() + ", GTFO.")
