#!/usr/bin/env python
#Filename:test2.py
#This file is tested for inject
import elements as el

f2 = open('cor.txt','w')
p = [0.0,0.0,0.0,0.0,0.0,0.0]
s = 0.0
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p =  el.drift(p,0.2)
s += 0.2
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.hkick(p,0.1,0.2)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.drift(p,0.1)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.hkick(p,0.1,-0.2)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.drift(p,1.0)
s += 1.0
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.hkick(p,0.1,-0.2)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.drift(p,0.1)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p = el.hkick(p,0.1,0.2)
s += 0.1
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
p =  el.drift(p,0.2)
s += 0.2
f2.write(str(s))
f2.write('\t')
for i in range(0,6):
		f2.write(str(p[i]))
		f2.write('\t')
f2.write('\n')
f2.close()
