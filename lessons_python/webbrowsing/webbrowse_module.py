import webbrowser, sys, pyperclip
import urllib.parse
# https://automatetheboringstuff.com/chapter11/

webbrowser.open('https://automatetheboringstuff.com')

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']
# Check if command line arguments were passed

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.']
    address = ' '.join(sys.argv[1:]) # Slice begin from index 1 not 0 and add all values from the right.
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#------#-------#---------#--------#


def mapit(address):
    # URL encode the address to create a valid URL
    url_encoded_address = urllib.parse.quote(address)

    # Construct the Google Maps URL with the encoded address
    maps_url = f"https://www.google.com/maps/place/{url_encoded_address}"

    # Open the URL in the default browser
    webbrowser.open(maps_url)

# Specific address
address = '1712 S Glendale Ave, Glendale, CA 91205'

# Call the function with the specific address
mapit(address)
