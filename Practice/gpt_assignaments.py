import re
def check(a, b):
    if a < b:
        print('A is less than B')
    elif a > b:
        print('B is less than A')
    else:
        print('A and B are equal')

check(12, 120)

# Number Check
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
print(isPhoneNumber('432-555-1234'))


# ZIP CODE Check
def isZipCode(text): # zip code
    if len(text) !=5:
        return False # not zip number-size
    for i in range(0, 5):
        if not text[i].isdecimal():
            return False # no zip code
    return True
print(isZipCode('9120i'))


# REGULAR Expression
Address = 'Find me on this address 345 Alin str. Los Angeles, California, 92344'
addressRegex = re.compile(r'\d\d\d\d\d')
print(addressRegex.findall(Address))


# REGULAR Expression - parenthesis in searched text using or "|" and show first sufix
chairRegex = re.compile(r'\b(Cha\w*)\b', re.IGNORECASE)
matches = chairRegex.findall('Yesterday I asked chatGPT where can I find chairs and it asked what kind of characteristics should it have? ')
if matches:
    for match in matches:
        print('We found (' + match + ') in text')  # Print the entire matching word
    else:
        print('No matches found')


