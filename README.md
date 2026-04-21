# ia_jeux_projet_3

### Question 2

1. Trouver un étudiant libre
- Structure : une pile "etu_libres" qui contient les identifiants des étudiants libres (non affetcés)
- Complexité : on récupère le prochain étudiant libre avec pop() en O(1), l'insertion d'un étudiant libre en O(1) aussi

2. Trouver le prochain parcours à qui proposer
- Structure : un tableau d'entiers "etu_propositions" de taille n (n étudiants) qui stocke pour chaque étudiant l'indice du prochain parcours à proposer dans sa liste de préférences
- Complexité : l'accès et la mise à jour en O(1)

3. Trouver la position de l’étudiant i dans le classement du parcours j
- Structure : une matrice inversée "rang_etu[j][i]" où l'on stocke le rang de l'étudiant i à l'indice i pour chaque parcours, elle sera pré-calculée une seule fois au début de l'algorithme
- Complexité : l'accès en O(1)

4. Trouver l’étudiant le moins préféré par le parcours j parmi ceux qui lui sont aﬀectés
- Structure : un tableau de listes "spe_aff" qui stocke les étudiants admis par chaque parcours
- Complexité : On parcourt les étudiants admis dans le parcours j (taille = CAPj capacité de parcours j), puis on compare leurs rangs via la matrice "rang_etu", la complécité est en O(CAPj)

5. Remplacer un étudiant par un autre dans l’aﬀectation courante d’un parcours j
- Structure : un tableau de listes "spe_aff" comme précédent
- Complexité : on retire l'étudiant le moins bien classé et on ajoute le nouveau en O(1)

### Question 3

Gale-Shapley "côté étudiant" : c'est les étudiants qui font les propositions aux masters
1. Initialisation : au début, chaque étudiant et chaque master est considéré comme libre
2. Sélection : tant qu'il existe un étudiant libre qui n'a pas encore proposé à tous les masters de sa liste
    - on choisit un tel étudiant I
    - cet étudiant I propose au premier master J de sa liste auquel il n'a pas encore fait de proposition
3. S'il y a encore de la place dans le master J : étudiant I est accepté temporairement dans ce master
4. Si le master J est déjà plein : ce master J regarde dans son affectation courante et trouve l'étudiant I' le moins préféré
    - si le master J préfère l'étudiant I : il accepte I, et I' devient libre
    - sinon : ce master J rejette la proposition de l'étudiant I
5. Terminaision : l'algorithme s'arrête quand il n'y a plus d'étudiant libre.