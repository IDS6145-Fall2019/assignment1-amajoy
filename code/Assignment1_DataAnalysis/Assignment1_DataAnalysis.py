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

print("Exit means are" + " " + str(exitsmean))
print("Exit standard deviation is" + " " + str(exitsstdv))


#please baby jesus let this graph things
#data.plot.hist(data.groupby("Station").nunique())

#can I show this as entries and exits per station?  Here goes. 
countbystation = data.groupby("Station").nunique()
pd.options.display.max_rows=380
print("This is the count by station" + " " + str(countbystation))
StationCount = data["Station"].nunique()
print("The number of stations is" + " " + str(StationCount))

#use the above to get the stations with escalators entry/exit for plotting

hvstations = ["Brighton", "63rd", "8 Av", "Archer Av", "Fulton", 
              "42nd St", "Broadway at 7th", "Flushing"]
avgperblockentries = [2496, 2403, 2525, 1999, 13542, 10918,1238, 2315]
avgperblockexits = [2499, 2349, 2511, 2048, 13623, 10917,1238, 2412]


#Trying so hard to make graphs - THEY WORK!!!! Don't delete this Amanda
plt.figure(figsize=(18, 6))
plt.title("Mean Entries per Time Block by Station")
plt.bar(hvstations, avgperblockentries)
plt.savefig("EntriesxTimeBlock.png")

plt.figure(figsize=(18, 6))
plt.title("Mean Exits per Time Block by Station")
plt.bar(hvstations,avgperblockexits)
plt.savefig("ExitsxTimeBlock.png")


#Too many returns - let's take a random sample
#sample = data.sample(frac=0.25)
#samplebystation = sample.groupby("Station").nunique()
#print("This is a random sample count by station" + " " + str(samplebystation))


#entrymeans = data.groupby(["Station", "Entries"]).mean()
#exitmeans = data.groupby(["Station", "Exits"]).mean()

#print(enterbystationsum)
#print(exitbystationsum)

#entriesgrouped = data.groupby("Station", "Entries")
#for group in entriesgrouped:
#  plt.figure()
#  plt.hist(group["Station"].entriesgroup)
#  plt.show()


#data.reset_index().pivot('index','Station','Entries').hist()
#
#
#for i in data["Entries"]:
#    #data["Entries"].
#    plt.hist(data["Entries"],by=data["Station"])



#failed attempt at graphs graveyard of hell
#plt.hist(x=samplebystation)
#data.plot.scatter(x="Entries", y = StationCount)


#let's try this for funsies. 
#data.plot(kind="bar",x="Station",y="Entries",color='blue')





