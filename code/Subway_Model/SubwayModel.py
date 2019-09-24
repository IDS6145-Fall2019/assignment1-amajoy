#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:54:55 2019

@author: Amanda
"""

#import math, time, _thread, sys, os


from station import stations
from trains import trains
from escalators import escalators
from people import people
from stairs import stairs
from elevators import elevators
from entrance import entrance






#def CreateStations(stations):
#    ''' Create some random stations'''
#    for i in range(0,20):
#        stations.append( escalators("Escalators {}".format(str(i)))
#
#    for i in range(0,50):
#        stations.append( stairs("Stairs {}".format(str(i))))
#
#    for i in range(0,5):
#        stations.append( elevators("Elevators {}".format(str(i))))


#
#
#def Simulate():
#    L = []
#    timestep = 0
#    _thread.start_new_thread(WaitForKeyPress, (L,))
#
#    while 1:
#        time.sleep(1) # delay for 1 second.
#        if L: break
#
#        print ("The timestep of the simulation is: {}".format(str(timestep)))
#        timestep+=1
#
#        if timestep%100 ==0: 
#            for c in containers:
#                c.waterReserve += thewater.Rain()
#
#        for c in containers:
#            for v in c.vegtables:
#                v.Grow()
#                c.nutrientReserve -= 2 * v.Volume()
#                c.waterReserve -= 8 * v.Volume()
#                if c.nutrientReserve <= 0.0 or c.waterReserve <= 0.0:
#                    v.Die()
#                    print("YOU KILLED YOUR PLANTS!!!!!")
#                    return
#            print("Container: Water Reserve {}, Nutrient Level {}".format(str(c.waterReserve),str(c.nutrientReserve)))
#
#
#
##Remember this method gets executed first since its our 'main'
#def main():
#
#    #Make some vegtables
#    veggies = []
#    CreatePlants(veggies)
#
#    #Print the Veggies
#    for v in veggies:
#        print(v)
#
#    global containers
#    containers.append( container(30, 200, gardenmixsoil("MySoil", 10.0, 20.0, 100.0), veggies) )
#
#    print("\nPress Any key to quit simulation...\n")
#    Simulate()
#
#
#
#if __name__ == "__main__":
#    main()