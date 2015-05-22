import math
import numpy as np
import lspace
import random
bunch = list()
L = 200.0
for i in range(0,10000):
		a = list()
		for k in range(0,5):
				a.append(0.0)
#		if i < 700:
#		  	phi = np.pi / 2 * -1
#		elif i < 1000:
#		  	phi = np.pi / 3 + np.pi / 2 * -1
#		elif i < 1600:
#		  	phi = np.pi / 2 * -1 + 2 * np.pi / 3
#		else:
#		  	phi = np.pi / 2
#phi =  math.pi  * int(i / 500) / 3.0 - math.pi / 2  
		phi = random.uniform(-math.pi/2,math.pi/2) 
		delta = 0.0
		a.append(phi)
		a.append(delta)
		bunch.append(a)
bunch = lspace.space(bunch,64, 0.01,0.01,7.8e12,200.0,1)
#epsilon0 = 8.8541878e-12
#density = np.zeros(16,dtype=np.float)
#fftden = np.zeros(16,dtype=np.float)
#fftphi = np.zeros(16,dtype=np.float)
#phi = np.zeros(16,dtype=np.float)
#for i in range(0,16):
#		density[i] = 7.8e12 * 1.602e-19 * 100 / epsilon0
#fftden = np.fft.fft(density)
#fftphi = fftden * -1.0 * 100.0**2/np.pi**2/16**2
#phi = np.fft.ifft(fftphi)
#phi = phi.real
#for i in range(0,15):
#		print (phi[i+1] -phi[i]) / (100.0/16)
