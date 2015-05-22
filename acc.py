#/usr/bin/env python
#Filename:acc.py

import numpy as np 
import matplotlib.pyplot as plt 

f1 = open(r'cor.txt','w')
def eta(gamma):
	gamma_tr = 4.889739
	return 1.0 / gamma_tr ** 2 - 1.0 / gamma ** 2
def gamma(deta):
	E0 = 251
#omega0 = 2 * np.pi / 0.001239 * 2000 
	detaE = deta * beta0 ** 2 * E0
	E = E0 + detaE
	gamma = (E + mass) / mass
	return gamma
mass = 938.272046
E0 = 250.0
gamma0 = (E0 + mass) / mass
beta0 = (1.0 - 1.0 / gamma0 ** 2) ** 0.5
pha0 = 0.5
pha20 = 0
h = 2
h2 = 4
v2 = -10.0 / 2000.0 
#v2 = 0.0
V_RF = 31.0 / 2000.0
r = v2 / V_RF
#cor = np.zeros((2000,2),dtype=np.float)
cor = np.zeros((2000,2),dtype=np.float)
pot = np.zeros((2000,2),dtype = np.float)
for j in range(0,2000):
	print j
	cor[0,0] = pha0 + 0.01 * j
	print cor[0,0]
	judge = False
	for i in range(1,2000):
		cor[i,1] = cor[i - 1,1] + V_RF / E0 / beta0 ** 2 * ((np.sin(cor[i - 1,0]) - np.sin(pha0)) + r * (np.sin(pha20 + h2 / h * (cor[i-1,0] - pha0)) - np.sin(pha20)))
		cor[i,0] = cor[i - 1,0] + 2 * np.pi * h * eta(gamma(cor[i,1])) * cor[i,1]
		judge = cor[i,1] >= 0.0 or judge
	#	print judge
		E0 += V_RF * np.sin(pha0) + v2 * np.sin(pha20)
	#print judge
	if judge != True:
		break
	#plt.plot(cor[:,0],cor[:,1],'o',markersize = 0.5)
cor[0,0] -= 0.02
#cor[0,0] = 1.9 + pha0
cor[0,1] = 0.000
for i in range(1,2000):
#	cor[i,1] = cor[i - 1,1] + V_RF / E0 / beta0 ** 2 * (np.sin(cor[i - 1,0]) - np.sin(pha0))
	cor[i,1] = cor[i - 1,1] + V_RF / E0 / beta0 ** 2 * ((np.sin(cor[i - 1,0]) - np.sin(pha0)) + r * (np.sin(pha20 + h2 / h * (cor[i-1,0] - pha0)) - np.sin(pha20)))
	cor[i,0] = cor[i - 1,0] + 2 * np.pi * h * eta(gamma(cor[i,1])) * cor[i,1]
	E0 += V_RF * np.sin(pha0) + v2 * np.sin(pha20)
	pot[i - 1,0] = (np.sin(cor[i - 1,0])) / 100
	pot[i - 1,1] = (np.sin(cor[i - 1,0]) + r * np.sin(h2 / h * (cor[i - 1,0] - pha0))) / 100
#	print cor[i,0],cor[i,1]
	f1.write(str(i))
	f1.write('\t')
	f1.write(str(cor[i,0]))
	f1.write('\t')
	f1.write(str(cor[i,1]))
	f1.write('\n')
plt.plot(cor[:,0],pot[:,0],'o',markersize = 1)
plt.plot(cor[:,0],pot[:,1],'o',markersize = 1)
plt.plot(cor[:,0],cor[:,1],markersize = 1)
for i in range(1,2000):
	cor[i,1] = cor[i - 1,1] + V_RF / E0 / beta0 ** 2 * (np.sin(cor[i - 1,0]) - np.sin(pha0))
#	cor[i,1] = cor[i - 1,1] + V_RF / E0 / beta0 ** 2 * ((np.sin(cor[i - 1,0]) - np.sin(pha0)) + r * (np.sin(pha20 + h2 / h * (cor[i-1,0] - pha0)) - np.sin(pha20)))
	cor[i,0] = cor[i - 1,0] + 2 * np.pi * h * eta(gamma(cor[i,1])) * cor[i,1]
	E0 += V_RF * np.sin(pha0) + v2 * np.sin(pha20)
phamax = 0.0
detamax = 0.0
phamix = 7.0
detamix = 0.1
phamax_i = 0
detamax_i = 0
phamix_i = 0
detamix_i = 0
for i in range(0,2000):
		if cor[i,0] > phamax:
				phamax = cor[i,0]
				phamax_i = i
		if cor[i,0] < phamix:
				phamix = cor[i,0]
				phamix_i = i
		if cor[i,1] > detamax:
				detamax = cor[i,1]
				detamax_i = i
		if cor[i,1] < detamix:
				detamix = cor[i,1]
				detamix_i = i
phasearea = 0.0
if phamax_i < phamix_i:
	for i in range(phamax_i,phamix_i):
			phasearea += (cor[i + 1,0] - cor[i,0]) * cor[i,1] * 2
if phamax_i > phamix_i:
	for i in range(phamix_i,phamax_i):
			phasearea += (cor[i + 1,0] - cor[i,0]) * cor[i,1] * 2
f1.write('---------------------------------------------')
f1.write('\n')
f1.write('phamax = ')
f1.write(str(phamax))
f1.write('\t')
f1.write('phamax_i = ')
f1.write(str(phamax_i))
f1.write('\t')
f1.write('phamix = ')
f1.write(str(phamix))
f1.write('\t')
f1.write('phamix_i = ')
f1.write(str(phamix_i))
f1.write('\n')
f1.write('detamax = ')
f1.write(str(detamax))
f1.write('\t')
f1.write('detamax_i = ')
f1.write(str(detamax_i))
f1.write('\t')
f1.write('detamix = ')
f1.write(str(detamix))
f1.write('\t')
f1.write('detamix_i = ')
f1.write(str(detamix_i))
f1.write('\n')
f1.write('phasearea = ')
f1.write(str(phasearea))

f1.close()
#plt.plot(cor[:,0],cor[:,1],'o',markersize = 1)
#plt.show()
plt.savefig('acc.png')
