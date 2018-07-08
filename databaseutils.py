#!/usr/bin/env python


import sqlite3
import projectconfig as cfg



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

   
   def set_price(self, exchange, transaction_type, currency, price):
      nowTimeStamp = '2018-07-08 00:00:00';
      dbQuery = "INSERT INTO PriceHistory VALUES ('%s', '%s', '%s','%s',%f)" % (exchange, transaction_type, nowTimeStamp, currency, price)
      print "dbQuery : "
      print dbQuery
   
      # Insert a row of data
      #c.execute("INSERT INTO PriceHistory VALUES ('GDAX', 2, '2006-01-05','LTC',163.35)")
      self.c.execute(dbQuery)

      # Save (commit) the changes
      self.conn.commit()

   # We can also close the connection if we are done with it.
   # Just be sure any changes have been committed or they will be lost.
   def close(self):
      self.conn.close()
      self.initialized = False

if __name__ == "__main__":
   dbutil = DatabaseUtils()
   dbutil.set_price("koinex", "sell", "LTC", 90)
   dbutil.close()
