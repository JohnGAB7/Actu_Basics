2. Indentation
===============

L'indentation est essentielle en Python, car elle détermine la structure du code en délimitant les blocs logiques, comme les fonctions, les boucles, et les conditions. Contrairement à de nombreux autres langages de programmation qui utilisent des symboles comme ``{}`` ou ``;`` pour structurer le code, Python s'appuie sur l'indentation. Chaque bloc de code est défini par son indentation, ce qui rend le code plus lisible et plus structuré. L'indentation est cruciale en Python, car elle détermine la hiérarchie des instructions; une indentation correcte est essentielle pour le bon fonctionnement du programme, et des erreurs d'indentation peuvent entraîner des erreurs de syntaxe.


**Exemple en Python:**

.. code-block:: python

    if x > 0:
        print("x est positif")
    else:
        print("x est négatif ou zéro")


Dans cet exemple, l'indentation indique que la ligne `print("x est positif")` appartient au bloc de code de la condition `if`, et que `print("x est négatif ou zéro")` appartient au bloc de code de la condition `else`.

**Exemple en C++ :**

.. code-block:: cpp

    if (x > 0) {
        cout << "x est positif" << endl;
    } else {
        cout << "x est négatif ou zéro" << endl;
    }

En C++, les accolades `{}` délimitent les blocs de code pour les conditions `if` et `else`. L'indentation aide à lire le code, mais le compilateur se fie aux accolades pour comprendre la structure.

En revanche, en Python, l'indentation est obligatoire et fait partie intégrante de la syntaxe. L'absence d'accolades rend la lecture du code plus naturelle et moins encombrée, mais elle exige une rigueur stricte en matière d'indentation.

Règles d'indentation en Python
-------------------------------

- **Utilisation de quatre espaces par niveau** : En Python, il est recommandé d'utiliser **quatre espaces** pour chaque niveau d'indentation. Bien que certains éditeurs permettent d'utiliser la touche de tabulation, il est préférable d'utiliser des espaces pour garantir la cohérence.

  **Exemple** :

  .. code-block:: python

      def ma_fonction():
          for i in range(5):
              if i % 2 == 0:
                  print(i)

  Dans cet exemple, chaque niveau de logique (fonction, boucle, condition) est décalé par quatre espaces.

**Blocs de Code**

Les blocs de code en Python sont créés par des structures d'indentation pour des éléments tels que :

- **Déclaration de fonctions** :

  .. code-block:: python

      def saluer():
          print("Bonjour")

- **Boucles** :

  .. code-block:: python

      for i in range(3):
          print(i)

- **Conditions** :

  .. code-block:: python

      if x > 0:
          print("x est positif")
      else:
          print("x est négatif ou nul")

Erreurs d'indentation Courantes et Comment les Éviter
------------------------------------------------------

- **Mélange de tabulations et d'espaces** : L'une des erreurs les plus fréquentes consiste à mélanger tabulations et espaces. Python considère ces deux types d'indentation comme différents, ce qui peut provoquer des erreurs. Configurez votre éditeur pour utiliser uniquement des espaces.

- **Mauvais alignement des blocs de code** : Veillez à respecter l'alignement des blocs de code à chaque niveau. Par exemple, assurez-vous que toutes les instructions dans une boucle ou une condition sont au même niveau d'indentation.

  **Exemple d'erreur** :

  .. code-block:: python

      for i in range(5):
          if i % 2 == 0:
           print(i)  # Mauvais alignement, provoque une erreur

En suivant ces règles d'indentation, vous garantirez une structure de code cohérente et lisible, essentielle pour éviter les erreurs de syntaxe dans Python.

Bonnes pratiques pour l'indentation
-------------------------------------

Une bonne indentation est essentielle pour la lisibilité et la maintenabilité du code. Voici quelques bonnes pratiques pour l'indentation en Python :

- **Utiliser des espaces ou des tabulations, mais pas les deux** : Mélanger des espaces et des tabulations peut entraîner des erreurs de syntaxe difficiles à détecter. Il est recommandé d'utiliser quatre espaces par niveau d'indentation.
- **Être cohérent** : Utilisez la même méthode d'indentation tout au long de votre code. La cohérence améliore la lisibilité et réduit les erreurs potentielles.
- **Indentation des blocs de code** : Indentez toutes les lignes de code qui appartiennent à un bloc, y compris les lignes de continuation.
- **Utiliser un éditeur de code avec support de l'indentation** : Utilisez un éditeur de code qui gère automatiquement l'indentation. Cela peut réduire le risque d'erreurs et améliorer la productivité.
- **Vérifier l'indentation dans les fichiers existants** : Lorsque vous modifiez du code existant, assurez-vous que votre indentation correspond à celle du fichier pour maintenir la cohérence.

**Exemple :**
.. code-block:: python

    def fonction_exemple(parametre):
        if parametre > 0:
            print("Le paramètre est positif")
        else:
            print("Le paramètre est négatif ou zéro")

    fonction_exemple(5)

En suivant ces bonnes pratiques, vous pouvez vous assurer que votre code Python est propre, lisible et facile à maintenir.

.. code-block:: python

    if x > 0:
        print("x est positif")
    else:
        print("x est négatif ou zéro")

