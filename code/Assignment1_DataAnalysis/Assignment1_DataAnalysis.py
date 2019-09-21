# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

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

data.plot.hist()
