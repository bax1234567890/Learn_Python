import copy
# https://www.youtube.com/watch?v=_AEJHKGk9ns
# list - mutable - can add, delete, move data
# string - immutable - can not be changed

"""
To recap:
- Strings can do a lot of the same things lists can do, but strings are immutable.
- Immutable values like strings and tuples cannot be modified "in place"
- Mutable values like lists can be modified in place.
- Variables don't contain lists, they contain references to lists.
- When passing a list argument to a function, you are actually passing a list reference.
- Changes made to a list in a function will affect the list outside the function.
- The \ line continuation character can be used to stretch Python instructions across multiple lines.
"""

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# MUTABLE list - references to the list [1, 2, 3, 4, 5]. We can change it when assign new variable 'Hello'
spam = [1, 2, 3, 4, 5]
cheese = spam
spam [1] = 'Hello'
print(spam)
print(cheese)

def eggs(cheese):
    cheese.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

# Completly separate list. Create a brand new list not just copy the list reference
# import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
# ['A', 42, 'C', 'D']
# ['A', 'B', 'C', 'D']
# spam was not modified


# can create easier to read value
spam = ['apple'
        'orange'
        'babanas'
        'cats']

print('Hello, My name is ' + \
      'Ion')

# ______________________________
"""EXAMPLES FROM YOUTUBE VIDEO"""
# x += y
# class List:
#     def _iadd_(self, other):
#         self.extend(other)
#         return

"""
Assign to X

X = ...
for X in ...
class X(...):
def fn(X):
import X
from ... import X
except ... as X:
with ... as X
"""


nums = [1, 2, 3]
for x in nums:
    x = x * 10
print(nums)

def func(x):
    # print(x)
    return
num = 17
func(num)
print(num)


def append_twice(a_list, val):
    a_list.append(val)
    a_list.append(val)
    return

nums = [1, 2, 3]
append_twice(nums, 7)
print(nums)
# 1, 2, 3, 7, 7


def append_twice_bad(a_list, val):
    a_list = a_list + [val, val]
    return
nums = [1, 2, 3]
append_twice_bad(nums, 7)
print(nums)
# 1, 2, 3


def append_twice_good(alist, val):
    a_list = alist + [val, val]
    return a_list
nums = [1, 2, 3]
nums = append_twice_good(nums, 7)
print(nums)

board = [[0] * 8] * 4
print(board)