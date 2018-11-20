#!/usr/bin/env python

from utils import readurl
from price import Price
from exchange import Exchange
import databaseutils as dbutils
import projectconfig as cfg                                                                                   


import json
import shutil
import wget
import os

#example for gdax_btc_url = "https://api.gdax.com/products/BTC-USD/ticker"
base_url = "https://api.gdax.com/products/"

class gdax(Exchange):

   def __init__(self):
      self.name = "gdax"

   def get_rates(self):
      self.price = Price()
      self.price.btc = self.get_price("BTC")
      if cfg.ENABLEBCH:
         self.price.bch = self.get_price("BCH")
      self.price.ltc = self.get_price("LTC")
      self.price.eth = self.get_price("ETH")
      self.price.tusd = 1
      self.store_rates(dbutils.TRANSACTION_SELL)
      self.store_rates(dbutils.TRANSACTION_BUY)

   def get_price(self, currency):
      url = base_url + currency + "-USD/ticker"
      cache_file_name = ".GDax" + currency + ".json"
      jsonfile = readurl(url, cache_file_name)
      price = float(jsonfile['price'])
      return  price

if __name__ == "__main__":
   gdaxobj = gdax()
   gdaxobj.get_rates()
   gdaxobj.print_price()
   print gdaxobj.price.btc

