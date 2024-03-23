
# Ask the user to enter a sentence.
str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip.
print(f"The length of the sentence is: {len(str_manip)}")

# Find the last letter in str_manip and replace every occurrence of this letter with '@'.
last_letter = str_manip[-1]
str_manip_replaced = str_manip.replace(last_letter, '@')
print(f"Modified sentence: {str_manip_replaced}")

# Print the last three characters in str_manip backwards.
print(f"Last three characters backwards: {str_manip[-3:][::-1]}")

# Create a five-letter word made up of the first three and last two characters in str_manip.
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"Five-letter word: {five_letter_word}")
