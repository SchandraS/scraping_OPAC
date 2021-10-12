# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp


# Main Function
if __name__ == "__main__" :

	#set print commands in scrapingLIBSYS to use piper() in ScrapeLogger
	scrp.print = scrp.scplg.piper

	#Open Log file
	scrp.scplg.openLog()

	# Creating Data Directory
	scrp.CreateData_dir()

	#UID setup
	UID_start = 2018122001 #first roll number
	UID_end   = 2018122012 #last roll number
	
	#UID Range
	UID_range = range(UID_start,UID_end+1)


	for UID in UID_range: #Iterate though UIds
		#Scraping Data for UID
		status_Scrape = scrp.ScrapeUserData(str(UID))

		if status_Scrape == scrp.err.SITE_DOWN: #if website is down
			print("!!!Terminal Message: Website is Down")
			break
		elif status_Scrape == scrp.err.INVALID_UID : #Invalid User ID, delete directory
			scrp.DeleteUser_dir(UID)

	#Closing Log File
	scrp.scplg.closeLog()