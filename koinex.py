#!/usr/bin/env python

from utils import readurl
from price import Price
from exchange import Exchange

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

      
      self.price.btc = float(jsonfile['prices']['BTC'])
      self.price.ltc = float(jsonfile['prices']['LTC'])
      self.price.eth = float(jsonfile['prices']['ETH'])
      self.price.bch = float(jsonfile['prices']['BCH'])

