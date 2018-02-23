#!/usr/bin/env python


import json

def readfile(filename):
   filecontents = ""
   with open("usdinr.txt", "r") as myfile:
      filecontents = myfile.read()
   return json.loads(filecontents)


def get_usd_inr_conversionusingreadfile():
   jsonfile = readfile("usdinr.txt")
   return jsonfile['rates']['INR']


def get_usd_inr_conversion():
   filecontents = ""
   with open("usdinr.txt", "r") as myfile:
      filecontents = myfile.read()
   xchangeratejson = json.loads(filecontents)

   return xchangeratejson['rates']['INR']
   
   
def get_price_koinex(currency, filename):
   filecontents = ""
   with open(filename, "r") as myfile:
      filecontents = myfile.read()
   koinexjson = json.loads(filecontents)
   price = koinexjson['prices'][currency]
   return  price

#Redundant method. Create a class and override getting the price part.
def get_price_gdax(currency, filename):
   filecontents = ""
   with open(filename, "r") as myfile:
      filecontents = myfile.read()
   gdaxjson = json.loads(filecontents)
   price = gdaxjson['price']
   return  price

def calculate_arbitrage(usdprice, inrprice, conversionrate):
   inrpriceinusd = inrprice / conversionrate
   arbitrage = (usdprice - inrpriceinusd)*100/usdprice
   return arbitrage
   

if __name__ == "__main__":
   price_koinex =  float(get_price_koinex("BTC", "koinexprice.txt"))
   print("koinex btc : " + str(price_koinex))
   price_gdax = float(get_price_gdax("BTC", "gdax.txt"))
   print("gdax btc : " + str(price_gdax))
   usd_inr = get_usd_inr_conversionusingreadfile()
   print("usd-inr : " + str(usd_inr))
   print("arbitrage : " + str(calculate_arbitrage(price_gdax, price_koinex, usd_inr))) 

