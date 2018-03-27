#!/usr/bin/env python

from emailcredentials import USERNAME, PASSWORD, TOADDRESSLIST
import time
import smtplib
import projectconfig as cfg


#TODO : Send email to the configured email address if there is a huge price difference in a short span of time.
#If the price becomes +/-y% with in x minutes then notify.
#Check the testsendgmail.py for the code to send email.


def checkforpricefluctuations(exchange):
   pass
   #print "In checkforpricefluctuations"
   # 1% in a span of 2 minutes is consider big.
   # 2% in a span of 5 minutes is consider big.
   # 3% in a span of 30 minutes is consider big.
   #TODO : Get the average price for every currency of this exchange for the past x minutes and if the difference is more than y%, send email.
 


def notifyviaemail(messageBody):
   print messageBody
   if messageBody and  cfg.DEVELOPER_MODE != True and cfg.emailcount < 20:
      cfg.emailcount = cfg.emailcount + 1
      to_addr_list = TOADDRESSLIST
      message = "Message Subject\n" + messageBody 
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(USERNAME, PASSWORD)
      problems = server.sendmail(USERNAME, to_addr_list, message)
      server.quit()

