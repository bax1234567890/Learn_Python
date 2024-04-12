import re
"""
- The ? says the group matches zero or one times.
- The * says the group matches zero or more times.
- The + says the group matches one or more times.
- The curly braces can match a specific number of times.
- The curly braces with two numbers matches a minimum and maximum number of times.
- Leaving out the first or second number in the curly braces says there is no minimum or maximum.
- Greedy matching match the longest string possible, nongreedy matching match the shortest string possible.
- Putting a question mark after the curly braces makes it do a nongreedy match."""


# Find Batman or Batwoman in the text
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

# Star (*) means zero or more repetetive characters
batRegex = re.compile(r'Bat(wo)*man') # Star *
mo1 = batRegex.search('The Adventures of Batman')
mop1 = mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mop2 = mo2.group()
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
mop3 = mo3.group()
print(mop1 + ', ' + mop2 + ', ' + mop3)


# Plus (+) means one or more time on the character in parenthesis
batRegex = re.compile(r'Bat(wo)+man')
mo4 = batRegex.search('The Adventures of Batwoman')
mop4 = mo4.group()
print(mop4)
mo5 = batRegex.search('The Adventures of Batwowowowowoman')
mop5 = mo5.group()
print(mop5)

# Use special characters +*?
regex = re.compile(r'\+\*\?')
mo6 = regex.search('I learn about +*? regex syntax')
mop6 = mo6.group()
print(mop6)

# Multiple times same characters
haRegex = re.compile(r'(Ha){3}')
mo7 = haRegex.search('He said "HaHaHa" 3 times')
mop7 = mo7.group()
print(mop7)

# Find multiple numbers
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') #? mean zero or 1 time
mo8 = phoneRegex.search('My numbers are 415-333-4456, 345-5423, 123-457-8954')
mop8 = mo8.group()
print(mop8)


digiRegex = re.compile(r'(\d){3,5})') # show biggest possible value "12345"
digiRegex.search('1234567890')

digiRegex = re.compile(r'(\d){3,5}?)') # show smollest possible value "12345"
digiRegex.search('1234567890')
di = digiRegex
print(di)