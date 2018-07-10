#!/usr/bin/env python

import sqlite3
import projectconfig as cfg


def create_db_if_not_exists():
   pass
   

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
   c.execute("REPLACE INTO CurrentPrice VALUES ('koinex', 1, 'LTC',272.35)")
   #c.execute("INSERT INTO CurrentPrice VALUES ('koinex', 1, 'LTC',172.35)")
   #c.execute("UPDATE CurrentPrice set Price  = 92 where Exchange = 'koinex' and TransactionType = 1 and CurrencyCode = 'LTC'")

   # Save (commit) the changes
   conn.commit()

   # We can also close the connection if we are done with it.
   # Just be sure any changes have been committed or they will be lost.
   conn.close()

