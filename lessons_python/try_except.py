def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div42by(2))
print(div42by(3))
print(div42by(0))
print(div42by(1))



print('How many cats do you have?')
number = input()
try:
    if int(number) >= 4:
        print('You have a lot of cats')
    elif int(number) == 0:
        print('You sould adopt a cat')
    elif int(number) <= -1:
        print('Insert positive number')
    else:
        print('You do not have some many cats')

except ValueError:
    print('You did not enter a number')