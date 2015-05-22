#!/usr/bin/env python
#Filename:spacetest.py
#This program is made to calculate the space charge to the beam transverse

import numpy as np

def space(bunch,m,n,energy,realcharge):
		lenth = len(bunch)
		bunchnp = np.zeros((lenth,7),dtype = np.float)
		density = np.zeros((m+1,n+1),dtype = np.float)
		L = 0.0
		W = 0.0
		for i in range(0,lenth):
				for k in range(0,7):
						bunchnp[i,k] = bunch[i][k]
				if abs(bunchnp[i,1]) > L:
				  		L = abs(bunchnp[i,1])
				if abs(bunchnp[i,3]) > W:
				  		W = abs(bunchnp[i,3])
		dx = L * 2.0 / m
		dy = L * 2.0 / n
		for i in range(0,lenth):
				numx = int(bunch[i,1] / dx) 	
				numy = int(bunch[i,3] / dy) 	
				w1 =  bunch[i,1] / dx -  numx
				w2 =  bunch[i,3] / dy - numy
				density[numx,numy] += (1-w1) * (1-w2)
				density[numx+1,numy] += w1 * (1-w2)
				density[numx,numy+1] += (1-w1) * w2
				density[numx+1,numy+1] += w1 * w2
		fftden = np.zeros((m+1,n+1),dtype = np.float)
		for i in range(0,m+1):
				fftdeny[i,:] = np.fft(density[i,:]) 
		coe = np.zeros((n+1,3),dtype = np.float)
		for i in range(0,n+1):
				coe[i,0] = 1.0
				coe[i,1] = 1.0
				coe[i,2] = 2.0 + (np.pi * i * dx / L) ** 2  
		ul = np.zeros((n+1,2),dtype = np.float)
		ul[0,0] = coe[0,1]
		for i in range(1,n+1):
				ul[i,1] = coe[i,0] / ul[i-1,0]
				ul[i,0] = coe[i,1] - ul[i,1] * coe[i - 1,2] 
