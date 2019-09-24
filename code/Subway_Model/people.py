#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:23:03 2019

@author: Amanda
"""

class people:
    ''' People that move through stations on escalators and stairs and elevators.'''

    def __init__(self, no, ps, hvy, ws):
        '''Set the name and properties for the station.'''
        self.randomnumber = no
        self.personalspace = ps
        self.heavybags = hvy
        self.walkorstand = ws
        