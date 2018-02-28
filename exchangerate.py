#!/usr/bin/env python

from utils import readurl

url="https://api.fixer.io/latest?base=USD"

def get_exchangerate():
   jsonfile = readurl(url, ".exchangerate.json")
   exchangerate = float(jsonfile['rates']['INR'])
   print("exchangerate : " + str(exchangerate))
   return exchangerate
