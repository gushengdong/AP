#!/usr/bin/python
#Filename: twiss.py

def gettwiss(Rx,Ry,twissx,twissy):
    #twissx and twissy in the form of beta alpha and gamma
    #Rx and Ry are the transmission matrix in the form r11 r12 r21 r22
    twissx2 = (Rx[0]**2 * twissx[0] - 2 * Rx[0] * Rx[1] * twissx[1] + Rx[1]**2 * twissx[2],-1 * Rx[0] * Rx[2] * twissx[0] + (Rx[0] * Rx[3] + Rx[1] * Rx[2]) * twissx[1] - Rx[1] * Rx[3] * twissx[2],Rx[2]**2 * twissx[0] - 2 * Rx[2] * Rx[3] * twissx[1] + Rx[3]**2 * twissx[2])
    twissy2 = (Ry[0]**2 * twissy[0] - 2 * Ry[0] * Ry[1] * twissy[1] + Ry[1]**2 * twissy[2],-1 * Ry[0] * Ry[2] * twissy[0] + (Ry[0] * Ry[3] + Ry[1] * Ry[2]) * twissy[1] - Ry[1] * Ry[3] * twissy[2],Ry[2]**2 * twissy[0] - 2 * Ry[2] * Ry[3] * twissy[1] + Ry[3]**2 * twissy[2])
    return twissx2,twissy2
