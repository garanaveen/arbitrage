#!/usr/bin/env python


import sqlite3
import projectconfig as cfg
from datetime import datetime
import time


TRANSACTION_SELL = 0
TRANSACTION_BUY = 1



class DatabaseUtils:
   instance = None
   initialized = False 

   class __DatabaseUtils: 
      def __init__(self): 
         pass
   
   def initialize_database(self):
      DB_FILE = cfg.ROOT_PATH + "PriceHistory.db"
      self.conn = sqlite3.connect(DB_FILE)
      self.c = self.conn.cursor()
      self.initialized = True

   def __init__(self):
      if not DatabaseUtils.instance:
         DatabaseUtils.instance = DatabaseUtils.__DatabaseUtils()
      if not self.initialized:
         self.initialize_database()

   def __getattr__(self, attr):
      return getattr(self.instance, attr)

   
   def set_current_arbitrage(self, exchange1, exchange2, transaction_type, currency, arbitrage_percent):
      dbQuery = "REPLACE INTO CurrentArbitrage VALUES ('%s', '%s', '%d', '%s', %f)" % (exchange1, exchange2, transaction_type, currency, arbitrage_percent)
      self.c.execute(dbQuery)
      self.conn.commit()
      
   def set_current_price(self, exchange, transaction_type, currency, price):
      dbQuery = "REPLACE INTO CurrentPrice VALUES ('%s', '%d', '%s', %f)" % (exchange, transaction_type, currency, price)
      #print "dbQuery : "
      #print dbQuery
   
      self.c.execute(dbQuery)

      # Save (commit) the changes
      self.conn.commit()

   def get_price(self, exchange, transaction_type, currency):
      return 0

   # We can also close the connection if we are done with it.
   # Just be sure any changes have been committed or they will be lost.
   def close(self):
      self.conn.close()
      self.initialized = False

   
   def get_minimum_buy_arbitrage_percent(self):
      #Need to give exchange1 and exchange2 as parameters when supporting multiple exchanges.
      dbQuery = "SELECT ArbitragePrice FROM CurrentArbitrage where TransactionType = 0;" # % (TRANSACTION_BUY)
      self.c.execute(dbQuery)
      minbuy = self.c.fetchone()[0]
      dbQuery = "SELECT CurrencyCode FROM CurrentArbitrage where TransactionType = 0;" # % (TRANSACTION_BUY)
      self.c.execute(dbQuery)
      buycurrency = str(self.c.fetchone()[0])
      return minbuy, buycurrency

   def get_maximum_sell_arbitrate_percent(self):
      dbQuery = "SELECT ArbitragePrice FROM CurrentArbitrage where TransactionType = 1;" # % (TRANSACTION_SELL)
      self.c.execute(dbQuery)
      maxsell = self.c.fetchone()[0]

      dbQuery = "SELECT CurrencyCode FROM CurrentArbitrage where TransactionType = 1;" # % (TRANSACTION_BUY)
      self.c.execute(dbQuery)
      sellcurrency = str(self.c.fetchone()[0])

      return maxsell, sellcurrency 

if __name__ == "__main__":
   dbutil = DatabaseUtils()
   #dbutil.set_current_price("koinex", TRANSACTION_SELL, "LTC", 90)
   #dbutil.set_current_arbitrage("koinex", "gdax", TRANSACTION_SELL, "LTC", 5)
   print "buy:"
   print dbutil.get_minimum_buy_arbitrage_percent()
   print "sell:"
   print dbutil.get_maximum_sell_arbitrate_percent()
   dbutil.close()


