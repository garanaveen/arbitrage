#!/usr/bin/env python

from price import Price
from exchange import Exchange

class Gdax(Exchange):

   def __init__(self):
      self.name = "Gdax"

   def get_rates(self):
      self.price = Price()
      self.price.btc = 5
      self.price.ltc = 6
      self.price.bch = 7
      self.price.eth = 8

   
