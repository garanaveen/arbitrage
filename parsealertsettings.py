#!/usr/bin/env python

import json
import shutil
import wget
import os
import projectconfig as cfg

#TODO : Handle invalid json file

FILE_NAME = "tada.ini"

def parse_my_alert_settings():
   print("parse")

   f = open(FILE_NAME, 'r')
   myalert = "dummyline"
   #TODO : If its not "LTC<2" format, ignore that line.
   while myalert:
       myalert = f.readline()
       if '>' in myalert:
          transactionType = "sell"
          currency,ratio = myalert.split('>')
       elif '<' in myalert:
          transactionType = "buy"
          currency,ratio = myalert.split('<')
       else:
          #ignore this line
          continue

       print "currency : " + currency.lower() + ", transactionType : " + transactionType + ", ratio : " + ratio 

   f.close()

if __name__ == "__main__":
   parse_my_alert_settings()

