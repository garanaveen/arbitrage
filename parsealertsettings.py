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
   myalert = f.readline()
   while myalert:
       if '>' in myalert:
          transactionType = "sell"
          currency,ratio = myalert.split('>')
       if '<' in myalert:
          transactionType = "buy"
          currency,ratio = myalert.split('<')

       print "currency : " + currency + ", transactionType : " + transactionType + ", ratio : " + ratio 
       myalert = f.readline()

   f.close()

if __name__ == "__main__":
   parse_my_alert_settings()

