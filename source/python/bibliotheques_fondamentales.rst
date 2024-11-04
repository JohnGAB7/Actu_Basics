.. _bibliotheques:

Bibliothèques Python
====================

Python dispose d'un écosystème riche en bibliothèques qui facilitent l'analyse de données. Dans cette section, nous allons explorer certaines des bibliothèques les plus populaires, notamment NumPy, Pandas, Matplotlib, et Seaborn.

NumPy
------

NumPy (Numerical Python) est une bibliothèque fondamentale pour le calcul scientifique en Python. Elle offre des structures de données puissantes, comme les tableaux multidimensionnels, et des fonctions pour effectuer des opérations mathématiques sur ces tableaux.

.. code-block:: python

    import numpy as np

    # Création d'un tableau NumPy
    tableau = np.array([1, 2, 3, 4, 5])

    # Calcul de la somme
    somme = np.sum(tableau)  # 15

    # Calcul de la moyenne
    moyenne = np.mean(tableau)  # 3.0

Pandas
-------

Pandas est une bibliothèque qui facilite la manipulation et l'analyse de données, en particulier des données tabulaires. Elle fournit des structures de données comme les DataFrames, qui permettent de travailler facilement avec des jeux de données complexes.

.. code-block:: python

    import pandas as pd

    # Création d'un DataFrame à partir d'un dictionnaire
    data = {
        "Nom": ["Alice", "Bob", "Charlie"],
        "Âge": [25, 30, 35],
        "Ville": ["Bruxelles", "Louvain", "Namur"]
    }
    df = pd.DataFrame(data)

    # Affichage des premières lignes du DataFrame
    print(df.head())

    # Sélection d'une colonne
    ages = df["Âge"]

    # Filtrage des données
    adultes = df[df["Âge"] > 30]

Matplotlib
-----------

Matplotlib est une bibliothèque de visualisation de données qui permet de créer des graphiques et des figures de manière simple et flexible. Elle est souvent utilisée pour visualiser des données analytiques et présenter des résultats.

.. code-block:: python

    import matplotlib.pyplot as plt

    # Données à tracer
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Création d'un graphique
    plt.plot(x, y, marker='o')
    plt.title("Graphique des Nombres Premiers")
    plt.xlabel("Index")
    plt.ylabel("Valeur")
    plt.grid()

    # Affichage du graphique
    plt.show()

Seaborn
--------

Seaborn est une bibliothèque de visualisation basée sur Matplotlib qui simplifie la création de graphiques informatifs et attrayants. Elle est particulièrement utile pour la visualisation de données statistiques et la création de graphiques complexes.

.. code-block:: python

    import seaborn as sns
    import matplotlib.pyplot as plt

    # Chargement d'un ensemble de données d'exemple
    titanic = sns.load_dataset("titanic")

    # Création d'un graphique de répartition
    sns.histplot(titanic["age"], bins=20, kde=True)
    plt.title("Distribution des Âges dans le Titanic")
    plt.xlabel("Âge")
    plt.ylabel("Fréquence")

    # Affichage du graphique
    plt.show()

Conclusion
----------

Dans cette section, nous avons exploré certaines des bibliothèques les plus importantes pour l'analyse de données en Python : NumPy, Pandas, Matplotlib et Seaborn. Chacune de ces bibliothèques joue un rôle clé dans le processus d'analyse et de visualisation des données, et il est essentiel de les maîtriser pour devenir un analyste de données efficace. Dans les sections suivantes, nous allons approfondir des concepts plus avancés et des techniques d'analyse de données.
