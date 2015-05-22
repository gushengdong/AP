#!/usr/bin/env python
#Filename:plotphase.py

import numpy as np
import elements as el
import matplotlib.pyplot as plt

bunch = el.readpar('dis.txt')
lenth = len(bunch)
print lenth
a = np.zeros((lenth,6),dtype = float)
for i in range(0,lenth):
				a[i,0] = bunch[i][1]
				a[i,1] = bunch[i][2]
				a[i,2] = bunch[i][3]
				a[i,3] = bunch[i][4]
				a[i,4] = bunch[i][5]
				a[i,5] = bunch[i][6]
#plt.figure(1) 
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
plt.sca(ax1) 
plt.xlabel('x')
plt.ylabel("x'")
plt.plot(a[:,0], a[:,1],'o',markersize=1)
plt.sca(ax2) 
plt.xlabel('y')
plt.ylabel("y'")
plt.plot(a[:,2], a[:,3],'o',markersize=1)
plt.sca(ax3) 
plt.xlabel('x')
plt.ylabel("y")
plt.plot(a[:,0], a[:,2],'o',markersize=1)
plt.sca(ax4) 
plt.xlabel(r'pha')
plt.ylabel(r'deta')
plt.plot(a[:,4], a[:,5],'o',markersize=1)
#plt.legend()
plt.savefig('dis1.png')
