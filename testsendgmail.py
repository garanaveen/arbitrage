#!/usr/bin/env python
from emailcredentials import USERNAME, PASSWORD, TOADDRESSLIST


import time
import smtplib
to_addr_list = TOADDRESSLIST
message = 'Test email from Va'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(USERNAME, PASSWORD)
for i in range(5):
   problems = server.sendmail(USERNAME, to_addr_list, message)
   time.sleep(3)
server.quit()


#Bookmarks,
#https://developers.google.com/gmail/api/guides/sending

#For sending emails programmaticaly,
#https://login.mailchimp.com/signup/success/ 


#https://www.quora.com/What-is-the-recommended-way-to-send-email-programmatically-with-Java

#If you get the following error, then visit this link and turn on.
#https://myaccount.google.com/lesssecureapps
#--------------
#Traceback (most recent call last):
#  File "./testsendgmail.py", line 10, in <module>
#    server.login(USERNAME, PASSWORD)
#  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/smtplib.py", line 622, in login
#    raise SMTPAuthenticationError(code, resp)
#smtplib.SMTPAuthenticationError: (534, '5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbtW\n5.7.14 LP6TDFEorlsLlLOWHJvrsiTLInIavybMcek5d6I_vzsTqhuiScTYA1Qr0XFTfA6ykv-pAL\n5.7.14 tOLhC4FDkRfIGN6es-MeeM8c0R6Rn_YG-vIcSGinU117F38M9kImIguK5y7Mhv8ouuG2rc\n5.7.14 t9bUg-aCyjls9UkU1crKYD7SLqYrlbfhIreCtZStcrGzjzODhzNIeSuVncJCAn46KZl3Bb\n5.7.14 aeZz2Wh_yjgH_cfirzfDJMu6A8hPs> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 e18sm589519wmc.21 - gsmtp')
