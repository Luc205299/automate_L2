def ajoute_int(matrice, entier, a_ou_b, h):
    """permet de remplir la table de transition"""
    if not matrice:
        if a_ou_b == 'a':
            matrice.append([entier, h, 0, 0])
        elif a_ou_b == 'b':
            matrice.append([entier, 0, h, 0])
        elif a_ou_b == 'c':
            matrice.append([entier, 0, 0, h])
    else:
        for i in range(len(matrice)):
            if entier == matrice[i][0]:
                if a_ou_b == 'a':
                    matrice[i][1] = h
                elif a_ou_b == 'b':
                    matrice[i][2] = h
                elif a_ou_b == 'c':
                    matrice[i][3] = h
                break
        else:
            matrice.append([entier] + ['/'] * (len(matrice[0]) - 1))
            for i in range(len(matrice)):
                if matrice[i][0] == entier:
                    if a_ou_b == 'a':
                        matrice[i][1] = h
                    elif a_ou_b == 'b':
                        matrice[i][2] = h
                    elif a_ou_b == 'c':
                        matrice[i][3] = h
                    break

    return matrice

i=0
def Afficher(fichier):
    """Permet d'afficher la table de transition"""
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
    for c in range(lig):

        print("_______________")
        for j in range(4):
            print(matrice[c-1][j],'|', end=' ')
        print()

    print("\n")
    
    
    
def standard(fichier):
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

                print("Voici les transitions de l'automate standardisé :")
                new_terminaux = []
                for i in range(nb_transition):
                    ligne = f.readline()
                    if ligne[2] in initial and ligne[2] not in new_terminaux and ligne[2] not in final:
                        new_terminaux.append(ligne[2])
                    elif ligne[0] in initial:
                        print('I',ligne[1:3])
                    else:
                        print(ligne[:3])

                print("Etat initial : I")
                print("Etat(s) terminal(aux) :",new_terminaux,final)
                       
def deterministe(fichier):
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
                est_deterministe = False
            transition.append(ligne[:2])

        print("L'automate est déterministe : ", est_deterministe)               
        
                   
                    
def complet(fichier):
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
        print("L'automate n'est pas déterministe, on ne peut donc pas dire s'il est complet")
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

            print("L'automate est complet :",est_complet,"\n")
