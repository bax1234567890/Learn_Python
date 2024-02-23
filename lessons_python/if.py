# if
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

# else
password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else :
    print('wrong password')


# elif
name  = 'Bob'
age = 30
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice')
elif age > 20:
    print('You are Alice')
elif age > 1:
    print('You are not Alice B')
else :
    print('wrong password')

# if input
print('Enter Name')
name = input()
if name != '':
    print('Your name is ' + name)
else:
    print('You did not enter a name.')


spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1