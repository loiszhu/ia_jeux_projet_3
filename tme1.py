def lire_preferences_etu(f) :
    monFichier = open(f, "r")
    contenu = monFichier.readlines()
    contenu = contenu[1:]
    monFichier.close()
    for i in range (0, len(contenu)) :
        contenu[i] = contenu[i].split()
        contenu[i] = [int(x) for x in contenu[i][2:]]
    return contenu

def lire_preferences_spe(f) :
    monFichier = open(f, "r")
    contenu = monFichier.readlines()

    ligne_cap = contenu[1].split()
    capacites = [int(x) for x in ligne_cap[1:]]

    contenu = contenu[2:]
    monFichier.close()
    for i in range (0, len(contenu)) :
        contenu[i] = contenu[i].split()
        contenu[i] = [int(x) for x in contenu[i][2:]]
    return contenu, capacites


def gale_shapley_etu(prefEtu, prefSpe, capacites):
    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)
    
    # Pile des étudiants libres
    etu_libres = list(range(nb_etu))

    # Tableau contenant l'indice du prochain master à proposer pour chaque étudiant dans sa liste de préférence
    etu_propositions = [0] * nb_etu

    # Matrice des rangs des étudiants pour chaque master
    rang_etu = [[0]*nb_etu for _ in range(nb_spe)]
    for spe_id in range(nb_spe):
        for rang, etu_id in enumerate(prefSpe[spe_id]):
            rang_etu[spe_id][etu_id] = rang

    # Tableau des listes des étudiants affectés pour chaque master
    spe_affectations = [[] for _ in range(nb_spe)]

    # Q10 - ajout d'un compteur d'itérations
    nb_iterations = 0

    # Tant qu'il existe un étudiant libre
    while (etu_libres) :
        # Q10 - incrémentation du compteur d'itérations à chaque boucle
        nb_iterations += 1

        # On prend un étudiant libre
        etu_id = etu_libres.pop()

        # S'il a déjà proposé à tous les masters, il ne peut plus proposer
        if etu_propositions[etu_id] >= nb_spe :
            continue

        # L'étudiant propose à son meilleur choix disponible
        spe_id = prefEtu[etu_id][etu_propositions[etu_id]]
        # Met à jour le prochain master à proposer de l'étudiant
        etu_propositions[etu_id] += 1

        # Si le master a encore de la place, alors on lui donne cette proposition
        if len(spe_affectations[spe_id]) < capacites[spe_id] :
            spe_affectations[spe_id].append(etu_id)
        # Sinon on compare si le master préfère l'étudiant actuel, ou l'étudiant déjà affecté
        else :
            # Trouve l'étudiant le moins préféré affecté par ce master
            pire_etu_aff = spe_affectations[spe_id][0]
            # Le rang d'étudiant le moins préféré affecté par ce master
            pire_rang_aff = rang_etu[spe_id][pire_etu_aff]
            # On parcourt les autres étudiants affecté pour trouver celui qui est moins préféré
            for etu in spe_affectations[spe_id]:
                rang = rang_etu[spe_id][etu]
                if rang > pire_rang_aff :
                    pire_rang_aff = rang
                    pire_etu_aff = etu
            
            # Le rang d'étudiant actuel
            rang_etu_actuel = rang_etu[spe_id][etu_id]

            # Si le rang de l'étudiant actuel est meilleur que le pire admis
            if rang_etu_actuel < pire_rang_aff :
                # Remplace le pire admis par l'étudiant actuel
                spe_affectations[spe_id].remove(pire_etu_aff)
                spe_affectations[spe_id].append(etu_id)
                # le pire redevient libre
                etu_libres.append(pire_etu_aff)
            # Sinon le master rejette l'étudiant actuel, qui reste libre
            else :
                etu_libres.append(etu_id)
    
    return spe_affectations, nb_iterations

def gale_shapley_spe(prefEtu, prefSpe, capacites):
    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)

    # Pile des masters libres
    spe_libres = list(range(nb_spe))

    # Tableau contenant l'indice du prochain étudiant à proposer pour chaque master dans sa liste de préférence
    spe_propositions = [0] * nb_spe

    # Matrice des rangs des masters pour chaque étudiant
    rang_spe = [[0]*nb_spe for _ in range(nb_etu)]
    for etu_id in range(nb_etu):
        for rang, spe_id in enumerate(prefEtu[etu_id]):
            rang_spe[etu_id][spe_id] = rang
    
    # Tableau d'id des masters pris par chaque étudiant (-1 si libre)
    etu_affectations = [-1] * nb_etu
    # Tableau des listes des étudiants affectés pour chaque master
    spe_affectations = [[] for i in range(nb_spe)]

    # Tant qu'il existe un master libre
    while (spe_libres) :
        # On prend un master libre au sommet de la pile
        spe_id = spe_libres.pop()

        # S'il a déjà proposé à tous les étudiants, il ne peut plus proposer
        if spe_propositions[spe_id] >= nb_etu:
            continue

        # Le master propose à son prochain meilleur choix disponible
        etu_id = prefSpe[spe_id][spe_propositions[spe_id]]
        spe_propositions[spe_id] += 1

        # identifiant de spé pris par l'étudiant (-1 si l'étudiant est libre)
        spe_pris = etu_affectations[etu_id]

        # Si l'étudiant n'a pas encore de master
        if spe_pris == -1 :
            # étudiant accepte la proposition de ce master
            etu_affectations[etu_id] = spe_id
            spe_affectations[spe_id].append(etu_id)
        # Si l'étudiant est déjà pris par un autre master, il compare les rangs
        # si l'étudiant préfère ce master que master qu'il a pris
        elif rang_spe[etu_id][spe_pris] > rang_spe[etu_id][spe_id]:
            # il abandonne l'offre de l'ancien master
            spe_affectations[spe_pris].remove(etu_id)

            # l'ancien master redevient libre s'il était pas dans la pile
            if spe_pris not in spe_libres:
                spe_libres.append(spe_pris)

            # l'étudiant rejoint ce nouveau master
            etu_affectations[etu_id] = spe_id
            spe_affectations[spe_id].append(etu_id)

        # Si ce master a encore de la place, on le remet dans la pile
        if (capacites[spe_id]) > len(spe_affectations[spe_id]):
            spe_libres.append(spe_id)

    return spe_affectations

def trouver_paires_instables(prefEtu, prefSpe, capacites, affectations):
    paires_instables = []

    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)

    # Affections de chaque étudiants
    etu_affectations = [-1] * nb_etu
    for spe_id in range(nb_spe):
        for etu_id in affectations[spe_id]:
            etu_affectations[etu_id] = spe_id
    
    # On vérifie pour chaque étudiant
    for etu_id in range(nb_etu):
        # l'id de master pris par cet étudiant (-1 s'il n'a pas de master)
        master_pris = etu_affectations[etu_id]

        # Si l'étudiant a un master
        if master_pris != -1 :
            # le rang de master dans la liste de préférence de cet étudiant
            rang_master_pris = prefEtu[etu_id].index(master_pris)
            # la liste des masters que l'étudaint préfère à son master actuel
            # (tous les masters qui ont un meilleur classement que master actuel)
            masters_preferes = prefEtu[etu_id][:rang_master_pris]
        # Si l'étudiant n'a pas de master
        else :
            # il prefère n'importe quel master de sa liste de préférence
            masters_preferes = prefEtu[etu_id]

        # On regarde tous ses masters préférés
        for spe_id in masters_preferes:
            # si le master a encore de la place
            if len(affectations[spe_id]) < capacites[spe_id] :
                paires_instables.append((etu_id, spe_id))
                continue

            # si le master est plein
            else : 
                # id de l'étudiant le moins préféré affecté par ce master
                pire_admis = affectations[spe_id][0]
                # Le rang d'étudiant le moins préféré affecté par ce master
                rang_pire_admis = prefSpe[spe_id].index(pire_admis)
                # On parcourt les autres étudiants affecté pour trouver celui qui est moins préféré
                for etu in affectations[spe_id]:
                    rang = prefSpe[spe_id].index(etu)
                    if rang > rang_pire_admis :
                        rang_pire_admis = rang
                        pire_admis = etu
                
                # rang de cet étudiant dans la liste de préférence de ce master
                rang_etu = prefSpe[spe_id].index(etu_id
                                                 )
                # si le master prédère cet étudiant à son pire admis
                if rang_etu < rang_pire_admis :
                    paires_instables.append((etu_id, spe_id))

    return paires_instables