#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:38:14 2019

@author: Amanda
"""


class elevators:
    ''' Elevators that move people in and out.'''

    def __init__(self, name, capacity, speed, height):
        '''Set the name and properties for the station.'''
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.height = height
        
        