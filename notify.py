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
   #print ("In checkforpricefluctuations")
   # 1% in a span of 2 minutes is consider big.
   # 2% in a span of 5 minutes is consider big.
   # 3% in a span of 30 minutes is consider big.
   #TODO : Get the average price for every currency of this exchange for the past x minutes and if the difference is more than y%, send email.
 


def notifyviaemail(subject, message):
   #print message
   if message and  cfg.EMAIL_NOTIFY == True and cfg.emailcount < 50:
      cfg.emailcount = cfg.emailcount + 1
      to_addr_list = TOADDRESSLIST
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(USERNAME, PASSWORD)

      emailmessage = 'Subject: {}\n\n{}'.format(subject, message)
      problems = server.sendmail(USERNAME, to_addr_list, emailmessage)
      server.quit()


if __name__ == "__main__":
   notifyviaemail("This is subject", "This is email main body")

