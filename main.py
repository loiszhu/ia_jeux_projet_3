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

    etu = {}
    for i in range (0, len(listePrefEtu)):
        etu[i] = True
    
    while ()
    
