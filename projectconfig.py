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

HOME_DIR=os.environ['HOME']
FILE_NAME = HOME_DIR + "/" + "myalerts.ini"


LOG_TO_STDOUT=True
if sys.platform.startswith('linux'):
   PLATFORMTYPE = "linux"
   EMAIL_NOTIFY=True
   DEVELOPER_MODE=True #This doesn't loop and prints to stdout
   POLLTIME = 30
   #This variable gets the quotes online everytime. Time consuming if True. 
   #Make it False if you are testing some other parts of the code which doesn't require live/current quotes. It will use cached files instead.
   LIVEQUOTE = False
   #This variable controls whether or not the results should be printed on stdout or history_arbitrage.log file.
   LOG_TO_STDOUT=True
   KEEP_LOOPING = False
   FILE_NAME = HOME_DIR + "/tmp/tada/" + "myalerts.ini"
else:
   PLATFORMTYPE = "mac"
   DEVELOPER_MODE = False
   POLLTIME = 30
   LIVEQUOTE = True
   LOG_TO_STDOUT=False
   KEEP_LOOPING = True
   FILE_NAME = HOME_DIR + "/tmp/tada/" + "myalerts.ini" #TODO : Figure out the right value for mac.

if 'aws' in platform.platform(): #TODO : Make it work on all three platforms with just one if elif else block.
   PLATFORM = "aws"
   EMAIL_NOTIFY=True
   LIVEQUOTE = True
   DEVELOPER_MODE=False
   LOG_TO_STDOUT=False
   POLLTIME=30
   KEEP_LOOPING = False
   FILE_NAME = HOME_DIR + "/arbitrage/" + "myalerts.ini"
   print ("Its AWS platform")

   
print ("sys.platform : " + sys.platform)

#QUOTETYPE = "lasttraded"

#highest_bid is your effective sell price (i.e. someone is ready to buy for that price)
#QUOTETYPE = "highest_bid"

#lowest_ask is your buy price (i.e. someone is ready to sell for that price)
#QUOTETYPE = "lowest_ask"

DEVELOPER_MODE=False
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

