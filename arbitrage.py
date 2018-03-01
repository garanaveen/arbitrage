#!/usr/bin/env python

from exchange import Exchange
import logging
#Calculates the arbitrage %age between two exhange rates.

class Arbitrage:
   def __init__(self):
      #TODO : This should be moved to some config file where all the classes have access to so that logging can be done from anywhere.
      logging.basicConfig(filename="arbitrage.log", level=logging.INFO)
   
   def printarbitrage(self, e1, e2):
      self.calculate_arbitrage("btc", e1.price.btc, e2.price.btc)
      self.calculate_arbitrage("ltc", e1.price.ltc, e2.price.ltc)
      self.calculate_arbitrage("eth", e1.price.eth, e2.price.eth)
      self.calculate_arbitrage("bch", e1.price.bch, e2.price.bch)

   def calculate_arbitrage(self, currency, p1, p2):
      ratio = (p1-p2)*100/p1
      logging.info(currency + ":" + str(p1) + "," + str(p2) + ", ratio:" + str(ratio))
      

