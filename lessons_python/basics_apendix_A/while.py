spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1


name = ''
while name != 'Your name':
    print('Please type your name')
    name = input()
# print('Thank you')

# infinit loop, True will never be False.
name = ''
while True:
    print('Please Type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

spam = 0
while spam < 5:
    spam  = spam + 1
    if spam == 3:
        continue
    print('spam is '+ str(spam))