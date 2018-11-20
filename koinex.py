#!/usr/bin/env python

from utils import readurl
from price import Price
from exchange import Exchange
from exchangerate import get_exchangerate
import projectconfig as cfg
import databaseutils as dbutils


import json
import shutil
import wget
import os

base_url = "https://koinex.in/api/ticker"

class koinex(Exchange):

   def __init__(self):
      self.name = "koinex"
      self.native = False
      #cfg.print_quote_type()

   def get_rates(self):
      self.price = Price()
       
      jsonfile = readurl(base_url, ".koinex.json")

      usdinrrate = get_exchangerate()

      #highest_bid is your effective sell price (i.e. someone is ready to buy for that price)
      if cfg.QUOTETYPE == "highest_bid": #sell
         self.nativePrice.btc = float(jsonfile['stats']['inr']['BTC']['highest_bid'])
         self.nativePrice.ltc = float(jsonfile['stats']['inr']['LTC']['highest_bid'])
         self.nativePrice.eth = float(jsonfile['stats']['inr']['ETH']['highest_bid'])
         if cfg.ENABLEBCH:
            self.nativePrice.bch = float(jsonfile['stats']['inr']['BCHABC']['highest_bid'])
         self.nativePrice.tusd = float(jsonfile['stats']['inr']['TUSD']['highest_bid'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate
         self.price.tusd = self.nativePrice.tusd/usdinrrate
         self.store_rates(dbutils.TRANSACTION_SELL)
      elif cfg.QUOTETYPE == "lowest_ask": #buy
         self.nativePrice.btc = float(jsonfile['stats']['inr']['BTC']['lowest_ask'])
         self.nativePrice.ltc = float(jsonfile['stats']['inr']['LTC']['lowest_ask'])
         self.nativePrice.eth = float(jsonfile['stats']['inr']['ETH']['lowest_ask'])
         if cfg.ENABLEBCH:
            self.nativePrice.bch = float(jsonfile['stats']['inr']['BCHABC']['lowest_ask'])
         self.nativePrice.tusd = float(jsonfile['stats']['inr']['TUSD']['lowest_ask'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate
         self.price.tusd = self.nativePrice.tusd/usdinrrate
         self.store_rates(dbutils.TRANSACTION_BUY)
      else:
         self.nativePrice.btc = float(jsonfile['prices']['inr']['BTC'])
         self.nativePrice.ltc = float(jsonfile['prices']['inr']['LTC'])
         self.nativePrice.eth = float(jsonfile['prices']['inr']['ETH'])
         if cfg.ENABLEBCH:
            self.nativePrice.bch = float(jsonfile['prices']['inr']['BCHABC'])
         self.nativePrice.tusd = float(jsonfile['prices']['inr']['TUSD'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate
         self.price.tusd = self.nativePrice.tusd/usdinrrate


#   def store_rates(self, transactionType):
#      Exchange.store_rates(self, self.name, transactionType)


if __name__ == "__main__":
   cfg.LIVEQUOTE = False
   cfg.QUOTETYPE = "highest_bid"
   jsonfile = readurl(base_url, ".koinex.json")
   tusdLastTradedPrice = float(jsonfile['prices']['inr']['TUSD'])
   print ("tusdLastTradedPrice : " + str(tusdLastTradedPrice))
   koinexobj = koinex()
   koinexobj.get_rates()
   koinexobj.print_price()
