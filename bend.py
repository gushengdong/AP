#!/usr/bin/python
#Filename: bend.py

import math

def sbend(alpha, length,Dx, Dpx):
    #alpha define the deflection angle(radian)
    #rho define the deflection radius(meter)
    #the rho is >0 or <0

    #h = 1 / abs(rho) * alpha / abs(alpha)
    rho = length / alpha
    kx = 1 / abs(rho)
    ky = 0
    s = rho * abs(alpha)
    a = math.sin(kx * s)
    b = math.cos(kx * s)
    rx11 = b
    rx12 = a / kx
    rx21 = -1 * kx * a
    rx22 = b
    ry11 = 1
    ry12 = s
    ry21 = 0
    ry22 = 1
    Rx = (rx11, rx12, rx21, rx22) 
    Ry = (ry11, ry12, ry21, ry22)
    Dx = rx11 * Dx + rx12 * Dpx + kx **3 * (1 - b)
    Dpx = rx21 * Dx + rx22 * Dpx + kx ** 2 * a
    return Rx, Ry,  Dx, Dpx
