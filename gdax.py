#!/usr/bin/env python

from price import Price
from exchange import Exchange

import json
import shutil
import wget
import os

gdax_btc_url = "https://api.gdax.com/products/BTC-USD/ticker"
base_url = "https://api.gdax.com/products/"

class Gdax(Exchange):

   def __init__(self):
      self.name = "Gdax"

   def get_rates(self):
      self.price = Price()
      self.price.btc = get_price("BTC")
      self.price.ltc = get_price("LTC")
      self.price.bch = get_price("BCH")
      self.price.eth = get_price("ETH")

   
def get_price(currency):
   url = base_url + currency + "-USD/ticker"
   print("url : "+ url)
   jsonfile = readurl(url, "gdax_btc.json")
   btc_price = jsonfile['price']
   return  btc_price


def readurl(url,outputFile = "ticker"):
	output = outputFile
	if os.path.exists(output):
	   os.remove(output)

	file = wget.download(url,output)
	f = open(file, 'r')
	htmlText = "\n".join(f.readlines())
	f.close()

	return json.loads(htmlText)


