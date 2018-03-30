#!/usr/bin/env python

from utils import readurl

url="https://api.fixer.io/latest?base=USD"

def get_exchangerate():
   jsonfile = readurl(url, ".exchangerate.json")
   exchangerate = float(jsonfile['rates']['INR'])
   return exchangerate


if __name__ == "__main__":
   exchangerate = get_exchangerate()
   print("\n" + "exchangerate : " + str(exchangerate))
