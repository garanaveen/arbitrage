#!/usr/bin/env python

from utils import readurl
import projectconfig as cfg
from exchangerateapikey import EXCHANGERATE_URL

#url="https://api.fixer.io/latest?base=USD"
#Create an account and replace the following url with your access_key.
#EXCHANGERATE_URL="http://data.fixer.io/api/latest?access_key=075191d834b8ceef6b09ea55dfa4b127"

def is_correct_frequency():
   correct_frequency = cfg.EXCHANGERATE_ITERATION % cfg.EXCHANGERATE_FREQUENCY == 0
   cfg.EXCHANGERATE_ITERATION += 1
   return correct_frequency

def is_correct_platform():
   #Linux platform has some trouble doing a wget on this url. If its linux, then execute this command and then run "./arbitrage".
   #wget https://api.fixer.io/latest?base=USD -O .exchangerate.json
   #return cfg.PLATFORMTYPE != "linux"
   return True

def get_usdinr():
      jsonfile = readurl(EXCHANGERATE_URL, ".exchangerate.json")
      inr = float(jsonfile['rates']['INR'])
      usd = float(jsonfile['rates']['USD'])
      exchangerate = inr/usd
      return exchangerate

def get_exchangerate():
   #if cfg.MATCHED_IN_PREVIOUS_ITERATION or (is_correct_frequency() and is_correct_platform()):
   if (is_correct_frequency() and is_correct_platform()):
      exchangerate = get_usdinr()
      cfg.logger.info("Getting live exchange rate 1 USD = %s INR" % exchangerate)
   else:
      liveQuoteOriginalValue = cfg.LIVEQUOTE
      cfg.LIVEQUOTE = False
      exchangerate = get_usdinr()
      cfg.LIVEQUOTE = liveQuoteOriginalValue

   return exchangerate

if __name__ == "__main__":
   cfg.MATCHED_IN_PREVIOUS_ITERATION = True
   rate = get_usdinr()
   print ("rate : " + str(rate))

