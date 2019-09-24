#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:39:51 2019

@author: Amanda
"""

class entrance:
    ''' Entrances allow people to move in and out of stations.'''

    def __init__(self, name, loc, kind):
        '''Set the name and properties for the station.'''
        self.name = name
        self.location = loc
        self.kindofentrance = kind

        