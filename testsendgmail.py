#!/usr/bin/env python

source .emailcredentials.txt
import smtplib
to_addr_list = TOADDRESSLIST
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


#https://www.quora.com/What-is-the-recommended-way-to-send-email-programmatically-with-Java



#Test line
#Test line 2

