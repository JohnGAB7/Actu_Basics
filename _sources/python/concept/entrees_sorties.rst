4. Entrées et Sorties
==========================

Les opérations d'entrée et de sortie (I/O) sont essentielles pour interagir avec les utilisateurs et afficher des informations. Python fournit des fonctions intégrées pour lire les entrées de l'utilisateur et afficher des sorties sur la console.

Fonction input()
-----------------

La fonction `input()` est utilisée pour lire une entrée de l'utilisateur sous forme de chaîne de caractères. Elle peut également afficher un message d'invite.

**Syntaxe générale :**

.. code-block:: python

    variable = input("Message d'invite : ")

**Exemple d'utilisation :**

.. code-block:: python

    nom = input("Entrez votre nom : ")
    print(f"Bonjour, {nom}!")

Dans cet exemple, la fonction `input()` affiche le message "Entrez votre nom :" et attend que l'utilisateur saisisse une entrée. La chaîne saisie par l'utilisateur est stockée dans la variable `nom`.

### Conversion des entrées

Les entrées lues par `input()` sont toujours de type chaîne de caractères. Si vous avez besoin d'une autre type de donnée, comme un entier ou un flottant, vous devez convertir l'entrée.

**Exemple de conversion :**

.. code-block:: python

    age = input("Entrez votre âge : ")
    age = int(age)  # Conversion de la chaîne en entier
    print(f"Vous avez {age} ans.")

Affichage avec print()
----------------------

La fonction `print()` est utilisée pour afficher des informations sur la console. Elle peut afficher des chaînes de caractères, des variables, des résultats d'expressions, etc.

**Syntaxe générale :**

.. code-block:: python

    print(objet1, objet2, ..., sep=' ', end='\n')

- `objet1, objet2, ...` : Les objets à afficher.
- `sep` : Le séparateur entre les objets (par défaut, un espace).
- `end` : Ce qui est affiché à la fin (par défaut, un saut de ligne).

**Exemple d'utilisation :**

.. code-block:: python

    nom = "Alice"
    age = 30
    print("Nom :", nom, "Âge :", age)

Dans cet exemple, `print()` affiche les valeurs des variables `nom` et `age`, séparées par des espaces.

### Séparateur et fin de ligne

Vous pouvez personnaliser le séparateur et la fin de ligne avec les paramètres `sep` et `end`.

**Exemple de séparateur :**

.. code-block:: python

    print("A", "B", "C", sep="-")  # Sortie : A-B-C

**Exemple de fin de ligne :**

.. code-block:: python

    print("Bonjour", end="!")
    print("Comment ça va?")  # Sortie : Bonjour!Comment ça va?

Formatage des chaînes de caractères
-----------------------------------

Le formatage des chaînes de caractères permet d'insérer des valeurs dans des chaînes de manière élégante et lisible. Python propose plusieurs méthodes pour formater des chaînes, notamment l'opérateur `%`, la méthode `str.format()`, et les f-strings (format strings).

### Opérateur `%`

L'opérateur `%` permet d'insérer des valeurs dans une chaîne en utilisant des spécificateurs de format.

**Syntaxe générale :**

.. code-block:: python

    "chaîne % spécificateur" % valeur

**Exemple d'utilisation :**

.. code-block:: python

    nom = "Alice"
    age = 30
    print("Nom : %s, Âge : %d" % (nom, age))  # Sortie : Nom : Alice, Âge : 30

### Méthode `str.format()`

La méthode `str.format()` offre une manière plus flexible de formater des chaînes.

**Syntaxe générale :**

.. code-block:: python

    "chaîne {}".format(valeur)

**Exemple d'utilisation :**

.. code-block:: python

    nom = "Alice"
    age = 30
    print("Nom : {}, Âge : {}".format(nom, age))  # Sortie : Nom : Alice, Âge : 30

### f-strings (format strings)

Les f-strings, introduites dans Python 3.6, permettent d'insérer des expressions directement dans des chaînes en les préfixant par `f` ou `F`.

**Syntaxe générale :**

.. code-block:: python

    f"chaîne {expression}"

**Exemple d'utilisation :**

.. code-block:: python

    nom = "Alice"
    age = 30
    print(f"Nom : {nom}, Âge : {age}")  # Sortie : Nom : Alice, Âge : 30

Les f-strings sont souvent préférées pour leur simplicité et leur lisibilité, en particulier lorsqu'il s'agit de formatage de chaînes complexes.

En utilisant ces méthodes, vous pouvez gérer efficacement les entrées et sorties en Python, ainsi que formater les chaînes de caractères pour afficher des informations de manière claire et structurée.

Gestion des erreurs et exceptions
=================================

La gestion des erreurs et des exceptions est cruciale pour écrire des programmes robustes et fiables. Les exceptions permettent de gérer les situations où une erreur se produit pendant l'exécution du programme, ce qui empêche le programme de planter et offre une manière de traiter l'erreur de manière appropriée.

Instructions try, except, else, finally
----------------------------------------

Python utilise les blocs `try`, `except`, `else` et `finally` pour gérer les exceptions. Voici un aperçu de chaque bloc :

- **try** : Ce bloc contient le code qui pourrait provoquer une exception.
- **except** : Ce bloc contient le code qui est exécuté si une exception se produit dans le bloc `try`.
- **else** : Ce bloc contient le code qui est exécuté si aucune exception ne se produit dans le bloc `try`.
- **finally** : Ce bloc contient le code qui est exécuté en dernier, que l'exception se produise ou non.

**Syntaxe générale :**

.. code-block:: python

    try:
        # Bloc de code susceptible de provoquer une exception
        pass
    except Erreur:
        # Bloc de code exécuté en cas d'exception
        pass
    else:
        # Bloc de code exécuté si aucune exception ne se produit
        pass
    finally:
        # Bloc de code exécuté en dernier
        pass

**Exemple d'utilisation :**

.. code-block:: python

    try:
        x = int(input("Entrez un nombre : "))
        result = 10 / x
    except ValueError:
        print("Erreur : Vous devez entrer un nombre entier.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro.")
    else:
        print(f"Le résultat est {result}")
    finally:
        print("Fin de l'exécution")

Dans cet exemple, le bloc `try` tente de lire un nombre de l'utilisateur et de diviser 10 par ce nombre. Si l'utilisateur entre une valeur qui n'est pas un entier, une exception `ValueError` est levée et gérée par le bloc `except`. Si l'utilisateur entre zéro, une exception `ZeroDivisionError` est levée et gérée. Le bloc `else` est exécuté uniquement si aucune exception ne se produit, et le bloc `finally` est toujours exécuté à la fin.

Levée d'exceptions (raise)
--------------------------

Il est parfois nécessaire de lever des exceptions manuellement pour indiquer qu'une situation anormale s'est produite. L'instruction `raise` permet de lever une exception.

**Syntaxe générale :**

.. code-block:: python

    raise NomDeLException("message")

**Exemple d'utilisation :**

.. code-block:: python

    def verifier_age(age):
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        return age

    try:
        age_utilisateur = int(input("Entrez votre âge : "))
        age_verifie = verifier_age(age_utilisateur)
        print(f"Votre âge est {age_verifie}")
    except ValueError as e:
        print(f"Erreur : {e}")

Dans cet exemple, la fonction `verifier_age` lève une exception `ValueError` si l'âge fourni est négatif. Le bloc `try` tente de lire l'âge de l'utilisateur et de vérifier qu'il est valide. Si une exception est levée, elle est gérée par le bloc `except`.

Bonnes pratiques pour la gestion des exceptions
-----------------------------------------------

Pour écrire un code robuste et facile à maintenir, il est important de suivre certaines bonnes pratiques lors de la gestion des exceptions :

- **Spécificité des exceptions** : Gérez les exceptions spécifiques plutôt que d'utiliser une clause `except` générale. Cela permet de traiter les erreurs de manière plus appropriée et de ne pas masquer d'autres exceptions inattendues.
  
  **Exemple :**

  .. code-block:: python

      try:
          x = int(input("Entrez un nombre : "))
      except ValueError:
          print("Erreur : Vous devez entrer un nombre entier.")

- **Éviter de masquer les erreurs** : Ne laissez pas le bloc `except` vide ou avec un `pass`. Cela pourrait masquer des erreurs qui devraient être corrigées.
  
  **Exemple à éviter :**

  .. code-block:: python

      try:
          x = int(input("Entrez un nombre : "))
      except:
          pass  # Mauvaise pratique

- **Utiliser le bloc `finally` pour le nettoyage** : Utilisez le bloc `finally` pour exécuter des actions de nettoyage, telles que la fermeture de fichiers ou la libération de ressources, même si une exception se produit.
  
  **Exemple :**

  .. code-block:: python

      try:
          fichier = open("fichier.txt", "r")
          contenu = fichier.read()
      except FileNotFoundError:
          print("Erreur : Le fichier n'existe pas.")
      finally:
          fichier.close()

- **Lever des exceptions appropriées** : Lorsque vous levez des exceptions, assurez-vous qu'elles sont appropriées pour la situation et fournissez des messages d'erreur clairs et informatifs.
  
  **Exemple :**

  .. code-block:: python

      def diviser(a, b):
          if b == 0:
              raise ZeroDivisionError("Division par zéro non autorisée")
          return a / b

  try:
      resultat = diviser(10, 0)
  except ZeroDivisionError as e:
      print(f"Erreur : {e}")

En suivant ces bonnes pratiques, vous pouvez écrire un code plus résilient et plus facile à déboguer, en assurant une gestion appropriée des erreurs et des exceptions.

