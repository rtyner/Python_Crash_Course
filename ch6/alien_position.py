alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_pos']))

# move the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print("New x-position: " + str(alien_0['x_pos']))