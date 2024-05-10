# SMTP - protocol sending email
"""
Second Edition: https://automatetheboringstuff.com/2e/chapter18/
Gmail - smtp.gmail.com
Outlook.com/Hotmail.com - smtp-mail.outlook.com
Yahoo - smtp.mail.yahoo.com
At&T - smtp.mail.att.net(port 465)
Comcast - smtp.comcast.net
Verizon - smtp.verizon.net(port 465)
"""
# ion.bota.qa@gmail.com, password: yjufpjujvgdgbrwx
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
# connect to the server
conn.ehlo() # connect to smtp server
conn.starttls() # begin incription
conn.login('ion.bota.qa@gmail.com', 'yjufpjujvgdgbrwx')
conn.sendmail('ion.bota.qa@gmail.com', 'bota.ion.oleg@gmail.com', 'Subject: So long.. \n\nD ear Al, \nSo long, and thanks for all the fish.\n\n-Al')
print(smtplib)
conn.quit()
