#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Arguments for arbirage.')

parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")

parser.add_argument("--loop", dest='loop', action="store_true",
                    help="run the arbitration in loop")
parser.add_argument("--noloop", dest='loop', action="store_false",
                    help="don't run the arbitration in loop")

opts = parser.parse_args()

if __name__ == "__main__":
   print ("verbose : ", opts.verbose)
   print ("loop : ", opts.loop)


