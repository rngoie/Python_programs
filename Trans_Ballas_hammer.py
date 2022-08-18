# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:09:02 2021

@author: Damos LINGUMA

"""
import numpy as np
#Mtrx =  [[8,7,9,9],
  #        [5,2,7,8],
   #       [5,1,4,8],
    #      [2,2,2,6]]
          #
def rech(e,M,n):
     l=0
     k=0
     
     while k!=M:
         if  M[k]!=e:
             l=l+1
             
         k=k+1
     return l    
  
   
#procedure de verification des disponibilite 
      
#SAISIE DE LA MATRICE DE DONNEE


def remplir(Aff, BarL, BarCol,taille1,taille2):
    for i in range(0,taille1):
        BarL[i]=0
        
        for j in range(0,taille2):
            #Mtrx[i][j]=input("saisir le cout d'affectation de la source %i vers la destination %j ")
            #Dcs[i][j]=Mtrx[i][j] 
            Aff[i][j]=0
           
        #Dispox[i]=input("saisir la disponibilité pour cette source ")    
    for j in range(0,taille2):
        BarCol[j]=0
        #Demandx[j]=input("saisir la quantite demandee ")
          
#REDUCTION MATRICE

 #minimum des ligne et colonnes amenagés
def  minL(L,C,M,Min,taille1,taille2,t,AdM):
    for i in range(0,taille1):
        if L[i]==0:
            mini=10000000000
            for j in range(0,taille2):
                if C[j]==0:
                    if mini>M[i][j]:
                        mini=M[i][j]
                        AdM[i]=j
                    #try:
                       #mini=min([nb for nb in M[j] if nb==0])
                    #AdM[i]=rech(min,[nb for nb in M[j] if nb==M[i][j]],taille)
                    #except:
                       #mini=0.0
                    
            Min[0][i]=mini
            
    return AdM 
              
def  minC(L,C,M,Min,taille1,taille2,t,AdM):
    for i in range(0,taille1):
        if C[i]==0:
            mini=1000000000000
            for j in range(0,taille2):
                if L[j]==0:
                    if mini>M[j][i]:
                        mini=M[j][i]
                        AdM[i]=j
                    #try:
                       #mini=min([nb for nb in M.transpose()[j] if nb==0])
                    #AdM[i]=rech(min,[nb for nb in M[j] if nb==M[j][i]],taille)
                    #except:
                       #mini=0.0
                    
            Min[1][i]=mini
            
    return AdM 
                      

                           
def minLCML(L,C,M,AdM,MinBisLC,taille1,taille2):
    for i in range(0,taille1):
        if L[i]==0:
            mini=1000000000000
            for j in range(0,taille2):
                if C[j]==0 and AdM[i]!=j:
                    if mini>M[i][j]:
                        mini=M[i][j]            
            MinBisLC[0][i]=mini
   
                     
    return MinBisLC               
                
def minLCM(L,C,M,AdM,MinBisLC,taille1,taille2):
    for i in range(0,taille1):
        if C[i]==0:
            mini=1000000000000
            for j in range(0,taille2):
                if L[j]==0 and AdM[i]!=j:
                    if mini>M[j][i]:
                        mini=M[j][i]
            MinBisLC[1][i]=mini  
                      
    return MinBisLC  

  
        
def penalite(L,C,Min,Penal,MinBis,n,m):
    for i in range(0,2):
        if i==0:
            k=n
        else:
            k=m
        for j in range(0,k):
            if i==0:
                if L[j]==0:
                    Penal[i][j]=MinBis[i][j]-Min[i][j]
            else:        
                if C[j]==0:
                    Penal[i][j]=MinBis[i][j]-Min[i][j]
               
               
def penaliteMax(L,C,Penal,taille1,taille2,absc,ordn):   
    maxim=-100
    for i in range(0,taille1):
        if L[i]==0:
            if maxim<Penal[0][i]:
                maxim=Penal[0][i]
                absc=0
                ordn=i
    
    for j in range(0,taille2):
        if C[j]==0:
            if maxim<Penal[1][j]:
                maxim=Penal[1][j]
                absc=1
                ordn=j
                        
    return  absc,ordn                     
    
    
def affectation(L,C,M,Dispox,Demandx,Aff,Min,taille1,taille2,absc,ordn,n,m):
        
    if absc==0:
        if L[ordn]==0:
            for j in range(0,taille2):
                if C[j]==0:
                    if Min[0][ordn]==M[ordn][j]:
                        if Dispox[ordn]<Demandx[j]:
                           quant=Dispox[ordn]
                           L[ordn]=1
                           n=n-1
                           Aff[ordn][j]=quant
                           Dispox[ordn]=Dispox[ordn]-quant
                           Demandx[j]=Demandx[j]-quant
                           if Demandx[j]==0.:
                               C[j]=1
                               m=m-1
                        else:
                          quant=Demandx[j]
                          C[j]=1
                          m=m-1
                          Aff[ordn][j]=quant
                          Dispox[ordn]=Dispox[ordn]-quant
                          Demandx[j]=Demandx[j]-quant
                          if Dispox[ordn]==0.:
                              L[ordn]=1
                              n=n-1
                              
                                                              
                         
    else:
       if C[ordn]==0:
            for j in range(0,taille1):
                if L[j]==0:
                    if Min[1][ordn]==M[j][ordn]:
                        if Dispox[j]<Demandx[ordn]:
                           quant=Dispox[j]
                           L[j]=1
                           n=n-1
                           Aff[j][ordn]=quant
                           Dispox[j]=Dispox[j]-quant
                           Demandx[ordn]=Demandx[ordn]-quant
                           if Demandx[ordn]==0.:
                               C[ordn]=1
                               m=m-1
                        else:
                            quant=Demandx[ordn]
                            C[ordn]=1
                            m=m-1
                            Aff[j][ordn]=quant
                            Dispox[j]=Dispox[j]-quant
                            Demandx[ordn]=Demandx[ordn]-quant
                            if Dispox[j]==0.:
                                L[j]=1
                                n=n-1  
                                 
                                                                                                                                               
    return n,m                    
                
def resultat(L,C,Dispox,Demandx,Aff,taille1,taille2):
    for i in range(0,taille1):
        for j in range(0,taille2):
            if L[i]==0 and C[j]==0:
                if Dispox[i]<Demandx[j]:
                    quant=Dispox[i]
                else:
                    quant=Demandx[j]
                    
                Aff[i][j]=quant
                Dispox[i]=Dispox[i]-quant
                Demandx[j]=Demandx[j]-quant
                
                        
   
    
def calculCout(Aff,cout,Dcs,taille1,taille2): 
    cout=0
    for i in range(0,taille1):
        for j in range(0,taille2):
            cout=cout+Dcs[i][j]*Aff[i][j]           
                 
    return cout             
           
def tour(n,m):
    if n<m:
        return m
    else:
        return n
                
              


def Ballas(Mtrx,Dispox,Demandx,n,m):
    

   
    absc=0
    ordn=0
    cout=0
    nbl=n
    nbc=m
    p=tour(n,m)
    Dcs=np.zeros((n,m),dtype="f")
    Penal=np.zeros((2,p),dtype="f")
    Min=np.zeros((2,p),dtype="f")
    for i in range(n):
        for j in range(m):
            Dcs[i][j]=Mtrx[i][j]
    MinBis=np.zeros((2,p),dtype="f")

    BarL=np.zeros((n),dtype="i")
    BarCol=np.zeros((m),dtype="i")
    Aff=np.zeros((n,m),dtype="i")
    AdMinLin=np.zeros((n),dtype="i")
    AdMinCol=np.zeros((m),dtype="i")
#debut algo
    remplir(Aff,BarL,BarCol,n,m)
    while nbl>=2 and nbc>=2:
    
    
         minL(BarL,BarCol,Mtrx,Min,n,m,1,AdMinLin)
         minC(BarL,BarCol,Mtrx,Min,m,n,0,AdMinCol)
    
         MinBis=minLCML(BarL,BarCol,Mtrx,AdMinLin,MinBis,n,m)
    
         MinBis=minLCM(BarL,BarCol,Mtrx,AdMinCol,MinBis,m,n)

    # calcul de la penalité sur les colonnes et les ligne
         penalite(BarL,BarCol,Min,Penal,MinBis,n,m)
    #recherche  de la penalité maximal
         absc,ordn=penaliteMax(BarL,BarCol,Penal,n,m,absc,ordn)
    #DEBUT PRECEDURE aFFECTaTION
         nbl,nbc=affectation(BarL,BarCol,Mtrx,Dispox,Demandx,Aff,Min,n,m,absc,ordn,nbl,nbc)
    #resultat affectation
    
    
    resultat(BarL,BarCol,Dispox,Demandx,Aff,n,m)
#affichage  et calcul du cout d' affectation
    
    print(Aff)
    return calculCout(Aff,cout,Dcs,n,m)
#fin

print(Ballas([[14., 64., 28., 88., 37., 22., 21.],  [31., 18., 71., 55., 54., 26., 84.],  [ 6., 10., 16., 82., 43.,  9., 61.]], [91., 90., 80.], [ 33.,  18.,  33.,  22.,  17.,  22., 116.], 3, 7))
#print(Prim_Dual([[37., 95., 22., 7., 86.],[72.,87.,60., 49., 51.],[70.,2.,24., 57., 79.]], [85.,94.,77.], [88.,26.,22., 9., 111.], 3, 5))
