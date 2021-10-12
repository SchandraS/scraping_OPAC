# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:26:55 2021

@author: shirish
"""

import HEADER_scrapingLIBSYS as headerVar
import datetime # for adding time
import pytz # for timezone()





def getTime(): # function to get current time in IST
	# using now() to get current time
	return datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

def openLog():#Opening a log file
	return open(headerVar.logFile,'a') #return file variable

def piper(S): #Prints the output to log file & stdout(terminal)
	log = openLog()
	global log
	log.write(S)
	print(S)

def closeLog(): #Closing Log File
	piper("\n#Log File Closed at:" + str(getTime()) + "\n\n")
	log.close()
	print("\n\n!!!Log file closed {Message after running log.close()}")

#set print commands in scrapingLIBSYS to use piper()
scrp.print = piper
