# opening file
read_file = open('read_file.txt', 'r')

# checking whether the file is readable
if read_file.readable():
    # splitting all the information from the file
    print(read_file.read())

    # reading individual line from the file
    print(read_file.readline())

    # reading all the information from the file and storing it in an array
    print(read_file.readline())
    print(read_file.readlines()[2])  # reading specific lines of information from an array

    # looping through all the lines of information from the file
    for data in read_file.readlines():
        print(data)

else:
    print('File is not readable')


# closing the file
read_file.close()
