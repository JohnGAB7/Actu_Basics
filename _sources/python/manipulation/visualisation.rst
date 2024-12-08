Visualisation de données avec Matplotlib et Seaborn
=======================================================

La visualisation de données est essentielle pour comprendre et communiquer les tendances, les anomalies et les relations dans vos données. Matplotlib et Seaborn sont deux bibliothèques Python populaires pour créer des visualisations de données.

Introduction à Matplotlib
--------------------------

Matplotlib est une bibliothèque de visualisation de données en 2D extrêmement flexible et puissante. Elle est largement utilisée pour créer des graphiques statiques, animés et interactifs en Python.

### Création de graphiques simples avec Matplotlib

Matplotlib permet de créer une variété de graphiques, y compris des graphiques en ligne, des histogrammes et des graphiques à barres.

**Exemple de graphique en ligne** :

.. code-block:: python

    import matplotlib.pyplot as plt

    # Données d'exemple
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Création du graphique en ligne
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Exemple de graphique en ligne')
    plt.show()

### Création d'histogrammes avec Matplotlib

Les histogrammes sont utiles pour visualiser la distribution d'un ensemble de données.

**Exemple d'histogramme** :

.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np

    # Données d'exemple
    data = np.random.randn(1000)

    # Création de l'histogramme
    plt.hist(data, bins=30, alpha=0.75)
    plt.xlabel('Valeur')
    plt.ylabel('Fréquence')
    plt.title('Exemple d\'histogramme')
    plt.show()

### Création de graphiques à barres avec Matplotlib

Les graphiques à barres sont utilisés pour comparer des valeurs entre différentes catégories.

**Exemple de graphique à barres** :

.. code-block:: python

    import matplotlib.pyplot as plt

    # Données d'exemple
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]

    # Création du graphique à barres
    plt.bar(categories, values)
    plt.xlabel('Catégories')
    plt.ylabel('Valeurs')
    plt.title('Exemple de graphique à barres')
    plt.show()

Introduction à Seaborn
----------------------

Seaborn est une bibliothèque de visualisation de données basée sur Matplotlib qui fournit une interface de haut niveau pour dessiner des graphiques statistiques attrayants et informatifs.

### Création de graphiques avec Seaborn

Seaborn simplifie la création de visualisations complexes, telles que les cartes de chaleur et les diagrammes de dispersion.

**Exemple de carte de chaleur** :

.. code-block:: python

    import seaborn as sns
    import numpy as np

    # Données d'exemple
    data = np.random.rand(10, 12)

    # Création de la carte de chaleur
    sns.heatmap(data, annot=True, cmap='viridis')
    plt.title('Exemple de carte de chaleur')
    plt.show()

**Exemple de diagramme de dispersion** :

.. code-block:: python

    import seaborn as sns
    import pandas as pd

    # Données d'exemple
    df = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50),
        'z': np.random.rand(50)
    })

    # Création du diagramme de dispersion
    sns.scatterplot(data=df, x='x', y='y', size='z', legend=False, palette='viridis')
    plt.title('Exemple de diagramme de dispersion')
    plt.show()

Personnalisation des visualisations
-----------------------------------

Matplotlib et Seaborn offrent de nombreuses options pour personnaliser les visualisations afin de mieux répondre à vos besoins spécifiques.

### Personnalisation avec Matplotlib

Vous pouvez ajuster les couleurs, les styles de lignes, les polices et bien plus encore.

**Exemple de personnalisation de graphique** :

.. code-block:: python

    import matplotlib.pyplot as plt

    # Données d'exemple
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Création du graphique avec personnalisation
    plt.plot(x, y, color='green', linestyle='--', marker='o')
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.title('Exemple de graphique personnalisé', fontsize=15)
    plt.grid(True)
    plt.show()

### Personnalisation avec Seaborn

Seaborn hérite de Matplotlib et permet des personnalisations avancées tout en gardant des commandes simples.

**Exemple de personnalisation avec Seaborn** :

.. code-block:: python

    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

    # Données d'exemple
    df = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50),
        'category': np.random.choice(['A', 'B', 'C'], 50)
    })

    # Création d'un graphique Seaborn avec personnalisation
    sns.set(style='whitegrid')
    sns.scatterplot(data=df, x='x', y='y', hue='category', palette='Set1', s=100)
    plt.title('Exemple de graphique Seaborn personnalisé')
    plt.show()

Avec ces outils et méthodes, vous pouvez créer des visualisations de données attractives et informatives, ce qui est essentiel pour l'analyse de données et la communication des résultats.
