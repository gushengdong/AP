#!/usr/bin/python
#Filename: quad.py

import math
def quadr(s0, G0, Brho0,n0):
	s = s0	#define the length of the quad
	G = G0	#define the gradient of the quad
	Brho = Brho0	#define the brho
	n = n0	#if a focusing quadrupole n>0 reverse n<0
	k = pow(abs(G / Brho),0.5)
	a = math.sin(k * s)
	b = math.cos(k * s)
	c = math.sinh(k * s)
	d = math.cosh(k * s)
	if n > 0:
		rx11 = b
		rx12 = a / k
		rx21 = -1 * a * k
		rx22 = b
		ry11 = d
		ry12 = c / k
		ry21 = k * c
		ry22 = d
	else:
		rx11 = d
		rx12 = c / k
		rx21 = k * c
		rx22 = d
		ry11 = b
		ry12 = a / k
		ry21 = -1 * a * k
		ry22 = b
	Rx = (rx11,rx12,rx21,rx22)
	Ry = (ry11,ry12,ry21,ry22)
	return Rx,Ry
