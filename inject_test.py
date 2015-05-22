#/usr/bin/env python
#Filename:inject_test.py

import elements as el
import math
import bump

l1 = 0.3
l2 = 1.38
l3 = 0.3
l4 = 1.96
l5 = 1.96
l6 = 0.3
l7 = 1.38
l8 = 0.3

ly1 = 0.3
ly2 = 1.38
ly3 = 0.3
ly4 = 2.0
ly5 = 2.0
ly6 = 0.3
ly7 = 1.38
ly8 = 0.3

hx,theta,hy,thetay = bump.bump(0,200,2000,20.0,6.278,5.556,0.0,0.0)
#hx,theta,hy,thetay = 20,10,0,0
theta1,theta2,theta3,theta4 = bump.theta(l1,l2,l3,l4,l5,l6,l7,l8,hx,theta)
thetay1,thetay2,thetay3,thetay4 = bump.theta(ly1,ly2,ly1,ly4,ly5,ly6,ly7,ly8,hy,thetay)
bunch = list()
a = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#a = [0.0,20.0,10.0,0.0,0.0,0.0,0.0]
bunch.append(a)

bunch,bunch_lost = el.hkick(bunch,l1,theta1,10000,10000)
print bunch
bunch,bunch_lost = el.drift(bunch,1.31,10000,10000)
print bunch
bunch,bunch_lost = el.vkick(bunch,ly3,thetay2,10000,10000)
print bunch
bunch,bunch_lost = el.drift(bunch,0.4,10000,10000)
print bunch
bunch,bunch_lost = el.hkick(bunch,l3,theta2,10000,10000)
print bunch
bunch,bunch_lost = el.drift(bunch,l4,10000,10000)
print bunch
bunch,bunch_lost = el.drift(bunch,l5,10000,10000)
print bunch
bunch,bunch_lost = el.hkick(bunch,l6,theta3,10000,10000)
print bunch
bunch,bunch_lost = el.drift(bunch,0.4,10000,10000)
bunch,bunch_lost = el.vkick(bunch,ly6,thetay3,10000,10000)
bunch,bunch_lost = el.drift(bunch,1.31,10000,10000)
print bunch
bunch,bunch_lost = el.hkick(bunch,l8,theta4,10000,10000)
print bunch

#print bunch
#bunch,bunch_lost = el.hkick(bunch,l1,theta1,10000,10000)
#print bunch
#bunch,bunch_lost = el.drift(bunch,l2,10000,10000)
#print bunch
#bunch,bunch_lost = el.hkick(bunch,l3,theta2,10000,10000)
#print bunch
#bunch,bunch_lost = el.drift(bunch,l4,10000,10000)
#print bunch
#bunch,bunch_lost = el.drift(bunch,l5,10000,10000)
#print bunch
#bunch,bunch_lost = el.hkick(bunch,l6,theta3,10000,10000)
#print bunch
#bunch,bunch_lost = el.drift(bunch,l7,10000,10000)
#print bunch
#bunch,bunch_lost = el.hkick(bunch,l8,theta4,10000,10000)
#print bunch
