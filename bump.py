#!/usr/bin/env python
#Filename:bump.py

import math

def theta(l1,l2,l3,l4,l5,l6,l7,l8,h,theta):
		theta1 = (h - (l3 / 2 + l4) * theta) /  (l1 / 2 + l3 / 2 + l2)
		theta2 = (1 + (l3 / 2 + l4) / (l1 / 2 + l3 / 2 + l2)) * theta - h /  (l1 / 2 + l3 / 2 + l2)
		theta4 = (h - (l6 / 2 + l5) * -1.0 * theta) /  (l8 / 2 + l6 / 2 + l7)
		theta3 = (1 + (l6 / 2 + l5) / (l8 / 2 + l6 / 2 + l7)) * -1.0 * theta - h /  (l8 / 2 + l6 / 2 + l7)
		#theta4 *= -1.0
		#theta3 *= -1.0 
		#theta4 = -1 * ((h - (l6 / 2 + l5) * -1.0 * theta) / (l8 / 2 + l6 / 2 + l7))
		#theta3 = -1 * ((1 + (l6 / 2 + l5) / (l7 / 2 + l6 / 2 + l7)) * -1.0 * theta - h /  (l7 / 2 + l6 / 2 + l7))
		return theta1,theta2,theta3,theta4

def bump(inject_num,inject_num_max,macro_num,x_max,betax,betay,alphax,alphay):

#the tradition funchtion
#		rho = 2.0 * macro_num  / x_max ** 2
#		x = ((2.0 * inject_num / inject_num_max * macro_num) / rho) ** 0.5
#		y = ((2.0 * (1.0 - float(inject_num) / inject_num_max) * macro_num) / rho) ** 0.5
#		hx = x_max - x
#		hy = x_max - y
#		thetax = 0.0
#		thetay = 0.0
#the moden function

		r = (float(inject_num) / inject_num_max * x_max ** 2) ** 0.5
		x = r * math.cos(inject_num * 0.875 * 2 * math.pi)
		y = (r ** 2 - x ** 2) ** 0.5
		PX = -1 * y
		PY = x
		px = (PX - alphax * x) / betax
		py = (PY - alphay * y) / betay
		hx = x_max - x
		hy = x_max - y
		thetax = -1.0 * px
		thetay = -1.0 * py
#print hx,thetax,hy,thetay
		return hx,thetax,hy,thetay

