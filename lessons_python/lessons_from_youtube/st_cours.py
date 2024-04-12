M = "My"
MyAge = 37
YourAge = 35
print(f'Hello, {M}, World')
print(f'I am older then you in {MyAge - YourAge} years')


# Just unique numbers
numbers = [1,2,3,4,5,6,7,8,9,2,5,3,5,2,3,6,5,4, 234, 323]
unique = {num for num in numbers}
print(unique)

# Float number after multiply
x = 1_000_000
y = 2_000
print(f'{x*y: ,}')


# Compare names - Access Denied
name = 'Chris'
if name in ['Bob' or 'Tom' or'Mike']:
    print('You can enter')
else:
    print('Access Denied')


# Lambda
def two_sum(x, y):
    return x + y
print((lambda x, y: x + y)(1, 2))

# Estimation in American Schools
def estimation(scare):
    if scare >= 90: return  'A'
    if scare >= 80: return  'B'
    if scare >= 70: return  'C'
    if scare >= 60: return  'D'
    if scare >= 50: return  'E'
    return 'F'
print(estimation(93))