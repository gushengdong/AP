#!/usr/bin/python
#Filename: edge.py

import math

def edger(beta,rho):
	#beta is the edge angle
	#rho is the curvature radius

	a = math.tan(beta)
	rx11 = 1
	ry11 = 1
	rx22 = 1
	ry22 = 1
	rx12 = 0
	ry12 = 0
	rx21 = a / abs(rho)
	ry21 = -rx21
	Rx = (rx11, rx12, rx21, rx22)
	Ry = (ry11, ry12, ry21, ry22)
	return Rx, Ry
