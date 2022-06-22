# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:02:59 2022

@author: adamm
"""

# traditional poly
#last elem = highest power
#first elem = lowest power ie x^0

trad_list = [1,2,3,4,5,6]

def trad(x,c):
    """ x is our x value.
        c is a list of coefficients"""
    #todo param validation
    
    pwr = 0;
    val = 0
    for i in range(len(c)):
        val += (x ** pwr) *(c[i])
        pwr += 1
    return val

def nest(x,c):
    """ x is our x value.
        c is a list of coefficients"""
    #todo param validation
    val = 0
    for i in range(len(c)-1,-1,-1):
        val *= x
        val += c[i]
    return val