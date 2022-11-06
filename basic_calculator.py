# getting inputs from user
first_number = int(input('Enter a number: '))
second_number = int(input('Enter another number: '))

result = 0
# printing instruction for user
print('Addition: "+"')
print('Subtraction: "-"')
print('Multiplication: "*"')
print('Division: "/"')
operator = input('Please Enter accordingly: ')

# applying conditions
if operator == '+':
    result = first_number + second_number

elif operator == '-':
    result = second_number - first_number

elif operator == '*':
    result = first_number * second_number

elif operator == '/':
    result = second_number / first_number

else:
    print('Please Enter Valid Input!!')

print('Result: ' + str(result))

