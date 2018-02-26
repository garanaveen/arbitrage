#!/usr/bin/env python

from price import Price

class Exchange:
   def __init__(self):
      self.name = "Exchange"

   def __str__(self):
      return self.name

   def get_rates(self):
      self.price = Price()
      self.price.btc = 1
      self.price.ltc = 2
      self.price.bch = 3
      self.price.eth = 4
 
   def print_price(self):
      print("btc:" + str(self.price.btc))
      print("ltc:" + str(self.price.ltc))
      print("bch:" + str(self.price.bch))
      print("eth:" + str(self.price.eth))
