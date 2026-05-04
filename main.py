# import exemple # Pour pouvoir utiliser les methodes de exemple.py
import tme1
import tme2
import tme3
import time
import matplotlib.pyplot as plt

# print("bonjour")
# maListe=exemple.lectureFichier("test.txt") # Execution de la methode lectureFichier du fichier exemple.
# print(maListe)
# print(len(maListe)) #Longueur de la liste.
# exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier


# TME 1

# Question 1
matPrefEtu = tme1.lire_preferences_etu("PrefEtu.txt")
print("Liste des préférences des étudiants sur les masters : \n", matPrefEtu, "\n")

matPrefSpe, capacites = tme1.lire_preferences_spe("PrefSpe.txt")
print("Liste des préférences des masters sur les étudiants : \n", matPrefSpe, "\n")
print("Liste des capacités d'étudiants de masters : \n", capacites, "\n")

# Question 3 - GS côté étudiant
debut = time.time()
affectations_etu_Q3, it_etu = tme1.gale_shapley_etu(matPrefEtu, matPrefSpe, capacites)
fin = time.time()
temps_exec = fin - debut
print("Résultat d'affectation retournée par l'algo côté étudiant : \n", affectations_etu_Q3)
print(f"le temps d'exécution de l'algo est {temps_exec * 1000: .5f} ms")

# Question 4 - GS côté parcours
debut = time.time()
affectations_etu_Q4, it_spe = tme1.gale_shapley_spe(matPrefEtu, matPrefSpe, capacites)
fin = time.time()
temps_exec = fin - debut
print("Résultat d'affectation retournée par l'algo côté parcours : \n", affectations_etu_Q4)
print(f"le temps d'exécution de l'algo est {temps_exec * 1000: .5f} ms")

# Question 6 - Test de stabilité
# GS côté étudiant
paires_etu = tme1.trouver_paires_instables(matPrefEtu, matPrefSpe, capacites, affectations_etu_Q3)
if not paires_etu:
    print("Aucune paire instable, affectation étudiant est stable")
else :
    print("Paires instables dans les affectations étudiants : ", paires_etu)

paires_spe = tme1.trouver_paires_instables(matPrefEtu, matPrefSpe, capacites, affectations_etu_Q4)
if not paires_spe:
    print("Aucune paire instable, affectation parcours est stable")
else :
    print("Paires instables dans les affectations parcours : ", paires_spe)

print("\n")


# TME 2

#Question 8 - Mesure du temps d'exécution de l'algorithme de Gale-Shapley
tailles, temps_etu = tme2.mesurer_temps(tme1.gale_shapley_etu)
tailles, temps_spe = tme2.mesurer_temps(tme1.gale_shapley_spe)

# Affichage de la courbe du temps d'exécution en fonction de n
plt.plot(tailles, temps_etu, label="GS côté étudiant")
plt.plot(tailles, temps_spe, label="GS côté parcours")
plt.xlabel("n (nombre d'étudiants)")
plt.ylabel("Temps (s)")
plt.title("Temps d'exécution Gale-Shapley")
plt.legend()
plt.show()

#Question 10 - Mesure du nombre d'itérations de l'algorithme de Gale-Shapley
tailles, iterations_etu = tme2.mesurer_iterations(tme1.gale_shapley_etu)
tailles, iterations_spe = tme2.mesurer_iterations(tme1.gale_shapley_spe)

# Affichage de la courbe du nombre d'itérations en fonction de n
plt.plot(tailles, iterations_etu, label="GS côté étudiant")
plt.plot(tailles, iterations_spe, label="GS côté parcours")
plt.xlabel("n (nombre d'étudiants)")
plt.ylabel("Nombre d'itérations")
plt.title("Nombre d'itérations Gale-Shapley")
plt.legend()
plt.show()


# TME 3

# Question 11 - Maximiser l'utilité minimale
scores_etudiants_11, aff_q11 = tme3.resoudre_equite(matPrefEtu, matPrefSpe, capacites)

# Question 12 - Maximiser l'utilité totale
scores_etudiants_12, aff_q12 = tme3.resoudre_efficacite(matPrefEtu, matPrefSpe, capacites)

# Question 14 - Trouver le plus petit k pour lequel 
k, scores_etudiants_14, aff_q14 = tme3.resoudre_plus_petit_k(matPrefEtu, matPrefSpe, capacites)

# Question 15 - Comparaison des solutions
tme3.evaluer_affectation("GS côté étudiant", affectations_etu_Q3, matPrefEtu, matPrefSpe, capacites)
tme3.evaluer_affectation("GS côté parcours", affectations_etu_Q4, matPrefEtu, matPrefSpe, capacites)
tme3.evaluer_affectation("Q11-Équité", aff_q11, matPrefEtu, matPrefSpe, capacites)
tme3.evaluer_affectation("Q12-Efficacité", aff_q12, matPrefEtu, matPrefSpe, capacites)
tme3.evaluer_affectation("Q14-Plus_petit_k", aff_q14, matPrefEtu, matPrefSpe, capacites)