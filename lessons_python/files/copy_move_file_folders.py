import shutil

# Copy file to another folder
# shutil.copy('/Users/ionbota/Documents/spam.txt', '/Users/ionbota/Documents')

# Copy + Rename
shutil.copy('/Users/ionbota/Documents/spam.txt', '/Users/ionbota/Downloads/spamspamspam.txt')

# Copy entire folder
shutil.copytree('/Users/ionbota/Documents/Resume', '/Users/ionbota/Downloads_Backup')

# Move folder
shutil.move('/Users/ionbota/Downloads_Backup', '/Users/ionbota/Downloads')