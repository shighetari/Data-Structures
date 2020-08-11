#Runtime Complexity

commands = ['n', 's', 'w', 'e' ]

selection = input()
# In the worst case, we'd have to iterate over every 
# element in the list to find what we're looking for
# So this is a linear operation
if selection in commands:
    #this is a vlid command
    #perform the user's command

# Constant time
# Constant time doesn't grow at all as the size of the input increases
commands[3] # The size of the input has no bearing on the efficiency of this operation

# Linear time
# Linear runtime grows 1 to 1 as the size of the input increases
for command in commands: # The zie of the input has a direct bearing on the efficiency
    print(command)

# Constant < Linear 

'''' 
What's being compared is how quickly the efficiency 
grows as a result of the input size.
 '''
 
 




