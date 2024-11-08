Compréhensions
==============

Les compréhensions en Python sont des expressions concises qui permettent de créer des listes, des dictionnaires, des ensembles et d'autres séquences en utilisant une syntaxe simple et élégante. Elles sont souvent utilisées pour rendre le code plus lisible et plus efficace.

Compréhensions de listes
------------------------

Les compréhensions de listes offrent un moyen compact de générer des listes à partir de séquences existantes. Elles sont généralement plus lisibles et plus rapides que les boucles `for` traditionnelles.

**Syntaxe générale :**

.. code-block:: python

    [expression for élément in séquence]

**Exemple d'utilisation :**

.. code-block:: python

    # Liste des carrés des nombres de 0 à 9
    carrés = [x**2 for x in range(10)]
    print(carrés)  # Sortie : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### Compréhensions de listes avec conditions

Vous pouvez ajouter des conditions pour inclure uniquement les éléments qui satisfont un certain critère.

**Syntaxe générale :**

.. code-block:: python

    [expression for élément in séquence if condition]

**Exemple d'utilisation :**

.. code-block:: python

    # Liste des carrés des nombres pairs de 0 à 9
    carrés_pairs = [x**2 for x in range(10) if x % 2 == 0]
    print(carrés_pairs)  # Sortie : [0, 4, 16, 36, 64]

Compréhensions de dictionnaires
-------------------------------

Les compréhensions de dictionnaires permettent de créer des dictionnaires de manière concise et lisible.

**Syntaxe générale :**

.. code-block:: python

    {clé: valeur for élément in séquence}

**Exemple d'utilisation :**

.. code-block:: python

    # Dictionnaire des carrés des nombres de 0 à 9
    carrés_dict = {x: x**2 for x in range(10)}
    print(carrés_dict)  # Sortie : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

### Compréhensions de dictionnaires avec conditions

Comme pour les listes, vous pouvez ajouter des conditions pour inclure uniquement les paires clé-valeur qui satisfont un certain critère.

**Syntaxe générale :**

.. code-block:: python

    {clé: valeur for élément in séquence if condition}

**Exemple d'utilisation :**

.. code-block:: python

    # Dictionnaire des carrés des nombres pairs de 0 à 9
    carrés_pairs_dict = {x: x**2 for x in range(10) if x % 2 == 0}
    print(carrés_pairs_dict)  # Sortie : {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

Compréhensions de sets
----------------------

Les compréhensions de sets permettent de créer des ensembles de manière concise et lisible.

**Syntaxe générale :**

.. code-block:: python

    {expression for élément in séquence}

**Exemple d'utilisation :**

.. code-block:: python

    # Ensemble des carrés des nombres de 0 à 9
    carrés_set = {x**2 for x in range(10)}
    print(carrés_set)  # Sortie : {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

### Compréhensions de sets avec conditions

Vous pouvez ajouter des conditions pour inclure uniquement les éléments qui satisfont un certain critère.

**Syntaxe générale :**

.. code-block:: python

    {expression for élément in séquence if condition}

**Exemple d'utilisation :**

.. code-block:: python

    # Ensemble des carrés des nombres pairs de 0 à 9
    carrés_pairs_set = {x**2 for x in range(10) if x % 2 == 0}
    print(carrés_pairs_set)  # Sortie : {0, 4, 16, 36, 64}

Compréhensions avec des conditions
----------------------------------

Les compréhensions en Python peuvent inclure des conditions pour filtrer les éléments qui doivent être inclus dans le résultat final. Ces conditions peuvent être ajoutées à toutes les formes de compréhensions : listes, dictionnaires et sets.

**Exemple de compréhension avec condition :**

.. code-block:: python

    # Liste des carrés des nombres impairs de 0 à 9
    carrés_impairs = [x**2 for x in range(10) if x % 2 != 0]
    print(carrés_impairs)  # Sortie : [1, 9, 25, 49, 81]

**Exemple de compréhension de dictionnaire avec condition :**

.. code-block:: python

    # Dictionnaire des cubes des nombres de 0 à 9 où le nombre est un multiple de 3
    cubes_dict = {x: x**3 for x in range(10) if x % 3 == 0}
    print(cubes_dict)  # Sortie : {0: 0, 3: 27, 6: 216, 9: 729}

**Exemple de compréhension de set avec condition :**

.. code-block:: python

    # Ensemble des carrés des nombres multiples de 4 de 0 à 15
    carrés_multiples_de_4 = {x**2 for x in range(16) if x % 4 == 0}
    print(carrés_multiples_de_4)  # Sortie : {0, 16, 64, 144, 256}

Les compréhensions en Python sont des outils puissants qui permettent de créer des structures de données de manière concise et efficace. Elles peuvent rendre votre code plus lisible et plus facile à écrire, tout en étant potentiellement plus performantes que les boucles traditionnelles.

