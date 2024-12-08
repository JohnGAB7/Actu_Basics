Chargement, nettoyage et manipulation des données
=================================================

Pandas permet de charger des données à partir de diverses sources telles que des fichiers CSV, Excel, des bases de données SQL, etc. Cette flexibilité fait de Pandas un outil incontournable pour les data scientists et les analystes de données.

Chargement des données
----------------------

Pandas offre plusieurs méthodes pour charger des données à partir de différents formats. Voici quelques exemples courants :

### Chargement de données à partir d'un fichier CSV

Les fichiers CSV (Comma-Separated Values) sont l'un des formats les plus couramment utilisés pour stocker des données tabulaires.

.. code-block:: python

    import pandas as pd

    # Chargement de données à partir d'un fichier CSV
    df = pd.read_csv('data.csv')

    # Afficher les premières lignes du DataFrame
    print(df.head())

### Chargement de données à partir d'un fichier Excel

Les fichiers Excel sont également largement utilisés pour stocker et partager des données. Pandas permet de lire directement les feuilles de calcul Excel.

.. code-block:: python

    import pandas as pd

    # Chargement de données à partir d'un fichier Excel
    df_excel = pd.read_excel('data.xlsx')

    # Afficher les premières lignes du DataFrame
    print(df_excel.head())

### Chargement de données à partir d'une base de données SQL

Pandas peut se connecter à des bases de données SQL pour lire des tables directement.

.. code-block:: python

    import pandas as pd
    import sqlite3

    # Connexion à la base de données SQLite
    conn = sqlite3.connect('database.db')

    # Lecture d'une table SQL dans un DataFrame
    df_sql = pd.read_sql_query('SELECT * FROM table_name', conn)

    # Afficher les premières lignes du DataFrame
    print(df_sql.head())

Nettoyage des données
----------------------

Le nettoyage des données est une étape cruciale dans l'analyse de données. Il inclut la gestion des valeurs manquantes, la suppression des duplicatas et la correction des types de données. Ces étapes assurent la qualité et la précision des analyses.

### Vérification des valeurs manquantes

Il est important de vérifier la présence de valeurs manquantes dans vos données avant de procéder à une analyse.

.. code-block:: python

    import pandas as pd

    # Vérification des valeurs manquantes
    print(df.isnull().sum())

### Remplacement des valeurs manquantes

Les valeurs manquantes peuvent être remplacées par des valeurs spécifiques, comme la moyenne de la colonne, ou supprimées.

.. code-block:: python

    import pandas as pd

    # Remplacement des valeurs manquantes par la moyenne
    df.fillna(df.mean(), inplace=True)

    # Suppression des lignes avec des valeurs manquantes
    df.dropna(inplace=True)

### Suppression des duplicatas

Les duplicatas peuvent fausser les résultats de votre analyse. Il est donc important de les identifier et de les supprimer.

.. code-block:: python

    import pandas as pd

    # Suppression des duplicatas
    df.drop_duplicates(inplace=True)

### Conversion des types de données

Assurez-vous que les colonnes de votre DataFrame ont les types de données appropriés pour éviter des erreurs dans les opérations ultérieures.

.. code-block:: python

    import pandas as pd

    # Conversion de types de données
    df['date'] = pd.to_datetime(df['date'])
    df['colonne_numerique'] = df['colonne_numerique'].astype(float)

Manipulation des données
------------------------

Pandas offre une multitude de méthodes pour manipuler les données, y compris la sélection, le filtrage, l'agrégation et le groupement.

### Sélection de colonnes spécifiques

Vous pouvez sélectionner une ou plusieurs colonnes d'un DataFrame en utilisant leur nom.

.. code-block:: python

    import pandas as pd

    # Sélection de colonnes spécifiques
    df_subset = df[['colonne1', 'colonne2']]

### Filtrage des lignes basées sur des conditions

Pandas permet de filtrer les lignes de données en fonction de conditions spécifiques.

.. code-block:: python

    import pandas as pd

    # Filtrage des lignes basées sur des conditions
    df_filtered = df[df['colonne1'] > 50]

### Agrégation des données

L'agrégation permet de calculer des statistiques sur des groupes de données.

.. code-block:: python

    import pandas as pd

    # Agrégation des données
    df_grouped = df.groupby('categorie').mean()

### Fusion de DataFrames

Pandas permet de fusionner plusieurs DataFrames sur une ou plusieurs colonnes communes.

.. code-block:: python

    import pandas as pd

    df1 = pd.DataFrame({
        'clé_commune': ['A', 'B', 'C'],
        'valeur1': [1, 2, 3]
    })

    df2 = pd.DataFrame({
        'clé_commune': ['A', 'B', 'D'],
        'valeur2': [4, 5, 6]
    })

    df_merged = pd.merge(df1, df2, on='clé_commune', how='inner')

Opérations statistiques de base
-------------------------------

NumPy et Pandas permettent de réaliser des opérations statistiques de base de manière simple et efficace.

### Utilisation de NumPy pour les statistiques

NumPy fournit un large éventail de fonctions pour les opérations statistiques, ce qui en fait une bibliothèque incontournable pour les calculs numériques.

.. code-block:: python

    import numpy as np

    # Création d'un tableau NumPy
    arr = np.array([1, 2, 3, 4, 5])

    # Calcul de la moyenne
    mean = np.mean(arr)

    # Calcul de la médiane
    median = np.median(arr)

    # Calcul de l'écart-type
    std_dev = np.std(arr)

    print(f'Moyenne: {mean}, Médiane: {median}, Écart-type: {std_dev}')

### Utilisation de Pandas pour les statistiques

Pandas intègre également des méthodes pour effectuer des analyses statistiques sur des données tabulaires.

.. code-block:: python

    import pandas as pd

    # Calcul de la moyenne pour chaque colonne
    mean_values = df.mean()

    # Calcul de la médiane pour chaque colonne
    median_values = df.median()

    # Calcul de l'écart-type pour chaque colonne
    std_dev_values = df.std()

    print(f'Moyennes: {mean_values}, Médians: {median_values}, Écart-types: {std_dev_values}')
