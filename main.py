# import exemple # Pour pouvoir utiliser les methodes de exemple.py
import tme1

# print("bonjour")
# maListe=exemple.lectureFichier("test.txt") # Execution de la methode lectureFichier du fichier exemple.
# print(maListe)
# print(len(maListe)) #Longueur de la liste.
# exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier


# TME 1

# Question 1

print("Liste des préférences des étudiants sur les masters")
listePrefEtu = tme1.lire_preferences_etu("PrefEtu.txt")
print(listePrefEtu)

print("\n")

print("Liste des préférences des masters sur les étudiants")
listePrefSpe, capacites = tme1.lire_preferences_spe("PrefSpe.txt")
print(listePrefSpe)


# Question 3
def aEtuLibre(dicoEtu):
    for etu in dicoEtu :
        if dicoEtu[etu] == False :
            return False
    return True

def gale_shapley_etu(prefSpe, prefEtu):
    # ensemble d'étudiants libres (au début tout le monde est libre)
    libres = list(a for a in range (len(prefEtu)))

    # compte le nombre de spé que l'étudiant a choisit
    propositions = list(0 for a in range (len(prefEtu)))

    # spé affectée pour chaque étudiant : {SpeX:EtuX, SpeY:EtuY, ...}
    aff = {}

    # tant qu'il existe un étudiant libre
    while (libres) :
        # sélectionne un étudiant
        etu = libres[0]

        # sélectionne la spé préféréé de l'étudiant
        spe = prefEtu[etu][propositions[etu]]
        propositions[etu] += 1 # incrémente le nombre de proposition de l'étu

        # si la spé est libre, alors on lui donne cette proposition
        if spe not in aff :
            aff[spe] = etu
            libres.pop(0)
        
        # sinon on compare si le spé préfère l'etu actuel, ou l'etu deja affecté
        else :
            autre = libres[0]
            # s'il préfère cet etu, on le remplace
            if prefSpe[spe].index(etu) < prefSpe[spe].index(autre) :
                aff[spe] = etu
                libres.pop(0)
                libres.append(autre)
    
    return aff
