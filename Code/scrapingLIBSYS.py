# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 18:06:18 2021

@author: Shirish Chandra Srivastav 
email: shirish.chandra@research.iiit.ac.in
"""
"""
http://2018122009:2018122009@10.4.20.51:8380/opac/myaccount/myAccount.html
http://2018122009:2018122009@10.4.20.51:8380/opac/OpacKiosk

TODO:
ok	1. turn code into fucntions and modularize it
	2. add logging functionality     


"""
import requests
import os
import HEADER_scrapingLIBSYS as headerVar
import ErrorCode_scrapingLIBSYS as err
import shutil #remove directories
import ScrapeLogger as scplg






#%
def CreateData_dir():# Setup Directory to Store Scrapped Data from website
	if not os.path.isdir(headerVar.dataPath):#creating directory for Data
		os.mkdir(headerVar.dataPath)
		print("Data Directory created\n")
		return 0
	else : #print it already exists
		print("Data directory already exists\n")
		return 1


#%
def DeleteUser_dir(UID): # Delete the Given User's directory
	print("~~ UID Invalid, Deleting Directory for: " + str(UID)) #Log & Print
	UID_dir = os.path.join(headerVar.dataPath, str(UID)) #Path to UID directory
	shutil.rmtree(UID_dir, ignore_errors = False) #Delete Directory and FIles
	print("~~ Directory Deleted:" + str(UID)) #Log & Print #Directory Deleted
	return 0


#%
def ScrapeUserData(UsrID):# User Payload and data Directory Setup

	#Printing time of start
	print("#Scraping started at IST:" + str(scplg.getTime()) + "\nFor User: " + str(UsrID) +'\n')
	
	#username & password variable (run on a loop)
	username = password = UsrID #'2018122009'

	payload = {	# paylaod to send to server
		'_rqst': '13',
		'OPAC_USERID': username,
		'PSWD': password,
		'staffLoginRequired':'false',
		'institution':'unchecked',
		'userSiteID':'99',
		'secAuthVal':'',
		'answer':''
		}
	

	#% Setup Directory for Current User
	userPath = os.path.join(headerVar.dataPath,str(username)) #path for current user directory
	
	try: #create directory for Current User
		os.mkdir(userPath)
	except:
		print("User directory already exists\n")
	
	
	#% Login & Scraping
	with requests.Session() as s: #Start session
	
		try: #Visit HomePage to set cookies
			r0 = s.get(headerVar.LIBSyURL)
			print("->Visiting OPAC to set cookies " + str(r0) + '\n')
		except : #not able to visit page.
			print("!Error: Not able to visit OPAC, VPN not connected or site down\n")
			return  err.SITE_DOWN #break over here and exit


		try: #Connect to server and authenticate
			r1 = s.post(headerVar.loginurl,data=payload)
			print("->login response\n" + r1.text + '\n')
			if "_loginError" in r1.text:
				print("!WARNING:invalid userID or user does not exist\n")
				return err.INVALID_UID #break from here
		except : #Not able to Connect
			print("->not able to post to server\n")
			return err.SERVER_POSTREQ_DOWN

	
	#% Visit Pages and Get Data
		try: #Get the data pages from OPAC
			r_BookHist = s.get(headerVar.url_BookIssueHistory)
			print("->Book History visit " + str(r_BookHist) + '\n')
	
			r_FineLog = s.get(headerVar.url_FineLog)
			print("->Fine Log History visit " + str(r_FineLog) + '\n')
	
			r_Profile = s.get(headerVar.url_Profile)
			print("->Profile visit " + str(r_Profile) + '\n')
	
			r_LoginHist = s.get(headerVar.url_LoginHist)
			print("->Login History visit " + str(r_LoginHist) + '\n')
	
			r_BookCart = s.get(headerVar.url_BookCart)
			print("->Book Cart visit " + str(r_BookCart) + '\n')
	
			r_Reservations = s.get(headerVar.url_Reservations)
			print("->Reservations visit " + str(r_Reservations) + '\n')
	
			r_Checkout = s.get(headerVar.url_Checkout)
			print("->Checkout visit " + str(r_Checkout) + '\n')
		except: #not able to fetch it
			print("!ERROR:Not able to fetch data form Data Pages on OPAC\n")
	
	
	#% Save Data in File.
		try: #Write data to file
			with open(userPath + '//BookHist.html','w') as BookHist:
				BookHist.write(r_BookHist.text)
				print("->Book History written\n")
		
			with open(userPath + '//FineLog.html','w') as FineLog:
				FineLog.write(r_FineLog.text)
				print("->Fine Log History written\n")
		
			with open(userPath + '//Profile.html','w') as Profile:
				Profile.write(r_Profile.text)
				print("->Profile written\n")
		
			with open(userPath + '//LoginHist.html','w') as LoginHist:
				LoginHist.write(r_LoginHist.text)
				print("->Login History written\n")
	
			with open(userPath + '//BookCart.html','w') as BookCart:
				BookCart.write(r_BookCart.text)
				print("->Book Cart written\n")
	
			with open(userPath + '//Reservations.html','w') as Reservations:
				Reservations.write(r_Reservations.text)
				print("->Reservations written\n")
	
			with open(userPath + '//Checkout.html','w') as Checkout:
				Checkout.write(r_Checkout.text)
				print("->Checkout written\n")
		except: #Was not Able to write Data to file
			print("!ERROR: Not able to write DATA to file\n")