import re
# Not Regular expressions - check if the number is USA format

def isPhoneNumber(text): # 415-555-1234
    if len(text) !=12:
        return False # not phone number-size
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
        if text[3] != '-':
            return  False # missing dash
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False # no first 3 digest
        if text[7] != '-':
            return False # missing last 4 digest
        return True
print(isPhoneNumber('415-555-1234'))

# NoT Regular expression - in the text it find 12 numbers in the and display them

message = 'Call me 414-555-1234 if I am at home and call me 323-456-4321 if I am not at home'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any number.')


# Regular Expression - find first number
# /d - is decimal
# r' - indicate that we use regular expressinos

message1 = 'Call me 414-555-1234 if I am at home and call me 323-456-4321 if I am not at home'

phoneNumberRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex1.search(message1)
print(mo1.group())


# Regular Expression - find all numbers

message1 = 'Call me 414-555-1234 if I am at home and call me 323-456-4321 if I am not at home'

phoneNumberRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex1.findall(message1))


#___________________________________
# Parenthesis have a special mining in regular expression, they mark where group begin and end
# Example 1
phoneNumberGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # when we want to show Parenthesis
phoneNumberGroup.search('My number is 435-345-6789')
mo = phoneNumberGroup.search('My number is 435-345-6789')
group1 = mo.group(1)
group2 = mo.group(2)
print('First group is (' + group1 + '). Second group is (' + group2 + ')')

# Example 2  - parenthesis in searched text using "\"
phoneNumberGroup2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d') #
mo1 = phoneNumberGroup2.search('My number is (415) 435-3455')
group3 = mo1.group()
print('I find number in text with parenthesis' + group3)


# Example 3  - parenthesis in searched text using "|"
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # find any of that sufixies
mo = batRegex.search('Batmobile lost a wheel')
group4 = mo.group()
print('We found (' + group4 + ') in text')


# Example 4  - parenthesis in searched text using or "|" and show first sufix
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
group4 = mo.group(1) # find first sufix
print('We found (' + group4 + ') in text')


# Example 5
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
group4 = mo.group(1) # find first sufix
print('We found (' + group4 + ') in text')




