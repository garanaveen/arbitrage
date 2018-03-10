#!/usr/bin/env python

import logging
import sys

LOG_TO_STDOUT=False

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

#LIVEQUOTE = False
LIVEQUOTE = True
#This gets the quotes online everytime. Time consuming.


QUOTETYPE = "lasttraded"
#QUOTETYPE = "highest_bid"
#QUOTETYPE = "lowest_ask"

