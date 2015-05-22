#/usr/bin/env python
#Filename:test4.py

import elements as el

bunch = list()
bunch_lost = list()
bunch = el.readpar('distribution.txt')
print bunch[1]
bunch,bunch_lost = el.quad(bunch,0.5,0.3,10,12)
el.dumppar(bunch,'dis.txt')
el.dumppar(bunch_lost,'lost.txt')
