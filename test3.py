#/usr/bin/env python
#Filename:test3.py

import elements as el

f1 = open('distribution.txt')
f2 = open('dis.txt','w')
f3 = open('lost.txt','w')
bunch = list()
bunch_lost = list()
for i in range(0,10000):
	line = f1.readline()
	t = line.split()
	b = list()
	for k in range(0,7):
		b.append(float(t[k]))
	bunch.append(b)
f1.close()
print bunch[1]
#bunch,bunch_lost = el.drift(bunch,0.2,10,12)
#bunch,bunch_lost = el.hkick(bunch,0.2,0.03,10,12)
#bunch,bunch_lost = el.sbend(bunch,2,0.3,0.15,0.15,10,12)
bunch,bunch_lost = el.quad(bunch,0.5,0.3,10,12)
lenth = len(bunch)
print lenth
for i in range(0,lenth):
	for k in range(0,7):
		f2.write(str(bunch[i][k]))
		f2.write('\t')
	f2.write('\n')
f2.close()
lenth = len(bunch_lost)
print lenth
for i in range(0,lenth):
	for k in range(0,7):
		f3.write(str(bunch_lost[i][k]))
		f3.write('\t')
	f3.write('\n')
f3.close()
