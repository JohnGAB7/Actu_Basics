2. Structures de contrôle
=============================

Les structures de contrôle permettent de diriger le flux d'exécution du programme en fonction de conditions ou de boucles. En Python, les principales structures de contrôle incluent les conditions (if, elif, else) et les boucles (for, while). Ces structures permettent de créer des programmes plus dynamiques et réactifs.

Conditions (if, elif, else)
---------------------------

Les instructions conditionnelles permettent d'exécuter des blocs de code spécifiques en fonction de conditions. Python utilise les mots-clés `if`, `elif` et `else` pour créer des structures conditionnelles.

**Syntaxe générale :**

.. code-block:: python

    if condition:
        # Bloc de code exécuté si la condition est vraie
    elif autre_condition:
        # Bloc de code exécuté si la première condition est fausse et l'autre_condition est vraie
    else:
        # Bloc de code exécuté si toutes les conditions précédentes sont fausses

**Exemple d'utilisation :**

.. code-block:: python

    x = 10

    if x > 0:
        print("x est positif")
    elif x == 0:
        print("x est zéro")
    else:
        print("x est négatif")

Dans cet exemple, le programme vérifie si `x` est supérieur à 0, égal à 0, ou inférieur à 0, et imprime le message correspondant.

### Conditions imbriquées

Les conditions peuvent être imbriquées les unes dans les autres pour créer des structures plus complexes.

**Exemple d'utilisation :**

.. code-block:: python

    x = 10
    y = 5

    if x > 0:
        if y > 0:
            print("x et y sont positifs")
        else:
            print("x est positif mais pas y")
    else:
        print("x n'est pas positif")

Boucles (for, while)
--------------------

Les boucles permettent de répéter l'exécution d'un bloc de code plusieurs fois. Python supporte deux types principaux de boucles : les boucles `for` et `while`.

### Boucles for

La boucle `for` itère sur une séquence (comme une liste, un tuple ou une chaîne de caractères) et exécute un bloc de code pour chaque élément de la séquence.

**Syntaxe générale :**

.. code-block:: python

    for élément in séquence:
        # Bloc de code à exécuter pour chaque élément

**Exemple d'utilisation :**

.. code-block:: python

    fruits = ["pomme", "banane", "cerise"]

    for fruit in fruits:
        print(fruit)

Dans cet exemple, la boucle `for` itère sur la liste `fruits` et imprime chaque fruit.

### Boucles while

La boucle `while` continue d'exécuter un bloc de code tant qu'une condition spécifiée est vraie.

**Syntaxe générale :**

.. code-block:: python

    while condition:
        # Bloc de code à exécuter tant que la condition est vraie

**Exemple d'utilisation :**

.. code-block:: python

    compteur = 0

    while compteur < 5:
        print(compteur)
        compteur += 1

Dans cet exemple, la boucle `while` continue d'exécuter le bloc de code tant que `compteur` est inférieur à 5.

**Boucles imbriquées**

Les boucles peuvent être imbriquées pour créer des structures plus complexes.

**Exemple d'utilisation :**

.. code-block:: python

    for i in range(3):
        for j in range(2):
            print(f"i = {i}, j = {j}")

Instructions de contrôle de boucle (break, continue, pass)
-----------------------------------------------------------

Python offre également des instructions pour contrôler le flux à l'intérieur des boucles : `break`, `continue`, et `pass`.

- **break** : Interrompt la boucle immédiatement.

  .. code-block:: python

      for i in range(10):
          if i == 5:
              break
          print(i)

- **continue** : Saute l'itération actuelle et passe à la suivante.

  .. code-block:: python

      for i in range(10):
          if i % 2 == 0:
              continue
          print(i)

- **pass** : N'effectue aucune action, généralement utilisé comme un espace réservé.

  .. code-block:: python

      for i in range(5):
          pass  # Espace réservé pour un futur code

En utilisant ces structures de contrôle, vous pouvez créer des programmes Python plus flexibles et sophistiqués. Elles sont fondamentales pour toute programmation, permettant des décisions conditionnelles et des itérations.

