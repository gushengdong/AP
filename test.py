#/usr/bin/env python
#Filename:test.py

import elements as el

f1 = open('distribution.txt')
f2 = open('dist.txt','w')
f3 = open('lost.txt','w')
a = list()
a_lost = list()
for i in range(0,10000):
	line = f1.readline()
	t = line.split()
	b = list()
	for k in range(0,6):
		b.append(float(t[k]))
	a.append(b)
f1.close()
		
for i in range(0,10000):
	a[i] = el.drift(a[i],0.2)
lenth = len(a)
print lenth
k = 0
for i in  a:
	k += 1  
	if a[k][0] > 10.0:
		a_lost.append(a[k])
		del a[k]
		k -= 1
lenth = len(a)
print lenth
for i in range(0,lenth):
	for k in range(0,6):
		f2.write(str(a[i][k]))
		f2.write('\t')
	f2.write('\n')
	print i
f2.close()
lenth = len(a_lost)
for i in range(0,lenth):
	for k in range(0,6):
		f3.write(str(a_lost[i][k]))
		f3.write('\t')
	f3.write('\n')
f3.close()
#print a
#a = el.hkick(a,0.2,0.05)
#print a
#a = el.quad(a,0.2,0.2)
#print a
#a = el.quad(a,0.3,-0.2)
#print a
#a = el.sbend(a,2.1,0.26,0.0,0.0)
#print a
#a = el.sbend(a,2.1,0.26,1.2,1.2)
#print a
