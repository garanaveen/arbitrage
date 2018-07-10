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

   
   def set_current_price(self, exchange, transaction_type, currency, price):
      dbQuery = "REPLACE INTO CurrentPrice VALUES ('%s', '%s', '%s', %f)" % (exchange, transaction_type, currency, price)
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

if __name__ == "__main__":
   dbutil = DatabaseUtils()
   price = 90;
   while True:
      dbutil.set_current_price("koinex", TRANSACTION_SELL, "LTC", price)
      time.sleep(1)
      price = price+1
   dbutil.close()


