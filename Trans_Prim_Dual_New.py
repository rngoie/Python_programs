from traceback import print_tb
 
import  numpy as np

def Prim_Dual(Matrx,Dispo,Dem,n,m):
    
    """ for i in range(1, 10):
    print(i) """
    tmpc = None
    #n = 5#int(input("Saisir le nombre d'origines : "))
    #m = 6#int(input("Saisir le nombre de destinations : "))
    chemins = []
    sommetD = []
    sommets = []
    file = []
    """ 
    [[ 0. 12.  0. 37. 71. 14.]
    [ 0. 13.  6.  5. 42. 10.]
    [43. 29. 19.  0. 29. 21.]
    [31.  0.  2. 27.  0.  0.]] """
    """ 
    [9, 12, 9, 6, 9, 10],
    [6, 8, 9, 11, 3, 11],
    [7, 3, 11, 2, 3, 10],
    [6, 8, 7, 10, 3, 5],
    [5, 6, 9, 2, 7, 3]
    """
    """ 
    [12, 27, 61, 49, 83, 35],
    [23, 39, 78, 28, 65, 42],
    [67, 56, 92, 24, 53, 54],
    [71, 43, 91, 67, 40, 49],
    """

    """ 
    [10, 30, 35, 15,],
    [20, 15, 20, 10,],
    [10, 30, 20, 20,],
    [30, 40, 35, 45,],
    """
   
#np.zeros((n,m))
    
    Trans = []
    Affect = []
    #Dcs = []
    Dcs=np.zeros((n,m),dtype="f")
    LineMin = []
    ColMin = []
    #Dispo = np.zeros((n))
    #Dem = np.zeros((m))
    ResLin = []
    ResCol = []
    MarkLin = []
    MarkCol = []
    Mark = []
    RefLin = []
    RefCol = []
    mauvaisChemin = []

    """ Table = np.zeros((10000, 4))
    Sortie = np.zeros((10000))
    Entree = np.zeros((10000))
    Adj = np.zeros((10000, 10000))
    Explo = np.zeros((10000)) """
    Init = []
    """ LinDep = np.zeros((100000))
    veto = np.zeros((100000))
    cptr1 = np.zeros((m))
    cptr2 = np.zeros((n)) """
    
    cptr1 = []
    cptr2 = []
    
    """ Mes vars """
    pointage = [None, None]
    continuer = True
    reperage = []
    ligne = None
    colonne = None
    
    Refer  = None
    Ref = None

    MarkCol2 = []
    MarkLin2 = []

    FauxChemin = False
    CasDispo = False

    #Definition des fonction pour la recherche du chemin
    def voisiner(t):
        v = []
        col_Sm = t[1]
        lig_Sm = t[0]
        for j in range(m):
            if(j != col_Sm and Trans[lig_Sm][j] == 0 and visite[lig_Sm][j] == 0):
                v.append([lig_Sm, j, None])
        for i in range(n):
            if(i != lig_Sm and Trans[i][col_Sm] == 0 and visite[i][col_Sm] == 0):
                v.append([i, col_Sm, None])
        return v

    #print("SAISIE DE LA MATRICE DE DONNEE")
    for i in range(n):
        for j in range(m):
            Dcs[i][j]=Matrx[i][j]
    for i in range(n):
        #Dcs.append([])
        Affect.append([])
        Mark.append([])
        Trans.append([])
        for j in range(m):
            #Matrx[i][j] = input("Saisir le cout de transport unitaire de la source {} vers la destination {} : ".format(i,j))
            #Dcs[i].append(Matrx[i][j])
            Affect[i].append(0)
            Mark[i].append(0)
            Trans[i].append(0)
            """ print("\n ======================Fin saisie=====================")
            print("SAISIE DU VECTEUR DE DISPONIBILITE")
            for i in range(n):
                Dispo[i] = input("Saisir la disponibilite de la source {} : ".format(i))
                print("SAISIE DU VECTEUR DE DEMANDE")
                
            for j in range(m):
                Dem[j] = input("Saisir la demande de la destination {} : ".format(j))
                """
    Total = 0

    for k in range(n):
        Total += Dispo[k]  
        MarkLin.append(0)
        MarkLin2.append(0)
        LineMin.append(0)
        ResLin.append([0,0])
        RefLin.append(0)
        Init.append(0)
        cptr2.append(0)
    for t in range(m): 
        MarkCol.append(0)
        MarkCol2.append(0)
        ColMin.append(0)
        ResCol.append([0,0])
        RefCol.append(0)
        cptr1.append(0)

    Trans = np.array(Trans)
    Affect = np.array(Affect)
    Dcs = np.array(Dcs)
    Mark = np.array(Mark)



    #print(ResCol)
    #Determination des minimums de lignes
    for i in range(n):
        mini = Matrx[i][0]
        for j in range(1, m):
            if (mini > Matrx[i][j]): 
                mini = Matrx[i][j]
        LineMin[i] = mini
        #print(mini)

    #Reduction de la matrice
    for i in range(n):
        for j in range(m):
            Trans[i][j] = Matrx[i][j] - LineMin[i]

    #Determination des minimums de colonnes
    for i in range(m):
        mini = Trans[0][i]
        for j in range(1, n):
            if (mini > Trans[j][i]) : 
                mini = Trans[j][i]
        ColMin[i] = mini

    #Reduction de la matrice reduite
    for i in range(m):
        for j in range(n):
            Trans[j][i] =Trans[j][i] - ColMin[i]

    #Controle optimal
    Cont = 0    
    for i in range(n):
        Cont += Dispo[i]
        #Affectations preliminaires
    for i in range(n):
        for j in range(m):
            if (Trans[i][j] == 0 and Mark[i][j] == 0 and Dispo[i] != 0 and Dem[j] != 0):
                if (Dispo[i] < Dem[j]):
                    quant =Dispo[i]
                    Affect[i][j] = Affect[i][j] + quant
                    Dispo[i] = 0
                    Dem[j] = Dem[j] - quant
                    Cont -= quant
                else :
                    quant = Dem[j]
                    Affect[i][j] = Affect[i][j] + quant
                    Dem[j] = 0
                    Dispo[i] = Dispo[i] - quant
                    Cont -= quant
                Mark[i][j] = 1
                """ print(Dispo)
                print(Dem) """
    #print("Total cont : {}".format(Cont))

    """ print(Affect)
    print(Mark) """
    ddd = 0
    """ Cont != 0 """
    while  Cont != 0:
        #print("Cont : {}, Dispo : {} , Dem : {} , MarkCol 1 : {}". format(Cont, Dispo, Dem, MarkCol))
        #premier marquage
        #print("Matrice affectation : {}".format(Affect))
        #print("mark Avant initialisation L = {} et C = {}".format(MarkLin2, MarkCol2))
            
        #mark initial
        for i in range(n):
            if(Dispo[i] != 0):
                #mark ligne arrivée
                Ref = i
                MarkLin2[Ref] = 1
                ResLin[Ref][0] = 0
                ResLin[Ref][1] = Dispo[Ref]
                ctrCasDispo = []
                for j in range(m):
                    if(Trans[Ref][j] == 0 and MarkCol2[j] == 0):
                        MarkCol2[j] = 1
                        ResCol[j][0] = Ref
                        ResCol[j][1] = ResLin[i][1]
                        if(Dem[j] != 0):
                            Refer = j
                            break
                break

        #print("mark initial L = {} et C = {}".format(MarkLin2, MarkCol2))
        mark_exit = 0
        if(Refer == None):
            #print("refer = None")
            while mark_exit == 0:
                nbrmarkL = 0
                nbrmarkC = 0
                #mark parcour markcol[j] == 1 pour trouve markLin[i] = 1
                for j in range(m):
                    if(MarkCol2[j] == 1):
                        #si on trouve la colonne alors on parcours chaque ligne de celle-ci
                        ctrZero = 0
                        ctrAffect = []
                        #recupere le nombre de zero et le i d'affectation
                        for i in range(n):
                            if(Trans[i][j] ==0):
                                ctrZero +=1
                                if(Affect[i][j] != 0):
                                    ctrAffect.append(i)
                                    #print("kfkkfkfk")
                        if(ctrZero > 1 and len(ctrAffect) > 0):
                            for i in range(n):
                                #print("coolll") 
                                if(Trans[i][j] == 0 and Affect[i][j] !=0):
                                    MarkLin2[i] = 1
                                    nbrmarkL +=1
                                    if (Affect[i][j] < ResCol[j][1]):
                                        ResLin[i][1] = Affect[i][j]
                                    else:
                                        ResLin[i][1] = ResCol[j][1]
                #print("mark parcour markcol[j] == 1  L = {} et C = {}".format(MarkLin2, MarkCol2))
                #mark parcour markLin[i] == 1 pour trouve markCol[j] = 1
                testMarkCol = 0
                testMarkCol2 = 0
                for j in range(m):
                    if(MarkCol2[j] == 1):
                        testMarkCol +=1
                        testMarkCol2 +=1
                for i in range(n):
                    if(MarkLin2[i] == 1):
                        for j in range(m):
                            if(Trans[i][j] ==0 and MarkCol2[j] == 0):
                                MarkCol2[j] = 1
                                testMarkCol2 +=1
                                nbrmarkC +=1
                                ResCol[j][0]= i
                                #ResCol[j][0] = i
                                ResCol[j][1] = ResLin[i][1]
                                if(Dem[j] != 0 ):
                                    Refer = j
                                    break
                                    ###iciciciicic                          

                #checking
                if(Refer != None): break
                #print("nbrmarkC = {} et nbrmarkL = {}".format(nbrmarkL, nbrmarkC))
                #print("mark parcour markLin[i] == 1  L = {} et C = {} ".format(MarkLin2, MarkCol2))
                if(testMarkCol2 == testMarkCol):
                    if(nbrmarkC != nbrmarkL):
                        mark_exit = 1
                        break
            
                if(Refer == None and nbrmarkC == 0 and nbrmarkL == 0):
                    break
           

        #print('rescol = {}, reslin = {}'.format(ResCol, ResLin))
        #print("MarkL : {}, markCol : {}, Ref : {}, Refer : {}".format(MarkLin2, MarkCol2, Ref, Refer))   

        if (Refer == None):
            ###
            #print("Calcul delta =================================")
            #Recherche de delta
            delta = 100000000000
            for i in range(n):
                if(MarkLin2[i] == 1):
                    for j in range(m):
                        if (MarkCol2[j] == 0):
                            if (delta > Trans[i][j]):
                                delta = Trans[i][j]
            #print("deltat donne {}".format(delta))
            #print("Avant Reduction")
            #print(Trans)
       
            if(delta == 100000000000):
                CasDispo = True
                
            if(delta != 100000000000):

                #Reduction
                for i in range(n):
                    if(MarkLin2[i] == 1):
                        for j in range(m):
                            if (MarkCol2[j] == 0): 
                                Trans[i][j] = Trans[i][j] - delta
                #print("Apres Reduction")
                #print(Trans)
                #print("deltat  = {}".format(delta))
                #Augmentation
                for j in range(m):
                    if(MarkCol2[j] == 1):
                        for i in range(n):
                            if(MarkLin2[i] == 0):
                                Trans[i][j] = Trans[i][j] + delta
                #print("Apres Augmentation")
                #print(Trans)

        else:
            #print("arrivée : {}, depart : {} ".format(Ref, Refer))
            #print("q1 = {}, q2 = {}".format(Dem[Refer], ResCol[Refer][1]))
            if (Dem[Refer] > ResCol[Refer][1] and ResCol[Refer][1] !=0):
                quant = ResCol[Refer][1]
            else:
                quant = Dem[Refer]
                #Stepping stones#### je commence ici glodi
                
            #print("quant d'affectation : {} ".format(quant))
            """ chargment depart et arrive """
            pointage[0] = Ref
            pointage[1] = Refer
            colonne = pointage[1]
            arrive = pointage[0]
            MarkCol[colonne] = 1
            MarkLin[arrive] = 1
            #cptr = 0
            #print("Pointage : {}, \n affect : \n{}\n trans : {}".format(pointage, Affect, Trans))
            #Phase d’initialisation
            sommetD = []
            ChenimTrouve = 0
            chemins = []
            for i in range(n):
                if(Trans[i][colonne] == 0):
                    #[ligne, colonne, father, visite]
                    sommetD.append([i, colonne, None]) 
                    if(i == arrive):
                        reperage.append([i, colonne])
                        ChenimTrouve = 1
                        break
            if(ChenimTrouve == 0):
                for sdd in range(len(sommetD)):
                    parcours = []
                    parcours2 = []
                    visite = []
                    visite2 = []
                
                    for i in range(n):
                        visite.append([])
                        visite2.append([])
                        #init visite
                        for j in range(m) :
                            visite[i].append(0)
                            visite2[i].append(0)

                    visite = np.array(visite)
                    voisins = []
                    file.append(sommetD[sdd])

                    #Parcours en largeur
                    while len(file) > 0:
                        t = file[0]
                        voisins = voisiner(t)
                        father = len(parcours)
                        #print("Voisins et father", voisins, father)
                        #print(visite)

                        #Phase d’action (parcours du graphe G)

                        for v in range(len(voisins)):
                            vL = voisins[v][0]
                            vC = voisins[v][1]
                            if(visite[vL][vC] == 0):
                                visite[vL][vC] = 1 #(visite en cours)
                                voisins[v][2] = father
                                file.append(voisins[v])
                                
                        p = file.pop(0)#Dequeue
                        visite[p[0]][p[1]] = 2 #Visite[t] = 2 : t deja visite
                        parcours.append(p)#ajout dans parcours
                        if(len(voisins) > 0):
                            ##si c'est l'arrivee
                            if(p[0] == arrive):
                                chemins.append([])
                                Ch_index = len(chemins)-1
                                if(len(parcours2) == 0):
                                    chemins[Ch_index].append(p)
                                    #print("chemin voisin > 0=============", chemins)
                                else:
                                    #print("reconstituer le chemin partant de l'arrive jusqu'au sommet de depart")
                                    chemins[Ch_index].append(p)
                                    fatherC = p[2]
                                    while fatherC != None:
                                        chemins[Ch_index].append(parcours[fatherC])
                                        fatherC = parcours[fatherC][2]
                            parcours2.append(p)
                            #print("chemin voisin > 0", chemins)
                        else:
                            if(p[0] == arrive):
                                chemins.append([])
                                Ch_index = len(chemins)-1
                                if(len(parcours2) == 0):
                                    chemins[Ch_index].append(p)
                                else:
                                    #print("traiter ce apres pour reconstituer le chemin partant du sommet")
                                    chemins[Ch_index].append(p)
                                    fatherC = p[2]
                                    while fatherC != None:
                                        chemins[Ch_index].append(parcours[fatherC])
                                        fatherC = parcours[fatherC][2]
                        
                            #print("chemin voisin == 0", chemins)
                            
                            #print("t donne  = {}, len voisins = {}".format(t, len(voisins)))


                    #print("les sommets depart donnes : {}\n file : {}\n parcours : {}\n".format(sommetD, file, np.array(parcours)))
                #print("les chemins donnent : {}".format(chemins))

                Distance = []
                for i in range(len(chemins)):
                    Distance.append(len(chemins[i]))

                #print(Distance)
                miniD = [0, Distance[0]]
                calculQ = 0
                for i in range(len(Distance)):
                    if (miniD[1] > Distance[i]):
                        miniD[1]= Distance[i]
                        miniD[0]= i
                    elif (miniD[1] == Distance[i]):
                        for j in range(len(chemins[miniD[0]])):
                            chm = chemins[miniD[0]][j]
                            #print(chm)
                            #print("affect = ", Affect[chm[0]][chm[1]], j%2)
                            if((j % 2) == 0):
                                calculQ = Affect[chm[0]][chm[1]] + quant
                            else :
                                calculQ = Affect[chm[0]][chm[1]] - quant
                            if(calculQ < 0):
                                miniD[1]= Distance[i]
                                miniD[0]= i
                        #print(calculQ, i)
                        
                #print(miniD)

                reperage = chemins[miniD[0]]
                
            #print(chemins[miniD[0]])
            #plus court chemin

            #print("chemin donne {} ".format(reperage))
            for i in range(len(reperage)):
                ll = reperage[i][0]
                cc = reperage[i][1]
                if(i == 0):
                    Affect[ll][cc] = Affect[ll][cc] + quant 
                else :
                    if((i % 2) == 1) : 
                        Affect[ll][cc] = Affect[ll][cc] - quant
                    else : Affect[ll][cc] = Affect[ll][cc] + quant
                if(Trans[ll][cc] == 0 and Affect[ll][cc] == 0):
                    Mark[ll][cc] = 0
            Dem[Refer] = Dem[Refer] - quant
            Dispo[Ref] = Dispo[Ref] - quant
            Cont -= quant

            #print("Cont {}, Dispo {}, Dem {}, Affect \n {}".format(Cont, Dispo, Dem, Affect))
            #print(Trans)
            #reinitialisation
            
            pointage = [None, None]
            continuer = True
            reperage = []
            ligne = None
            colonne = None
            Ref = None
            Refer = None
            """ for i in range(n):
                MarkLin[i] = 0
                Init[i] = 0
                for j in range(m):
                    MarkCol[j] = 0 """
        
            for i in range(n):
                MarkLin2[i] = 0
            for j in range(m): 
                MarkCol2[j] = 0
        ddd +=1
        for i in range(n):
                MarkLin2[i] = 0
        for j in range(m): 
            MarkCol2[j] = 0
    cout = 0
    for i in range(n):
            for j in range(m):
                if(Affect[i][j] != 0):
                    cout += Dcs[i][j] * Affect[i][j]



    #print(cout)
    print(Affect)
    return cout

print(Prim_Dual([[14., 64., 28., 88., 37., 22., 21.],  [31., 18., 71., 55., 54., 26., 84.],  [ 6., 10., 16., 82., 43.,  9., 61.]], [91., 90., 80.], [ 33.,  18.,  33.,  22.,  17.,  22., 116.], 3, 7))