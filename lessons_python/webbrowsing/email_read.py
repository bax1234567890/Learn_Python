#pip install imapclient
#pip3 install pyzmail36
"""
BEFORE date -   These three search keys return, respectively, messages that
ON date         were received by IMAP server before, on, or after the
SINCE date      given date. The date must be formatted like '2024, 3, 20'. Also, while SINCE will match
                message on and after BEFORE Marth 20 2024, will match only messages before
                Marth 20 2024

SUBJECT strint      - Returns messages where string is found in the subject body,
BODY string         or either, respectively. If string has spaces in it, then enclose
TEXT string         it with double quotes: 'TEXT "search with spaces"'.
"""

import imapclient
import datetime
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('ion.bota.qa@gmail.com', 'yjufpjujvgdgbrwx')
conn.select_folder('INBOX', readonly=True) # navigate to INBOX
UIDs = conn.search([u'SINCE', datetime.date(2024, 3, 20)]) # Check emails since Mar 20 2024
rawMessage = conn.fetch([262], ['BODY[]', 'FLAGS'])
print(rawMessage)
print(UIDs)
message = pyzmail.PzMessage.factory(rawMessage[262][b'BODY[]'])
subject = message.get_subject()
address_from = message.get_addresses('from')
address_to = message.get_addresses('to')
blank_corbon_copy = message.get_addresses('bbc')

print('Subject: ' + subject)
print('From: ' + str(address_from))
print('To: ' + str(address_to))
print('Blank: ' + str(blank_corbon_copy))


# HTML email

# Read email body
text_part = message.text_part.get_payload().decode('UTF-8')
print(text_part)

# Find all sectoins
print(conn.list_folders())

# Modify inbox folder
modify = conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['ON', datetime.date(2024, 5, 10)])
conn.delete_messages(294)
# conn.delete_messages(UIDs) # if want to delete all emails in this day
print(UIDs)



# import imapclient
# import os
# from imapclient import IMAPClient
#
# # It's safer to use environment variables for credentials
# EMAIL_ADDRESS = os.getenv('ion.bota.qa@gmail.com')
# EMAIL_PASSWORD = os.getenv('yjufpjujvgdgbrwx')
#
# try:
#     # Connect to the IMAP server with SSL
#     conn = IMAPClient('imap.gmail.com', ssl=True)
#
#     # Log in to the server
#     conn.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#
#     # Select the INBOX in readonly mode
#     conn.select_folder('INBOX', readonly=True)
#
#     # Search for emails since a specific date
#     emails_since = conn.search(['SINCE 20-MAR-2024'])
#     print("UIDs of emails since 20-MAR-2024:", emails_since)
#
# except IMAPClient.Error as e:
#     print("An error occurred:", e)
#
# finally:
#     # Log out and close the connection safely
#     conn.logout()
