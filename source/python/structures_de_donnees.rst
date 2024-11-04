.. _structures_donnees:

Structures de Données en Python
=================================

Les structures de données en Python permettent d'organiser et de manipuler des collections d'objets de manière efficace. Dans cette section, nous explorerons les principales structures de données disponibles en Python, notamment les listes, les tuples, les ensembles et les dictionnaires.

Listes
------

Les listes sont des collections ordonnées d'éléments, qui peuvent contenir des types de données variés. Elles sont modifiables et permettent d'ajouter, de supprimer ou de modifier des éléments.

.. code-block:: python

    # Déclaration d'une liste
    fruits = ["pomme", "banane", "cerise"]

    # Accéder à un élément
    premier_fruit = fruits[0]  # "pomme"

    # Ajouter un élément
    fruits.append("orange")

    # Supprimer un élément
    fruits.remove("banane")

Tuples
-------

Les tuples sont similaires aux listes, mais ils sont immuables, ce qui signifie que leurs éléments ne peuvent pas être modifiés une fois créés. Ils sont souvent utilisés pour représenter des données fixes.

.. code-block:: python

    # Déclaration d'un tuple
    coordonnees = (10.0, 20.0)

    # Accéder à un élément
    x = coordonnees[0]  # 10.0

    # Les tuples ne peuvent pas être modifiés
    # coordonnees[0] = 15.0  # Cela provoquerait une erreur

Ensembles
---------

Les ensembles sont des collections non ordonnées d'éléments uniques. Ils sont particulièrement utiles pour effectuer des opérations de théorie des ensembles, comme l'union et l'intersection.

.. code-block:: python

    # Déclaration d'un ensemble
    nombres = {1, 2, 3, 4, 5}

    # Ajouter un élément
    nombres.add(6)

    # Supprimer un élément
    nombres.remove(3)

    # Vérifier l'appartenance
    est_present = 2 in nombres  # True

Dictionnaires
-------------

Les dictionnaires sont des collections non ordonnées d'éléments sous forme de paires clé-valeur. Ils permettent d'accéder rapidement aux valeurs en utilisant leurs clés.

.. code-block:: python

    # Déclaration d'un dictionnaire
    personne = {
        "nom": "Alice",
        "age": 30,
        "ville": "Bruxelles"
    }

    # Accéder à une valeur
    nom_personne = personne["nom"]  # "Alice"

    # Ajouter une nouvelle paire clé-valeur
    personne["profession"] = "Ingénieur"

    # Supprimer une paire clé-valeur
    del personne["age"]

Conclusion
----------

Dans cette section, nous avons exploré les principales structures de données en Python : listes, tuples, ensembles et dictionnaires. Chacune de ces structures a ses propres caractéristiques et utilisations, et il est important de choisir celle qui convient le mieux à vos besoins lors de la manipulation de données. Dans les sections suivantes, nous examinerons des concepts plus avancés et comment utiliser ces structures dans des contextes pratiques.
