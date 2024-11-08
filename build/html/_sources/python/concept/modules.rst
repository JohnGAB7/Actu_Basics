5. Modules et importations
=============================

Les modules en Python sont des fichiers contenant des définitions et des instructions Python. Un module permet de regrouper du code qui peut être réutilisé dans d'autres programmes. Les modules facilitent l'organisation du code et le rendent plus modulaire et maintenable.

Importation de modules
----------------------

Pour utiliser les fonctions et les classes définies dans un module, vous devez d'abord importer le module dans votre programme. Python fournit plusieurs façons d'importer des modules.

### Importation simple

La manière la plus courante d'importer un module est d'utiliser l'instruction `import` suivie du nom du module.

**Syntaxe générale :**

.. code-block:: python

    import nom_du_module

**Exemple d'utilisation :**

.. code-block:: python

    import math
    print(math.sqrt(16))  # Sortie : 4.0

Dans cet exemple, le module `math` est importé et la fonction `sqrt` est utilisée pour calculer la racine carrée d'un nombre.

### Importation avec alias

Vous pouvez également donner un alias à un module importé en utilisant le mot-clé `as`. Cela peut rendre le code plus court et plus lisible.

**Syntaxe générale :**

.. code-block:: python

    import nom_du_module as alias

**Exemple d'utilisation :**

.. code-block:: python

    import math as m
    print(m.sqrt(16))  # Sortie : 4.0

### Importation de parties spécifiques d'un module

Vous pouvez importer des fonctions, des classes ou des variables spécifiques d'un module en utilisant l'instruction `from ... import`.

**Syntaxe générale :**

.. code-block:: python

    from nom_du_module import nom_de_la_fonction

**Exemple d'utilisation :**

.. code-block:: python

    from math import sqrt
    print(sqrt(16))  # Sortie : 4.0

### Importation de tout le contenu d'un module

Vous pouvez importer toutes les fonctions, classes et variables d'un module en utilisant l'instruction `from ... import *`. Cependant, cette pratique est généralement déconseillée car elle peut entraîner des conflits de noms.

**Syntaxe générale :**

.. code-block:: python

    from nom_du_module import *

Utilisation des fonctions et classes des modules
------------------------------------------------

Une fois qu'un module est importé, vous pouvez utiliser ses fonctions, classes et variables en les appelant avec la notation par point (`module.nom_de_la_fonction`).

**Exemple d'utilisation :**

.. code-block:: python

    import math

    # Utilisation de la fonction sqrt du module math
    racine = math.sqrt(25)
    print(racine)  # Sortie : 5.0

    # Utilisation de la constante pi du module math
    pi = math.pi
    print(pi)  # Sortie : 3.141592653589793

Création de modules
--------------------

Vous pouvez créer vos propres modules en enregistrant des fichiers Python (.py) contenant des définitions de fonctions, de classes et de variables. Ces modules peuvent ensuite être importés dans d'autres programmes.

**Exemple de création de module :**

1. Créez un fichier nommé `mon_module.py` avec le contenu suivant :

   .. code-block:: python

       # mon_module.py

       def saluer(nom):
           return f"Bonjour, {nom}!"

       PI = 3.14159

2. Utilisez ce module dans un autre fichier Python :

   .. code-block:: python

       # programme_principal.py

       import mon_module

       message = mon_module.saluer("Alice")
       print(message)  # Sortie : Bonjour, Alice!

       print(mon_module.PI)  # Sortie : 3.14159

Gestion des dépendances avec pip
--------------------------------

`pip` est le gestionnaire de paquets de Python. Il permet d'installer et de gérer les bibliothèques et les dépendances Python. Avec `pip`, vous pouvez installer des paquets depuis le Python Package Index (PyPI) et d'autres index de paquets.

### Installation de paquets

Pour installer un paquet, utilisez la commande `pip install` suivie du nom du paquet.

**Exemple d'installation :**

.. code-block:: shell

    pip install requests

Cette commande installe la bibliothèque `requests`, qui est utilisée pour effectuer des requêtes HTTP.

### Désinstallation de paquets

Pour désinstaller un paquet, utilisez la commande `pip uninstall` suivie du nom du paquet.

**Exemple de désinstallation :**

.. code-block:: shell

    pip uninstall requests

### Liste des paquets installés

Pour lister tous les paquets installés, utilisez la commande `pip list`.

**Exemple :**

.. code-block:: shell

    pip list

### Mise à jour des paquets

Pour mettre à jour un paquet, utilisez la commande `pip install --upgrade` suivie du nom du paquet.

**Exemple de mise à jour :**

.. code-block:: shell

    pip install --upgrade requests

### Fichier requirements.txt

Pour gérer les dépendances d'un projet, vous pouvez utiliser un fichier `requirements.txt` qui liste tous les paquets nécessaires. Vous pouvez installer toutes les dépendances en utilisant la commande `pip install -r requirements.txt`.

**Exemple de fichier requirements.txt :**

.. code-block:: text

    requests==2.25.1
    numpy==1.19.5

**Installation des dépendances à partir du fichier requirements.txt :**

.. code-block:: shell

    pip install -r requirements.txt

En utilisant ces techniques, vous pouvez importer et utiliser des modules, créer vos propres modules et gérer les dépendances de vos projets Python de manière efficace et organisée.

