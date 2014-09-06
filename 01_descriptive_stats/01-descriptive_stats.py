import pandas as pd
import datetime
import os
from calendar import monthrange

wd = '/Users/danielmsheehan/Desktop/tripData2013/' #work dir, create folder called day in your work dir

countByMonth = []

for i in range(1,13): 
	inCSV = wd+'trip_data_'+str(i)+'.csv'
	df = pd.read_csv(inCSV)
	theCount = len(df.index)
	print 'for month ' + str(i) + ', the count of taxi trips is:'
	print theCount
	x = monthrange(2013, i)
	daysInMonth = x[1]
	y = (theCount * 1.0)/daysInMonth  #mult times 1.0 so its a float result
	print 'month ' + str(i) + ' has ' + str(daysInMonth) + ' number of days, averaging ' + str(y) + ' taxi trips per day'
	countByMonth.append(theCount)

countByYear = sum(countByMonth)
print 'the total number of trips in the year is ' + str(countByYear)
z = (countByYear)/365.0  #mult times 1.0 so its a float result
print 'the average number of taxi trips per day is ' + str(z)