#!/usr/bin/env python

#Use this file to test out generic things on python

import projectconfig as cfg
import time
import os

if __name__ == "__main__":
   
   repo_myalerts_file = cfg.ROOT_PATH + "myalerts.ini"
   repo_myalerts_file_time = os.path.getctime(repo_myalerts_file)
   print ("repo_myalerts_file_time : ", repo_myalerts_file_time)

   home_myalerts_file = cfg.HOME_DIR + "/myalerts.ini"
   home_myalerts_file_time = os.path.getctime(home_myalerts_file)
   print ("home_myalerts_file_time : ", home_myalerts_file_time)

   if(repo_myalerts_file > home_myalerts_file):
      print ("repo_myalerts_file : ", repo_myalerts_file, "is the latest")
   else:
      print ("home_myalerts_file : ", home_myalerts_file, "is the latest")

   print (type(home_myalerts_file_time))

   if (1530111334.7842515 > 1530111663.7674978):
      print ("1530111334.7842515 is larger")
   else:
      print ("1530111663.7674978 is larger")


