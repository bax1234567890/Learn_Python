# append() and insert() List Method

"""
- Methods are functions that are "called on" values.
- The index() list method returns the index of an item in the list.
- The append() list method adds a value to the end of a list.
- The insert() list method adds a value anywhere inside a list.
- The remove() list method removes an item, specified by the value, from a list.
- The sort() list method sorts the items in a list.
- The sort() method's reverse=True keyword argument can sort in reverse order.
- Sorting happens in "ASCII-betical" order. To sort normally, pass key=str. lower.
- These list methods operate on the list "in place", rather than returning a new list value.
"""

# Add new value to List
spam = ['hello', 'I', 'Am', 'Ion']
spam.append('Taya')
print(spam)
# ['hello', 'I', 'Am', 'Ion', 'Taya']

# insert one value in desired index
spam.insert(1, 'chicken')
print(spam)


# delete value
spam = ['hello', 'I', 'Am', 'Ion']
spam.remove('hello')
print(spam)

# remove by index
del spam[0]

# sort values
# spam = [2, 3, 4, 5, 9, 1, ]
spam = ['cat', 'bat', 'dog', 'bird']
spam.sort()
print(spam)

# reverse sorting
spam = ['cat', 'bat', 'dog', 'bird']
spam.sort(reverse=True)
print(spam)

# ASCII-betical order
spam = ['Alice', 'Bob', 'Marta', 'cat', 'chair', 'Jeff', 'apple']
spam.sort(key=str.lower)
print(spam)

