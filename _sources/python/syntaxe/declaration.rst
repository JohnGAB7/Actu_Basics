2. Déclaration de Variables
===========================

La déclaration de variables en Python est fondamentale pour stocker et manipuler des données. Dans cette sous-section, nous couvrirons les conventions de nommage, les types de données de base et des techniques avancées comme l'affectation multiple.

Nommer les Variables
--------------------

Les noms de variables doivent être descriptifs et suivre certaines conventions de style pour assurer la lisibilité du code.

- **Règles de base pour nommer les variables** :
  
  - Les noms de variables doivent commencer par une lettre (a-z, A-Z) ou un underscore (`_`) et peuvent contenir des lettres, des chiffres (0-9) et des underscores.
  - Les caractères spéciaux comme `@`, `#`, `$` ne sont pas autorisés.
  - Python est sensible à la casse, ce qui signifie que `maVariable` et `mavariable` sont deux variables différentes.

  **Exemples** :

  .. code-block:: python

      nom = "Alice"  # valide
      âge = 25       # valide
      _score = 100   # valide
      1er_score = 50 # invalide (ne commence pas par une lettre ou un underscore)

- **Conventions de nommage** :
  
  En Python, les développeurs suivent généralement deux conventions pour les noms de variables :

  - **snake_case** : Utilise des underscores pour séparer les mots. C'est la convention la plus courante pour les variables en Python.
    
    **Exemple** : `nombre_total`, `nom_utilisateur`

  - **camelCase** : Utilise des majuscules pour distinguer les mots à partir du deuxième mot. Cette convention est moins courante en Python, mais elle peut être utilisée.

    **Exemple** : `nombreTotal`, `nomUtilisateur`

Expressions et affectations
----------------------------

Les variables sont créées par simple affectation, sans déclaration préalable, et le type est déterminé dynamiquement. Python offre une syntaxe concise pour diverses opérations :

.. code-block:: python

    x = 10
    y = "texte"
    z = [1, 2, 3]

Python permet l'affectation de plusieurs variables en une seule ligne, ce qui peut simplifier le code et le rendre plus lisible.

- **Affectation simple de plusieurs variables** : Vous pouvez affecter plusieurs variables en une ligne en séparant chaque variable par une virgule et en assignant des valeurs correspondantes.

  .. code-block:: python

      x, y, z = 5, 10, 15  # x = 5, y = 10, z = 15

- **Affectation de la même valeur à plusieurs variables** : Vous pouvez également assigner la même valeur à plusieurs variables en utilisant un seul signe égal.

  .. code-block:: python

      a = b = c = 0  # a, b et c sont tous égaux à 0

Cette syntaxe est particulièrement utile pour initialiser plusieurs variables avec une même valeur par défaut.

En suivant ces règles et conventions, vous pouvez créer des variables claires, lisibles et cohérentes, facilitant la compréhension de votre code.

commentaires
-------------

Les commentaires sont des lignes de texte dans le code qui ne sont pas exécutées. Ils permettent d'expliquer ou de clarifier le code, aidant ainsi à la compréhension du programme par les autres développeurs (ou par vous-même dans le futur). Python propose plusieurs façons d'ajouter des commentaires, qu'ils soient sur une seule ligne ou multi-lignes.

**Commentaires sur une Ligne**

Pour ajouter un commentaire sur une seule ligne, utilisez le symbole `#`. Tout texte après ce symbole, jusqu'à la fin de la ligne, sera ignoré par Python.

**Exemple** :

.. code-block:: python

    # Ceci est un commentaire
    x = 10  # Ce commentaire explique la variable x

Les commentaires sur une seule ligne sont pratiques pour de courtes explications, ou pour ajouter des notes à côté du code.

**Commentaires Multi-lignes**

Pour des commentaires plus longs, Python permet l'utilisation de triple guillemets (`'''` ou `"""`). Bien que les triple guillemets soient principalement utilisés pour les chaînes de documentation, ils peuvent également servir de commentaire multi-ligne si la chaîne n'est pas assignée à une variable.

**Exemple** :

.. code-block:: python

    '''
    Ce commentaire explique le fonctionnement du code suivant.
    Il peut s'étendre sur plusieurs lignes sans avoir besoin de symboles supplémentaires.
    '''
    def ma_fonction():
        pass

Notez que cette pratique est surtout utilisée lorsque vous avez des explications détaillées ou des notes de développement temporaires. Pour les documentations plus formelles, préférez utiliser les chaînes de documentation (docstrings).

**Bonnes Pratiques pour les Commentaires**

Les commentaires jouent un rôle crucial dans la documentation du code. Ils aident les développeurs à comprendre rapidement la fonctionnalité du code et à naviguer plus facilement dans le programme. Voici quelques bonnes pratiques pour l'utilisation des commentaires dans la documentation :

- **Décrire la finalité des fonctions et des classes** : Utilisez des commentaires pour expliquer ce que fait une fonction ou une classe et pourquoi elle est nécessaire.
- **Expliquer la logique complexe** : Pour les algorithmes ou les logiques complexes, ajoutez des commentaires pour décrire le processus étape par étape.
- **Marquer les sections importantes** : Utilisez des commentaires pour signaler des sections importantes du code, telles que les initialisations, les boucles principales, ou les blocs de code critiques.
- **Fournir des exemples d'utilisation** : Ajoutez des commentaires avec des exemples d'utilisation du code, montrant comment appeler une fonction ou utiliser une classe.

**Exemple d'utilisation:**
.. code-block:: python

    def calculer_somme(a, b):
        """
        Cette fonction calcule la somme de deux nombres.
        
        Args:
        a (int, float): Le premier nombre.
        b (int, float): Le deuxième nombre.
        
        Returns:
        int, float: La somme des deux nombres.
        
        Exemple :
        >>> calculer_somme(5, 3)
        8
        """
        return a + b

Voici quelques bonnes pratiques pour rédiger des commentaires efficaces :

- **Soyez concis et pertinent** : Les commentaires doivent être brefs et clairs. Évitez de commenter des évidences ; commentez plutôt les parties complexes ou les choix de conception.

- **Mettez à jour les commentaires** : Si le code est modifié, assurez-vous de mettre à jour les commentaires pour qu'ils restent pertinents.

- **Expliquez pourquoi, pas comment** : En général, il est plus utile d'expliquer la logique derrière une décision (le "pourquoi") plutôt que de décrire ce que fait le code, qui est souvent évident par lui-même.

- **Utilisez des commentaires pour clarifier les raccourcis** : Si vous avez utilisé un raccourci ou une optimisation non triviale, un commentaire peut aider les autres développeurs à comprendre l'intention.

**Exemples de bonnes pratiques** :

.. code-block:: python

    # Initialise la liste des scores avec une valeur de zéro pour chaque joueur
    scores = [0] * nombre_de_joueurs

    # Vérifie si le fichier existe avant de tenter de le lire
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as fichier:
            contenu = fichier.read()

Une documentation bien commentée aide non seulement à comprendre le code existant, mais facilite également la collaboration entre les développeurs et la maintenance du projet à long terme. En suivant ces pratiques, vos commentaires deviendront des outils précieux pour la compréhension et la maintenance du code, facilitant ainsi le travail d'équipe et les mises à jour du projet.

