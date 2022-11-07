# creating lists
names = ['Utsab', 'John', 'Harry', 'Dahal']

# accessing individual item from list
print(names[2])
print(names[-1])
print(names[1:3])

# updating individual item from list
names[2] = 'Sam'
print(names[2])

# creating lists for list function examples
numbers = [1, 5, 2, 6, 8, 10]
peoples = ['Utsab', 'John', 'Harry', 'Dahal', 'Utsab', 'Sam']

# using build-in functions
# allows us to append items/lists to a list, insert, remove items from lists
peoples.extend(numbers)
peoples.append('Robert')
peoples.insert(2, 'Chris')
peoples.remove('Utsab')
peoples.clear()
print(peoples)

# pop an item off of the lists
peoples.pop()
print(peoples)

# checking whether the item is in list or not
print(peoples.index('Utsab'))

# counts specific item in the list
print(peoples.count('Utsab'))

# sorts the list in ascending order/alphabetical order
numbers.sort()
peoples.sort()
print(numbers)
print(peoples)

# reverse the list
numbers.reverse()
print(numbers)

# make a copy of a lists
list_value = peoples.copy()
print(list_value)