# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 03:13:36 2021

@author: shirish
"""
from itertools import chain

def getRange(filePath):
	"""
	gets the ranges from the specified file.
	And turns them, into a single iterable.

	Parameters
	----------
	filePath : TYPE string
		DESCRIPTION.
		Path to the file with ranges of Uid srch

	Returns
	-------
	usrRange : TYPE range()
		DESCRIPTION.
		iterable that contains all the ranges for the srch

	"""
	usrRange = []

	with open(filePath ,'r')  as rF:
		rangeF_lines = rF.readlines()
		for Rline in rangeF_lines:
			UIDs = Rline.split()
			uid_start = UIDs[0]
			uid_end   = UIDs[1]
			usrRange = chain(usrRange,range(int(uid_start),int(uid_end)+1))
	return usrRange




# usrRange = chain(range(2021201001,2021201099+1), range(2021202001,2021202099+1),\
# 				  range(2020202001,2020202099+1),range(2019101001,2019101150+1),\
# 					  range(2018101001,2018101150+1),range(2020101001,2020101150+1))


"""
Ranges Done-
2018121001-2018121020
2019121001-2019121020
2020121001-2020121020
2021121001-2021121020


2018122001-2018122020
2019122001-2019122020
2020122001-2020122020
2021122001-2021122020

2020201001,2020201099
2021201001,2021201099
2021202001,2021202099
2020202001,2020202099

2019101001,2019101150+1
2018101001,2018101150+1
2020101001,2020101150+1

"""
