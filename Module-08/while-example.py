# Create the variable for user input
user_input = ''
# Create the list to store the values
user_list = []

while user_input.lower().strip() != 'done':
    if user_input:
        user_list.append(user_input)
    user_input = input('Enter a new value, or done when done: ')

print(user_list)