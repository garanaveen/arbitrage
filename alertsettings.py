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
   tool_tip = ""
   def __init__(self, c, r, t, tip):
      self.currency = c 
      self.ratio = r
      self.transaction_type = t 
      self.tool_tip = tip

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

   def get_tool_tip(self, transaction_type, currency, ratio):
      tool_tip = "Empty tooltip"
      if transaction_type == "buy":
         tool_tip = "buy if ratio is less than %s" % ratio
      elif transaction_type == "sell":
         tool_tip = "sell if ratio is greater than %s" % ratio
      return tool_tip.rstrip()
         
      #Print sell buy suggestion
   def parse_my_alert_settings(self):
      f = open(FILE_NAME, 'r')
      myalert = "dummyline"
      while myalert:
          myalert = f.readline()
          p = re.compile('^[ a-zA-Z]{3}[><]-?\d+\.?\d+?$')
          if(p.match(myalert)):
             if '>' in myalert:
                transactionType = "sell"
                currency,r = myalert.split('>')
                ratio = float(r)
                tool_tip = self.get_tool_tip(transactionType, currency, ratio)
                alert = Alert(currency.lower(), ratio, transactionType, tool_tip)
                self.alerts.append(alert)
             elif '<' in myalert:
                transactionType = "buy"
                currency,r = myalert.split('<')
                ratio = float(r)
                tool_tip = self.get_tool_tip(transactionType, currency, ratio)
                alert = Alert(currency.lower(), ratio, transactionType, tool_tip)
                self.alerts.append(alert)
             else:
                #ignore this line
                continue
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
      tool_tip = "Empty tool tip"
      for a in self.alerts[:]:
         #print "currency : " + a.currency.lower() + ", transactionType : " + a.transaction_type + ", ratio : " + str(a.ratio)
         if self.is_currency_same(a.currency, currency) and a.transaction_type == cfg.get_transaction_type():
            if(cfg.get_transaction_type() == "sell") and (ratio > a.ratio):
                  matched = True
                  tool_tip = a.tool_tip
            if(cfg.get_transaction_type() == "buy") and (ratio < a.ratio):
                  matched = True
                  tool_tip = a.tool_tip
      return matched, tool_tip

if __name__ == "__main__":
   alrtSettings = AlertSettings()
   print "QUOTETYPE : " + cfg.get_transaction_type()
   matched, toop_tip = alrtSettings.is_alert_settings_matched('ltc', -4.5)
   if (matched):
      print "ltc < -4.5 matched"
   else:
      print "NOT : ltc < -4.5 didn't match"

   matched, toop_tip = alrtSettings.is_alert_settings_matched('ltc', -14.5)
   if (matched):
      print "ltc < -14.5 matched"
   else:
      print "NOT : ltc < -14.5 didn't match"
