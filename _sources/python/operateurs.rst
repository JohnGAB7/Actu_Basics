Opérateurs en Python
#####################

Python propose une large variété d'opérateurs pour manipuler des données et contrôler le flux d'exécution. Voici un aperçu des principaux types d'opérateurs et de leur utilisation.

Opérateurs arithmétiques
-------------------------

Les opérateurs arithmétiques permettent d'effectuer des opérations de calcul sur des valeurs numériques.

- **Addition (``+``)** : Additionne deux valeurs.

  .. code-block:: python

     resultat = 3 + 2  # Résultat : 5

- **Soustraction (``-``)** : Soustrait une valeur de l'autre.

  .. code-block:: python

     resultat = 5 - 2  # Résultat : 3

- **Multiplication (``*``)** : Multiplie deux valeurs.

  .. code-block:: python

     resultat = 3 * 2  # Résultat : 6

- **Division (``/``)** : Divise une valeur par l'autre. Retourne un flottant.

  .. code-block:: python

     resultat = 5 / 2  # Résultat : 2.5

- **Division entière (``//``)** : Division qui renvoie uniquement la partie entière.

  .. code-block:: python

     resultat = 5 // 2  # Résultat : 2

- **Modulo (``%``)** : Retourne le reste de la division.

  .. code-block:: python

     resultat = 5 % 2  # Résultat : 1

- **Exponentiation (``**``)** : Élève un nombre à la puissance d'un autre.

  .. code-block:: python

     resultat = 3 ** 2  # Résultat : 9

Opérateurs de comparaison
-------------------------

Ces opérateurs comparent deux valeurs et renvoient un booléen (``True`` ou ``False``).

- **Égal à (``==``)** : Vérifie si les deux valeurs sont égales.

  .. code-block:: python

     3 == 3  # Résultat : True

- **Différent de (``!=``)** : Vérifie si les deux valeurs sont différentes.

  .. code-block:: python

     3 != 2  # Résultat : True

- **Supérieur à (``>``)** : Vérifie si la première valeur est supérieure à la seconde.

  .. code-block:: python

     5 > 3  # Résultat : True

- **Inférieur à (``<``)** : Vérifie si la première valeur est inférieure à la seconde.

  .. code-block:: python

     3 < 5  # Résultat : True

- **Supérieur ou égal à (``>=``)** : Vérifie si la première valeur est supérieure ou égale à la seconde.

  .. code-block:: python

     5 >= 5  # Résultat : True

- **Inférieur ou égal à (``<=``)** : Vérifie si la première valeur est inférieure ou égale à la seconde.

  .. code-block:: python

     3 <= 4  # Résultat : True

Opérateurs logiques
-------------------

Les opérateurs logiques sont utilisés pour combiner plusieurs expressions de comparaison.

- **Et (``and``)** : Retourne ``True`` si les deux conditions sont vraies.

  .. code-block:: python

     (3 > 2) and (5 > 3)  # Résultat : True

- **Ou (``or``)** : Retourne ``True`` si au moins une des conditions est vraie.

  .. code-block:: python

     (3 > 2) or (5 < 3)  # Résultat : True

- **Non (``not``)** : Inverse la valeur d'une condition.

  .. code-block:: python

     not (3 > 2)  # Résultat : False

Opérateurs d'affectation
-------------------------

Les opérateurs d'affectation permettent d'assigner des valeurs aux variables, souvent en combinant une opération.

- **Affectation simple (``=``)** : Assigne une valeur à une variable.

  .. code-block:: python

     x = 5

- **Addition et affectation (``+=``)** : Ajoute et affecte.

  .. code-block:: python

     x += 3  # Équivaut à x = x + 3

- **Soustraction et affectation (``-=``)** : Soustrait et affecte.

  .. code-block:: python

     x -= 2  # Équivaut à x = x - 2

- **Multiplication et affectation (``*=``)** : Multiplie et affecte.

  .. code-block:: python

     x *= 4  # Équivaut à x = x * 4

- **Division et affectation (``/=``)** : Divise et affecte.

  .. code-block:: python

     x /= 2  # Équivaut à x = x / 2

- **Division entière et affectation (``//=``, ``%=``, ``**=``)** : Fonctionnent de la même manière que les précédents avec l’opérateur correspondant.

Opérateurs d'appartenance
--------------------------

Ces opérateurs vérifient si un élément appartient (ou non) à une séquence (comme une liste, une chaîne ou un tuple).

- **Dans (``in``)** : Retourne ``True`` si l'élément est présent dans la séquence.

  .. code-block:: python

     'a' in 'actuaire'  # Résultat : True

- **Pas dans (``not in``)** : Retourne ``True`` si l'élément n'est pas présent dans la séquence.

  .. code-block:: python

     'z' not in 'actuaire'  # Résultat : True

Opérateurs d'identité
---------------------

Ces opérateurs comparent les emplacements mémoire de deux objets.

- **Est (``is``)** : Retourne ``True`` si les deux objets sont identiques (même emplacement mémoire).

  .. code-block:: python

     a = [1, 2, 3]
     b = a
     a is b  # Résultat : True

- **N'est pas (``is not``)** : Retourne ``True`` si les deux objets ne sont pas identiques.

  .. code-block:: python

     a = [1, 2, 3]
     b = [1, 2, 3]
     a is not b  # Résultat : True

Opérateurs binaires
-------------------

Les opérateurs binaires effectuent des opérations au niveau des bits. Ils sont utilisés principalement pour manipuler les bits dans des applications plus avancées.

- **ET binaire (``&``)** : Compare les bits et retourne 1 si les deux bits sont 1.

  .. code-block:: python

     resultat = 5 & 3  # Résultat : 1 (101 & 011 = 001)

- **OU binaire (``|``)** : Compare les bits et retourne 1 si au moins un des bits est 1.

  .. code-block:: python

     resultat = 5 | 3  # Résultat : 7 (101 | 011 = 111)

- **OU exclusif (``^``)** : Retourne 1 si les bits sont différents.

  .. code-block:: python

     resultat = 5 ^ 3  # Résultat : 6 (101 ^ 011 = 110)

- **Décalage à gauche (``<<``)** : Décale les bits vers la gauche en ajoutant des zéros à droite.

  .. code-block:: python

     resultat = 5 << 1  # Résultat : 10 (101 devient 1010)

- **Décalage à droite (``>>``)** : Décale les bits vers la droite en supprimant les bits les plus à droite.

  .. code-block:: python

     resultat = 5 >> 1  # Résultat : 2 (101 devient 10)

Autres opérateurs
----------------------

Les chaînes de caractères peuvent être concaténées, répétées et utilisées avec diverses méthodes de manipulation de texte :
.. code-block:: python

    s1 = "Bonjour"
    s2 = "le monde"

    # Concaténation
    s3 = s1 + " " + s2  # "Bonjour le monde"

    # Répétition
    s4 = s1 * 3  # "BonjourBonjourBonjour"

    # Méthodes de chaîne de caractères
    s5 = s1.upper()  # "BONJOUR"
    s6 = s1.lower()  # "bonjour"


Cette section fournit une vue d'ensemble de tous les opérateurs Python, facilitant la compréhension de leur utilisation dans diverses expressions et leur priorité d'évaluation.
