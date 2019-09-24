#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:19:04 2019

@author: Amanda
"""

class stations:
    ''' Stations that hold passengers, escalators, and trains.'''

    def __init__(self, name, esc, turn):
        '''Set the name and properties for the station.'''
        self.name = name
        self.escalators = esc
        self.turnstiles = turn

