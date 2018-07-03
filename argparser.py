#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Arguments for arbirage.')

parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("--debug", help="print debugging output",
                    action="store_true")

parser.add_argument("--loop", dest='loop', action="store_true",
                    help="run the arbitration in loop")
parser.add_argument("--noloop", dest='loop', action="store_false",
                    help="don't run the arbitration in loop")

parser.add_argument("--buy", dest='buyonly', action="store_true",
                    help="runs arbitrage for buy only")

parser.add_argument("--sell", dest='sellonly', action="store_true",
                    help="runs arbitrage for sell only")

parser.add_argument("-c", "--currency", dest='currency', default='all',
                    help="specify 3 letter acronym of the currency (ex : ltc)")

opts = parser.parse_args()

if __name__ == "__main__":
   print ("verbose : ", opts.verbose)
   print ("debug : ", opts.debug)
   print ("loop : ", opts.loop)
   print ("currency : ", opts.currency)

   if opts.currency is 'eth':
      print ("True")

