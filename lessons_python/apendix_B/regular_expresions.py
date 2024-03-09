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
