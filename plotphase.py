#!/usr/bin/env python
#Filename:plotphase.py

import numpy as np
import matplotlib.pyplot as plt

def plotphase(bunch,s):
		lenth = len(bunch)
		a = np.zeros((lenth,6),dtype = float)
		for i in range(0,lenth):
				a[i,0] = bunch[i][1]
				a[i,1] = bunch[i][2]
				a[i,2] = bunch[i][3]
				a[i,3] = bunch[i][4]
				a[i,4] = bunch[i][5]
				a[i,5] = bunch[i][6]
		plt.figure() 
		ax1 = plt.subplot(221)
		ax2 = plt.subplot(222)
		ax3 = plt.subplot(223)
		ax4 = plt.subplot(224)
	 	plt.sca(ax1) 
		plt.xlabel(r'x')
#	plt.ylabel(r"$\x'$")
		plt.ylabel(r"x'")
		plt.plot(a[:,0], a[:,1],'o',markersize=1)
	 	plt.sca(ax2) 
		plt.xlabel(r'y')
#plt.ylabel(r"$\y'$")
		plt.ylabel(r"y'")
		plt.plot(a[:,2], a[:,3],'o',markersize=1)
	 	plt.sca(ax3) 
		plt.xlabel('x')
		plt.ylabel("y")
		plt.plot(a[:,0], a[:,2],'o',markersize=1)
	 	plt.sca(ax4) 
		plt.xlabel(r'$\phi$')
#plt.ylabel(r'$\deta$')
		plt.ylabel(r'$\delta$')
		plt.plot(a[:,4], a[:,5],'o',markersize=1)
#plt.xlim(-3.14*2,3.14*2)
#		plt.xlim(-3.14,3.14)
#		plt.ylim(-0.1,0.1)
#plt.legend()
		plt.savefig(s)
