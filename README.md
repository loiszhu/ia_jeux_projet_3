# ia_jeux_projet_3

# Question 2

1. Trouver un étudiant libre
- Structure : une liste "libres" qui contient les identifiants des étudiants libres (non affetcés)
- Complexité : on récupère le prochain étudiant libre avec pop() en O(1), l'insertion d'un étudiant libre en O(1) aussi

2. Trouver le prochain parcours à qui proposer
- Structure : une liste "propositions" de taille n (n étudiants) qui stocke pour chaque étudiant l'indice du prochain parcours à proposer dans sa liste de préférences
- Complexité : l'accès et la mise à jour en O(1)

3. Trouver la position de l’étudiant i dans le classement du parcours j
- Structure : une matrice des rangs inversée "rang[j][i]" où l'on stocke le rang de l'étudiant i à l'indice i pour chaque parcours
- Complexité : l'accès en O(1)

4. Trouver l’étudiant le moins préféré par le parcours j parmi ceux qui lui sont aﬀectés
- Structure : un tableau de listes "admis" qui stocke les étudiants admis par chaque parcours
- Complexité : On parcourt les étudiants admis dans le parcours j (taille = CAPj capacité de parcours j), puis on compare leurs rangs via la matrice "rang", la complécité est en O(CAPj)

5. Remplacer un étudiant par un autre dans l’aﬀectation courante d’un parcours j
- Structure : un tableau de listes "admis" comme précédent
- Complexité : on retire l'étudiant le moins bien classé et on ajoute le nouveau en O(1)