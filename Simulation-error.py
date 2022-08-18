# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:38:52 2021

@author: Ruffin NGOIE
"""
import random
import numpy as np
#import pylab as pl
import matplotlib.pyplot as plt
from munkres import Munkres, print_matrix, make_cost_matrix
m = Munkres()

def Munkress(matrix):
    indexes = m.compute(matrix)
    total = 0
    for row, column in indexes: 
        value = matrix[row][column]
        total += value   
    return total

def Hybride(Mtrx):
  n=len(Mtrx)
  Dcs=[0]*n
  for i in range(n):
    Dcs[i]=[0]*n
  for i in range(n):
    for j in range(n):
        Dcs[i][j]=Mtrx[i][j]
  Penal=[0]*2
  MiniL=[0]*n
  MiniCol=[0]*n
  Min=[0]*2
  MinBis=[0]*2
  BarLin=[0]*n
  BarCol=[0]*n
  Aff=[0]*n
  AdMinLin=[0]*n
  AdMinCol=[0]*n
  for i in range(2):
    Penal[i]=[0]*n
    Min[i]=[0]*n
    MinBis[i]=[0]*n
  for j in range(n):
    Aff[j]=[0]*n
  for i in range(n):
    BarLin[i]=0
    BarCol[i]=0
    for j in range(n):
        Aff[i][j]=0
  for i in range(n):
    for i in range(n):
        M=100000000
        for j in range(n):
            if M>Mtrx[i][j] and BarLin[i]==0 and BarCol[j]==0:
                M=Mtrx[i][j]
        MiniL[i]=M
    for i in range(n):
        for j in range(n):
            if BarLin[i]==0 and BarCol[j]==0:
                Mtrx[i][j]=Mtrx[i][j]-MiniL[i]
    for i in range(n):
        M=100000000
        for j in range(n):
            if M>Mtrx[j][i] and BarLin[j]==0 and BarCol[i]==0:
                M=Mtrx[j][i]
        MiniCol[i]=M
    for i in range(n):
        for j in range(n):
            if BarLin[j]==0 and BarCol[i]==0:
                Mtrx[j][i]=Mtrx[j][i]-MiniCol[i]
    for i in range(n):
        if BarLin[i]==0:
            mini=10000000
            for j in range(n):
                if BarCol[j]==0:
                    if mini>Mtrx[i][j]:
                        mini=Mtrx[i][j]
                        AdMinLin[i]=j
            Min[0][i]=mini
    for i in range(n):
        if BarCol[i]==0:
            mini=100000000
            for j in range(n):
                if BarLin[j]==0:
                    if mini>Mtrx[j][i]:
                        mini=Mtrx[j][i]
                        AdMinCol[i]=j
            Min[1][i]=mini
    for i in range(n):
        if BarLin[i]==0:
            mini=100000000
            for j in range(n):
                if BarCol[j]==0 and AdMinLin[i]!=j:
                    if mini>Mtrx[i][j]:
                        mini=Mtrx[i][j]
            MinBis[0][i]=mini
    for i in range(n):
        if BarCol[i]==0:
            mini=1000000000
            for j in range(n):
                if BarLin[j]==0 and AdMinCol[i]!=j:
                    if mini>Mtrx[j][i]:
                        mini=Mtrx[j][i]
            MinBis[1][i]=mini
    for i in range(2):
        for j in range(n):
            if i==0:
                if BarLin[j]==0:
                    Penal[i][j]=MinBis[i][j]-Min[i][j]
            else:
                if BarCol[j]==0:
                    Penal[i][j]=MinBis[i][j]-Min[i][j]
    maxi=-100
    for i in range(2):
        for j in range(n):
            if i==0:
                if BarLin[j]==0:
                    if maxi<Penal[i][j]:
                        maxi=Penal[i][j]
                        absc=i
                        ordn=j
            else:
                if BarCol[j]==0:
                    if maxi<Penal[i][j]:
                        maxi=Penal[i][j]
                        absc=i
                        ordn=j
    if absc==0:
        if BarLin[ordn]==0:
            for j in range(n):
                if BarCol[j]==0:
                    if Min[0][ordn]==Mtrx[ordn][j]:
                        Aff[ordn][j]=1
                        BarLin[ordn]=1
                        BarCol[j]=1
                        break
    else:
            if BarCol[ordn]==0:
                for j in range(n):
                    if BarLin[j]==0:
                        if Min[1][ordn]==Mtrx[j][ordn]:
                            Aff[j][ordn]=1
                            BarLin[j]=1
                            BarCol[ordn]=1
                            break
  for i in range(n):
    for j in range(n):
        if Aff[i][j]==0 and BarLin[i]==0 and BarCol[j]==0:
           Aff[i][j]=1
           break
  
  cout=0
  for i in range(n):
    for j in range(n):
        if Aff[i][j]==1:
            cout=cout+Dcs[i][j]   
  return cout

x=[]
y=[]  
for n in range(3,31):
    Mtrx=[0]*n
    for i in range(n):
        Mtrx[i]=[0]*n
    cp=0
    for k in range(1,101):
        
        for i in range(1,n):
            for j in range(1,n):
                Mtrx[i][j]=random.randint(1,100)
        Mun=Munkress(Mtrx)
        Hyb=Hybride(Mtrx)
        c=(Hyb-Mun)/Mun        
        cp+=c
    err=cp/100
    x.append(n)
    y.append(err)
    #print(n,"|",cp)
a=[3,30]
b=[0,0]
plt.xlabel('Order of square matrix', fontsize=8)
plt.ylabel('Error rate', fontsize=8)
plt.plot(x,y,'-', color='blue', label='Hybrid greedy algorithm error')
plt.plot(a,b,'-', color='red', label='Kuhn-Munkres error (0.0 %)')
plt.legend(loc='center right', fontsize=8)
plt.show()