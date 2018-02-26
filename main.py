#!/usr/bin/env python

from exchange import Exchange
from gdax import Gdax

if __name__ == "__main__":
   gex = Gdax()
   print(gex)
   gex.get_rates()
   gex.print_price()



