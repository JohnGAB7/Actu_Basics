1. Opérateurs
================

Les opérateurs sont des symboles utilisés pour effectuer des opérations sur des variables et des valeurs. En Python, il existe plusieurs types d'opérateurs, chacun ayant un rôle spécifique.

Opérateurs arithmétiques
------------------------

Les opérateurs arithmétiques sont utilisés pour effectuer des opérations mathématiques de base.

- **Addition (+)** : Additionne deux valeurs.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a + b  # result est 8

- **Soustraction (-)** : Soustrait une valeur d'une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a - b  # result est 2

- **Multiplication (*)** : Multiplie deux valeurs.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a * b  # result est 15

- **Division (/)** : Divise une valeur par une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a / b  # result est 1.666...

- **Division entière (//)** : Divise une valeur par une autre et renvoie la partie entière.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a // b  # result est 1

- **Modulo (%)** : Renvoie le reste d'une division.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a % b  # result est 2

- **Exponentiation (**)** : Élève une valeur à la puissance d'une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = a ** b  # result est 125

Opérateurs de comparaison
-------------------------

Les opérateurs de comparaison sont utilisés pour comparer deux valeurs et renvoient un booléen (``True`` ou False).

- **Égal (==)** : Compare si deux valeurs sont égales.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a == b)  # result est False

- **Différent (!=)** : Compare si deux valeurs sont différentes.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a != b)  # result est ``True``

- **Inférieur (<)** : Compare si une valeur est inférieure à une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a < b)  # result est False

- **Supérieur (>)** : Compare si une valeur est supérieure à une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a > b)  # result est ``True``

- **Inférieur ou égal (<=)** : Compare si une valeur est inférieure ou égale à une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a <= b)  # result est False

- **Supérieur ou égal (>=)** : Compare si une valeur est supérieure ou égale à une autre.
  
  .. code-block:: python
  
      a = 5
      b = 3
      result = (a >= b)  # result est ``True``

Opérateurs logiques
-------------------

Les opérateurs logiques sont utilisés pour effectuer des opérations logiques sur des valeurs booléennes (``True`` ou False).

- **Et (and)** : Renvoie ``True`` si les deux opérandes sont vrais.
  
  .. code-block:: python
  
      a = True
      b = False
      result = a and b  # result est False

- **Ou (or)** : Renvoie ``True`` si au moins un des opérandes est vrai.
  
  .. code-block:: python
  
      a = True
      b = False
      result = a or b  # result est ``True``

- **Non (not)** : Inverse la valeur de l'opérande.
  
  .. code-block:: python
  
      a = True
      result = not a  # result est False

Opérateurs d'affectation
------------------------

Les opérateurs d'affectation sont utilisés pour affecter des valeurs à des variables.

- **Affectation (=)** : Affecte une valeur à une variable.
  
  .. code-block:: python
  
      a = 5

- **Affectation avec addition (+=)** : Ajoute une valeur à une variable et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a += 3  # a est maintenant 8

- **Affectation avec soustraction (-=)** : Soustrait une valeur d'une variable et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a -= 3  # a est maintenant 2

- **Affectation avec multiplication (*=)** : Multiplie une variable par une valeur et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a *= 3  # a est maintenant 15

- **Affectation avec division (/=)** : Divise une variable par une valeur et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a /= 3  # a est maintenant 1.666...

- **Affectation avec division entière (//=)** : Divise une variable par une valeur, arrondit le résultat à l'entier le plus proche et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a //= 3  # a est maintenant 1

- **Affectation avec modulo (%=)** : Calcule le reste de la division d'une variable par une valeur et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a %= 3  # a est maintenant 2

- **Affectation avec exponentiation (**=)** : Élève une variable à la puissance d'une valeur et affecte le résultat à cette variable.
  
  .. code-block:: python
  
      a = 5
      a **= 3  # a est maintenant 125

Opérateurs d'appartenance
--------------------------

Ces opérateurs vérifient si un élément appartient (ou non) à une séquence (comme une liste, une chaîne ou un tuple).

- **Dans (in)** : Retourne ``True`` si l'élément est présent dans la séquence.

  .. code-block:: python

     'a' in 'actuaire'  # Résultat : True 

- **Pas dans (not in)** : Retourne ``True`` si l'élément n'est pas présent dans la séquence.

  .. code-block:: python

     'z' not in 'actuaire'  # Résultat : True

Opérateurs d'identité
---------------------

Ces opérateurs comparent les emplacements mémoire de deux objets.

- **Est (is)** : Retourne ``True`` si les deux objets sont identiques (même emplacement mémoire).

  .. code-block:: python

     a = [1, 2, 3]
     b = a
     a is b  # Résultat : True

- **N'est pas (is not)** : Retourne ``True`` si les deux objets ne sont pas identiques.

  .. code-block:: python

     a = [1, 2, 3]
     b = [1, 2, 3]
     a is not b  # Résultat : True

Opérateurs binaires
-------------------


Les opérateurs bit à bit sont utilisés pour effectuer des opérations sur les bits individuels des valeurs.

- **Et bit à bit (&)** : Effectue une opération ET sur chaque bit des opérandes.
  
  .. code-block:: python
  
      a = 5  # En binaire : 0101
      b = 3  # En binaire : 0011
      result = a & b  # En binaire : 0001, result est 1

- **Ou bit à bit (|)** : Effectue une opération OU sur chaque bit des opérandes.
  
  .. code-block:: python
  
      a = 5  # En binaire : 0101
      b = 3  # En binaire : 0011
      result = a | b  # En binaire : 0111, result est 7


- **OU exclusif (^)** : Retourne 1 si les bits sont différents.

  .. code-block:: python

     resultat = 5 ^ 3  # Résultat : 6 (101 ^ 011 = 110)

- **Décalage à gauche (<<)** : Décale les bits vers la gauche en ajoutant des zéros à droite.

  .. code-block:: python

     resultat = 5 << 1  # Résultat : 10 (101 devient 1010)

- **Décalage à droite (>>)** : Décale les bits vers la droite en supprimant les bits les plus à droite.

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
