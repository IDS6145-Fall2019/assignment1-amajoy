#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:53:36 2019

@author: Amanda
"""


import matplotlib.pyplot as plt
import numpy as np
#import chaospy as cp

#Pseudo-Random Uniform Distributions

plt.subplot(3, 5, 1)
x100 = [np.random.uniform(0,2,100)]
plt.title("N=100")
plt.ylabel("Uniform")
plt.hist(x100)
plt.yticks([])
plt.xticks([])
    
plt.subplot(3, 5, 2)
x500 = [np.random.uniform(0,2,500)]
plt.title("N=500")
plt.hist(x500)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 3)
x1k = [np.random.uniform(0,2,1000)]
plt.title("N=1000")
plt.hist(x1k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 4)
x2k = [np.random.uniform(0,2,2000)]
plt.title("N=2000")
plt.hist(x2k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 5)
x5k = [np.random.uniform(0,2,5000)]
plt.title("N=5000")
plt.hist(x5k)
plt.yticks([])
plt.xticks([])

#Pseudo-Random Exponential Distributions


plt.subplot(3, 5, 6)
x100 = [np.random.exponential(2,100)]
plt.ylabel("Exponential")
plt.hist(x100)
plt.yticks([])
plt.xticks([])
    
plt.subplot(3, 5, 7)
x500 = [np.random.exponential(2,500)]
plt.hist(x500)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 8)
x1k = [np.random.exponential(2,1000)]
plt.hist(x1k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 9)
x2k = [np.random.exponential(2,2000)]
plt.hist(x2k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 10)
x5k = [np.random.exponential(2,5000)]
plt.hist(x5k)
plt.yticks([])
plt.xticks([])


#Pseudo-Random Binomial Distribution


plt.subplot(3, 5, 11)
x100 = np.random.binomial(10, 0.5, 100)
plt.ylabel("Binomial")
plt.hist(x100)
plt.yticks([])
plt.xticks([])
    
plt.subplot(3, 5, 12)
x500 = np.random.binomial(10, 0.5, 500)
plt.hist(x500)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 13)
x1k = np.random.binomial(10, 0.5, 1000)
plt.hist(x1k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 14)
x2k = np.random.binomial(10, 0.5, 2000)
plt.hist(x2k)
plt.yticks([])
plt.xticks([])

plt.subplot(3, 5, 15)
x5k = np.random.binomial(10, 0.5, 5000)
plt.hist(x5k)
plt.yticks([])
plt.xticks([])


#Quasi-Random 



plt.savefig("Plotting 1D RNG.png")
