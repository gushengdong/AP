#/usr/bin/env python
#Filename:inject.py

import elements as el
import math

C = 2.99792458e8  #speed of light [m/sec]                                
E0 = 0.938272310  #proton mass [GeV]                                     
einj = 0.08       #[GeV] injection kinetic Energy                        
ek = 0.08                                                                 
PC = (ek * (ek + 2 * E0)) ** 0.5      #  Value PC                                 
brho = 1.e9 * PC / C             #  Value BRHO                               

ang = 2 * math.pi / 24.0
ee = ang / 2.0
lbend = 2.1
lqf01 = 0.41
lqd02 = 0.90
lqf03 = 0.41
lqf04 = 0.45
lqd05 = 0.90
lqf06 = 0.62

l1001 = 5.5
l1011 = 0.8
l1021 = 1.15
l1031 = 3.8
l1032 = 1.2
l1033 = 1.3
l1041 = 1.3
l1051 = 0.8
l1061 = 0.9
l1062 = 1.75

lkicker = 0.3
lk_qd = 0.4
lk_qf = 0.45

kqf06 = 0.80297056 / brho     
kqd05 = -0.76457619 / brho      
kqf04 = 0.752954981 / brho     
kqf03 = 0.87652783 / brho     
kqd02 = -0.76457619 / brho      
kqf01 = 0.97741500095 / brho

bunch = list()
bunch_lost = list()
bunch = el.readpar('distribution.txt')
bunch,bunch_lost = el.drift(bunch,l1001,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf01,kqf01,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1011,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqd02,kqd02,15000,15000)
bunch,bunch_lost = el.drift(bunch,lk_qd,15000,15000)
bunch,bunch_lost = el.drift(bunch,lkicker,15000,15000)
bunch,bunch_lost = el.drift(bunch,lk_qf,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf03,kqf03,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1031,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1032,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1033,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf04,kqf04,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1041,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqd05,kqd05,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1051,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf06,kqf06,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1061,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1062,15000,15000)

bunch,bunch_lost = el.drift(bunch,l1062,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1061,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf06,kqf06,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1051,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqd05,kqd05,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1041,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf04,kqf04,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1033,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1032,15000,15000)
bunch,bunch_lost = el.sbend(bunch,lbend,ang,ee,ee,15000,15000)
bunch,bunch_lost = el.drift(bunch,l1031,15000,15000)
bunch,bunch_lost = el.quad(bunch,lqf03,kqf03,15000,15000)
bunch,bunch_lost = el.drift(bunch,lk_qf,15000,15000)
bunch,bunch_lost = el.drift(bunch,lkicker,15000,15000)
bunch,bunch_lost = el.drift(bunch,lk_qd,15000,15000)
#bunch,bunch_lost = el.quad(bunch,lqd02,kqd02,15000,15000)
#bunch,bunch_lost = el.drift(bunch,l1011,15000,15000)
#bunch,bunch_lost = el.quad(bunch,lqf01,kqf01,15000,15000)
#bunch,bunch_lost = el.drift(bunch,l1001,15000,15000)


el.dumppar(bunch,'dis.txt')
el.dumppar(bunch_lost,'lost.txt')
