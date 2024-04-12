
# Read mode - return single string
helloFile = open('/Users/ionbota/Documents/hello.txt')
helloFile.read()
helloFile.close()

# Readlines Method - return list of strings
helloFile = open('/Users/ionbota/Documents/hello.txt')
helloFile.readlines()

# Write Method - if there is no file it will create new one
helloFile2 = open('/Users/ionbota/Documents/hello2.txt', 'w')
helloFile2.write('Hello!!!!\n')
helloFile2.write('Hello!!!!\n')
helloFile2.write('Hello!!!!\n')
helloFile2.write('How are you?!')


baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon it is not a vegetable')


# Apend Mode - does not override existing text in file
baconFile = open(('bacon.txt'), 'a')
baconFile.write('\n\n\nBacon is delicious')
baconFile.close()

# Shelve - can contain list, arrays
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Yukki', 'Tobby', 'Maxic', 'Kim']
shelfFile.close

shelfFile = shelve.open('mydata')
shelfFile['cats']

list(shelfFile.keys()) # ['cats']

list(shelfFile.values()) # [['Yukki', 'Tobby', 'Maxic', 'Kim']]