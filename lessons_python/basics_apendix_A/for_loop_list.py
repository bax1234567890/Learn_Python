
spam = list(range(0, 100, 3))
print(spam)
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

for i in range(len(spam)):
    print(spam)

# Walk through the "supplies" take index and show name of the index
# It will work with any length of List
supplies = ['pens', 'staples', 'flame', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# Multiple Assignment
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(size)
print(color)
print(disposition)

# One more example of Multiple Assignment
size, color, disposition = 'skiny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

# Swapping Variables
a = 'AAA'
b = 'BBB'
a, b = b, a
print('A changed to ' + a)
print('B changed to ' + b)

# Swapping Variables one more way
a = 'AAA'
b = 'BBB'
c = a
a = b
b = c
print('A changed to ' + a)
print('B changed to ' + b)


# Augmented Assignment Operators
spam1 = 42
spam1 += 1
print('Add ' + str(spam1))

spam2 = 42
spam2 -= 1
print('Minus ' + str(spam2))

spam3 = 42
spam3 /= 1
print('Devide ' + str(spam3))

spam4 = 43
spam4 %= 2
print('Module 43 % 2 = ' + str(spam4))