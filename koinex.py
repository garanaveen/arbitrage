#!/usr/bin/env python

from utils import readurl
from price import Price
from exchange import Exchange
from exchangerate import get_exchangerate
import projectconfig as cfg

import json
import shutil
import wget
import os

base_url = "https://koinex.in/api/ticker"

class Koinex(Exchange):

   def __init__(self):
      self.name = "Koinex"

   def get_rates(self):
      self.price = Price()
      jsonfile = readurl(base_url, ".koinex.json")

      usdinrrate = get_exchangerate()
      #usdinrrate = 1
      
      #If True get the price that people are willing to buy. Else get the last trade price.
      if True:
         self.price.btc = float(jsonfile['stats']['BTC']['highest_bid'])/usdinrrate
         self.price.ltc = float(jsonfile['stats']['LTC']['highest_bid'])/usdinrrate
         self.price.eth = float(jsonfile['stats']['ETH']['highest_bid'])/usdinrrate
         self.price.bch = float(jsonfile['stats']['BCH']['highest_bid'])/usdinrrate
      else:
         self.price.btc = float(jsonfile['prices']['BTC'])/usdinrrate
         self.price.ltc = float(jsonfile['prices']['LTC'])/usdinrrate
         self.price.eth = float(jsonfile['prices']['ETH'])/usdinrrate
         self.price.bch = float(jsonfile['prices']['BCH'])/usdinrrate

