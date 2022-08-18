# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:42:04 2022

@author: Ruffin-Benoît NGOIE
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import Trans_Ballas_hammer as TBH
import Trans_Hybride as TH
import Trans_Prim_Dual_New as TPD

x=[]
y=[]
z=[]
w=[]
for n in range(3,8):
    #Mtrx=[0]*n
    Dispox=np.zeros((n),dtype="f")
    Disp1=np.zeros((n),dtype="f")
    Disp2=np.zeros((n),dtype="f")
    for m in range(3,8):
        Matrx=np.zeros((n,m),dtype="f")
        Mat1=np.zeros((n,m),dtype="f")
        Demandx=np.zeros((m),dtype="f")
        Dema1=np.zeros((m),dtype="f")
        Dema2=np.zeros((m),dtype="f")
        Dcs=np.zeros((n,m),dtype="f")
        cpt1=0
        cpt2=0
        for t in range(10):
            s1=0
            for i in range(n):
                Dispox[i]=random.randint(50, 100)
                Disp1[i]=Dispox[i]
                Disp2[i]=Dispox[i]
                s1+=Dispox[i]
                for j in range(m):
                    Matrx[i,j]=random.randint(1, 100)
                    Dcs[i,j]=Matrx[i,j]
                    Mat1[i,j]=Matrx[i,j]
                   
            s2=0
            #print(Matrx)
            #print(Disp2)
            #print(Dispox)
            for j in range(m-1):
                Demandx[j]=random.randint(1, np.int(s1/m))
                Dema1[j]=Demandx[j]
                Dema2[j]=Demandx[j]
                s2+=Demandx[j]
            Demandx[m-1]=s1-s2
            Dema1[m-1]=Demandx[m-1]
            Dema2[m-1]=Demandx[m-1]            
            print(n, ' fois ', m)
            print('Matrx depart') 
            print(Matrx)
            print('Disponibilite') 
            print(Disp2)
            print('Demande') 
            print(Dema1)
            CoutPrim=TPD.Prim_Dual(Matrx, Disp2, Dema2, n, m)
            print('Primal ', CoutPrim)                                            
            CoutHyb=TH.Hybride(Matrx, Disp1, Dema1, n, m)
            print('Hyb ', CoutHyb)
            #print('Matrx')
            #print(Mat1)
            CoutBal=TBH.Ballas(Mat1, Dispox, Demandx, n, m)
            print('Balas ', CoutBal)
            
            if CoutHyb==CoutPrim:
                cpt1+=1
            if CoutBal==CoutPrim:
                cpt2+=1
        x.append(n)
        y.append(m)
        z.append(cpt1)
        w.append(cpt2)
a=[3, 50, 50, 3]
b=[3,3, 50, 50] 
c=[10,10, 10, 10] 
#X,Y=np.meshgrid(x,y)
#Z,T=np.meshgrid(z,t)
ax=plt.axes(projection='3d')
  
ax.set_xlabel('Origins')
ax.set_ylabel('Destinations')
ax.set_zlabel('Performance')
ax.set_zlabel('Performance')
ax.plot3D(x,y,z,'blue')
ax.scatter3D(x,y,z,c=z,cmap='Blues')
ax.plot3D(x,y,w,'orange')
ax.scatter3D(x,y,w,c=w,cmap='Oranges')
ax.plot3D(a,b,c,'blue')
ax.scatter3D(a,b,c,c=c,cmap='Purples')
#ax.plot_surface(a,b,c,rstride=1, cstride=1,cmap='Blues', edgecolor='none')
#ax.plot_surface(a,b,c,rstride=1, cstride=1,cmap='Dodgedblue', edgecolor='none')
ax.set_title('Algorithms performance')



