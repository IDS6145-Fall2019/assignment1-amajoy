#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:02:27 2019

@author: Amanda
"""

class trains:
    ''' Trains that bring passengers to stations '''

    def __init__(self, name, line, cars):
        '''Set the name and vertices of the shape'''
        self.name = name
        self.line = line
        self.cars = cars


    def __str__(self):
        '''Definition for the print statement'''
        return "trains: '{}' of type ({}) has {} cars.".format(
            self.name,str(self.__class__.__name__),
            str(self.subwaycars))
    
        


