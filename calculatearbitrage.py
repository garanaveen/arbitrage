#!/usr/bin/env python

from exchange import Exchange
from alertsettings import AlertSettings
from exchangerate import get_exchangerate
import  notify as ntf
import projectconfig as cfg
from argparser import opts
import logging
import databaseutils as dbutilsobj
from databaseutils import DatabaseUtils

from gdax import gdax
from koinex import koinex

#Calculates the arbitrage %age between two exhange rates.

class CalculateArbitrage:
   alrtSettings = None
   def __init__(self, exchange1, exchange2):
      self.e1 = exchange1
      self.e2 = exchange2
      self.maxsellarbitragepercent = -100
      self.maxsellarbitragecurrency = None
      self.minbuyarbitragepercent = 100
      self.minbuyarbitragecurrency = None
      self.notifysubject = ""
      self.notifymessage = ""
      self.alrtSettings = AlertSettings()
      self.dbutil = DatabaseUtils()

      cfg.logger.info("Creating a new instance of AlertSettings()")
   
   def printarbitrage(self):
      cfg.logger.info("-------------------------------")
      if opts.verbose:
         exchangeRate = "Exchange rate : " + str(get_exchangerate())
         cfg.logger.info(exchangeRate)
      if opts.currency == 'btc':
         self.calculate_arbitrage("btc", self.e1.nativePrice.btc, self.e1.price.btc, self.e2.price.btc)
      elif opts.currency == 'ltc':
         self.calculate_arbitrage("ltc", self.e1.nativePrice.ltc, self.e1.price.ltc, self.e2.price.ltc)
      elif opts.currency == 'eth':
         self.calculate_arbitrage("eth", self.e1.nativePrice.eth, self.e1.price.eth, self.e2.price.eth)
      elif opts.currency == 'bch':
         self.calculate_arbitrage("bch", self.e1.nativePrice.bch, self.e1.price.bch, self.e2.price.bch)
      else:
         self.calculate_arbitrage("btc", self.e1.nativePrice.btc, self.e1.price.btc, self.e2.price.btc)
         self.calculate_arbitrage("ltc", self.e1.nativePrice.ltc, self.e1.price.ltc, self.e2.price.ltc)
         self.calculate_arbitrage("eth", self.e1.nativePrice.eth, self.e1.price.eth, self.e2.price.eth)
         self.calculate_arbitrage("bch", self.e1.nativePrice.bch, self.e1.price.bch, self.e2.price.bch)

      if opts.debug:
         self.printmaxminarbitrage()

      if cfg.EMAIL_NOTIFY:
         ntf.notifyviaemail(self.notifysubject, self.notifymessage)

   def calculate_arbitrage(self, currency, np1, p1, p2):
      diff = p1-p2
      ratio = (p1-p2)*100/p2
      self.storemaxminarbitrage(ratio, currency)
      stringToPrint =  currency + "-" + str(self.e1) + "(" + str(round(np1,0)) + "):" + str(round(p1, 2)) + "," + str(self.e2) + ":" + "," + str(p2) + " : Diff(" + str(round(diff, 2)) + ")" + ", ratio:" + str(round(ratio, 2)) + "% - " + cfg.get_transaction_type()
      stringToEmail =  currency + "-" + str(self.e1) + "(" + str(round(np1,0)) + "), ratio:" + str(round(ratio, 2)) + " : " + cfg.get_transaction_type()
      stringToEmail += "\n" + stringToPrint
      (is_matched, trade_tip) = self.alrtSettings.is_alert_settings_matched(currency, ratio)
      if(is_matched):
         cfg.MATCHED = True
         appendExtraInfo = " (TradeTip : " + trade_tip + ")"
         appendExtraInfo = " (MATCHES myalerts.ini)"
         stringToPrint += appendExtraInfo
         stringToEmail += appendExtraInfo
         self.notifysubject += currency + ":" + str(round(ratio,2)) + "%,"
         self.notifymessage += stringToEmail + "\n"
         #print stringToPrint
      
      cfg.logger.info(stringToPrint)
      
   def storemaxminarbitrage(self, ratio, currency):
      #TODO : Store them in CurrentArbitrage table of database.
      if cfg.QUOTETYPE == "highest_bid": #sell
         if(self.maxsellarbitragepercent < ratio):
            self.maxsellarbitragepercent = ratio
            self.maxsellarbitragecurrency = currency
	    self.dbutil.set_current_arbitrage('koinex', 'gdax',  dbutilsobj.TRANSACTION_SELL, currency, ratio)
            if opts.verbose:
               cfg.logger.info("set_current_arbitrage(), %d, %s, %f", dbutilsobj.TRANSACTION_SELL, currency, ratio)
      elif cfg.QUOTETYPE == "lowest_ask": #buy
         if(self.minbuyarbitragepercent > ratio):
            self.minbuyarbitragepercent = ratio
            self.minbuyarbitragecurrency = currency
	    self.dbutil.set_current_arbitrage('koinex', 'gdax', dbutilsobj.TRANSACTION_BUY, currency, ratio)
            if opts.verbose:
               cfg.logger.info("set_current_arbitrage(), %d, %s, %f", dbutilsobj.TRANSACTION_SELL, currency, ratio)
      if self.maxsellarbitragepercent > self.minbuyarbitragepercent:
         print "spread found"

   def printmaxminarbitrage(self):
      print "maxsell, " , self.maxsellarbitragepercent, self.maxsellarbitragecurrency
      print "minbuy, ", self.minbuyarbitragepercent, self.minbuyarbitragecurrency

if __name__ == "__main__":
   cfg.QUOTETYPE = "highest_bid"

   gex = gdax()
   gex.get_rates()
   koine = koinex()
   koine.get_rates()
 
   calarb = CalculateArbitrage(koine, gex)
   calarb.storemaxminarbitrage(6, 'LTC')


