# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp
import datetime # for adding time
import pytz # for timezone()
import ErrorCode_scrapingLIBSYS as err

def getTime(): # function to get current time in IST
	# using now() to get current time
	return datetime.datetime.now(pytz.timezone('Asia/Kolkata'))


# Creating Directory
scrp.CreateData_dir()

#Opening a log file
log = open(scrp.headerVar.dataPath + "\\log.txt",'a')

def piper(S): #Prints the output to log file & stdout(terminal)
	global log
	log.write(S)
	print(S)

#set print commands in scrapingLIBSYS to use piper()
scrp.print = piper

#UID setup
UID_start = 2018122001 #first roll number
UID_end   = 2018122012 #last roll number

#UID Range
UID_range = range(UID_start,UID_end+1)

if __name__ == "__main__" : # Main Function
	for UID in UID_range: #Iterate though UIds
		piper("#Scraping started at IST:" + str(getTime()) + "\nFor User:" + str(UID) +'\n')

		#Scraping Data for UID
		status_Scrape = scrp.ScrapeUserData(str(UID))
		if status_Scrape == err.SITE_DOWN:
			print("!!!Terminal Message: Website is Down")
			break


	#Closing Log File
	piper("\n#Log File Closed at:" + str(getTime()) + "\n\n")
	log.close()
	print("\n\n!!!Log file closed {Message after running log.close()}")