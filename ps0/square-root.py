#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:55:14 2020

@author: feujio
"""
import math

EPSILON = 0.001
error = math.inf
x = 16

g = int(input("Start with a guess: "))

while (error > EPSILON):
    square = g*g
    error = x - square
    print("error: " + str(error))
    if error <= EPSILON:
        print(f"The answer is: {g}")
        break
    else:
        g = (g + x/g)/2