# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:58:01 2021

@author: RKSRIVASTAVA
"""

import requests
from bs4 import BeautifulSoup
import os

LIBSyURL = ('http://10.4.20.51:8380/opac/')
loginurl = ('http://10.4.20.51:8380/opac/OpacKiosk')
secure_url = ('http://10.4.20.51:8380/opac/myaccount/myAccount.html')

username = password = '2021101001'
#password = '2018122009'


url_BookIssueHistory = ('http://10.4.20.51:8380/opac/myaccount/history.html')
url_FineLog = ('http://10.4.20.51:8380/opac/myaccount/log.html')
url_Profile = ('http://10.4.20.51:8380/opac/myaccount/myProfile.html')
url_LoginHist = ('http://10.4.20.51:8380/opac/myaccount/loginHistory.html')
url_redirectSrch = ('http://10.4.20.51:8380/opac/search/search.html')

# paylaod to send to server
payload = {
	'_rqst': '13',
	'OPAC_USERID': username,
	'PSWD': password,
	'staffLoginRequired':'false',
	'institution':'unchecked',
	'userSiteID':'99',
	'secAuthVal':'',
	'answer':''
	}


with requests.Session() as s: #start session
	r0 = s.get(LIBSyURL)
	print("->Visiting OPAC to set cookies " + str(r0))
	r1 = s.post(loginurl,data=payload)
	print("->login response\n" + r1.text)

# 	r3 = s.post(loginurl, data=payload2)
# 	print(r3.text)
# 	r4 = s.post(loginurl, data=payload3)
# 	print(r4.text)
	r2 = s.get(url_Profile)
	print("->Profile Page visit " + str(r2))

	soup = BeautifulSoup(r2.content, 'html.parser')
	#print(soup.prettify())
	f = open("Profile.html",'w')
	f.write(r2.text)
	f.close()

	r3 = s.get(url_BookIssueHistory)
	print("->Book History visit " + str(r3))

	f = open("BookHistory.html",'a')
	print = f.write
	f.write(r3.text)
	print("helloe")
	f.close()


