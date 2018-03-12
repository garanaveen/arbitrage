#!/usr/bin/env python

import logging
import sys

if sys.platform.startswith('linux'):
   #This variable gets the quotes online everytime. Time consuming if True. 
   #Make it False if you are testing some other parts of the code which doesn't require live/current quotes. It will use cached files instead.
   LIVEQUOTE = False
   #This variable controls whether or not the results should be printed on stdout or history_arbitrage.log file.
   LOG_TO_STDOUT=True
else:
   LIVEQUOTE = True
   LOG_TO_STDOUT=False
   
print ("sys.platform : " + sys.platform)

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

QUOTETYPE = "lasttraded"
#QUOTETYPE = "highest_bid"
#QUOTETYPE = "lowest_ask"

