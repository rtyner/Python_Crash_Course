players = ['charles', 'matina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())