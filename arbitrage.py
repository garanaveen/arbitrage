#!/usr/bin/env python

from exchange import Exchange
import projectconfig as cfg
import logging

#Calculates the arbitrage %age between two exhange rates.

class Arbitrage:
   def __init__(self, exchange1, exchange2):
      self.e1 = exchange1
      self.e2 = exchange2
   
   def printarbitrage(self):
      self.calculate_arbitrage("btc", self.e1.price.btc, self.e2.price.btc)
      self.calculate_arbitrage("ltc", self.e1.price.ltc, self.e2.price.ltc)
      self.calculate_arbitrage("eth", self.e1.price.eth, self.e2.price.eth)
      self.calculate_arbitrage("bch", self.e1.price.bch, self.e2.price.bch)

   def calculate_arbitrage(self, currency, p1, p2):
      ratio = (p1-p2)*100/p1
      cfg.logger.info(currency + "-" + str(self.e1) + ":" + str(p1) + "," + str(self.e2) + ":" + "," + str(p2) + ", ratio:" + str(ratio))
      

