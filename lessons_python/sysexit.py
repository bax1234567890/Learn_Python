import sys
import pyperclip

"""
- You can import moludes and get access to new functions
- The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool
- The sys.exit() function will immediately quit your program
- The pyperclip third-party module has copy() and paste() functions for reading and writing text to the clipboard
"""

# Copy and paste text
pyperclip.copy("Hello, World!")
text = pyperclip.paste()
print(text)

pyperclip.copy("Hello, World!")
print(pyperclip.paste())


# sys exit function
print('Hello')
sys.exit()


print('Goodbye')