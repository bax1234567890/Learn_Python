import os

# 'folder/folder2/folder3'
os.path.join('folder', 'folder2', 'folder3')

#'/'
os.sep

# current worker directory as a string value
# '/Users/ionbota/PycharmProjects/Learn_Python'
os.getcwd()

#Change current working directory
os.chdir('/')

# Absolute file path - full path from the root
# '/Users/ionbota/PycharmProjects/Learn_Python/spam.png'


# Relative file path
# //PycharmProjects/Learn_Python/spam.png
os.chdir('/Users/ionbota/PycharmProjects/Learn_Python')
os.path.abspath('spam.png')

# single dor(.) means this directory
# two (..) dots mean parent folder
# Convert relative path to absolute
os.path.abspath('..//..//spam.png')


os.path.isabs('..//..//spam.png') # False
os.path.isabs('/..//..//spam.png') # True


# Retrive directory part of that
os.path.basename('/folder1//folder2//folder3//spam.png')  #'spam.png'

os.path.isfile('/folder1//folder2')

os.path.getsize('/Users/ionbota/PycharmProjects/Learn_Python/spam.png') # get size of folder

# os.path.listdir('Resume')


# -------#----------#----------#---------
"""
totalSize = 0
for filename in os.listdir('//autobook'):
    is not os.path.isfile(os.path.join('//autobook', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('//autobook', filename))
"""


#os.makedirs('/delicios/walnut/waffles')


