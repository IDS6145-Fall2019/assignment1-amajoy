#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:53:36 2019

@author: Amanda
"""


import matplotlib.pyplot as plt
import numpy as np
import chaospy as cp

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

plt.show()
plt.savefig('1DPD_RNG_Pseudo.png')


#Quasi-Randomness
#Uniform Distribution 


plt.subplot(3, 5, 1)
uniform = cp.J(cp.Uniform(0,1))
x100 = uniform.sample(100,rule="S")
plt.hist(x100, density=True, bins=30)
plt.title("N=100")
plt.ylabel("Uniform")
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 2)
uniform = cp.J(cp.Uniform(0,1))
x500 = uniform.sample(500,rule="S")
plt.hist(x500, density=True, bins=30)
plt.title("N=500")
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 3)
uniform = cp.J(cp.Uniform(0,1))
x1k = uniform.sample(1000,rule="S")
plt.hist(x1k, density=True, bins=30)
plt.title("N=1000")
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 4)
uniform = cp.J(cp.Uniform(0,1))
x2k = uniform.sample(2000,rule="S")
plt.hist(x2k, density=True, bins=30)
plt.title("N=2000")
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 5)
uniform = cp.J(cp.Uniform(0,1))
x5k = uniform.sample(5000,rule="S")
plt.hist(x5k, density=True, bins=30)
plt.title("N=5000")
plt.yticks([])
plt.xticks([])




#Exponential Distribution




plt.subplot(3, 5, 6)
uniform = cp.J(cp.Exponential())
x100 = uniform.sample(100,rule="S")
plt.hist(x100, density=True, bins=30)
plt.ylabel("Exponential")
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 7)
uniform = cp.J(cp.Exponential())
x500 = uniform.sample(500,rule="S")
plt.hist(x500, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 8)
uniform = cp.J(cp.Exponential())
x1k = uniform.sample(1000,rule="S")
plt.hist(x1k, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 9)
uniform = cp.J(cp.Exponential())
x2k = uniform.sample(2000,rule="S")
plt.hist(x2k, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 10)
uniform = cp.J(cp.Exponential())
x5k = uniform.sample(5000,rule="S")
plt.hist(x5k, density=True, bins=30)
plt.yticks([])
plt.xticks([])



#Normal Distribution - I can't find any binomial distrobution docs Sad face

plt.subplot(3, 5, 11)
uniform = cp.J(cp.Normal(0,1))
x100 = uniform.sample(100,rule="S")
plt.hist(x100, density=True, bins=30)
plt.ylabel("Normal")
plt.yticks([])
plt.xticks([])





plt.subplot(3, 5, 12)
uniform = cp.J(cp.Normal(0,1))
x500 = uniform.sample(500,rule="S")
plt.hist(x500, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 13)
uniform = cp.J(cp.Normal(0,1))
x1k = uniform.sample(1000,rule="S")
plt.hist(x1k, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 14)
uniform = cp.J(cp.Normal(0,1))
x2k = uniform.sample(2000,rule="S")
plt.hist(x2k, density=True, bins=30)
plt.yticks([])
plt.xticks([])




plt.subplot(3, 5, 15)
uniform = cp.J(cp.Normal(0,1))
x5k = uniform.sample(5000,rule="S")
plt.hist(x5k, density=True, bins=30)
plt.yticks([])
plt.xticks([])

plt.show()
plt.savefig("Plotting_1D_RNG_Quasi.png")
