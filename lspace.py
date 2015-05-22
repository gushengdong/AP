#!/usr/bin/env python
#Filename:lspace.py
#This program is made to calculate the space charge to the beam transverse
#The number of the grides m prefered to be 2**n

import numpy as np

def space(bunch,m,energy0,energy1,realnum,macronum,length,h):
		q = 1.0
		epsilon0 = 8.8541878e-12
		lenth = len(bunch)
		realcharge = realnum / macronum * 1.602e-19 #* 0.02 * 0.02 
		mass = 938.272046
		gamma0 = (energy0 + mass) / mass
		beta0 = (1.0 - 1.0 / gamma0 ** 2) ** 0.5
		gamma1 = (energy1 + mass) / mass
		beta1 = (1.0 - 1.0 / gamma1 ** 2) ** 0.5
		bunchnp = np.zeros((lenth,2),dtype = np.float)
		density = np.zeros(m,dtype = np.float)
		phaL = 0.00001
		for i in range(0,lenth):
				bunchnp[i,0] = bunch[i][5]
				bunchnp[i,1] = bunch[i][6]
				if abs(bunchnp[i,0]) > phaL:
				  		phaL = abs(bunchnp[i,0])
		ds = phaL * 2.0 / (m - 1.0) #/ h / np.pi / 2 * length
		for i in range(0,lenth):
				nums = int((bunchnp[i,0] + phaL) / ds) 	
				if nums == m - 1:
					nums -= 1
#print nums
#	nums -=1
#if bunchnp[i,0] < 0:
#					nums -= 1
#nums_ = nums + int(m / 2) 	
#	nums_ = nums - 1 	
				w1 =  (bunchnp[i,0] + phaL) / ds -  nums 
				density[nums] += (1-w1) 
				density[nums + 1] += w1
#		density[0] *= 2.0
#		density[m - 1] *= 2.0
#print density
		L = 2.0 * phaL / gamma0  / h / np.pi / 2 * length
		ds_r = L / (m-1.0)
#print ds_r
		for i in range(0,m):
#density[i] = realcharge / 10000 / ds_r  * density[i] #/ epsilon0
				density[i] = realcharge  / ds_r  * density[i] / epsilon0 / 2.0 / np.pi / ds_r ** 2
#print density

		fftdens = np.zeros(m,dtype = np.float)
		for i in range(0,m):
#fftdens = np.fft.fft(density) * (-1 * L ** 2 / np.pi ** 2 / m ** 2) 
				fftdens = np.fft.fft(density) * (-1 * L ** 2 / np.pi ** 2 / (i + 1.0) ** 2) 
		phas = np.fft.ifft(fftdens)
#print np.fft.ifft(np.fft.fft(phas) / (-1 * L ** 2 / np.pi ** 2 / (i + 1.0) ** 2))
		phas = phas.real
#print phas
		Ei = np.zeros(m,dtype = np.float)
		for i in range(0,m - 1):
				Ei[i] = -1 * (phas[i+1] - phas[i]) / ds_r / gamma0 ** 2
#print Ei

		for i in range(0,lenth):
				nums = int(bunchnp[i,0] / ds) + int(m / 2) 	
				detaE = bunch[i][6] * beta1 ** 2 * energy1
				bunch[i][6] = (detaE + energy0 +  q * Ei[nums] * length / 1.0e6 - energy1) / energy1 / beta1 ** 2
#bunchnp[i,1] = realnum / lenth * q * Ei[nums] / gamma1 ** 2 * length #this is for the full ring,it should be changed latter
#	for i in range(0,lenth):
#				bunch[i][6] =  bunchnp[i,1]
		return bunch
