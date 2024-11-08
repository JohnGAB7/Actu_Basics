6. Compréhensions
=====================

Les compréhensions en Python sont des expressions concises qui permettent de créer des listes, des dictionnaires, des ensembles et d'autres séquences en utilisant une syntaxe simple et élégante. Elles sont souvent utilisées pour rendre le code plus lisible et plus efficace.

Compréhension de Liste
------------------------

La compréhension de liste permet de générer des listes à partir d'itérables ou séquences tels que des listes, des chaînes de caractères, ou des ensembles, en appliquant une expression à chaque élément, avec une syntaxe beaucoup plus concise que les boucles traditionnelles.

**Syntaxe générale :**

La syntaxe de la compréhension de liste suit le modèle suivant :

.. code-block:: python

    [expression for element in iterable if condition]

- **expression** : L'opération ou transformation appliquée à chaque élément de l'itérable.
- **element** : La variable représentant chaque élément de l'itérable.
- **iterable** : La séquence d'éléments sur laquelle on itère (liste, chaîne, ensemble, etc.).
- **condition** (facultative) : Un filtre qui permet de sélectionner uniquement les éléments satisfaisant cette condition.

Exemples de base (Création d'une liste de carrés à partir d'une liste de nombres) :

   .. code-block:: python

       nombres = [1, 2, 3, 4, 5]
       carrés = [n * n for n in nombres]
       print(carrés)  # Résultat : [1, 4, 9, 16, 25]

   Ici, chaque nombre de la liste `nombres` est élevé au carré et ajouté à la nouvelle liste `carrés`.

Exemples de base (Création d'une liste de carrés à partir d'un ensemble de nombres) :
   
.. code-block:: python

    # Ensemble des carrés des nombres pairs de 0 à 9
    carrés_pairs_set = {x**2 for x in range(10) if x % 2 == 0}
    print(carrés_pairs_set)  # Sortie : {0, 4, 16, 36, 64}

**Compréhensions de listes avec conditions** 

Vous pouvez ajouter des conditions pour inclure uniquement les éléments qui satisfont un certain critère.

   .. code-block:: python

       nombres = [1, 2, 3, 4, 5]
       pairs = [n for n in nombres if n % 2 == 0]
       print(pairs)  # Résultat : [2, 4]

   Ici seuls les nombres pairs de la liste `nombres` sont ajoutés à la liste `pairs`.

.. code-block:: python

    # Ensemble des carrés des nombres multiples de 4 de 0 à 15
    carrés_multiples_de_4 = {x**2 for x in range(16) if x % 4 == 0}
    print(carrés_multiples_de_4)  # Sortie : {0, 16, 64, 144, 256}

**Compréhensions imbriquées**

Les compréhensions de liste imbriquées permettent de créer des listes multidimensionnelles ou de transformer des données en appliquant des transformations complexes.

Exemple : Création d'une matrice 3x3 :

.. code-block:: python

    matrice = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(matrice)  # Résultat : [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

Dans cet exemple, chaque sous-liste représente une ligne de la matrice et est générée en multipliant `i` et `j` pour chaque élément.

**Compréhensions avec plusieurs conditions**

Il est possible d'ajouter plusieurs conditions dans une compréhension de liste pour affiner davantage les résultats.

Exemple :

.. code-block:: python

    nombres = [1, 2, 3, 4, 5, 6]
    result = [n for n in nombres if n % 2 == 0 and n > 2]
    print(result)  # Résultat : [4, 6]

Seuls les nombres pairs supérieurs à 2 sont sélectionnés.

Compréhension de Dictionnaire
-----------------------------

La compréhension de dictionnaire permet de générer des dictionnaires en appliquant une expression à chaque élément d'un itérable. Elle utilise une syntaxe similaire à la compréhension de liste mais avec des paires clé-valeur.

**Syntaxe de base**

La syntaxe de la compréhension de dictionnaire est :

.. code-block:: python

    {key_expression: value_expression for element in iterable if condition}

- **key_expression** : L'expression utilisée pour définir la clé.
- **value_expression** : L'expression utilisée pour définir la valeur.
- **element** : La variable représentant chaque élément de l'itérable.
- **iterable** : La séquence d'éléments sur laquelle on itère.
- **condition** (facultative) : Un filtre pour inclure uniquement les éléments satisfaisant cette condition.

Exemples de base (Création d'un dictionnaire de carrés) :

   .. code-block:: python

       nombres = [1, 2, 3, 4]
       carrés = {n: n * n for n in nombres}
       print(carrés)  # Résultat : {1: 1, 2: 4, 3: 9, 4: 16}

   Chaque nombre `n` de la liste `nombres` devient une clé dans le dictionnaire `carrés`, avec son carré en valeur.

**Compréhensions de dictionnaire avec conditions**

   .. code-block:: python

       nombres = range(10)
       pairs = {n: n ** 2 for n in nombres if n % 2 == 0}
       print(pairs)  # Résultat : {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

   Seuls les nombres pairs sont inclus dans le dictionnaire `pairs`, où chaque clé est le nombre et la valeur est son carré.

**Compréhensions imbriquées dans les dictionnaires**

Il est possible d'imbriquer des compréhensions de dictionnaire pour créer des structures de données plus complexes, telles que des dictionnaires contenant des listes ou des dictionnaires imbriqués.

Exemple : Dictionnaire de listes :

.. code-block:: python

    table = {n: [n * i for i in range(1, 6)] for n in range(1, 4)}
    print(table)  # Résultat : {1: [1, 2, 3, 4, 5], 2: [2, 4, 6, 8, 10], 3: [3, 6, 9, 12, 15]}

Dans cet exemple, chaque clé du dictionnaire `table` est un nombre, et la valeur associée est une liste des multiples de ce nombre.

**Compréhensions avec conditions multiples**

Comme pour les listes, il est possible d'ajouter plusieurs conditions pour affiner davantage les valeurs du dictionnaire.

Exemple :

.. code-block:: python

    nombres = range(10)
    result = {n: n * n for n in nombres if n % 2 == 0 and n > 0}
    print(result)  # Résultat : {2: 4, 4: 16, 6: 36, 8: 64}

Seuls les nombres pairs strictement positifs sont sélectionnés.

Les compréhensions de liste et de dictionnaire en Python offrent un moyen puissant et concis de manipuler des collections de données. Elles permettent de réduire le besoin de structures de contrôle explicites, comme les boucles `for` ou les instructions `if`, et rendent le code à la fois plus lisible et plus optimisé. Bien qu'elles soient extrêmement utiles pour des opérations simples, il est recommandé de les utiliser avec des expressions et conditions simples pour éviter de rendre le code difficile à lire.
