#!/usr/bin/env python

import json
import shutil
import wget
import os
import projectconfig as cfg

#TODO : Handle invalid json file

def readurl(url,outputFile = "ticker"):
   output = outputFile

   file = output
   if cfg.livequote:
      if os.path.exists(output):
         os.remove(output)

      file = wget.download(url,output)

   f = open(file, 'r')
   htmlText = "\n".join(f.readlines())
   f.close()

   return json.loads(htmlText)

