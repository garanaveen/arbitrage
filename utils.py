#!/usr/bin/env python


import json
import shutil
import wget
import os


#This is a global method and should probably reside in a common place like util.py
def readurl(url,outputFile = "ticker"):
	output = outputFile
	if os.path.exists(output):
	   os.remove(output)

	file = wget.download(url,output)
	f = open(file, 'r')
	htmlText = "\n".join(f.readlines())
	f.close()

	return json.loads(htmlText)


