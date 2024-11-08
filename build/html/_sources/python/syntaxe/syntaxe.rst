Syntaxe et concepts de base
############################

Syntaxe
-------

La syntaxe d'un langage de programmation définit les règles qui régissent la structure et l'ordonnancement des instructions. Une syntaxe claire et cohérente est essentielle pour plusieurs raisons :

- **Lisibilité** : Un code lisible permet aux développeurs de comprendre facilement le fonctionnement d'un programme, de collaborer efficacement avec d'autres développeurs et de maintenir le code sur le long terme.
- **Débogage** : Une syntaxe claire réduit les erreurs syntaxiques et facilite la détection et la correction des bugs. Les développeurs peuvent se concentrer sur la logique de leur programme plutôt que sur la résolution de problèmes syntaxiques.
- **Productivité** : Une syntaxe simple et intuitive permet aux développeurs d'écrire du code plus rapidement et plus efficacement. Moins de temps passé à apprendre et à se souvenir de la syntaxe signifie plus de temps pour résoudre des problèmes complexes et développer des fonctionnalités.
- **Collaboration** : Une syntaxe cohérente facilite la collaboration entre les développeurs, car chacun peut comprendre et modifier le code de l'autre sans avoir à se familiariser avec des règles syntaxiques complexes ou non intuitives.

Une syntaxe bien conçue améliore la qualité du code, accélère le développement et favorise la collaboration entre les développeurs. Python privilégie la lisibilité grâce à une syntaxe claire qui impose l'indentation pour délimiter les blocs de code, ce qui favorise l'écriture de code structuré et propre.

Comparé à d'autres langages de programmation, Python se distingue par sa syntaxe simple et intuitive. Voici quelques comparaisons avec d'autres langages couramment utilisés :

- **Python vs. C++** : C++ est un langage puissant mais complexe, avec une syntaxe riche et souvent difficile à maîtriser. Python, en revanche, met l'accent sur la simplicité et la lisibilité, ce qui le rend plus accessible aux débutants.
- **Python vs. Java** : Java est un langage orienté objet avec une syntaxe stricte et une gestion explicite des types. Python offre une syntaxe plus concise et dynamique, permettant aux développeurs d'écrire moins de code pour accomplir les mêmes tâches.
- **Python vs. JavaScript** : JavaScript est principalement utilisé pour le développement web côté client, avec une syntaxe flexible mais parfois incohérente. Python, avec sa syntaxe cohérente et ses puissantes bibliothèques, est idéal pour un large éventail d'applications au-delà du web.
- **Python vs. Ruby** : Ruby est un autre langage interprété avec une syntaxe élégante et orientée objet. Cependant, Python dispose d'une communauté plus vaste et d'une meilleure documentation, ce qui en fait un choix plus populaire pour de nombreux développeurs.
- **Python vs. R** : R est un langage spécialisé pour l'analyse statistique et la visualisation de données, avec une syntaxe particulière à cet usage. Python, grâce à des bibliothèques comme Pandas et Matplotlib, offre des capacités similaires tout en restant un langage de programmation généraliste.

En résumé, la syntaxe simple et claire de Python, combinée à sa polyvalence et à sa vaste communauté, en fait un langage de choix pour de nombreux développeurs, quel que soit leur niveau de compétence ou leur domaine d'application.


**Indentation**

L'indentation est un aspect crucial de la syntaxe en Python. Contrairement à de nombreux autres langages de programmation qui utilisent des accolades `{}` pour délimiter les blocs de code, Python utilise l'indentation. Chaque bloc de code est défini par son indentation, ce qui rend le code plus lisible et plus structuré. L'indentation est cruciale en Python, car elle détermine la hiérarchie des instructions. Python utilise l'indentation pour définir la structure du code; une indentation correcte est essentielle pour le bon fonctionnement du programme, et des erreurs d'indentation peuvent entraîner des erreurs de syntaxe.

L'indentation joue un rôle clé dans Python car elle définit les blocs de code qui appartiennent ensemble. Cela inclut les blocs de code pour les fonctions, les boucles, les conditions, et autres structures de contrôle.

**Exemple :**
.. code-block:: python

    if x > 0:
        print("x est positif")
    else:
        print("x est négatif ou zéro")


Dans cet exemple, l'indentation indique que la ligne `print("x est positif")` appartient au bloc de code de la condition `if`, et que `print("x est négatif ou zéro")` appartient au bloc de code de la condition `else`.

Une indentation cohérente permet de s'assurer que le code est correctement structuré et facile à lire. En Python, il est courant d'utiliser quatre espaces pour chaque niveau d'indentation, bien que certains développeurs préfèrent utiliser des tabulations.

Dans de nombreux autres langages de programmation, tels que C, C++, Java, et JavaScript, les blocs de code sont délimités par des accolades `{}`. L'indentation est utilisée pour améliorer la lisibilité, mais elle n'est pas nécessaire pour définir la structure du code.

**Exemple en C++ :**

.. code-block:: cpp

    if (x > 0) {
        cout << "x est positif" << endl;
    } else {
        cout << "x est négatif ou zéro" << endl;
    }

En C++, les accolades `{}` délimitent les blocs de code pour les conditions `if` et `else`. L'indentation aide à lire le code, mais le compilateur se fie aux accolades pour comprendre la structure.

En revanche, en Python, l'indentation est obligatoire et fait partie intégrante de la syntaxe. L'absence d'accolades rend la lecture du code plus naturelle et moins encombrée, mais elle exige une rigueur stricte en matière d'indentation.

**Bonnes pratiques pour l'indentation**

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

**Expressions et affectations**

Les variables sont créées par simple affectation, sans déclaration préalable, et le type est déterminé dynamiquement. Python offre une syntaxe concise pour diverses opérations :

.. code-block:: python

    x = 10
    y = "texte"
    z = [1, 2, 3]

**Commentaires**

Les commentaires sont des annotations dans le code qui sont ignorées par l'interpréteur Python. Ils sont utilisés pour expliquer et documenter le code, rendant ainsi le programme plus facile à comprendre et à maintenir. Les commentaires peuvent être utilisés pour décrire la logique, signaler des sections importantes, ou fournir des informations supplémentaires sur le fonctionnement du code.

Les commentaires sur une seule ligne commencent par le symbole \#. Tout ce qui suit le symbole \# sur la même ligne est considéré comme un commentaire et est ignoré par l'interpréteur.

    .. code-block:: python
        
    \# Ceci est un commentaire sur une seule ligne
    x = 5  \# Initialisation de la variable x avec la valeur 5

Les commentaires sur une seule ligne sont souvent utilisés pour ajouter des notes rapides ou des explications courtes directement au-dessus ou à côté du code pertinent.

Pour écrire des commentaires qui s'étendent sur plusieurs lignes, il est courant d'utiliser des guillemets triples (""" ou '''). Bien que techniquement ces guillemets définissent une chaîne de caractères multilignes, lorsqu'ils ne sont pas assignés à une variable, Python les traite comme des commentaires.

**Exemple :**
.. code-block:: python

    """
    Ce commentaire s'étend sur plusieurs lignes.
    Il peut être utilisé pour fournir des explications détaillées ou
    pour commenter des sections de code plus longues.
    """

    def ma_fonction():
        '''
        Cette fonction fait quelque chose de très important.
        Utilisez ce commentaire pour expliquer la logique complexe
        ou fournir des informations supplémentaires.
        '''
        pass

Les commentaires multi-lignes sont utiles pour documenter des fonctions, expliquer des algorithmes complexes, ou fournir des descriptions détaillées de certaines parties du code.

Les commentaires jouent un rôle crucial dans la documentation du code. Ils aident les développeurs à comprendre rapidement la fonctionnalité du code et à naviguer plus facilement dans le programme. Voici quelques bonnes pratiques pour l'utilisation des commentaires dans la documentation :

- **Décrire la finalité des fonctions et des classes** : Utilisez des commentaires pour expliquer ce que fait une fonction ou une classe et pourquoi elle est nécessaire.
- **Expliquer la logique complexe** : Pour les algorithmes ou les logiques complexes, ajoutez des commentaires pour décrire le processus étape par étape.
- **Marquer les sections importantes** : Utilisez des commentaires pour signaler des sections importantes du code, telles que les initialisations, les boucles principales, ou les blocs de code critiques.
- **Fournir des exemples d'utilisation** : Ajoutez des commentaires avec des exemples d'utilisation du code, montrant comment appeler une fonction ou utiliser une classe.

**Exemple :**
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

Une documentation bien commentée aide non seulement à comprendre le code existant, mais facilite également la collaboration entre les développeurs et la maintenance du projet à long terme.

Mots-clés du langage
---------------------

Les mots-clés sont des termes réservés dans Python, destinés à structurer le langage et gérer les contrôles de flux et d’exécution. Ils ne peuvent pas être utilisés comme identifiants (noms de variables ou fonctions). La liste des mots-clés est disponible avec ``keyword.kwlist`` dans le module ``keyword``.

.. admonition:: Remarque
   :class: important

   Python a évolué de manière significative entre la version 2.7 et la 3.x. Certains mots-clés ont été ajoutés, tandis que d'autres sont devenus obsolètes.

En Python 2.x., voici les mots-clés principaux :

 ``and``, ``as``, ``assert``, ``break``, ``class``, ``continue``, ``def``, ``del``, ``elif``, ``else``, ``except``, ``exec``, ``finally``, ``for``, ``from``, ``global``, ``if``, ``import``, ``in``, ``is``, ``lambda``, ``not``, ``or``, ``pass``, ``print``, ``raise``, ``return``, ``try``, ``while``, ``with``, ``yield``.

Avec Python 3.x., certains changements importants sont introduits; ``print`` et ``exec`` ne sont plus des mots-clés, mais des fonctions intégrées (``builtins``). ``True``, ``False``, ``None`` et ``nonlocal`` deviennent des mots-clés. ``True``, ``False`` et ``None`` étaient présents auparavant mais modifiables (par exemple, ``True = 1``). En Python 3, ces valeurs sont fixées et non modifiables.
``async`` et ``await`` sont ajoutés en Python 3.5 pour supporter l'exécution asynchrone.

En resumé Python possède 35 mots-clés réservés qui définissent la structure et le flux de contrôle d'un programme. 


.. list-table:: Liste des mots-clés Python sous les versions 2.x.
   :header-rows: 0
   :widths: auto

   * - ``and``
     - ``as``
     - ``assert``
     - ``break``
     - ``class``
     - ``def``
     - ``del``
   * - ``elif``
     - ``else``
     - ``except``
     - ``finally``
     - ``for``
     - ``from``
     - ``global``
   * - ``if``
     - ``import``
     - ``continue``
     - ``in``
     - ``is``
     - ``lambda``
     - ``not``
   * - ``or``
     - ``pass``
     - ``raise``
     - ``return``
     - ``try``
     - ``while``
     - ``with``
   * - ``yield``
     - ``True``
     - ``False``
     - ``None``
     - ``async``
     - ``await``
     -
     
Ces mots-clés ne peuvent pas être utilisés comme noms de variables, de fonctions ou de classes.

.. list-table:: Mots-clés Python avec descriptions
   :header-rows: 1
   :widths: 20 80

   * - Catégorie
     - Description et Exemples
   * - **Contrôle de flux**
     - - ``if``, ``elif``, ``else`` : Exécutent du code en fonction de conditions.
       - ``for``, ``while`` : Boucles qui itèrent ou continuent tant qu'une condition est vraie.
       - ``break`` : Interrompt une boucle.
       - ``continue`` : Passe à l'itération suivante de la boucle.

       .. code-block:: python

           x = 10
           if x > 0:
               print("Positif")
           elif x == 0:
               print("Zéro")
           else:
               print("Négatif")

           for i in range(5):
               if i == 2:
                   continue
               print(i)  # Imprime 0, 1, 3, 4
   * - **Définition de fonctions**
     - - ``def`` : Déclare une fonction.
       - ``return`` : Spécifie la valeur renvoyée par une fonction.

       .. code-block:: python

           def addition(a, b):
               return a + b
   * - **Fonctions anonymes**
     - ``lambda`` : Crée une fonction anonyme.

       .. code-block:: python

           carré = lambda x: x * x
           print(carré(4))  # Affiche 16
   * - **Gestion d'exceptions**
     - - ``try``, ``except``, ``finally`` : Bloc de gestion des erreurs.
       - ``raise`` : Lève une exception manuellement.

       .. code-block:: python

           try:
               x = 1 / 0
           except ZeroDivisionError:
               print("Erreur de division par zéro")
           finally:
               print("Opération terminée")
   * - **Classes et objets**
     - - ``class`` : Déclare une classe.
       - ``self`` : Référence l'instance courante dans une méthode.
       - ``super`` : Appelle les méthodes de la super-classe.

       .. code-block:: python

           class Personne:
               def __init__(self, nom):
                   self.nom = nom

               def saluer(self):
                   return f"Bonjour, {self.nom}"

           personne = Personne("Alice")
           print(personne.saluer())  # Affiche "Bonjour, Alice"
   * - **Types spéciaux et gestion du contexte**
     - - ``True``, ``False`` : Valeurs booléennes.
       - ``None`` : Absence de valeur.
       - ``with``, ``as`` : Gèrent le contexte pour des ressources comme les fichiers.

       .. code-block:: python

           with open("fichier.txt", "r") as f:
               contenu = f.read()
   * - **Programmation asynchrone**
     - - ``async`` : Définit une fonction asynchrone.
       - ``await`` : Attends le résultat d'une fonction asynchrone.

       .. code-block:: python

           import asyncio

           async def main():
               print("Bonjour")
               await asyncio.sleep(1)
               print("Monde")

           asyncio.run(main())  # Exécute la fonction asynchrone
   * - **Opérateurs logiques et de comparaison**
     - - ``and``, ``or``, ``not`` : Opérateurs logiques pour combiner des expressions.
       - ``is``, ``in`` : Testent l'identité et l'appartenance.

       .. code-block:: python

           a = [1, 2, 3]
           b = a
           print(a is b)  # True car a et b pointent vers le même objet
           print(2 in a)  # True car 2 est dans la liste

Types de base
-------------

Python fournit plusieurs types ou objet de base pour représenter différentes catégories de données. Ces types sont classés en numériques, séquentiels, ensembles, mappages, booléens, et spéciaux.

**Les types numériques**


Les types numériques sont utilisés pour manipuler les nombres.

- **int** : Représente des entiers relatifs. Avant la version 3.0, ce type était dénommé `long`, et le type `int` correspondait à un entier de 32 ou 64 bits. Toutefois, une conversion automatique en type `long` évitait tout débordement. Maintenant, ce type correspond aux entiers relatifs avec une précision illimitée sans restriction de taille.

  .. code-block:: python

      x = 42

- **float** : Représente des nombres à virgule flottante, équivalent au type `double` du langage C. Ce type peut représenter tout nombre entre −1,7 × 10^308 et 1,7 × 10^308 sur les plateformes conformes à l'IEEE 754.

  .. code-block:: python

      y = 3.14159

- **complex** : Représente des nombres complexes, c'est-à-dire deux nombres flottants (une partie réelle et une partie imaginaire).

  .. code-block:: python

      z = 1 + 2j

**Les types itérables**


- **str** : Représente une chaîne de caractères. À partir de la version 3.0, les chaînes de caractères sont en Unicode sur 16 ou 32 bits. Les objets `str` sont immuables. Dans les versions précédentes, ces objets étaient respectivement de type `unicode` et `str`.

  .. code-block:: python

      texte = "Bonjour"

- **list** : Les listes sont des tableaux dynamiques qui acceptent des types de données hétérogènes. Elles s'étendent automatiquement pour s'adapter à l'ajout d'éléments.

  .. code-block:: python

      ma_liste = [1, "deux", 3.0]

- **tuple** : Les tuples (ou n-uplets) sont des listes immuables d'objets, qui peuvent être de types hétérogènes. Une fois créés, leur contenu ne peut pas être modifié.

  .. code-block:: python

      mon_tuple = (1, "deux", 3.0)


- **set** : Un ensemble est une collection non ordonnée d'objets uniques. Les ensembles ne peuvent pas contenir de doublons et ne conservent pas l'ordre des éléments.

  .. code-block:: python

      mon_ensemble = {1, 2, 3}

- **frozenset** : Forme immuable d'un ensemble. Une fois créé, son contenu ne peut pas être modifié.

  .. code-block:: python

      mon_frozenset = frozenset([1, 2, 3])

- **dict** : Dictionnaires pour stocker des paires clé-valeur. Les dictionnaires sont des tableaux associatifs permettant d'associer une clé unique à une valeur.


  .. code-block:: python

      mon_dico = {"clé1": "valeur1", "clé2": "valeur2"}

- **bytes** : Chaînes d'octets immuables, utilisées pour les données binaires.

  .. code-block:: python

      données = b"Octets"

- **bytearray** : Chaînes d'octets modifiables.

  .. code-block:: python

      données_modifiables = bytearray(b"Octets")

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

**Autres types spéciaux**

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

Opérateurs en Python
--------------------

Python propose une large variété d'opérateurs pour manipuler des données et contrôler le flux d'exécution. Voici un aperçu des principaux types d'opérateurs et de leur utilisation.

**Opérateurs arithmétiques**

Les opérateurs arithmétiques permettent d'effectuer des opérations de calcul sur des valeurs numériques.

- **Addition (``+``)** : Additionne deux valeurs.

  .. code-block:: python

     resultat = 3 + 2  # Résultat : 5

- **Soustraction (``-``)** : Soustrait une valeur de l'autre.

  .. code-block:: python

     resultat = 5 - 2  # Résultat : 3

- **Multiplication (``*``)** : Multiplie deux valeurs.

  .. code-block:: python

     resultat = 3 * 2  # Résultat : 6

- **Division (``/``)** : Divise une valeur par l'autre. Retourne un flottant.

  .. code-block:: python

     resultat = 5 / 2  # Résultat : 2.5

- **Division entière (``//``)** : Division qui renvoie uniquement la partie entière.

  .. code-block:: python

     resultat = 5 // 2  # Résultat : 2

- **Modulo (``%``)** : Retourne le reste de la division.

  .. code-block:: python

     resultat = 5 % 2  # Résultat : 1

- **Exponentiation (``**``)** : Élève un nombre à la puissance d'un autre.

  .. code-block:: python

     resultat = 3 ** 2  # Résultat : 9

**Opérateurs de comparaison**

Ces opérateurs comparent deux valeurs et renvoient un booléen (``True`` ou ``False``).

- **Égal à (``==``)** : Vérifie si les deux valeurs sont égales.

  .. code-block:: python

     3 == 3  # Résultat : True

- **Différent de (``!=``)** : Vérifie si les deux valeurs sont différentes.

  .. code-block:: python

     3 != 2  # Résultat : True

- **Supérieur à (``>``)** : Vérifie si la première valeur est supérieure à la seconde.

  .. code-block:: python

     5 > 3  # Résultat : True

- **Inférieur à (``<``)** : Vérifie si la première valeur est inférieure à la seconde.

  .. code-block:: python

     3 < 5  # Résultat : True

- **Supérieur ou égal à (``>=``)** : Vérifie si la première valeur est supérieure ou égale à la seconde.

  .. code-block:: python

     5 >= 5  # Résultat : True

- **Inférieur ou égal à (``<=``)** : Vérifie si la première valeur est inférieure ou égale à la seconde.

  .. code-block:: python

     3 <= 4  # Résultat : True

**Opérateurs logiques**

Les opérateurs logiques sont utilisés pour combiner plusieurs expressions de comparaison.

- **Et (``and``)** : Retourne ``True`` si les deux conditions sont vraies.

  .. code-block:: python

     (3 > 2) and (5 > 3)  # Résultat : True

- **Ou (``or``)** : Retourne ``True`` si au moins une des conditions est vraie.

  .. code-block:: python

     (3 > 2) or (5 < 3)  # Résultat : True

- **Non (``not``)** : Inverse la valeur d'une condition.

  .. code-block:: python

     not (3 > 2)  # Résultat : False

**Opérateurs d'affectation**

Les opérateurs d'affectation permettent d'assigner des valeurs aux variables, souvent en combinant une opération.

- **Affectation simple (``=``)** : Assigne une valeur à une variable.

  .. code-block:: python

     x = 5

- **Addition et affectation (``+=``)** : Ajoute et affecte.

  .. code-block:: python

     x += 3  # Équivaut à x = x + 3

- **Soustraction et affectation (``-=``)** : Soustrait et affecte.

  .. code-block:: python

     x -= 2  # Équivaut à x = x - 2

- **Multiplication et affectation (``*=``)** : Multiplie et affecte.

  .. code-block:: python

     x *= 4  # Équivaut à x = x * 4

- **Division et affectation (``/=``)** : Divise et affecte.

  .. code-block:: python

     x /= 2  # Équivaut à x = x / 2

- **Division entière et affectation (``//=``, ``%=``, ``**=``)** : Fonctionnent de la même manière que les précédents avec l’opérateur correspondant.

**Opérateurs d'appartenance**

Ces opérateurs vérifient si un élément appartient (ou non) à une séquence (comme une liste, une chaîne ou un tuple).

- **Dans (``in``)** : Retourne ``True`` si l'élément est présent dans la séquence.

  .. code-block:: python

     'a' in 'actuaire'  # Résultat : True

- **Pas dans (``not in``)** : Retourne ``True`` si l'élément n'est pas présent dans la séquence.

  .. code-block:: python

     'z' not in 'actuaire'  # Résultat : True

**Opérateurs d'identité**

Ces opérateurs comparent les emplacements mémoire de deux objets.

- **Est (``is``)** : Retourne ``True`` si les deux objets sont identiques (même emplacement mémoire).

  .. code-block:: python

     a = [1, 2, 3]
     b = a
     a is b  # Résultat : True

- **N'est pas (``is not``)** : Retourne ``True`` si les deux objets ne sont pas identiques.

  .. code-block:: python

     a = [1, 2, 3]
     b = [1, 2, 3]
     a is not b  # Résultat : True

**Opérateurs binaires**

Les opérateurs binaires effectuent des opérations au niveau des bits. Ils sont utilisés principalement pour manipuler les bits dans des applications plus avancées.

- **ET binaire (``&``)** : Compare les bits et retourne 1 si les deux bits sont 1.

  .. code-block:: python

     resultat = 5 & 3  # Résultat : 1 (101 & 011 = 001)

- **OU binaire (``|``)** : Compare les bits et retourne 1 si au moins un des bits est 1.

  .. code-block:: python

     resultat = 5 | 3  # Résultat : 7 (101 | 011 = 111)

- **OU exclusif (``^``)** : Retourne 1 si les bits sont différents.

  .. code-block:: python

     resultat = 5 ^ 3  # Résultat : 6 (101 ^ 011 = 110)

- **Décalage à gauche (``<<``)** : Décale les bits vers la gauche en ajoutant des zéros à droite.

  .. code-block:: python

     resultat = 5 << 1  # Résultat : 10 (101 devient 1010)

- **Décalage à droite (``>>``)** : Décale les bits vers la droite en supprimant les bits les plus à droite.

  .. code-block:: python

     resultat = 5 >> 1  # Résultat : 2 (101 devient 10)

**Autres opérateurs**

Les chaînes de caractères peuvent être concaténées, répétées et utilisées avec diverses méthodes de manipulation de texte :
.. code-block:: python

    s1 = "Bonjour"
    s2 = "le monde"

    # Concaténation
    s3 = s1 + " " + s2  # "Bonjour le monde"

    # Répétition
    s4 = s1 * 3  # "BonjourBonjourBonjour"

    # Méthodes de chaîne de caractères
    s5 = s1.upper()  # "BONJOUR"
    s6 = s1.lower()  # "bonjour"


Cette section fournit une vue d'ensemble de tous les opérateurs Python, facilitant la compréhension de leur utilisation dans diverses expressions et leur priorité d'évaluation.
