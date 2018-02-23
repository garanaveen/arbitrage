#!/usr/bin/env python

import json
import shutil
import wget
import os

koinex_url="https://koinex.in/api/ticker"
gdax_btc_url = "https://api.gdax.com/products/BTC-USD/ticker"
currency_url="https://api.fixer.io/latest?base=USD"

def readurl(url,outputFile = "ticker"):
	output = outputFile
	if os.path.exists(output):
	   os.remove(output)

	file = wget.download(url,output)
	f = open(file, 'r')
	htmlText = "\n".join(f.readlines())
	f.close()

	return json.loads(htmlText)

def readfile(filename):
   filecontents = ""
   with open(filename, "r") as myfile:
      filecontents = myfile.read()
   return json.loads(filecontents)

def get_usd_inr_conversion():
   jsonfile = readurl(currency_url, "usdinr.json")
   return jsonfile['rates']['INR']

def get_price_koinex(currency):
   jsonfile = readurl(koinex_url, "koinex.json")
   return jsonfile['prices'][currency]

#Redundant method. Create a class and override getting the price part.
def get_price_gdax(currency, filename): #currency is unused for now.
   jsonfile = readurl(gdax_btc_url, "gdax_btc.json")
   price = jsonfile['price']
   return  price

def calculate_arbitrage(usdprice, inrprice, conversionrate):
   inrpriceinusd = inrprice / conversionrate
   arbitrage = (usdprice - inrpriceinusd)*100/usdprice
   return arbitrage
   

if __name__ == "__main__":
   price_koinex =  float(get_price_koinex("BTC"))
   print("koinex btc : " + str(price_koinex))
   price_gdax = float(get_price_gdax("BTC", "gdax.txt"))
   print("gdax btc : " + str(price_gdax))
   usd_inr = get_usd_inr_conversion()
   print("usd-inr : " + str(usd_inr))
   print("arbitrage : " + str(calculate_arbitrage(price_gdax, price_koinex, usd_inr))) 

