#!/usr/bin/env python

from exchange import Exchange
from gdax import Gdax
from koinex import Koinex
from exchangerate import get_exchangerate

if __name__ == "__main__":

   gex = Gdax()
   print(gex)
   gex.get_rates()
   gex.print_price()

   koinex = Koinex()
   print(koinex)
   koinex.get_rates()
   koinex.print_price()


   get_exchangerate()

