#!/usr/bin/env python
#Filename:tspace.py
#This program is made to calculate the space charge to the beam transverse

import numpy as np

def space(bunch,m_,n_,k_,energy,realnum,macronum,length,h,kappa):
		clight = 2.99792458e8  #speed of light [m/sec]
		q = 1.602e-19
		epsilon0 = 8.8541878e-12
		realcharge = realnum * q / macronum
		mass = 938.272046 
		mass_k = mass * 1.0e6 * q / clight ** 2 
		gamma0 = (energy + mass) / mass
		beta0 = (1.0 - 1.0 / gamma0 ** 2) ** 0.5
		lenth = len(bunch)
		bunchnp = np.zeros((lenth,7),dtype = np.float)
		l1 = 0.0001
		l2 = 0.0001
		l3 = 0.0001
		for i in range(0,lenth):
				for k in range(0,7):
						bunchnp[i,k] = bunch[i][k]
						if abs(bunchnp[i,5]) > l3:
								l3 = abs(bunchnp[i,5])
						if abs(bunchnp[i,1]) > l1:
								l1 = abs(bunchnp[i,1])
						if abs(bunchnp[i,3]) > l2:
								l2 = abs(bunchnp[i,3])
		l1 *= 2.0
		l2 *= 2.0
		l3 *= 2.0
		l3_r = l3 / gamma0 / h / np.pi / 2.0 * length
		dl3 = l3  / (k_ - 1.0) 
		dl3_r = l3_r  / (k_ - 1.0) 
		dl1 = l1  / (m_ - 1.0) #/ 1000.0
		dl2 = l2  / (n_ - 1.0) #/ 1000.0
		density = np.zeros((m_,n_,k_),dtype = np.float)
		densityl3 = 0.0
		densityl3_ = 0.0
		density00 = 0.0
		density01 = 0.0
		density10 = 0.0
		density11 = 0.0
		for i in range(0,lenth):
				numsl3 = int((bunchnp[i,5] + l3 / 2) / dl3)  	
				if numsl3 == k_ - 1:
					numsl3 -= 1
				wl3 =  (bunchnp[i,5] + l3 / 2.0) / dl3 -  numsl3 
				densityl3 = (1.0-wl3) 
				densityl3_ = wl3
				numsl1 = int((bunchnp[i,1] + l1 / 2) / dl1)
				if numsl1 == m_ - 1:
					numsl1 -= 1
				numsl2 = int((bunchnp[i,3] + l2 / 2) / dl2)
				if numsl2 == n_ - 1:
					numsl2 -= 1
				wl1 =  (bunchnp[i,1] + l1 / 2.0) / dl1 -  numsl1
				wl2 =  (bunchnp[i,3] + l2 / 2.0) / dl2 -  numsl2
				density00 = (1.0-wl1) * (1.0-wl2)
				density10 = wl1 * (1.0-wl2)
				density01 = (1-wl1) * wl2
				density11 = wl1 * wl2
				density[numsl1,numsl2,numsl3] += densityl3 * density00
				density[numsl1 + 1,numsl2,numsl3] += densityl3 * density10
				density[numsl1,numsl2 + 1,numsl3] += densityl3 * density01
				density[numsl1 + 1,numsl2 + 1,numsl3] += densityl3 * density11
				density[numsl1,numsl2,numsl3 + 1] += densityl3_ * density00
				density[numsl1 + 1,numsl2,numsl3 + 1] += densityl3_ * density10
				density[numsl1,numsl2 + 1,numsl3 + 1] += densityl3_ * density01
				density[numsl1 + 1,numsl2 + 1,numsl3 + 1] += densityl3_ * density11
#intention the up uniform is mm when we compute the ** we shoule change the union to meter
		l1_m = l1 / 1000.0
		l2_m = l2 / 1000.0
		dl1_m = dl1 / 1000.0
		dl2_m = dl2 / 1000.0
		density /= (dl1_m **2 * dl2_m ** 2 * dl3_r * epsilon0 / realcharge) # here we have change the density
		densityfft = np.zeros((m_,n_,k_),dtype = np.float)
		for i in range(0,k_):
				for k in range(0,m_):
					   densityfft[k,:,i] = dl1_m ** 2 * np.fft.fft(density[k,:,i])
		phifft = np.zeros((m_,n_,k_),dtype = np.float)
		for i in range(0,k_):
				for k in range(0,n_):
						coe = np.zeros((m_,2),dtype = np.float)
						ai = 1.0
						bi = 1.0
#print l2_m
						ci = -1.0 * (2 + (np.pi * k * dl1_m / l2_m) ** 2)
						coe[0,1] = bi
						for m in range(1,m_):
								coe[m,0] = ai / coe[m - 1,1] #this is l
								coe[m,1] = bi / coe[m,0] * ci #this is u
#phifft_b = np.zeros(m_,dtype = np.float)
						y = np.zeros(m_,dtype = np.float)
						y[0] = densityfft[0,k,i]
						for  m in range(1,m_):
								y[m] = densityfft[m,k,i] - coe[m,0] * y[m - 1]
						phifft[m_-1,k,i] = y[m_-1]		
						for m in range(2,m_ + 1):
								phifft[m_-m,k,i] = (y[m_-m] - ci * phifft[m_-m + 1,k,i]) / coe[m_-m,1]
						phi = np.zeros((m_,n_,k_),dtype = np.float)
						for k in range(0,k_):
								for m in range(0,m_):
										phi[m,:,k] = (np.fft.ifft(phifft[m,:,k])).real
		ei = np.zeros((m_,n_,k_,2),dtype = np.float)
		for k in range(0,k_):
				for m in range(0,m_-1):
						for n in range(0,n_ - 1):
								ei[m,n,k,0] = -(phi[m+1,n,k] - phi[m,n,k]) / dl1_m
								ei[m,n,k,1] = -(phi[m,n+1,k] - phi[m,n,k]) / dl2_m
#print ei[m,n,k,0]
#print ei[m,n,k,:]
		print ei[3,4,5,0]
		for i in range(0,lenth):
				k = int((bunchnp[i,5] + l3 / 2) / dl3)  	
				m = int((bunchnp[i,1] + l1 / 2) / dl1)
				n = int((bunchnp[i,3] + l2 / 2) / dl2)
				fx = q * ei[m,n,k,0]
				fy = q * ei[m,n,k,1]
				bunch[i][2] +=  (fx / (mass_k * gamma0 * beta0 * clight ** 2) * kappa / gamma0 ** 2 * 1000.0)
				bunch[i][4] +=  (fy / (mass_k * gamma0 * beta0 * clight ** 2) * kappa / gamma0 ** 2 * 1000.0)
		return bunch
