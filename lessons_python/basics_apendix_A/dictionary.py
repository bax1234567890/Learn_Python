# collection of many key: values
import pprint

"""
To recap:
- Dictionaries contain key-value pairs. Keys are like a list's indexes.
- Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
- Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
- The keys), values), and items) methods will return list-like values of a dictionary's keys, values, and both keys and values, respectively.
- The get() method can return a default value if a key doesn't exist.
- The setdefault) method can set a value if a key doesn't exist.
- The pprint module's pprint) "pretty print" function can display a dictionary value cleanly. The pformat) function returns a string value of this output.
"""


myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

spam = {12345: 'Combination', 42: 'Random numbers'}
print(spam[42])

# Dictionary have no order
eggs = {'name': 'Yukki', 'species': 'Schotish Fold', 'age': '2'}
apple = {'species': 'Schotish Fold', 'name': 'Yukki',  'age': '2'}
eggs == apple
# True

# Dict are mutable like List
list(eggs.keys())
# ['name', 'species', 'age']

list(eggs.values())
# ['Yukki', 'Schotish Fold', '2']

list(eggs.items())
# [('name', 'Yukki'), ('species', 'Schotish Fold'), ('age', '2')]

eggs.keys()
# dict_keys(['name', 'species', 'age'])


for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

# GET
eggs.get('age', 0)
# if key does not exist return 0. If exist return value

picnicItems = {'alpples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic.')
# no naplins in PicnocItems and we return 0


# SET default method - oposite of GET method
if 'colors' not in eggs:
    eggs['color'] = 'black'

eggs.setdefault('color', 'black')


# Character Counting Program Example
message = 'It was a bright cold day in April, and the clocks were sticking thirteen.'
count = {}
for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# print(count)


# PPrint - print in the order
pprint.pprint(count)
