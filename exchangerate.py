#!/usr/bin/env python

from utils import readurl
import projectconfig as cfg

url="https://api.fixer.io/latest?base=USD"

def get_exchangerate():
   #Linux platform has some trouble doing a wget on this url. If its linux, then execute this command and then run "./arbitrage".
   #wget https://api.fixer.io/latest?base=USD -O .exchangerate.json
   if cfg.PLATFORMTYPE == "linux":
      liveQuoteOriginalValue = cfg.LIVEQUOTE
      cfg.LIVEQUOTE = False
      jsonfile = readurl(url, ".exchangerate.json")
      exchangerate = float(jsonfile['rates']['INR'])
      cfg.LIVEQUOTE = liveQuoteOriginalValue
   else:
      jsonfile = readurl(url, ".exchangerate.json")
      exchangerate = float(jsonfile['rates']['INR'])

   return exchangerate


if __name__ == "__main__":
   exchangerate = get_exchangerate()
   print("\n" + "exchangerate : " + str(exchangerate))

