#!/usr/bin/python
#Filename: drift.py

def driftr(s):
    rx11 = 1.0
    ry11 = 1.0
    rx22 = 1.0
    ry22 = 1.0
    rx21 = 0.0
    ry21 = 0.0
    rx12 = s
    ry12 = s
    Rx = (rx11,rx12,rx21,rx22)
    Ry = (ry11,ry12,ry21,ry22)
    return Rx, Ry
