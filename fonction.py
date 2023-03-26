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
    for c in range(lig-1):
        print("j=",lig-1)
        print("_______________")
        for j in range(4):
            print(matrice[c][j],'|', end=' ')
        print()

    print("\n")