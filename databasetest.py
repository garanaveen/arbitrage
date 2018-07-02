#!/usr/bin/env python


import sqlite3
import projectconfig as cfg

if __name__ == "__main__":

   
   DB_FILE = cfg.ROOT_PATH + "PriceHistory.db"
   conn = sqlite3.connect(DB_FILE)

   c = conn.cursor()

   # Create table
   #c.execute('''CREATE TABLE stocks
   #             (date text, trans text, symbol text, qty real, price real)''')


   #TODO : Check if the file is present before trying to open it. If the file is not present, throw an error to user.

   SQL_FILE = cfg.ROOT_PATH + "PriceHistory.sql"
   file_object  = open(SQL_FILE, mode='r')
   with file_object as f:
      c.executescript(f.read())

   # Insert a row of data
   c.execute("INSERT INTO PriceHistory VALUES ('KOINEX', 1, '2006-01-05','LTC',172.35)")
   c.execute("INSERT INTO PriceHistory VALUES ('GDAX', 1, '2006-01-05','ETH',663.35)")
   c.execute("INSERT INTO PriceHistory VALUES ('KOINEX', 2, '2006-01-05','ETH',710.35)")
   c.execute("INSERT INTO PriceHistory VALUES ('GDAX', 2, '2006-01-05','LTC',163.35)")

   # Save (commit) the changes
   conn.commit()

   # We can also close the connection if we are done with it.
   # Just be sure any changes have been committed or they will be lost.
   conn.close()

