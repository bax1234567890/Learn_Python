import requests
import urllib3

"""
Call requests.get() to download the file.
Call open() with 'wb' to create a new file in write binary mode.
Loop over the Response object’s iter_content() method.
Call write() on each iteration to write the content to the file.
Call close() to close the file.
"""


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.status_code # if it was downloaded status code should be 200

len(res.text) # how many characters are in the book>

print(res.text[:500]) # print first 500 characters

#------#-------#---------#--------#


import requests

# Send HTTP GET request
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Check if the request was successful
if res.status_code == 200:
    print("Success!")
    # For example, print the first 500 characters of the text file
    print(res.text[:500])
else:
    print("Failed to retrieve the document. Status code:", res.status_code)

playFile = open('RomeoAndJuliet.txt', 'wb')  # open in right binary mode
for chunk in res.iter_content(100000):    # How many bits each chunk will contain per iteration
    playFile.write(chunk)

