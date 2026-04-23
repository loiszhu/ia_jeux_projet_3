import random
import time
import tme1
import matplotlib.pyplot as plt

# n : nombre d'étudiants, m : nombre de masters

# Génération aléatoire des préférences des étudiants
def generer_pref_etu(n, m) :
    CE = []
    for i in range(n) :
        # On génère une liste de préférence aléatoire pour chaque étudiant
        pref = list(range(m))
        random.shuffle(pref)
        CE.append(pref)
    return CE

# Génération aléatoire des préférences des masters
def generer_pref_spe(n, m) :
    CP = []
    for i in range(m) :
        # On génère une liste de préférence aléatoire pour chaque master
        pref = list(range(n))
        random.shuffle(pref)
        CP.append(pref)
    return CP

# Génération aléatoire des capacités de chaque master
def generer_capacites(n, m) :
    # base : nombre d'étudiants par master si la répartition était parfaite
    base = n // m
    # capacites : liste des capacités de chaque master, initialisée à base
    capacites = [base] * m
    # reste : nombre d'étudiants qui restent à répartir après avoir attribué base étudiants à chaque master
    reste = n - base * m

    # On répartit les étudiants restants un par un aux masters de manière aléatoire
    for i in range(reste) :
        capacites[i] += 1
    return capacites

# Mesure du temps d'exécution de l'algorithme de Gale-Shapley
def mesurer_temps() :
    # On teste pour des tailles de n allant de 200 à 2000 par pas de 200
    tailles = list(range(200, 2001, 200))
    # temps_moyens contiendra le temps moyen d'exécution pour chaque taille de n
    temps_moyens = []

    for n in tailles :
        # m fixé à 10 pour observer l'impact du nombre d'étudiants sur le temps d'exécution
        m = 10
        # total contiendra la somme des temps d'exécution pour les 10 répétitions, afin de calculer la moyenne
        total = 0

        # On répète 10 fois pour chaque taille afin d'obtenir une moyenne plus fiable
        for _ in range(10) :
            # Génération aléatoire des préférences et des capacités pour n étudiants et m masters
            CE = generer_pref_etu(n, m)
            CP = generer_pref_spe(n, m)
            capacites = generer_capacites(n, m)

            # Mesure du temps d'exécution de l'algorithme de Gale-Shapley côté étudiant
            debut = time.time()
            tme1.gale_shapley_etu(CE, CP, capacites)
            fin = time.time()

            # Ajout du temps d'exécution à total pour calculer la moyenne plus tard
            total += fin - debut

        # Calcul du temps moyen d'exécution pour cette taille de n et ajout à la liste des temps moyens
        temps_moyens.append(total / 10)

    return tailles, temps_moyens

# Affichage de la courbe du temps d'exécution en fonction de n
def afficher_courbe_temps(tailles, temps):
    plt.plot(tailles, temps)
    plt.xlabel("n (nombre d'étudiants)")
    plt.ylabel("Temps (s)")
    plt.title("Temps d'exécution Gale-Shapley")
    plt.show()

# Mesure du nombre d'itérations de l'algorithme de Gale-Shapley côté étudiant
def mesurer_iterations() :
    tailles = list(range(200, 2001, 200))
    iterations_moyennes = []

    for n in tailles :
        m = 10
        total_iterations = 0

        for _ in range(10) :
            CE = generer_pref_etu(n, m)
            CP = generer_pref_spe(n, m)
            capacites = generer_capacites(n, m)

            _, nb_iterations = tme1.gale_shapley_etu(CE, CP, capacites)
            total_iterations += nb_iterations

        iterations_moyennes.append(total_iterations / 10)
    
    return tailles, iterations_moyennes

# Affichage de la courbe du nombre d'itérations en fonction de n
def afficher_courbe_ite(tailles, iterations):
    plt.plot(tailles, iterations)
    plt.xlabel("n (nombre d'étudiants)")
    plt.ylabel("Nombre d'itérations")
    plt.title("Nombre d'itérations Gale-Shapley")
    plt.show()