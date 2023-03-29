def ajoute_int(matrice, entier, a_ou_b, h):
    """permet de remplir la table de transition"""
    if not matrice:
        if a_ou_b == 'a':
            matrice.append([entier, " "+str(h)+" ", ' / ', ' / ',' / '])
        elif a_ou_b == 'b':
            matrice.append([entier, ' / ', " "+str(h)+" ", ' / ',' / '])
        elif a_ou_b == 'c':
            matrice.append([entier, ' / ', ' / ', " "+str(h)+" ",' / '])
        elif a_ou_b == 'd':
            matrice.append([entier, ' / ', ' / ', ' / '," "+str(h)+" "])
    else:
        for i in range(len(matrice)):
            if entier == matrice[i][0]:
                if a_ou_b == 'a':
                    if matrice[i][1] != ' / ':
                        matrice[i][1] = str(matrice[i][1]) + ',' + str(h)
                    else:
                        matrice[i][1] = " "+str(h)+" "
                elif a_ou_b == 'b':
                    if matrice[i][2] != ' / ':
                        matrice[i][2] = str(matrice[i][2]) + ',' + str(h)
                    else:
                        matrice[i][2] = " "+str(h)+" "
                elif a_ou_b == 'c':
                    if matrice[i][3] != ' / ':
                        matrice[i][3] = matrice[i][3] + ',' + str(h)
                    else:
                        matrice[i][3] = " "+str(h)+" "
                elif a_ou_b == 'd':
                    if matrice[i][4] != ' / ':
                        matrice[i][4] = str(matrice[i][4]) + ',' + str(h)
                    else:
                        matrice[i][4] = " "+str(h)+" "
                break
        else:
            matrice.append([entier] + [' / '] * (len(matrice[0]) - 1))
            for i in range(len(matrice)):
                if matrice[i][0] == entier:
                    if a_ou_b == 'a':
                        if matrice[i][1] != ' / ':
                            matrice[i][1] = str(matrice[i][1]) + ',' + str(h)
                        else:
                            matrice[i][1] = " "+str(h)+" "
                    elif a_ou_b == 'b':
                        if matrice[i][2] != ' / ':
                            matrice[i][2] = matrice[i][2] + ',' + h
                        else:
                            matrice[i][2] = " "+str(h)+" "
                    elif a_ou_b == 'c':
                        if matrice[i][3] != ' / ':
                            matrice[i][3] = matrice[i][3] + ',' + h
                        else:
                            matrice[i][3] =" "+str(h)+" "
                    elif a_ou_b == 'd':
                        if matrice[i][4] != ' / ':
                            matrice[i][4] = matrice[i][4] + ',' + h
                        else:
                            matrice[i][4] = " "+str(h)+" "
                    break

    return matrice

i=0
def Afficher(fichier):
    """Permet d'afficher la table de transition, principalement que graphique (parcours de tableaux) qui va appeler la fonction ajoute_int pour creer le tableau"""
    EI=[]

    ET=[]
    with open(fichier, "r") as f:
        ligne = f.readline()
        col = ligne.strip()  # nbr alphabet
        col=int(col)
        ligne = f.readline()
        lig = ligne.strip()  # nbr etat
        lig=int(lig)
        ligne = f.readline()
        EI = ligne.strip(" ") #etat initial
        ligne = f.readline()
        ET = ligne.strip(" ") #etat terminal
        ligne = f.readline()
        nbr_transition = ligne.strip()  # etat terminal
        ligne = f.readline()
        b = list(ligne.strip())  # etat terminal
        print("Etat(s) initial(aux) : ",EI[1:])#affiche le ou les EI
        print("Etat(s) terminal(aux) : ",ET[1:])#affiche le ou les ET
        matrice=[]
        for p in range(int(nbr_transition)):
            temp =list(ligne.strip())
            print(temp)
            matrice=ajoute_int(matrice,int(temp[0]),temp[1],int(temp[2]))
            ligne = f.readline()
    print("\ntable de transition : ")
    for c in range(lig-1):
        print("___________________________")
        for j in range(5):
            print(matrice[c-1][j],'|', end=' ')
        print()
    print("___________________________")
    print("\n")
    
    
    
def standard(fichier):
    """On va dans un premier temps verifier si les conditions sont True ou False:
    False : si il y a un ou plusieurs EI, si les etats destinataire des transitions est egale aux EI.
    True: sinon il est standardisé et il affiche.
    Standardisation :
    On va dans un premier temps rechercher les etats finaux et les remplacer par des I pour l'affichage, on recupere aussi les etats teerminaux. On va ensuite affiche les transitions correspondantes
    avec les etats terminaux et initial.
    """
    #un seul état initial ?
    est_standard = True
    with open(fichier, 'r') as f:
        nb_initial = 0
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        nb_initial = int(ligne[0])

        if nb_initial > 1:
            est_standard = False

    #transition sur un état initial ?
    initial = []
    nb_transition = 0
    with open(fichier, 'r') as f:
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        initial = ligne.strip(" ")
        ligne = f.readline()
        ligne = f.readline()
        nb_transition = int(ligne)

        for i in range(nb_transition):
            ligne = f.readline()
            print("test ",ligne[2])
            if ligne[2] in initial:
                est_standard = False


    print("L'automate est standard :", est_standard)

    if est_standard == False:
        print("Souhaitez vous standardiser cet automate ? (o/n)")
        reponse = input()

        if reponse == 'o' or reponse == 'O':
            with open(fichier, 'r') as f:
                ligne = f.readline()
                ligne = f.readline()
                ligne = f.readline()
                ligne = f.readline()
                final = ligne.strip(" ")
                ligne = f.readline()
                final = final[2:]
                print("f=", final) #recup l'EI
                print("Voici les transitions de l'automate standardisé :")
                new_terminaux = []
                for i in range(nb_transition):
                    ligne = f.readline()
                    if ligne[2] in initial and ligne[2] not in new_terminaux and ligne[2] not in final: #recherche d'autre EI
                        new_terminaux.append(ligne[2]) #ajoute a la liste
                    elif ligne[0] in initial:
                        print('I',ligne[1:3]) #afficheles transition avec I
                    else:
                        print(ligne[:3]) #affiche le reste des transitions
                """affichage final"""
                print("Etat initial : I")
                print("Etat(s) terminal(aux) :",new_terminaux,final)



def deterministe(fichier):
    """Permet de dire si l'automate est deterministe ou non.
    Pour cela,on va verifier qu'un etat ne renvoie pas deux fois la meme mettre en rajoutant sa lettre dans une liste,
     si il est detecte dans cette derniere, l'etat sera egale à False sinon il sera egale a True"""
    transition = []
    est_deterministe = True
    nb_transition = 0
    with open(fichier, 'r') as f:

        #Passe les 5 premières lignes :
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        nb_transition = ligne.strip()

        for i in range(int(nb_transition)):
            ligne = f.readline()
            if ligne[:2] in transition:
                print(ligne[:2], "?")
                est_deterministe = False
            transition.append(ligne[:2])

        print("L'automate est déterministe : ", est_deterministe)                        
                   
                    
def complet(fichier):
    """ Permet de savoir si l'automate est complet ou non.
    On verifie d'abord que ce dernier est deterministe, si ce dernier ne l'est pas on renvoie qu'il ne l'est pas.
    Si il est deterministe,"""
    transition = []
    est_deterministe = True
    nb_transition = 0
    with open(fichier, 'r') as f:

        # Passe les 5 premières lignes :
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        ligne = f.readline()
        nb_transition = ligne.strip()

        for i in range(int(nb_transition)):
            ligne = f.readline()
            if ligne[:2] in transition:
                est_deterministe = False
            transition.append(ligne[:2])

    if est_deterministe == False:
        print("L'automate n'est pas déterministe, on ne peut donc pas dire s'il est complet,"
              "on recupere tous les etats des transitions, on compare ensuite le nombre d'etat et de symbole, si il est different, Il est False "
              "idem si le nombre de transition est different du produit du nombre d'etat et du nombre de symbole. Si l'automate reste True alors on print qu'il est complet.")
    else:
        nb_etat = 0
        nb_symbole = 0
        est_complet = True
        etat = []
        with open(fichier, 'r') as f:

            # Passe les 5 premières lignes :
            ligne = f.readline()
            nb_symbole = ligne.strip()
            ligne = f.readline()
            nb_etat = ligne.strip()
            ligne = f.readline()
            ligne = f.readline()
            ligne = f.readline()

            for i in range(int(nb_transition)):
                ligne = f.readline()
                etat.append(ligne[:1])
        
            for i in etat:
                if etat.count(i) != int(nb_symbole):
                    est_complet = False
            
            if int(nb_transition) != int(nb_etat)*int(nb_symbole):
                est_complet = False

            print("L'automate est complet :",est_complet)
