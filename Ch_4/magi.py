magi = ['alice', 'david', 'carolina']

for magi in magi:
    # because both of the lines below are indented
    # each line will be executed for each magi
    print(magi.title() + ", that was a great trick!")
    # \n means newline
    print("I can't wait to see your next trick, " + magi.title() + ".\n")

# since this line isn't indented, it's printed only once
print("Thank you, everyone. That was a great magic show!")
