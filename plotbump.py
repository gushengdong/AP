#!/usr/bin/env python
#Filename:plotbump.py

import matplotlib.pyplot as plt
import numpy as np

f1 = open('cor.txt')
a = list()
line = f1.readline()
#print line
while line:
	t = line.split()
#	print t
	b = list()
	b.append(float(t[0]))
	b.append(float(t[1]))
	line = f1.readline()
	a.append(b)
lenth = len(a)
c = np.zeros((lenth,2),dtype = np.float)
for i in range(0,lenth):
		c[i,0] = a[i][0]
		c[i,1] = a[i][1]

plt.plot(c[:,0],c[:,1])
plt.show()
