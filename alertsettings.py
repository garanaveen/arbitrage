#!/usr/bin/env python

import json
import shutil
import wget
import os
import projectconfig as cfg
import re


FILE_NAME = "myalerts.ini"

class Alert:
   currency = 'cur'
   ratio = 0
   transaction_type = 'invalid'
   def __init__(self, c, r, t):
      self.currency = c 
      self.ratio = float(r)
      self.transaction_type = t 

class AlertSettings:
   class __AlertSettings:
      def __init__(self):
         pass
   instance = None
   def __init__(self):
      if not AlertSettings.instance:
         AlertSettings.instance = AlertSettings.__AlertSettings()
         self.parse_my_alert_settings()
      
   def __getattr__(self):
      return getattr(self.instance)

   alerts = []

   def parse_my_alert_settings(self):
      f = open(FILE_NAME, 'r')
      myalert = "dummyline"
      while myalert:
          myalert = f.readline()
          #TODO : Check for this regex AAA>1 or bbb<2. Ignore otherwise.
          p = re.compile('^[ a-zA-Z]{3}[><]-?\d{1,2}$')
          if(p.match(myalert)):
          
              print "Did match the regex %s" % myalert
	      if '>' in myalert:
		 transactionType = "sell"
		 currency,ratio = myalert.split('>')
		 alert = Alert(currency.lower(), ratio, transactionType)
		 self.alerts.append(alert)
	      elif '<' in myalert:
		 transactionType = "buy"
		 currency,ratio = myalert.split('<')
		 alert = Alert(currency.lower(), ratio, transactionType)
		 self.alerts.append(alert)
	      else:
		 #ignore this line
		 continue
          else:
             print "Din't match the regex %s" % myalert

      f.close()

   def print_everything(self):
      for a in self.alerts[:]:
         print "currency : " + a.currency.lower() + ", transactionType : " + a.transaction_type + ", ratio : " + str(a.ratio)
   def is_currency_same(self, alertcurrency, currentcurrency):
      retVal = (alertcurrency == currentcurrency) or (alertcurrency == "all")
      #print "alertcurrency : " + alertcurrency + ", currentcurrency : " + currentcurrency + ", retVal : " + str(retVal)
      return retVal

   def is_alert_settings_matched(self, currency, ratio):
      matched = False
      for a in self.alerts[:]:
         #print "currency : " + a.currency.lower() + ", transactionType : " + a.transaction_type + ", ratio : " + str(a.ratio)
         if self.is_currency_same(a.currency, currency) and a.transaction_type == cfg.get_transaction_type():
            if(cfg.get_transaction_type() == "sell") and (ratio > a.ratio):
                  matched = True
            if(cfg.get_transaction_type() == "buy") and (ratio < a.ratio):
                  matched = True
      return matched

if __name__ == "__main__":
   alrtSettings = AlertSettings()
   print "QUOTETYPE : " + cfg.get_transaction_type()
   if (alrtSettings.is_alert_settings_matched('ltc', 4.5)):
      print "success"
   else:
      print "failure"
