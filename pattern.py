
# Program to output a specific pattern using an if-else statement in combination with a single for loop.

# Define the maximum height of the pattern.
max_height = 5

# Use a single for loop to generate the pattern.
for i in range(1, max_height * 2):
    # Determine the number of stars to print.
    # For the first part (increasing stars), print 'i' stars.
    # For the second part (decreasing stars), print '2*max_height - i' stars.
    if i <= max_height:
        stars = i
    else:
        stars = 2 * max_height - i
    
    # Print the stars for the current line.
    print('*' * stars)
