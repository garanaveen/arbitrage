#!/usr/bin/env python

from price import Price

class Exchange:
   price = Price()
   nativePrice = Price()
   native = True #If this exchange is not in USD, then assign it to false.
   name = "Exchange"

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
   
   def store_rates(self):
      pass
      #print ("TODO : store_rates to the PriceHistory.db")
      #TODO : open PriceHistory.db and store the price

