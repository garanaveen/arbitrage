#!/usr/bin/env python

import smtplib
to_addr_list = ['sampleemail@gmail.com']
message = 'Test email from Va'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(USERNAME, PASSWORD)
problems = server.sendmail(USERNAME, to_addr_list, message)
server.quit()


#Bookmarks,
#https://developers.google.com/gmail/api/guides/sending

#For sending emails programmaticaly,
#https://login.mailchimp.com/signup/success/ 

