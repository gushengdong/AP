#!/usr/bin/python
#Filename: elements.py

import math

def sbend(bunch,l,angle,e1,e2,r1,r2):
		#l is the length
		#angle is the bend angle
		#e1,e2 is the edge angle in and out
		lenth = len(bunch)
		rho = l / angle
		a = math.tan(e1)
		rx21 = a / abs(rho)
		ry21 = -rx21
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx12 = 0.0
		ry12 = 0.0
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
	
		a = math.sin(angle)
		b = math.cos(angle)
		rx11 = b
		rx12 = a * rho 
		rx21 = -1.0 * a / rho
		rx22 = b
		ry11 = 1.0
		ry12 = l
		ry21 = 0.0
		ry22 = 1.0
		Dx = abs(l / angle) **3 * (1.0 - b)
		Dpx = abs(l / angle) ** 2 * a
		for i in range(0,lenth):
				p = bunch[i]
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2] + Dx * p[6],rx21 * p[1] + rx22 * p[2] + Dpx * p[6],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p

		a = math.tan(e2)
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx12 = 0.0
		ry12 = 0.0
		rx21 = a / abs(rho)
		ry21 = -rx21
		for i in range(0,lenth):
				p = bunch[i]
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
		i = 0
		bunch_lose = list()
		for k in bunch:
				p = bunch[i]
#if p[1] > r1 or p[3] > r2:
				if (p[1]) ** 2 / r1 ** 2  + (p[3]) ** 2 / r2 ** 2 > 1.0:
					bunch_lose.append(p) 
					del bunch[i]
					i -= 1
				i += 1
		return bunch,bunch_lose

def quad(bunch,l,k1,r1,r2):
	lenth = len(bunch)
	k = (abs(k1)) ** 0.5
	a = math.sin(k * l)
	b = math.cos(k * l)
	c = math.sinh(k * l)
	d = math.cosh(k * l)
	if k1 > 0:
		rx11 = b
		rx12 = a / k
		rx21 = -1.0 * a * k
		rx22 = b
		ry11 = d
		ry12 = c / k
		ry21 = k * c
		ry22 = d
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
	else:
		rx11 = d
		rx12 = c / k
		rx21 = k * c
		rx22 = d
		ry11 = b
		ry12 = a / k
		ry21 = -1.0 * a * k
		ry22 = b
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
	i = 0
	bunch_lose = list()
	for k in bunch:
			p = bunch[i]
#	if p[1] > r1 or p[3] > r2:
			if (p[1]) ** 2 / r1 ** 2  + (p[3]) ** 2 / r2 ** 2 > 1.0:
				bunch_lose.append(p) 
				del bunch[i]
				i -= 1
			i += 1
	return bunch,bunch_lose
	
def hkick(bunch,l,angle,r1,r2):
		lenth = len(bunch)
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx21 = 0.0
		ry21 = 0.0
		rx12 = l / 2.0
		ry12 = l / 2.0
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				angle = angle #* (1 + p[6])
				p[2] += angle	
				bunch[i] = p
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx21 = 0.0
		ry21 = 0.0
		rx12 = l / 2.0
		ry12 = l / 2.0
		for i in range(0,lenth):
				p = bunch[i]
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
		i = 0
		bunch_lose = list()
		for k in bunch:
				p = bunch[i]
#	if p[1] > r1 or p[3] > r2:
				if (p[1]) ** 2 / r1 ** 2  + (p[3]) ** 2 / r2 ** 2 > 1.0:
					bunch_lose.append(p) 
					del bunch[i]
					i -= 1
				i += 1
		return bunch,bunch_lose
def vkick(bunch,l,angle,r1,r2):
		lenth = len(bunch)
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx21 = 0.0
		ry21 = 0.0
		rx12 = l / 2.0
		ry12 = l / 2.0
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				angle = angle #* (1 + p[5])
				p[4] += angle	
				bunch[i] = p
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx21 = 0.0
		ry21 = 0.0
		rx12 = l / 2.0
		ry12 = l / 2.0
		for i in range(0,lenth):
				p = bunch[i]
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
		i = 0
		bunch_lose = list()
		for k in bunch:
				p = bunch[i]
#if p[1] > r1 or p[3] > r2:
				if (p[1]) ** 2 / r1 ** 2  + (p[3]) ** 2 / r2 ** 2 > 1.0:
					bunch_lose.append(p) 
					del bunch[i]
					i -= 1
				i += 1
		return bunch,bunch_lose
def drift(bunch,l,r1,r2):
		lenth = len(bunch)
		rx11 = 1.0
		ry11 = 1.0
		rx22 = 1.0
		ry22 = 1.0
		rx21 = 0.0
		ry21 = 0.0
		rx12 = l
		ry12 = l
		for i in range(0,lenth):
				p = bunch[i]
				p[0] += l
				p[1],p[2],p[3],p[4] = rx11 * p[1] + rx12 * p[2],rx21 * p[1] + rx22 * p[2],ry11 * p[3] + ry12 * p[4],ry21 * p[3] + ry22 * p[4]
				bunch[i] = p
		i = 0
		bunch_lose = list()
		for k in bunch:
				p = bunch[i]
##if p[1] > r1 or p[3] > r2:
				if (p[1]) ** 2 / r1 ** 2  + (p[3]) ** 2 / r2 ** 2 > 1.0:
					bunch_lose.append(p) 
					del bunch[i]
					i -= 1
				i += 1
		return bunch,bunch_lose
def readpar(s):
		f1 = open(s)
		bunch = list()
		line = f1.readline()
		while line:
			t = line.split()
			b = list()
			for k in range(0,7):
				b.append(float(t[k]))
			bunch.append(b)
		 	line = f1.readline()
		f1.close()
		return bunch
def dumppar(bunch,s):
		f1 = open(s,'w')
		lenth = len(bunch)
		for i in range(0,lenth):
				for k in range(0,7):
						f1.write(str(bunch[i][k]))
						f1.write('\t')
				f1.write('\n')
		f1.close()
def acc(bunch,v1,v2,pha2,energy0,energy1,h,h2):
		bunch_lose = list()
		lenth = len(bunch)
		mass = 938.272046
		gamma0 = (energy0 + mass) / mass
		beta0 = (1.0 - 1.0 / gamma0 ** 2) ** 0.5
		gamma1 = (energy1 + mass) / mass
		beta1 = (1.0 - 1.0 / gamma1 ** 2) ** 0.5
		for i in range(0,lenth):
#bunch[i][6] = (detaE + energy0 + v1 * math.sin(bunch[i][5]) + v2 * math.sin(h2 / h * bunch[i][5] - pha2) - energy1) / energy1 / beta1 ** 2
#bunch[i][6] = bunch[i][6] + v1 / energy0 / beta0 ** 2 * ((math.sin(bunch[i][5]) - math.sin(pha0)) + r * (math.sin(pha20 + h2 / h * (bunch[i][5] - pha0)) - math.sin(pha20)))
				detaE = bunch[i][6] * beta1 ** 2 * energy1
				bunch[i][6] = (detaE + energy0 + v1 * math.sin(bunch[i][5]) + v2 * math.sin(h2 / h * bunch[i][5] - pha2) - energy1) / energy1 / beta1 ** 2
				energy = energy1 + detaE
				gamma = (energy + mass) / mass
				gamma_tr = 4.889739
				eta = 1.0 / gamma_tr ** 2 - 1.0 / gamma ** 2
				bunch[i][5] = bunch[i][5] + 2 * math.pi * h * eta * bunch[i][6]
		i = 0
		for k in bunch:
				p = bunch[i]
##if p[1] > r1 or p[3] > r2:
				if p[5] > math.pi or p[5] < -1.0 * math.pi:
					bunch_lose.append(p) 
					del bunch[i]
					i -= 1
				i += 1
		return bunch,bunch_lose
