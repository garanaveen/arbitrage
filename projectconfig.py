#!/usr/bin/env python

import logging
import platform
import sys
import os

emailcount = 0
ITERATION = 0
EXCHANGERATE_ITERATION = 0
EXCHANGERATE_FREQUENCY = 2000
EMAIL_NOTIFY=True
KEEP_LOOPING=True
VERBOSE=False

MATCHED=False
#This variable gets the quotes online everytime. Time consuming if True. 
#Make it False if you are testing some other parts of the code which doesn't require live/current quotes. It will use cached files instead.
LIVEQUOTE = True

#This variable controls whether or not the results should be printed on stdout or history_arbitrage.log file.
LOG_TO_STDOUT=True

HOME_DIR=os.environ['HOME'] + "/"

if 'aws' in platform.platform():
   PLATFORM = "aws"
   EMAIL_NOTIFY=True
   LOG_TO_STDOUT=False
   POLLTIME=30
   KEEP_LOOPING = True
   ROOT_PATH= HOME_DIR + "arbitrage/"
   #print ("Its AWS platform")

elif 'Ubuntu' in platform.platform():
   PLATFORMTYPE = "linux"
   EMAIL_NOTIFY=True
   POLLTIME = 30
   LIVEQUOTE = False
   LOG_TO_STDOUT=True
   KEEP_LOOPING = False
   ROOT_PATH= HOME_DIR + "tmp/tada/"

else:
   PLATFORMTYPE = "mac"
   POLLTIME = 30
   LOG_TO_STDOUT=True
   KEEP_LOOPING = True
   ROOT_PATH = HOME_DIR + "Documents/Github/arbitrage/" 
   
FILE_NAME = ROOT_PATH + "myalerts.ini"
#print ("sys.platform : " + sys.platform)

#QUOTETYPE = "lasttraded"

#highest_bid is your effective sell price (i.e. someone is ready to buy for that price)
#QUOTETYPE = "highest_bid"

#lowest_ask is your buy price (i.e. someone is ready to sell for that price)
#QUOTETYPE = "lowest_ask"

logger = logging.getLogger('arbitrage')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

if LOG_TO_STDOUT:
   fh = logging.StreamHandler(sys.stdout)   
   fh.setFormatter(formatter)
else:
   LOG_FILE = HOME_DIR + "history_arbitrage.log"
   fh = logging.FileHandler(LOG_FILE)
   fh.setFormatter(formatter)

logger.addHandler(fh)

def print_quote_type():
   transactionType = get_transaction_type()
   quoteType = "QUOTETYPE : " + QUOTETYPE + " : " + transactionType
   logger.info(quoteType)
   
def get_transaction_type():
   transactionType = "lasttraded"
   if QUOTETYPE == "highest_bid":
      transactionType = "sell"
   elif QUOTETYPE == "lowest_ask":
      transactionType = "buy"
   return transactionType

