#!/usr/bin/env python

from exchange import Exchange
from gdax import Gdax

if __name__ == "__main__":
   ex = Exchange()
   print(ex)
   ex.get_rates()
   ex.print_price()
   


   gex = Gdax()
   print(gex)
   gex.get_rates()
   gex.print_price()
