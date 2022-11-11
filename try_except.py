# try block
try:
    # getting input from user
    user_input = int(input('Enter a Numeric Value: '))
    print(user_input)

# except block
except ValueError:
    print('Invalid Input. You must enter a numeric value.')
