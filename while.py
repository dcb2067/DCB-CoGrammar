
# Program to calculate the average of numbers entered by the user, excluding -1.

# Initialize variables to store the sum and count of numbers entered.
total = 0
count = 0

# Use a while loop to repeatedly ask the user to enter a number.
while True:
    # Ask the user to enter a number.
    number = input("Enter a number: ")
    
    # Check if the input is '-1'. If so, break the loop.
    if number == '-1':
        break
    
    # Convert the input to a float and add it to the total sum.
    # Also, increment the count of numbers entered.
    try:
        number = float(number)
        total += number
        count += 1
    except ValueError:
        # If the conversion fails, inform the user and continue.
        print("Please enter a valid number.")

# Calculate the average of the numbers entered, excluding -1.
if count > 0:
    average = total / count
    print(f"The average of the entered numbers is: {average}")
else:
    print("No valid numbers were entered.")
