# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:26:55 2021

@author: shirish
"""

import HEADER_scrapingLIBSYS as headerVar
import datetime # for adding time
import pytz # for timezone()

#Initialize Logger file GLOBAL variable
log = None


def getTime(): # function to get current time in IST
	return datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

def openLog():#Opening a log file
	global log
	log =  open(headerVar.logFile,'a') #return file variable
	piper("\n#Log File Opened at: " + str(getTime()) + "\n")
	return log

def piper(S): #Prints the output to log file & stdout(terminal)
	global log
	log.write(S)
	print(S)

def closeLog(): #Closing Log File
	global log
	piper("\n#Log File Closed at: " + str(getTime()) + "\n\n")
	try : # to close the file
		log.close()
		print("\n\n!!!Log file closed {Message after running log.close()}")
	except: #not able to close
		print("\n\n!!!Log file NOT closed {Message after running log.close()}")

#set print commands in scrapingLIBSYS to use piper()
# scrp.print = piper
