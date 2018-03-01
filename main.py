#!/usr/bin/env python

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

      koinex = Koinex()
      koinex.get_rates()
      #koinex.print_price()


      arb = Arbitrage()
      arb.printarbitrage(koinex, gex)
#      time.sleep(30)

