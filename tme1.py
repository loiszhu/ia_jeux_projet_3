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


# Question 3

def gale_shapley_etu(prefEtu, prefSpe, capacites):
    nb_etu = len(prefEtu)
    nb_spe = len(prefSpe)
    
    # Pile des étudiants libres
    etu_libres = list(range(nb_etu))

    # Tableau contenant l'indice du prochain master à proposer pour chaque étudiant
    etu_propositions = [0] * nb_etu

    # Matrice des rangs des étudiants pour chaque master
    rang_etu = [[0]*nb_etu for i in range(nb_spe)]
    for spe_id in range(nb_spe):
        for rang, etu_id in enumerate(prefSpe[spe_id]):
            rang_etu[spe_id][etu_id] = rang

    # Tableau des listes des étudiants affectés pour chaque master
    spe_aff = [[] for i in range(nb_spe)]

    # Tant qu'il existe un étudiant libre
    while (etu_libres) :
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
        if len(spe_aff[spe_id]) < capacites[spe_id] :
            spe_aff[spe_id].append(etu_id)
        # Sinon on compare si le master préfère l'étudiant actuel, ou l'étudiant déjà affecté
        else :
            # Trouve l'étudiant le moins préféré affecté par ce master
            pire_etu_aff = spe_aff[spe_id][0]
            # Le rang d'étudiant le moins préféré affecté par ce master
            pire_rang_aff = rang_etu[spe_id][pire_etu_aff]
            # On parcourt les autres étudiants affecté pour trouver celui qui est moins préféré
            for etu in spe_aff[spe_id]:
                rang = rang_etu[spe_id][etu]
                if rang > pire_rang_aff :
                    pire_rang_aff = rang
                    pire_etu_aff = etu
            
            # Le rang d'étudiant actuel
            rang_etu_actuel = rang_etu[spe_id][etu_id]

            # Si le rang de l'étudiant actuel est meilleur que le pire admis
            if rang_etu_actuel < pire_rang_aff :
                # Remplace le pire admis par l'étudiant actuel
                spe_aff[spe_id].remove(pire_etu_aff)
                spe_aff[spe_id].append(etu_id)
                # le pire redevient libre
                etu_libres.append(pire_etu_aff)
            # Sinon le master rejette l'étudiant actuel, qui reste libre
            else :
                etu_libres.append(etu_id)
    
    return spe_aff
