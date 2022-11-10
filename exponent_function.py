# function declaration to power the certain number
def power(base_number, power_number):
    result = 1
    # for loop to multiply the base_number with base_number by power_number times
    for index in range(power_number):
        result = result * base_number

    return result


# calling function
print(power(2, 3))
