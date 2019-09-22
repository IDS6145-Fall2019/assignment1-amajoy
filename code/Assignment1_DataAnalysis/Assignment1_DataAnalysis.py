# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#please god let this import data
data = pd.read_csv("Turnstile_Usage_Data__2018.csv") 

#testing to make sure I have something in here
#data.head()
#print(data.head())

#making sure I have all bazillion lines in - or at least a lot of them
print("The data shape is"+ " " + str(data.shape))

#get descriptive statistics
dstats = data.describe()
print("The descriptive statistics are" + " " + str(dstats))

#checking descriptive statistics the long way
entriesmean = data["Entries"].mean()
entriesstdv = data["Entries"].std()

print("Entry means are" + " " + str(entriesmean))
print("Entry standard deviation is" + " " + str(entriesstdv))

exitsmean = data["Exits"].mean()
exitsstdv = data["Exits"].std()
data
print("Exit means are" + " " + str(exitsmean))
print("Exit standard deviation is" + " " + str(exitsstdv))



#please baby jesus let this graph things
#data.plot.hist(data.groupby("Station").nunique())

#can I show this as entries and exits per station?  Here goes. 
countbystation = data.groupby("Station").nunique()
print("This is the count by station" + " " + str(countbystation))
StationCount = data["Station"].nunique()
print("The number of stations is" + " " + str(StationCount))



#failed attempt at graphs graveyard
#plt.hist(x=countbystation)
#data.plot.scatter(x="Entries", y = StationCount)


#let's try this
data.plot(kind="bar",x="Station",y="Entries",color='red')


