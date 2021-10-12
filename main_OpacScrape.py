# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp
log = open(scrp.headerVar.dataPath + "\\log.txt",'a')
f = open(scrp.headerVar.dataPath + "\\logger.txt",'a')
#print = f.write = log.write
#L = ["hellow1",'HEDHED']
#f.writelines(L)

if __name__ == "__main__" : # Main Function
	scrp.CreateData_dir() # Creating Directory
	print("\nhello2")
	log.close()
	f.close()