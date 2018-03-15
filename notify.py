#!/usr/bin/env python

from emailcredentials import USERNAME, PASSWORD, TOADDRESSLIST
import time
import smtplib

#TODO : Send email to the configured email address if there is a huge price difference in a short span of time.
#If the price becomes +/-3% with in 5 minutes then notify.


def checkforpricefluctuations(exchange):
   print "In checkforpricefluctuations"
   #TODO : Get the average price for every currency of this exchange for the past 5 minutes and if the difference is more than 3%, send email.


def notifyviaemail(messageBody):
        print ("In notify : sending" + messageBody)
        print (type(messageBody))

	to_addr_list = TOADDRESSLIST
        message = "Message Subject\n" + messageBody 
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(USERNAME, PASSWORD)
	problems = server.sendmail(USERNAME, to_addr_list, message)
	server.quit()


