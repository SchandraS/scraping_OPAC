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

#%%
def CreateData_dir():# Setup Directory to Store Scrapped Data from website
	try: #creating directory for Data
		os.mkdir(headerVar.dataPath)
	except:
		print("Data directory already exists")
#%%
def ScrapeUserData(UsrID):# User Payload and data Directory Setup
	
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
	
	#r =requests.post(loginurl, data=payload)
	#print(r.text)
	#%% Setup Directory for Current User
	userPath = headerVar.dataPath +'//'+ str(username) #path for current user directory
	
	try: #create directory for Current User
		os.mkdir(userPath)
	except:
		print("user directory already exists")
	
	
	#%% Login & Scraping
	with requests.Session() as s: #Start session
	
		try: #Visit HomePage to set cookies
			r0 = s.get(headerVar.LIBSyURL)
			print("->Visiting OPAC to set cookies " + str(r0))
		except : #not able to visit page.
			print("!Error: Not able to visit OPAC, VPN not connected or site down")
			return  err.SITE_DOWN #break over here and exit


		try: #Connect to server and authenticate
			r1 = s.post(headerVar.loginurl,data=payload)
			print("->login response\n" + r1.text)
			if "_loginError" in r1.text:
				print("!WARNING:invalid userID or user does not exist")
				return err.INVALID_UID #break from here
		except : #Not able to Connect
			print("->not able to post to server")
			return err.SERVER_POSTREQ_DOWN

	
	#%% Visit Pages and Get Data
		try: #Get the data pages from OPAC
			r_BookHist = s.get(headerVar.url_BookIssueHistory)
			print("->Book History visit " + str(r_BookHist))
	
			r_FineLog = s.get(headerVar.url_FineLog)
			print("->Fine Log History visit " + str(r_FineLog))
	
			r_Profile = s.get(headerVar.url_Profile)
			print("->Profile visit " + str(r_Profile))
	
			r_LoginHist = s.get(headerVar.url_LoginHist)
			print("->Login History visit " + str(r_LoginHist))
	
			r_BookCart = s.get(headerVar.url_BookCart)
			print("->Book Cart visit " + str(r_BookCart))
	
			r_Reservations = s.get(headerVar.url_Reservations)
			print("->Reservations visit " + str(r_Reservations))
	
			r_Checkout = s.get(headerVar.url_Checkout)
			print("->Checkout visit " + str(r_Checkout))
		except: #not able to fetch it
			print("!ERROR:Not able to fetch data form Data Pages on OPAC")
	
	
	#%% Save Data in File.
		try: #Write data to file
			with open(userPath + '//BookHist.html','w') as BookHist:
				BookHist.write(r_BookHist.text)
				print("->Book History written ")
		
			with open(userPath + '//FineLog.html','w') as FineLog:
				FineLog.write(r_FineLog.text)
				print("->Fine Log History written ")
		
			with open(userPath + '//Profile.html','w') as Profile:
				Profile.write(r_Profile.text)
				print("->Profile written ")
		
			with open(userPath + '//LoginHist.html','w') as LoginHist:
				LoginHist.write(r_LoginHist.text)
				print("->Login History written ")
	
			with open(userPath + '//BookCart.html','w') as BookCart:
				BookCart.write(r_BookCart.text)
				print("->Book Cart written ")
	
			with open(userPath + '//Reservations.html','w') as Reservations:
				Reservations.write(r_Reservations.text)
				print("->Reservations written ")
	
			with open(userPath + '//Checkout.html','w') as Checkout:
				Checkout.write(r_Checkout.text)
				print("->Checkout written ")
		except: #Was not Able to write Data to file
			print("!ERROR: Not able to write DATA to file")