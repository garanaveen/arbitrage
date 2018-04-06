#!/usr/bin/env python

from exchange import Exchange
from alertsettings import AlertSettings
import  notify as ntf
import projectconfig as cfg
import logging

#Calculates the arbitrage %age between two exhange rates.

class CalculateArbitrage:
   alrtSettings = AlertSettings()
   def __init__(self, exchange1, exchange2):
      self.e1 = exchange1
      self.e2 = exchange2
      self.notifymessage = ""
   
   def printarbitrage(self):
      cfg.logger.info("-------------------------------")
      self.calculate_arbitrage("btc", self.e1.price.btc, self.e2.price.btc)
      self.calculate_arbitrage("ltc", self.e1.price.ltc, self.e2.price.ltc)
      self.calculate_arbitrage("eth", self.e1.price.eth, self.e2.price.eth)
      self.calculate_arbitrage("bch", self.e1.price.bch, self.e2.price.bch)
      ntf.notifyviaemail(self.notifymessage)

   def calculate_arbitrage(self, currency, p1, p2):
      ratio = (p1-p2)*100/p2
      stringToPrint =  currency + "-" + str(self.e1) + ":" + str(round(p1, 2)) + "," + str(self.e2) + ":" + "," + str(p2) + ", ratio:" + str(round(ratio, 2)) + " : " + cfg.get_transaction_type()
      (is_matched, trade_tip) = self.alrtSettings.is_alert_settings_matched(currency, ratio)
      if(is_matched):
         self.notifymessage = self.notifymessage + stringToPrint + "\n" 
         stringToPrint += " (TradeTip : " + trade_tip + ")"
         stringToPrint += " (MATCHES myalerts.ini)"
         #print stringToPrint
      cfg.logger.info(stringToPrint)
      


def match_notify_conditions(ratio):
   retVal = False
   if ((ratio > 11) and cfg.QUOTETYPE == "highest_bid"):
      retVal = True
   if ((ratio < 7) and cfg.QUOTETYPE == "lowest_ask"):
      retVal = True

   return retVal
   
   
