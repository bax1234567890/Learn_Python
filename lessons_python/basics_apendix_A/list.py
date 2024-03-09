# Index - single value
# Slice - list of values


spam = [['cat', 'rat', 'dog'], [33, 44, 67, 76, 99]]
spam[0][2] # 'dog'

spamt = ['cat', 'rat', 'dog']
spamt[-2] # 'rat'

"""
spam = ['cat', 'rat', 'dog']
'This is ' + spam[0] + ' it love to catch ' + spam[-2]
# 'This is cat it love to catch rat'
"""

spam = ['cat', 'rat', 'dog', 'pinguin', 'duck']
spam[1:3]
#['rat', 'dog']

# Assign new value to SPAM Index
spam = ['cat', 'rat', 'dog', 'pinguin', 'duck']
spam[1] = 'hamster'
print('This is ' + spam[0] + ' it love to catch ' + spam[-4])
# 'This is cat it love to catch hamster'

# Assign new value to SPAM Slice
spam = [10, 20, 30]
spam[1:3] = ['Cat', 'Dog', 'Fox']
# [10, 'Cat', 'Dog', 'Fox']

# Slice short
spam = ['car', 'boat', 'plane', 'drone']
spam[:2]
# From 0 to index 2 -> ['car', 'boat']

# Slice short
spam = ['car', 'boat', 'plane', 'drone']
spam[1:]
# From 1 to last index -> ['boat', 'plane', 'drone']

# Delete value from the list
spam = ['car', 'boat', 'plane', 'drone']
del spam[2]
# Index 2 'plane' is deleted -> ['car', 'boat', 'drone']