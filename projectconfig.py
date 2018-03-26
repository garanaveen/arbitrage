#!/usr/bin/env python

import logging
import sys

emailcount = 0

LOG_TO_STDOUT=True
if sys.platform.startswith('linux'):
   DEVELOPER_MODE=True #This doesn't loop and prints to stdout
   #This variable gets the quotes online everytime. Time consuming if True. 
   #Make it False if you are testing some other parts of the code which doesn't require live/current quotes. It will use cached files instead.
   LIVEQUOTE = False
   #This variable controls whether or not the results should be printed on stdout or history_arbitrage.log file.
   LOG_TO_STDOUT=True
else:
   LIVEQUOTE = True
   LOG_TO_STDOUT=False

   
print ("sys.platform : " + sys.platform)

#QUOTETYPE = "lasttraded"

#highest_bid is your effective sell price (i.e. someone is ready to buy for that price)
#QUOTETYPE = "highest_bid"

#lowest_ask is your buy price (i.e. someone is ready to sell for that price)
QUOTETYPE = "lowest_ask"

DEVELOPER_MODE=True
LIVEQUOTE = True


logger = logging.getLogger('arbitrage')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

if LOG_TO_STDOUT:
   fh = logging.StreamHandler(sys.stdout)   
   fh.setFormatter(formatter)
else:
   fh = logging.FileHandler('history_arbitrage.log')
   fh.setFormatter(formatter)

logger.addHandler(fh)


def print_quote_type():
   transactionType = "lasttraded"
   if QUOTETYPE == "highest_bid":
      transactionType = "sellprice"
   elif QUOTETYPE == "lowest_ask":
      transactionType = "buyprice"
   quoteType = "QUOTETYPE : " + QUOTETYPE + " : " + transactionType

   logger.info(quoteType)
