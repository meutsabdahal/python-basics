# creating boolean variable
is_cloudy = True
is_sunny = True

# if statement
if is_cloudy and is_sunny:
    print('It might not rain today')
elif is_cloudy and not is_sunny:
    print('It might rain today')
else:
    print("It's clear")


# declaring function
def max_number(num1, num2, num3):
    # comparing three numbers
    if num1 >= num2 and num1 >= 3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# calling function
print(max_number(3, 4, 5))
