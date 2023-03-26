import C3_fonction as fct

fichier = input("Quel fichier souhaitez-vous utiliser  ? ")

fichier = "C3-" + str(fichier) + ".txt"

fct.Afficher(fichier)
fct.deterministe(fichier)
fct.complet(fichier)
fct.standard(fichier)
