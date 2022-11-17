# opening file
write_file = open('read_file.txt', 'a')
over_write_file = open('read_file.txt', 'w')

# writing to a file
write_file.write('\nI am enjoying')

# overwriting to a file
over_write_file.write('\nI am enjoying very much')

# closing the file
write_file.close()