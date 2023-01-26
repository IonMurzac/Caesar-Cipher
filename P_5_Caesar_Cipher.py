# Import all necessary libraries
from multiprocessing.resource_sharer import stop

# List of characters that can be encoded or decoded
CHARACTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "&", " "]

# Get input from user
# Prompt user to enter text to be encoded or decoded
user_text = input("Please enter the text you want to encode or decode: ")
# Prompt user to select option to encode or decode
user_option = input("Please select what you want to do with the entered text, 'encoding = e' or 'decoding = d': ")
# Prompt user to enter shift value
user_shift = int(input("Enter the number of characters with which you want to make the shift: "))

# Add spaces between characters
user_text_with_space = " ".join(user_text)
# Split the text by spaces
split_user_text = user_text_with_space.split(" ", -1)

# Replace empty spaces with actual space character
for each_space in range(len(split_user_text)):
    if split_user_text[each_space] == '':
        split_user_text[each_space] = " "

# List of indexes of each character
each_letter_index_list = []

# Find the index of each character in the CHARACTERS list
for each_letter in split_user_text:
    each_letter_index = CHARACTERS.index(each_letter)
    each_letter_index_list.append(each_letter_index)

# List of modified indexes    
modified_index_list = []

# Modify index based on user's option and shift value
# If the user wants to encode the text
if user_option == "e":
    for index in each_letter_index_list:
        modified_index = index + user_shift
        # If the modified index is within the range of CHARACTERS list
        if modified_index <= 68:
            modified_index_list.append(modified_index)
        # Else, wrap around to the beginning of the list
        else:
            modified_index -= 69
            modified_index_list.append(modified_index)

# If the user wants to decode the text
elif user_option == "d":
    for index in each_letter_index_list:
        modified_index = index - user_shift
        # If the modified index is within the range of CHARACTERS list
        if 0 < modified_index or modified_index <= 68:
            modified_index_list.append(modified_index)
         # Else, wrap around to the end of the list
        elif modified_index < 0:
            modified_index += user_shift
            modified_index_list.append(modified_index)
        else:
            break

# else statement for handling invalid input for user_option        
else:
    print("You did something wrong!")

# Creating a list to store the modified characters
encoding_text_list = []

# Iterating through the modified index list and adding the 
# \corresponding character to the encoding_text_list
for index in modified_index_list:
    encoding_text_list.append(CHARACTERS[index])

# Joining the list of characters to get the final encoded or decoded text
encoding_text = "".join(encoding_text_list)

# Printing the final encoded or decoded text
print(f"Your modified text is : {encoding_text}")
    