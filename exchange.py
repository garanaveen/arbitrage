#!/usr/bin/env python

from price import Price
from databaseutils import DatabaseUtils

class Exchange:
   price = Price()
   nativePrice = Price()
   native = True #If this exchange is not in USD, then assign it to false.
   name = "Exchange"
   dbutil = DatabaseUtils()

   def __init__(self):
      pass

   def __str__(self):
      return self.name

   def get_rates(self):
      "Default rates. This method is supposed to be overridden by derived class and price should be set based on live quote for the exchange."
      self.price.btc = 1
      self.price.ltc = 2
      self.price.bch = 3
      self.price.eth = 4
 
   def print_price(self):
      print("\n")
      print("btc:" + str(self.price.btc))
      print("ltc:" + str(self.price.ltc))
      print("bch:" + str(self.price.bch))
      print("eth:" + str(self.price.eth))
   
   def store_rates(self, transactionType):
      self.dbutil.set_current_price(self.name, transactionType, "BTC", self.price.btc)
      self.dbutil.set_current_price(self.name, transactionType, "LTC", self.price.ltc)
      self.dbutil.set_current_price(self.name, transactionType, "ETH", self.price.eth)
      self.dbutil.set_current_price(self.name, transactionType, "BCH", self.price.bch)


