#!/usr/bin/env python

#Use this file to test out generic things on python

import platform
import projectconfig as cfg

if __name__ == "__main__":
   print ("platform : ", platform.platform()) 
   print ("ROOT_PATH : ", cfg.ROOT_PATH)
   print ("FILE_PATH : ", cfg.FILE_NAME)
