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
      
      self.price.btc = float(jsonfile['prices']['BTC'])/usdinrrate
      self.price.ltc = float(jsonfile['prices']['LTC'])/usdinrrate
      self.price.eth = float(jsonfile['prices']['ETH'])/usdinrrate
      self.price.bch = float(jsonfile['prices']['BCH'])/usdinrrate

