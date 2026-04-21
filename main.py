# import exemple # Pour pouvoir utiliser les methodes de exemple.py
import tme1
import time

# print("bonjour")
# maListe=exemple.lectureFichier("test.txt") # Execution de la methode lectureFichier du fichier exemple.
# print(maListe)
# print(len(maListe)) #Longueur de la liste.
# exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier


# TME 1

# Question 1

listePrefEtu = tme1.lire_preferences_etu("PrefEtu.txt")
print("Liste des préférences des étudiants sur les masters : \n", listePrefEtu, "\n")

listePrefSpe, capacites = tme1.lire_preferences_spe("PrefSpe.txt")
print("Liste des préférences des masters sur les étudiants : \n", listePrefSpe, "\n")
print("Liste des capacités d'étudiants de masters : \n", capacites, "\n")

# Question 3
debut = time.time()
affectations_etu = tme1.gale_shapley_etu(listePrefEtu, listePrefSpe, capacites)
fin = time.time()
temps_exec = fin - debut
print("Résultat d'affectation retournée par l'algo côté étudiant : \n", affectations_etu)
print(f"le temps d'exécution de l'algo est {temps_exec * 1000: .5f} ms")

# Question 4
debut = time.time()
affectations_spe = tme1.gale_shapley_spe(listePrefEtu, listePrefSpe, capacites)
fin = time.time()
temps_exec = fin - debut
print("Résultat d'affectation retournée par l'algo côté parcours : \n", affectations_spe)
print(f"le temps d'exécution de l'algo est {temps_exec * 1000: .5f} ms")

# Question 6 - Test de stabilité
paires_etu = tme1.trouver_paires_instables(listePrefEtu, listePrefSpe, capacites, affectations_etu)
if not paires_etu:
    print("Aucune paire instable, affectation étudiant est stable")
else :
    print("Paires instables dans les affectations étudiants : ", paires_etu)

paires_spe = tme1.trouver_paires_instables(listePrefEtu, listePrefSpe, capacites, affectations_spe)
if not paires_spe:
    print("Aucune paire instable, affectation parcours est stable")
else :
    print("Paires instables dans les affectations parcours : ", paires_spe)