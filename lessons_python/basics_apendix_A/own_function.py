"""
    Argument - the value passed  in the functional call
    Parameter - The value inside the function
"""

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello There!')
hello()
hello()
hello()

#________________________

def hello(name):
    print('Hello + ' + name)

hello('Olvia')
hello('Taya')


# RETURN VALUE
def plusOne(number):
    return number + 1
#6

newNumber = plusOne(5)
print(newNumber)

# None VALUE
"""
None
spam = print()
spam == None
"""

# KEYWORD ARGUEMNTS
print('Hello', end='')
print('World')
#HelloWorld

print('python', 'hunt', 'dear', sep='ABC')
#pythonABChuntABCdear