# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:48:07 2021

@author: shirish
"""

import scrapingLIBSYS as scrp
import scrape_Range as scrng
import sys #for arguments
import os

# Main Function
if __name__ == "__main__" :

	arguments = sys.argv #Arguments with which script is run
	argLen = len(sys.argv) #Length of Arguments with which script is run

	if argLen > 1 : # if arguments are more than 1 ie. more than file name that is run{arguments[0]}
		# UID Setup
		UID_start = int(arguments[1])
		UID_end   = int(arguments[2])
		if argLen >= 4 : #if argument length is 4, which means logFile's name is passed
			scrp.headerVar.logName = str(arguments[3])
	else : #Default Range UID Setup
		UID_start = 2020101001 #first roll number
		UID_end   = 2020101002 #last roll number


	# Set UID Range
	if argLen >= 5 :  #if arguments have scrapeRange file name
		RangeFile_path = os.path.join(scrp.headerVar.ParentDir,str(arguments[4]))
		UID_range = scrng.getRange(RangeFile_path) #get the range iteratable
	else : # set Uid range using the values from the shell
		UID_range = range(UID_start,UID_end+1)


	#set print commands in scrapingLIBSYS to use piper() in ScrapeLogger
	scrp.print = scrp.scplg.piper

	# Creating Data Directory
	scrp.CreateData_dir()
	count_range = 0 #initialize iterator to go through UIDs

	SkipNumUID = 100 #Number of UID's to be skipped

	#Initialize counter that counts how many time UID is invalid consecutively.
	counter_InvalidUID = 0

	#Number of times the UID allowed to be invalid consecutively before skipping
	SkipThreshold = 5 + 1

	while count_range < len(UID_range): #Iterate though UIds
		# Assign User ID
		UID = UID_range[count_range]

		#Scraping Data for UID
		status_Scrape = scrp.ScrapeUserData(str(UID))

		#Increment the Iterator
		count_range += 1

		if status_Scrape == scrp.err.SITE_DOWN: #if website is down
			print("!==Terminal Message: Website is Down")
			break
		elif status_Scrape == scrp.err.INVALID_UID : #Invalid User ID, delete directory
			#scrp.DeleteUser_dir(UID)
			print("!==Terminal Message: INVALID UID")
			counter_InvalidUID += 1 #Increment number of Invalid UID counter by 1

			if counter_InvalidUID == SkipThreshold : # number of invalid uids encountered reaches SkipThreshold value
				count_range = ((count_range-1) - (counter_InvalidUID-1)) + SkipNumUID
				counter_InvalidUID = 0
		else : #in case of Scraped some data
			counter_InvalidUID = 0
			pass

	#Closing Log File
	scrp.scplg.closeLog()
