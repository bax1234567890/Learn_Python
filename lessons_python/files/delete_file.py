import os
import shutil
os.getcwd()
os.unlink('bacon.txt')

# Delete just if the folder is empty
os.rmdir('/Users/ionbota/Downloads/Downloads_Backup')

# Delete entire folder with all files
shutil.rmtree('/Users/ionbota/Downloads/Downloads_Backup')
os.chdir('/Users/ionbota/Downloads/Downloads_Backup/spam.txt')

for filename in os.listdir():
    if filename.endswitch('.txt'):
        # os.unlink(filename)
        print((filename))

