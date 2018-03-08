#!/usr/bin/env python

import smtplib
to_addr_list = ['testgmailaccount@gmail.com']
message = 'Test email from Va'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('testgmailaccount@gmail.com','xxxxxxxx')
problems = server.sendmail('testgmailaccount@gmail.com', to_addr_list, message)
server.quit()




#Bookmarks,
#https://developers.google.com/gmail/api/guides/sending

#For sending emails programmaticaly,
#https://login.mailchimp.com/signup/success/ 
