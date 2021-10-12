# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp
import datetime # for adding time
import pytz # for timezone()
    
# using now() to get current time 
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 

#OPening a log file
log = open(scrp.headerVar.dataPath + "\\log.txt",'a')

def piper(S): #Prints the output to log file & stdout(terminal)
	global log
	log.write(S)
	scrp.print(S)

scrp.print = piper #set print commands in scrapingLIBSYS to use piper()

if __name__ == "__main__" : # Main Function
	scrp.CreateData_dir() # Creating Directory
	#print("\nhello2")
	UID = "2018122009"
	scrp.ScrapeUserData(UID)
	log.close()