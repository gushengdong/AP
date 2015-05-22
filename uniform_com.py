#!/usr/bin/env python
#Filename:uniform_com.py

import matplotlib.pyplot as plt
import elements as el
import numpy as np
import math

bunch = el.readpar('dis.txt')
lenth = len(bunch)
for i in range(0,lenth):

