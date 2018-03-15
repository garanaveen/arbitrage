#!/usr/bin/env python

from notify import checkforpricefluctuations
from exchange import Exchange
from gdax import Gdax
from koinex import Koinex
from exchangerate import get_exchangerate
from arbitrage import Arbitrage

import time

if __name__ == "__main__":

#   while True:
      gex = Gdax()
      gex.get_rates()
      #gex.print_price()
      gex.store_rates()

      koinex = Koinex()
      koinex.get_rates()
      #koinex.print_price()
      koinex.store_rates()


      arb = Arbitrage(koinex, gex)
      arb.printarbitrage()
      checkforpricefluctuations('KOINEX')
      checkforpricefluctuations('GDAX')
#      time.sleep(30)

