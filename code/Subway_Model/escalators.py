#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:33:01 2019

@author: Amanda
"""

class escalators:
    ''' Escalators that move people in and out.'''

    def __init__(self, name, length, speed):
        '''Set the name and properties for the station.'''
        self.name = name
        self.length = length
        self.speed = speed
    
        