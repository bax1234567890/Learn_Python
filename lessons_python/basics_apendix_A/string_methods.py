import pyperclip
# lower case and upper case
"""
isalpha() - letters only
isalnum() - letters and numbers only
isdecimal() - numbers only
isspace() - whiitespace only
isrirle() - titlecase only
startswith() - begin asked value
endswith() - end asked value
join() - concatinate value and add new value
split() - split all strings in words
rjust() - add padding to right of word
ljust() -  add padding to left of word
"""

answer = 'YES'
if answer.lower() == 'yes':
    print('Run again')

# isupper(), islower() -> verify on boolean level if expression is true
spam = 'Hello'
lower = spam.islower()
print(lower)

spam = 'Hello'
upper = spam.isupper()
print(upper)

spam = 'Hello'
upper = spam.upper().isupper() # change value to upper case and verify if it is upper
print(upper)


spam = 'Hello World'
spam[5].isspace() # fith character is space

spam = 'This Is Title Case' # all words starts with uppercase
spam.istitle()

spam = 'hello world'
print(spam.title()) # all words starts with upper case letter

# Start with
print(spam.startswith('hello'))
print(spam.endswith('d'))

# JOIN
animals = ['cats', 'bears', 'bats']
join1 = '\n\n'.join(animals)
join2 = ' '.join(animals)
join3 = ''.join(animals)
join_all = join1 + join2 + join3
print(join_all)

# SPLIT
split = 'Hello, my name is Ion'
split_words = split.split()
print(split_words)

split_by_m = split.split('m')
print((split_by_m))

# RJUST and LJUST and CENTER

split1 = 'Hello1'
split2 = 'Hello2'
split3 = 'Hello3'

split_words = split1.rjust(10)
split_wordsR = split1.rjust(10, '#')
split_wordsL = split2.ljust(10, '-')
split_wordsC = split3.center(20, '=')
print(split_wordsR)
print(split_wordsL)
print(split_wordsC)


example = '    x     '
print_example1 = example.strip()
print_example2 = example.lstrip()
print_example3 = example.rstrip()

print(print_example1)
print(print_example2)
print(print_example3)


spam = 'Hello there!'
replace = spam.replace('e', 'XYZ')
print(replace)


# Pyperclip - copy
# install and import Pyperclip

pyperclip.copy('Hey there') # copy value
paste = pyperclip.paste() # paste value
print(paste)