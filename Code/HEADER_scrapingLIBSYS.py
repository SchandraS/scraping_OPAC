# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:22:39 2021

@author: shirish
"""
# Important URL's
loginurl = ('http://10.4.20.51:8380/opac/OpacKiosk')
secure_url = ('http://10.4.20.51:8380/opac/myaccount/myAccount.html')
LIBSyURL = ('http://10.4.20.51:8380/opac/')

#post request
#_rqst=13&OPAC_USERID=2018122009&PSWD=82a3b4dcc3aadc184d91adb6c863dcba08237fbe08aed70b511ff367d3dd96af&staffLoginRequired=false&institution=unchecked&userSiteID=99&secAuthVal=&answer=&tokenId=C7B4K0H1B5F5I2W8

#data urls
url_BookIssueHistory = ('http://10.4.20.51:8380/opac/myaccount/history.html')
url_FineLog = ('http://10.4.20.51:8380/opac/myaccount/log.html')
url_Profile = ('http://10.4.20.51:8380/opac/myaccount/myProfile.html')
url_LoginHist = ('http://10.4.20.51:8380/opac/myaccount/loginHistory.html')
url_BookCart = ('http://10.4.20.51:8380/opac/myaccount/showCart.html')
url_Reservations = ('http://10.4.20.51:8380/opac/myaccount/reservations.html')
url_Checkout = ('http://10.4.20.51:8380/opac/myaccount/checkout.html')

# Directory variables
newDir = "Data"
ParentDir = "C:\\Users\\RKSRIVASTAVA\\Documents\\Python Scripts\\scraping_OPAC"
dataPath = ParentDir + "\\" + newDir
# dataPath = os.path.join(ParentDir,newDir)
logFile = ParentDir + "\\" + "log.txt"
