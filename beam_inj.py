#!/usr/bin/env python
#Filename:beam_inj.py

import math
import math
import matplotlib.pyplot as plt
import random
import numpy as np

def beam(betax,betay,alphax,alphay,emitx,emity,deta,number):
		gammax = (1 + alphax ** 2) / betax
		gammay = (1 + alphay ** 2) / betay
		bunch = list()
		for i in range(0,number):
				ele = list()
				betax0 = betax
				betay0 = betay
				gammax0 = 1.0 / betax
				gammay0 = 1.0 / betay
				sigmmax0 = (emitx * betax0) ** 0.5
				sigmmaxp0 = (emitx * gammax0) ** 0.5
				sigmmay0 = (emity * betay0) ** 0.5
				sigmmayp0 = (emity * gammay0) ** 0.5
				sigmmax = (emitx * betax) ** 0.5
				sigmmaxp = (emitx * gammax) ** 0.5
				sigmmay = (emity * betay) ** 0.5
				sigmmayp = (emity * gammay) ** 0.5
				x = random.gauss(0.0,sigmmax0)
				xp = random.gauss(0.0,sigmmaxp0) - alphax / betax * x
				y = random.gauss(0.0,sigmmay0)
				yp = random.gauss(0.0,sigmmayp0) - alphay / betax * y
				flag = (x > 3.0 * sigmmax or xp > 3.0 * sigmmaxp or y > 3.0 * sigmmay or yp > 3.0 * sigmmayp)
				while flag:
						x = random.gauss(0.0,sigmmax0)
						xp = random.gauss(0.0,sigmmaxp0) - alphax / betax * x
						y = random.gauss(0.0,sigmmay0)
						yp = random.gauss(0.0,sigmmayp0) - alphay / betax * y
						flag = (x > 3.0 * sigmmax or xp > 3.0 * sigmmaxp or y > 3.0 * sigmmay or yp > 3.0 * sigmmayp)
				pha = 0.0 #this one should be changed latter
				s = 0.0 #this one should be changed latter
				ele.append(s)
				ele.append(x)
				ele.append(xp)
				ele.append(y)
				ele.append(yp)
				ele.append(pha)
				ele.append(deta)
				bunch.append(ele)
		return bunch
