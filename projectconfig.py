#!/usr/bin/env python

import logging

logger = logging.getLogger('arbitrage')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('history_arbitrage.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


#livequote = False
livequote = True #This gets the quotes online everytime. Time consuming.

