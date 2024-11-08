6. Les Types de données en Python
=================================

Python propose une variété de types de données pour stocker et manipuler différentes formes d'informations. Ils se divisent principalement en deux catégories : les types de base et les structures de données intégrées.

Types de base
-------------

Les types de données de base en Python sont les fondations des valeurs manipulées par le programme.

**Les types numériques**


Les types numériques sont utilisés pour manipuler les nombres.

- **Entiers (`int`)** : Représente des entiers relatifs. Avant la version 3.0, ce type était dénommé `long`, et le type `int` correspondait à un entier de 32 ou 64 bits. Toutefois, une conversion automatique en type `long` évitait tout débordement. Maintenant, ce type correspond aux entiers relatifs avec une précision illimitée sans restriction de taille.

  .. code-block:: python

      x = 42

- **Flottants (`float`)** : Représente des nombres à virgule flottante, équivalent au type `double` du langage C. Ce type peut représenter tout nombre entre −1,7 × 10^308 et 1,7 × 10^308 sur les plateformes conformes à l'IEEE 754.

  .. code-block:: python

      y = 3.14159

- **complex** : Représente des nombres complexes, c'est-à-dire deux nombres flottants (une partie réelle et une partie imaginaire).

  .. code-block:: python

      z = 1 + 2j

**Les objets itérables**

- **Chaîne de caractère (`str`)** : Représente une chaîne de caractères. À partir de la version 3.0, les chaînes de caractères sont en Unicode sur 16 ou 32 bits. Les objets `str` sont immuables. Dans les versions précédentes, ces objets étaient respectivement de type `unicode` et `str`.

  .. code-block:: python

      texte = "Bonjour"

- **bytes** : Chaînes d'octets immuables, utilisées pour les données binaires.

  .. code-block:: python

      données = "Octets"

- **bytearray** : Chaînes d'octets modifiables.

  .. code-block:: python

      données_modifiables = bytearray("Octets")

- **file** : Correspond à un fichier obtenu grâce à la méthode `open()`. Il permet de lire ou d'écrire des données dans des fichiers.

Il existe également d'autres types d'objets itérables, comme `range`, obtenu via la méthode `range()`, ainsi que les types associés aux méthodes de dictionnaires `.keys()`, `.values()`, et `.items()`. La plupart d'entre eux sont immuables.

Les objets itérables sont parcourus à l'aide d'une boucle `for` de la manière suivante :

.. code-block:: python

    for element in objet_iterable:
        traiter(element)

Pour une chaîne de caractères, l'itération se fait caractère par caractère.

Il existe également d'autres objets, n'étant ni numériques ni itérables

**Types booléens**

- **bool** : Représente les valeurs ``True`` et ``False``.

  .. code-block:: python

      est_vrai = True

- **None** : Indique l'absence de valeur.

  .. code-block:: python

      valeur_inconnue = None

Structures de données intégrées
-------------------------------

Python fournit plusieurs structures de données intégrées (objet itérables particuliers) qui permettent de stocker des collections de valeurs.

- **Listes (`list`)** : Les listes sont des collections ordonnées d'éléments, qui peuvent contenir des types de données variés. Elles sont modifiables et permettent d'ajouter, de supprimer ou de modifier des éléments. Elles s'étendent automatiquement pour s'adapter à l'ajout d'éléments.

.. code-block:: python

    ma_liste = [1, "deux", 3.0]


.. code-block:: python

    # Déclaration d'une liste
    fruits = ["pomme", "banane", "cerise"]

    # Accéder à un élément
    premier_fruit = fruits[0]  # "pomme"

    # Ajouter un élément
    fruits.append("orange")

    # Supprimer un élément
    fruits.remove("banane")

- **Tuples (`tuple`)** : Les tuples sont similaires aux listes, mais ils sont immuables, ce qui signifie que leurs éléments ne peuvent pas être modifiés une fois créés. Ils sont souvent utilisés pour représenter des données fixes.

.. code-block:: python

    # Déclaration d'un tuple
    coordonnees = (10.0, 20.0)

    # Accéder à un élément
    x = coordonnees[0]  # 10.0

    # Les tuples ne peuvent pas être modifiés
    # coordonnees[0] = 15.0  # Cela provoquerait une erreur

- **Ensembles (`set`)** : Un ensemble est une collection non ordonnée d'objets uniques. Les ensembles ne peuvent pas contenir de doublons et ne conservent pas l'ordre des éléments. Ils sont particulièrement utiles pour effectuer des opérations de théorie des ensembles, comme l'union et l'intersection.

.. code-block:: python

    # Déclaration d'un ensemble
    nombres = {1, 2, 3, 4, 5}

    # Ajouter un élément
    nombres.add(6)

    # Supprimer un élément
    nombres.remove(3)

    # Vérifier l'appartenance
    est_present = 2 in nombres  # True

.. code-block:: python

     mon_ensemble = {1, 2, 3}

- **frozenset** : Forme immuable d'un ensemble. Une fois créé, son contenu ne peut pas être modifié.

  .. code-block:: python

      mon_frozenset = frozenset([1, 2, 3])

- **Dictionnaires (`dict`)** : Les dictionnaires sont des collections non ordonnées d'éléments sous forme de paires clé-valeur. Ils permettent d'accéder rapidement aux valeurs en utilisant leurs clés.

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

Types spéciaux
--------------------------

Python fournit des types pour des opérations avancées et des manipulations d'objets.

- **memoryview** : Vue mémoire sur des objets bytearray, bytes, ou autres tampons.

  .. code-block:: python

      vue = memoryview(b"Exemple")

.. - **range** : Génère une séquence d'entiers.

..   .. code-block:: python

..       for i in range(5):
..           print(i)

- **slice** : Représente une partie d'une séquence.

  .. code-block:: python

      sous_liste = slice(1, 3)

- **type** : Retourne le type d'un objet.

  .. code-block:: python

      type_de_x = type(5)

- **object** : Classe de base dont tous les objets Python héritent.

- **NotImplementedType** : Indique l'absence d'implémentation d'une méthode ou d'un type. Utilisé dans les opérations qui ne sont pas prises en charge.

- **exception** : Type utilisé pour les messages d'erreur levés lors de l'exécution d'un programme.

- **function** : Type d'une fonction, utilisé lors de l'appel des mots-clés `def` et `lambda`.

- **module** : Type d'un module, utilisé lors de l'importation avec les mots-clés `import` et `from`.

Conversions de types
--------------------

Python permet de convertir une valeur d'un type à un autre, ce processus est appelé **casting**. Les fonctions intégrées facilitent cette conversion pour différents types.

- **Convertir en entier (`int()`)** :
  Convertit une valeur en entier si c'est possible.

  **Exemple** :
  
  .. code-block:: python
  
      entier = int("42")  # Résultat : 42

- **Convertir en flottant (`float()`)** :
  Convertit une valeur en flottant.

  **Exemple** :
  
  .. code-block:: python
  
      flottant = float("3.14")  # Résultat : 3.14

- **Convertir en chaîne (`str()`)** :
  Convertit une valeur en chaîne de caractères.

  **Exemple** :
  
  .. code-block:: python
  
      chaine = str(42)  # Résultat : "42"

- **Convertir en booléen (`bool()`)** :
  Convertit une valeur en booléen. Les valeurs `0`, `0.0`, `""`, `None`, et les collections vides retournent `False`, sinon `True`.

  **Exemple** :
  
  .. code-block:: python
  
      bool_value = bool("")  # Résultat : False

Ces conversions de types sont essentielles pour manipuler des données dans différentes situations et permettent une grande flexibilité dans le code.
