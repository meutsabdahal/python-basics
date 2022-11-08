# variables declaration
secret_word = 'tiger'
user_input = ''
no_of_guesses = 0
guess_limit = 5
out_of_limit = False

# while loop
while user_input != secret_word and not out_of_limit:
    # checking whether user has guess limit left or not
    if no_of_guesses < guess_limit:
        user_input = input('Enter your guessed word: ')
        no_of_guesses += 1
    else:
        out_of_limit = True

# if statement for printing result
if out_of_limit:
    print('You Lose!! Please try again')
else:
    print('Congratulations!! You Won')