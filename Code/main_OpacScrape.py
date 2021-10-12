# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp
import datetime # for adding time
import pytz # for timezone()
# import os
# import shutil

def getTime(): # function to get current time in IST
	# using now() to get current time
	return datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

"""
"""
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


# Main Function
if __name__ == "__main__" :

	#UID setup
	UID_start = 2018122001 #first roll number
	UID_end   = 2018122012 #last roll number
	
	#UID Range
	UID_range = range(UID_start,UID_end+1)


	for UID in UID_range: #Iterate though UIds
		#piper("#Scraping started at IST:" + str(getTime()) + "\nFor User: " + str(UID) +'\n')

		#Scraping Data for UID
		status_Scrape = scrp.ScrapeUserData(str(UID))

		if status_Scrape == scrp.err.SITE_DOWN: #if website is down
			print("!!!Terminal Message: Website is Down")
			break
		elif status_Scrape == scrp.err.INVALID_UID : #Invalid User ID
# 			piper("~~ UID Invalid, Deleting Directory for: " + str(UID)) #Log & Print
# 			UID_dir = os.path.join(scrp.headerVar.dataPath, str(UID)) #Path to UID directory
# 			shutil.rmtree(UID_dir, ignore_errors = False) #Delete Directory and FIles
# 			piper("~~ Directory Deleted:" + str(UID)) #Log & Print #Directory Deleted
			pass


# 	#Closing Log File
# 	piper("\n#Log File Closed at: " + str(getTime()) + "\n\n")
# 	log.close()
# 	print("\n\n!!!Log file closed {Message after running log.close()}")