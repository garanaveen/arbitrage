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
      self.native = False
      #cfg.print_quote_type()

   def get_rates(self):
      self.price = Price()
       
      jsonfile = readurl(base_url, ".koinex.json")

      usdinrrate = get_exchangerate()

      #If True get the price that people are willing to buy. Else get the last trade price.
      if cfg.QUOTETYPE == "highest_bid":
         self.nativePrice.btc = float(jsonfile['stats']['BTC']['highest_bid'])
         self.nativePrice.ltc = float(jsonfile['stats']['LTC']['highest_bid'])
         self.nativePrice.eth = float(jsonfile['stats']['ETH']['highest_bid'])
         self.nativePrice.bch = float(jsonfile['stats']['BCH']['highest_bid'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate
      elif cfg.QUOTETYPE == "lowest_ask":
         self.nativePrice.btc = float(jsonfile['stats']['BTC']['lowest_ask'])
         self.nativePrice.ltc = float(jsonfile['stats']['LTC']['lowest_ask'])
         self.nativePrice.eth = float(jsonfile['stats']['ETH']['lowest_ask'])
         self.nativePrice.bch = float(jsonfile['stats']['BCH']['lowest_ask'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate
      else:
         self.nativePrice.btc = float(jsonfile['prices']['BTC'])
         self.nativePrice.ltc = float(jsonfile['prices']['LTC'])
         self.nativePrice.eth = float(jsonfile['prices']['ETH'])
         self.nativePrice.bch = float(jsonfile['prices']['BCH'])
         self.price.btc = self.nativePrice.btc/usdinrrate
         self.price.ltc = self.nativePrice.ltc/usdinrrate
         self.price.eth = self.nativePrice.eth/usdinrrate
         self.price.bch = self.nativePrice.bch/usdinrrate


