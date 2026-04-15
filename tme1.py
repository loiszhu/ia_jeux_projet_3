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