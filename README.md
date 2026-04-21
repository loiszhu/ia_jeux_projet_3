# ia_jeux_projet_3

### Question 2 - Choix des structures de données et complexité pour "côté étudiant"

1. Trouver un étudiant libre
- Structure : une pile "etu_libres" qui contient les identifiants des étudiants libres (non affetcés). On récupère le prochain étudiant libre avec .pop(), et on insère un étudiant libre avec .append()
- Complexité :  l'insertion et la suppression en O(1)

2. Trouver le prochain parcours à qui proposer
- Structure : un tableau d'entiers "etu_propositions" de taille n (n étudiants) qui stocke pour chaque étudiant l'indice du prochain parcours à proposer dans sa liste de préférences prefEtu[etu_id]
- Complexité : l'accès et la mise à jour en O(1)

3. Trouver la position de l’étudiant i dans le classement du parcours j
- Structure : une matrice "rang_etu[master_j][etu_i]" où l'on stocke le rang de l'étudiant i à l'indice i pour chaque parcours. Elle sera pré-calculée une seule fois au début de l'algorithme
- Complexité : précalcul en O(n*m), l'accès en O(1)

4. Trouver l’étudiant le moins préféré par le parcours j parmi ceux qui lui sont aﬀectés
- Structure : un tableau de listes "spe_affectations" qui stocke les étudiants admis par chaque parcours
- Complexité : On parcourt les étudiants admis dans le parcours j (taille = CAPj capacité de parcours j), puis on compare leurs rangs via la matrice "rang_etu", la complécité est en O(CAPj) (ou en temps constant dans ce projet car la capacité de chaque master est très petite)

5. Remplacer un étudiant par un autre dans l’aﬀectation courante d’un parcours j
- Structure : un tableau de listes "spe_affectations" comme précédent
- Complexité : la suppression de l'étudiant le moins bien classé en O(CAPj) (ou en temps constant comme c'est négligeable) et l'ajout d'un nouveau en O(1)

### Question 3 - Algorithme "côté étudiant"

Gale-Shapley "côté étudiant" : c'est les étudiants qui font les propositions aux masters

#### Algorithme :

1. Initialisation : au début, chaque étudiant et chaque master est considéré comme libre
2. Sélection : tant qu'il existe un étudiant libre qui n'a pas encore proposé à tous les masters de sa liste
    - on choisit un tel étudiant i
    - cet étudiant i propose au premier master j de sa liste auquel il n'a pas encore fait de proposition
3. S'il y a encore de la place dans le master j : étudiant i est accepté temporairement dans ce master
4. Si le master j est déjà plein : ce master j regarde dans son affectation courante et trouve l'étudiant i' le moins préféré
    - si le master j préfère l'étudiant i : il accepte i, et i' devient libre
    - sinon : ce master j rejette la proposition de l'étudiant i
5. Terminaison : l'algorithme s'arrête quand il n'y a plus d'étudiant libre

#### Complexité de l'algorithme "côté étudiant" : 
- le pré-calcul de la matrice prend O(n*m)
- la boucle principale effectue au plus n*m propositions
- Chaque opération interne est en O(1) ou O(Capacité)

#### La complexité totale est de O(n*m) donc O(n^2)

### Question 4 - Algorithme "côté parcours"

Gale-Shapley "côté parcours" : C'est les masters qui font les propositions, et les étudiants ont le droit de les refuser

#### Choix de structures de données et complexité: 
1. Trouver un master libre à chaque itération
- Structure : une pile "spe_libres" qui contient des identifiants des masters qui ont encore de la place. 
- Complexité : l'ajout et la suppression en O(1)

2. Trouver le prochain étudiant à qui faire une proposition
- Structure : un tableau d'entiers "spe_propositions" de taille m (m masters) qui stocke pour chaque master l'indice du prochain étudiant à proposer dans sa liste de préférences prefSpe[spe_id]
- Complexité : la recherche et la mise à jour en O(1)

3. Trouver la position du master j dans le classement de l'étudiant i
- Structure : une matrice "rang_spe[etu_i][master_j]" où l'on stocke le rang de master j à l'indice j pour chaque étudiant. Elle sera pré-calculée une seule fois au début de l'algorithme
- Complexité : précalcul en O(nb_etu + nb_spe), l'accès en O(1)

4. Remplacer un master par un autre master j' dans l'affectation courante de l'étudiant
- Structure : un tableau d'entiers "affectations" qui stock l'identifiant du master pris par chaque étudiant, -1 si l'étudiant est libre
- Complexité : l'accès et la mise à jour en O(1)

#### Algorithme :
1. Initialisation : au début, chaque master et chaque étudiant est considéré comme libre
2. Sélection : tant qu"il existe un master libre (la capacité n'est pas atteinte) qui n'a pas encore proposé à tous les étudiants
    - on choisit un tel master j
    - ce master j propose au premier étudiant i de sa liste auquel il n'a pas encore fait de proposition
3. Si l'étudiant i n'a pas encore de master : étudiant i accepte la proposition de ce master
4. Si l'étudiant i est déjà pris par un autre master j' : 
    - si l'étudiant i préfère le master j que j' : il abandonne l'offre de master j' et rejoint le master j
    - sinon : la proposition de master j est rejetté
5. Terminaison : l'algorithme s'arrête quand il n'y a plus de master libre

#### La complexité de l'algorithme "côté parcours" est pareil que celui de côté étudiant : O(n^2)


### Question 5 - Résultats obtenus :

Affectations "côté étudiant" : [[12, 5], [4], [9], [8], [10, 11], [0], [1], [7], [6], [3, 2]]   
Affectations "côté parcours" : [[5, 12], [4], [9], [8], [10, 11], [0], [1], [7], [6], [3, 2]]

### Question 6 - Stabilité de l'affectation
Une paire (étudiant_i, master_j) est instable si :
- étudiant_i préfère master_j à son affectation courante
et
- master_j a soit une place libre, soit un étudiant affecté qu'il aime moins que étudiant_i

#### Les étapes pour trouver des paires instables : 
1. Reconstruire l'affectation des étudiants (une liste d'identifiants des masters)
2. Pour chaque étudiant, on liste les masters que l'étudiant prèfère à son master actuel
3. On regarde si ces masters préférés veulent cet étudiant
    - si le master a encore de la place => paire instable
    - si le master est plein, et s'il préfère cet étudiant à son pire admis => paire instable

Note sur la complexité : Pour des raisons de lisibilité, on a utilisé .index() pour retrouver les rangs dans la fonction trouver_paires_instables. Pour une implémentation optimale sur des données tres nombreux, il suffirait d'utiliser les matrices de rangs précalculées (comme dans nos 2 algorithmes précédents) pour effectuer ces comparaisons en O(1).   

D'après le test, on observe que les deux algorithmes (étudiant et parcours) retournent la même affectation, et il n'existe pas de paires instables, donc notre résultat est stable.   