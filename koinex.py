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

class koinex(Exchange):

   def __init__(self):
      self.name = "koinex"
      cfg.print_quote_type()

   def get_rates(self):
      self.price = Price()
      jsonfile = readurl(base_url, ".koinex.json")

      usdinrrate = get_exchangerate()

      #If True get the price that people are willing to buy. Else get the last trade price.
      if cfg.QUOTETYPE == "highest_bid":
         self.price.btc = float(jsonfile['stats']['BTC']['highest_bid'])/usdinrrate
         self.price.ltc = float(jsonfile['stats']['LTC']['highest_bid'])/usdinrrate
         self.price.eth = float(jsonfile['stats']['ETH']['highest_bid'])/usdinrrate
         self.price.bch = float(jsonfile['stats']['BCH']['highest_bid'])/usdinrrate
      elif cfg.QUOTETYPE == "lowest_ask":

         self.price.btc = float(jsonfile['stats']['BTC']['lowest_ask'])/usdinrrate
         self.price.ltc = float(jsonfile['stats']['LTC']['lowest_ask'])/usdinrrate
         self.price.eth = float(jsonfile['stats']['ETH']['lowest_ask'])/usdinrrate
         self.price.bch = float(jsonfile['stats']['BCH']['lowest_ask'])/usdinrrate
      else:
         self.price.btc = float(jsonfile['prices']['BTC'])/usdinrrate
         self.price.ltc = float(jsonfile['prices']['LTC'])/usdinrrate
         self.price.eth = float(jsonfile['prices']['ETH'])/usdinrrate
         self.price.bch = float(jsonfile['prices']['BCH'])/usdinrrate


