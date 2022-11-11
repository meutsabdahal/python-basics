# creating basic 2D list
number_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# printing a specific element from the array
print(number_list[0][0])

# nested loop
for row in number_list:
    for column in row:
        print(column)