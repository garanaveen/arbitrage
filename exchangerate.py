#!/usr/bin/env python

from utils import readurl
import projectconfig as cfg

url="https://api.fixer.io/latest?base=USD"

def is_correct_frequency():
   return cfg.ITERATION % cfg.EXCHANGERATE_FREQUENCY == 0

def is_correct_platform():
   #Linux platform has some trouble doing a wget on this url. If its linux, then execute this command and then run "./arbitrage".
   #wget https://api.fixer.io/latest?base=USD -O .exchangerate.json
   return cfg.PLATFORMTYPE != "linux"

def get_exchangerate():
   if is_correct_frequency() and is_correct_platform():
      print "Getting live exchange rate"
      jsonfile = readurl(url, ".exchangerate.json")
      exchangerate = float(jsonfile['rates']['INR'])
   else:
      liveQuoteOriginalValue = cfg.LIVEQUOTE
      cfg.LIVEQUOTE = False
      jsonfile = readurl(url, ".exchangerate.json")
      exchangerate = float(jsonfile['rates']['INR'])
      cfg.LIVEQUOTE = liveQuoteOriginalValue

   return exchangerate


if __name__ == "__main__":
   exchangerate = get_exchangerate()
   print("\n" + "exchangerate : " + str(exchangerate))

