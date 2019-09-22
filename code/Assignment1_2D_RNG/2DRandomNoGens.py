#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:54:35 2019

@author: Amanda
"""


import matplotlib.pyplot as plt
import random
import sobol_seq


#time to make plots - I can't figure out how to for loop this
#Pseudo-Random up top
    
plt.subplot(2, 5, 1)
x100 = [random.uniform(0,4) for x in range(100)]
y100 = [random.uniform(0,4) for x in range(100)]
plt.title("N=100")
plt.ylabel("Pseudo-Random")
plt.scatter(x100, y100, s=1, marker = '.')
plt.yticks([])
plt.xticks([])
    

plt.subplot(2, 5, 2)
x500 = [random.uniform(0,4) for x in range(500)]
y500 = [random.uniform(0,4) for x in range(500)]
plt.title("N=500")
plt.scatter(x500, y500, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 3)
x1k = [random.uniform(0,4) for x in range(1000)]
y1k = [random.uniform(0,4) for x in range(1000)]
plt.title("N=1000")
plt.scatter(x1k, y1k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 4)
x2k = [random.uniform(0,4) for x in range(2000)]
y2k = [random.uniform(0,4) for x in range(2000)]
plt.title("N=2000")
plt.scatter(x2k, y2k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 5)
x5k = [random.uniform(0,4) for x in range(5000)]
y5k = [random.uniform(0,4) for x in range(5000)]
plt.title("N=5000")
plt.scatter(x5k, y5k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


#Quasi-Random goes down here.  Fingers crossed.  

plt.subplot(2, 5, 6)
sobol_100_x = sobol_seq.i4_sobol_generate(4, 100)
x100 = sobol_100_x[:,0]
y100 = sobol_100_x[:,1]
plt.ylabel("Quasi Random")
plt.scatter(x100, y100, s=1, marker = '.')
plt.yticks([])
plt.xticks([])
    

plt.subplot(2, 5, 7)
sobol_500_x = sobol_seq.i4_sobol_generate(4, 500)
x500 = sobol_500_x[:,0]
y500 = sobol_500_x[:,1]
plt.scatter(x500, y500, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 8)
sobol_1000_x = sobol_seq.i4_sobol_generate(4, 1000)
x1k = sobol_1000_x[:,0]
y1k = sobol_1000_x[:,1]
plt.scatter(x1k, y1k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 9)
sobol_2000_x = sobol_seq.i4_sobol_generate(4, 2000)
x2k = sobol_2000_x[:,0]
y2k = sobol_2000_x[:,1]
plt.scatter(x2k, y2k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])


plt.subplot(2, 5, 10)
sobol_5000_x = sobol_seq.i4_sobol_generate(4, 5000)
x5k = sobol_5000_x[:,0]
y5k = sobol_5000_x[:,1]
plt.scatter(x5k, y5k, s=1, marker = '.')
plt.yticks([])
plt.xticks([])



plt.savefig("Plotting 2D RNG.png")



