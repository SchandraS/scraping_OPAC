# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp

log = open(scrp.headerVar.dataPath + "\\log.txt",'a')

def piper(S): #Pipes the output two file
	global log
	log.write(S)
	scrp.print


scrp.print = piper #set print commands in scrapingLIBSYS to use piper()

if __name__ == "__main__" : # Main Function
	scrp.CreateData_dir() # Creating Directory
	print("\nhello2")
	log.close()