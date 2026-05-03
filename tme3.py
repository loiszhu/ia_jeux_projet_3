import gurobipy as gp

def resoudre_efficacite(prefEtu, prefSpe, capacites):
    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)

    # Calculer les scores de Borda
    # u[i][j] = utilité de l'étudiant i pour le master j
    u = [[nb_spe-prefEtu[i].index(j) for j in range(nb_spe)] for i in range(nb_etu)]
    # v[j][i] = utilité du master j pour l'étudaint i
    v = [[nb_etu-prefSpe[j].index(i) for i in range(nb_etu)] for j in range(nb_spe)]

    # Initialiser le modèle Gurobi
    model = gp.Model("Maximiser_efficacite")
    model.Params.LogToConsole = 0

    # Créer des variables binaires x_ij
    x = {}
    for i in range(nb_etu):
        for j in range(nb_spe):
            x[i,j] = model.addVar(vtype=gp.GRB.BINARY, name=f"x_{i}{j}")

    # Fonction objectif : maximiser la somme des utilités
    objectif = gp.quicksum(x[i,j] * (u[i][j] + v[j][i]) for i in range(nb_etu) for j in range(nb_spe))
    model.setObjective(objectif, gp.GRB.MAXIMIZE)

    # Ajouter des contraintes
    # Contrainte 1 : Chaque étudiant est affecté à un seul parcours
    for i in range(nb_etu):
        model.addConstr(gp.quicksum(x[i,j] for j in range(nb_spe)) == 1, name=f"Etu_{i}")
    
    # Contrainte 2 : Respect des capacités des parcours
    for j in range(nb_spe):
        model.addConstr(gp.quicksum(x[i,j] for i in range(nb_etu)) <= capacites[j] , name=f"Master_{j}")
        
    # Résolution mathématique par le solveur
    model.optimize()

    # Résultats
    if model.status == gp.GRB.OPTIMAL :
        somme_utilite = model.objVal

        # On récupère les scores des étudiants dans cette affectation optimale
        scores_etudiants = []
        for i in range(nb_etu):
            for j in range(nb_spe):
                # Si x_ij vaut 1 (aux erreurs d'arrondi près)
                if x[i,j].X > 0.5:
                    scores_etudiants.append(u[i][j])
        
        # Calculer l'utilité moyenne globale de l'affectation
        utilite_moyenne = somme_utilite / nb_etu 
        utilite_minimale = min(scores_etudiants)

        print(f"Q12 - Résultats de l'Efficacité")
        print(f"Somme des utilités (Etu + Masters) : {somme_utilite}")
        print(f"Utilité moyenne par affectation : {utilite_moyenne:.2f}")
        print(f"Utilité minimale (le pire score d'un étudiant) : {utilite_minimale}")

        return scores_etudiants
    else:
        print("Aucune solution optimale trouvée.")
        return None


def resoudre_plus_petit_k(prefEtu, prefSpe, capacites):
    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)

    # Calculer les scores de Borda
    # u[i][j] = utilité de l'étudiant i pour le master j
    u = [[nb_spe-prefEtu[i].index(j) for j in range(nb_spe)] for i in range(nb_etu)]
    # v[j][i] = utilité du master j pour l'étudaint i
    v = [[nb_etu-prefSpe[j].index(i) for i in range(nb_etu)] for j in range(nb_spe)]

    # Tester les valeurs de k de 1 jusqu'au nombre total de masters
    for k in range(1, nb_spe+1):
        # Initialiser le modèlre Gurobi
        model = gp.Model(f"Plus_petit_k_{k}")
        model.Params.LogToConsole = 0

        # Créer des variables binaires x_ij
        x = {}
        for i in range(nb_etu):
            for j in range(nb_spe):
                x[i,j] = model.addVar(vtype=gp.GRB.BINARY, name=f"x_{i}{j}")

        # Fonction objectif : maximiser la somme des utilités
        objectif = gp.quicksum(x[i,j] * (u[i][j] + v[j][i]) for i in range(nb_etu) for j in range(nb_spe))
        model.setObjective(objectif, gp.GRB.MAXIMIZE)

        # Ajouter des contraintes
        # Contrainte 1 : Chaque étudiant est affecté à un seul parcours
        for i in range(nb_etu):
            model.addConstr(gp.quicksum(x[i,j] for j in range(nb_spe)) == 1, name=f"Etu_{i}")
        
        # Contrainte 2 : Respect des capacités des parcours
        for j in range(nb_spe):
            model.addConstr(gp.quicksum(x[i,j] for i in range(nb_etu)) <= capacites[j] , name=f"Master_{j}")

        # Contrainte 3 : Chaque étudiant a au pire son k-ième choix
        for i in range(nb_etu):
            model.addConstr(gp.quicksum(x[i,j] * u[i][j] for j in range(nb_spe)) >= (nb_spe - k), name=f"Equite_k_etu_{i}")
    
        # Résolution mathématique par le solveur
        model.optimize()

        # Résultats
        # Si le modèle trouve une solution optimale, on s'arrête
        if model.status == gp.GRB.OPTIMAL :
            somme_utilite = model.objVal
            affectations = [0] * nb_etu
            scores_etudiants = []
            for i in range(nb_etu):
                for j in range(nb_spe):
                    # Si x_ij vaut 1 (aux erreurs d'arrondi près)
                    if x[i,j].X > 0.5:
                        affectations[i] = j
                        rang_obtenu = nb_spe - u[i][j]
                        print(f"Affectation : Etudiant {i} - Master {j} ({rang_obtenu}e voeu)")
                        scores_etudiants.append(u[i][j])

            print(f"Q14 - Résultat trouvé pour k = {k}")
            print(f"Somme des utilités (Etu + Masters) : {somme_utilite}")
            
            return k, affectations, scores_etudiants
        else :
            # Si le modèle est irréalisable, on continue la boucle
            print(f"Pas de solution possible pour k = {k}")

    print("Aucune solution optimale trouvée.")
    return None, None, None