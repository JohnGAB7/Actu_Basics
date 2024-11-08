3. Fonctions
===============

Les fonctions en Python sont des blocs de code réutilisables qui effectuent une tâche spécifique. Elles permettent de structurer le code de manière modulaire, ce qui facilite la lecture, la maintenance et le réutilisation du code.

Définition et appel de fonctions
----------------------------------

Une fonction est définie à l'aide du mot-clé `def`, suivi du nom de la fonction, des parenthèses et d'un deux-points. Le corps de la fonction est indente.

**Syntaxe générale :**

.. code-block:: python

    def nom_de_la_fonction(parametres):
        """
        Description de la fonction.
        """
        # Corps de la fonction
        instructions

**Exemple d'utilisation :**

.. code-block:: python

    def saluer():
        """
        Cette fonction affiche un message de salutation.
        """
        print("Bonjour!")

    # Appel de la fonction
    saluer()

Dans cet exemple, la fonction `saluer` est définie sans paramètres et affiche simplement "Bonjour!" lorsqu'elle est appelée.

Paramètres et arguments
-----------------------

Les fonctions peuvent accepter des paramètres, qui sont des variables locales définies dans la déclaration de la fonction. Lors de l'appel de la fonction, les valeurs spécifiques fournies pour ces paramètres sont appelées arguments.

**Syntaxe générale :**

.. code-block:: python

    def nom_de_la_fonction(parametre1, parametre2):
        """
        Description de la fonction.
        """
        # Corps de la fonction utilisant les paramètres
        instructions

**Exemple d'utilisation :**

.. code-block:: python

    def saluer_personne(nom):
        """
        Cette fonction affiche un message de salutation personnalisé.
        """
        print(f"Bonjour, {nom}!")

    # Appel de la fonction avec un argument
    saluer_personne("Alice")

Dans cet exemple, la fonction `saluer_personne` prend un paramètre `nom` et affiche un message de salutation personnalisé.

### Paramètres par défaut

Les fonctions peuvent également avoir des paramètres avec des valeurs par défaut. Cela permet d'appeler la fonction sans fournir explicitement des arguments pour ces paramètres.

**Exemple d'utilisation :**

.. code-block:: python

    def saluer_personne(nom="inconnu"):
        """
        Cette fonction affiche un message de salutation personnalisé avec un nom par défaut.
        """
        print(f"Bonjour, {nom}!")

    # Appel de la fonction sans argument
    saluer_personne()

    # Appel de la fonction avec un argument
    saluer_personne("Bob")

Valeurs de retour
-----------------

Les fonctions peuvent renvoyer des valeurs à l'aide de l'instruction `return`. Cela permet à la fonction de produire une sortie qui peut être utilisée dans d'autres parties du programme.

**Syntaxe générale :**

.. code-block:: python

    def nom_de_la_fonction(parametres):
        """
        Description de la fonction.
        """
        # Corps de la fonction
        resultat = ...
        return resultat

**Exemple d'utilisation :**

.. code-block:: python

    def addition(a, b):
        """
        Cette fonction renvoie la somme de deux nombres.
        """
        return a + b

    # Appel de la fonction et utilisation de la valeur de retour
    resultat = addition(3, 4)
    print(resultat)  # Sortie : 7

Fonctions lambda (fonctions anonymes)
-------------------------------------

Les fonctions lambda sont des fonctions anonymes définies à l'aide du mot-clé `lambda`. Elles peuvent prendre plusieurs arguments, mais ne peuvent contenir qu'une seule expression.

**Syntaxe générale :**

.. code-block:: python

    lambda parametres: expression

**Exemple d'utilisation :**

.. code-block:: python

    # Fonction lambda pour additionner deux nombres
    addition = lambda a, b: a + b

    # Utilisation de la fonction lambda
    print(addition(3, 4))  # Sortie : 7

Les fonctions lambda sont souvent utilisées pour des opérations simples et rapides, généralement en combinaison avec des fonctions de haut niveau comme `map`, `filter`, et `reduce`.

Portée des variables (global, local)
------------------------------------

La portée d'une variable définit l'endroit où la variable peut être utilisée dans le programme. Python distingue les variables locales et globales.

### Variables locales

Les variables locales sont définies à l'intérieur d'une fonction et ne sont accessibles que dans cette fonction.

**Exemple d'utilisation :**

.. code-block:: python

    def ma_fonction():
        x = 10  # Variable locale
        print(x)

    ma_fonction()
    # print(x) provoquerait une erreur, car x n'est pas défini en dehors de la fonction

### Variables globales

Les variables globales sont définies en dehors de toutes les fonctions et sont accessibles depuis n'importe quelle fonction du programme.

**Exemple d'utilisation :**

.. code-block:: python

    x = 10  # Variable globale

    def ma_fonction():
        print(x)

    ma_fonction()  # Sortie : 10

### Utilisation du mot-clé `global`

Le mot-clé `global` permet de modifier une variable globale à l'intérieur d'une fonction.

**Exemple d'utilisation :**

.. code-block:: python

    x = 10  # Variable globale

    def changer_x():
        global x
        x = 20

    changer_x()
    print(x)  # Sortie : 20

En utilisant ces concepts, vous pouvez définir, appeler et manipuler des fonctions en Python de manière efficace et structurée.