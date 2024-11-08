
Programmation fonctionnelle
---------------------------

La programmation fonctionnelle est un paradigme qui traite le calcul comme l'évaluation de fonctions mathématiques et évite l'état mutable et les effets de bord. Python prend en charge la programmation fonctionnelle en permettant d'utiliser des fonctions comme objets de première classe, c'est-à-dire que les fonctions peuvent être passées en arguments, retournées par d'autres fonctions, et assignées à des variables.

**Caractéristiques de la Programmation Fonctionnelle**

1. **Fonctions de Première Classe** :
   Les fonctions peuvent être manipulées comme n'importe quel autre objet. Elles peuvent être passées en arguments, retournées par d'autres fonctions, ou assignées à des variables.

   .. code-block:: python

       def carre(x):
           return x * x

       def appliquer(f, x):
           return f(x)

       print(appliquer(carre, 5))  # Affiche 25

2. **Fonctions Anonymes (`lambda`)** :
   Les fonctions anonymes, ou `lambda`, permettent de créer de petites fonctions sans avoir besoin de les nommer.

   .. code-block:: python

       ajouter = lambda x, y: x + y
       print(ajouter(3, 4))  # Affiche 7

3. **Fonctions d'Ordre Supérieur** :
   Ce sont des fonctions qui prennent d'autres fonctions en argument ou retournent des fonctions. Cela permet de créer des abstractions et de réutiliser du code.

   .. code-block:: python

       def appliquer_deux_fois(f, x):
           return f(f(x))

       print(appliquer_deux_fois(carre, 3))  # Affiche 81

4. **Immutabilité** :
   La programmation fonctionnelle privilégie l'utilisation de structures de données immuables, ce qui réduit les effets de bord et facilite le raisonnement sur le code.

5. **Récursion** :
   Les fonctions peuvent s'appeler elles-mêmes pour résoudre des problèmes. La récursion est souvent utilisée en programmation fonctionnelle pour remplacer les boucles.

   .. code-block:: python

       def factorielle(n):
           if n == 0:
               return 1
           else:
               return n * factorielle(n - 1)

       print(factorielle(5))  # Affiche 120

**Outils et Modules de Programmation Fonctionnelle en Python**

Python fournit plusieurs outils et modules qui facilitent la programmation fonctionnelle :

- **`map()`** : Applique une fonction à tous les éléments d'un itérable et renvoie un nouvel itérable.

   .. code-block:: python

       nombres = [1, 2, 3, 4]
       resultats = list(map(carre, nombres))
       print(resultats)  # Affiche [1, 4, 9, 16]

- **`filter()`** : Filtre les éléments d'un itérable en appliquant une fonction de test qui renvoie `True` ou `False`.

   .. code-block:: python

       pairs = list(filter(lambda x: x % 2 == 0, nombres))
       print(pairs)  # Affiche [2, 4]

- **`reduce()`** : Réduit un itérable à une seule valeur en appliquant successivement une fonction. Ce module nécessite l'importation de `functools`.

   .. code-block:: python

       from functools import reduce

       somme = reduce(lambda x, y: x + y, nombres)
       print(somme)  # Affiche 10

**Avantages de la Programmation Fonctionnelle**

- **Simplicité et Lisibilité** : La séparation des préoccupations et l'utilisation de fonctions pures rendent le code plus facile à lire et à maintenir.
  
- **Tests Faciles** : Les fonctions pures sont plus simples à tester, car leur sortie dépend uniquement de leurs entrées.

- **Concurrence** : La programmation fonctionnelle facilite la gestion de la concurrence, car les fonctions n'ont pas d'état mutable.

**Inconvénients**

- **Performance** : La récursion peut être moins performante que les boucles pour certains problèmes, en particulier en raison de la surcharge d'appels de fonction.

- **Courbe d'Apprentissage** : Les développeurs venant de paradigmes impératifs peuvent trouver la transition vers la programmation fonctionnelle plus difficile.

La programmation fonctionnelle en Python offre un moyen puissant et flexible d'écrire du code clair et concis. En utilisant des fonctions de première classe, des fonctions anonymes, et des outils comme `map()`, `filter()`, et `reduce()`, les développeurs peuvent tirer parti des avantages de ce paradigme tout en profitant des capacités de Python.


Programmation orientée objet
----------------------------

La programmation orientée objet (POO) est un paradigme qui utilise des "objets" pour modéliser des entités du monde réel. Les objets combinent à la fois des données et des comportements, permettant ainsi une approche modulaire et réutilisable pour la conception de logiciels. Python prend en charge la POO de manière complète, offrant des mécanismes pour définir des classes, des objets, créer des instances, et utiliser l'héritage.

**Concepts Clés de la POO**

1. **Classes et Objets** :
   - Une classe est une structure qui définit un type d'objet, incluant des attributs (données) et des méthodes (comportements).
   - Un objet est une instance d'une classe. Chaque objet a ses propres valeurs d'attributs.

   .. code-block:: python

       class Voiture:
           def __init__(self, marque, modele):
               self.marque = marque
               self.modele = modele

           def demarrer(self):
               print("La {self.marque} {self.modele} démarre.")

       ma_voiture = Voiture("Toyota", "Corolla")
       ma_voiture.demarrer()  # Affiche "La Toyota Corolla démarre."


- **class** : Déclare une nouvelle classe.
- **self** : Représente l'instance actuelle.
- **__init__** : Initialise une nouvelle instance.

2. **Attributs** :
   - Les attributs sont des variables qui stockent des données relatives à un objet. Ils peuvent être définis à l'aide de `self` dans la méthode spéciale `__init__`.

3. **Méthodes** :
   - Les méthodes sont des fonctions définies à l'intérieur d'une classe qui décrivent les comportements d'un objet. Les méthodes doivent toujours inclure `self` comme premier paramètre pour faire référence à l'instance de l'objet.

4. **Héritage** :
   - L'héritage permet de créer une nouvelle classe (classe dérivée) à partir d'une classe existante (classe de base), en réutilisant les attributs et méthodes de la classe de base.

   .. code-block:: python

       class Vehicule:
           def demarrer(self):
               print("Le véhicule démarre.")

       class Moto(Vehicule):
           def faire_du_bruit(self):
               print("La moto fait vroom!")

       ma_moto = Moto()
       ma_moto.demarrer()  # Affiche "Le véhicule démarre."
       ma_moto.faire_du_bruit()  # Affiche "La moto fait vroom!"

5. **Polymorphisme** :
   - Le polymorphisme permet d'utiliser des méthodes ayant le même nom mais un comportement différent en fonction de l'objet. Cela permet de traiter des objets de classes différentes de manière uniforme.

   .. code-block:: python

       class Chat:
           def parler(self):
               print("Miaulement")

       class Chien:
           def parler(self):
               print("Aboiement")

       def faire_parler(animal):
           animal.parler()

       mon_chat = Chat()
       mon_chien = Chien()
       faire_parler(mon_chat)  # Affiche "Miaulement"
       faire_parler(mon_chien)  # Affiche "Aboiement"

6. **Encapsulation** :
   - L'encapsulation consiste à regrouper des données (attributs) et des comportements (méthodes) dans une classe tout en restreignant l'accès direct à certaines données. Les attributs peuvent être rendus privés en les préfixant avec un double underscore `__`.

   .. code-block:: python

       class CompteBancaire:
           def __init__(self, solde):
               self.__solde = solde  # Attribut privé

           def deposer(self, montant):
               self.__solde += montant

           def afficher_solde(self):
               print(f"Solde: {self.__solde}")

       compte = CompteBancaire(1000)
       compte.deposer(500)
       compte.afficher_solde()  # Affiche "Solde: 1500"
       # print(compte.__solde)  # Provoque une erreur

**Avantages de la Programmation Orientée Objet**

- **Modularité** : Le code est organisé en modules, ce qui facilite sa maintenance et sa réutilisation.
- **Réutilisation** : Les classes peuvent être réutilisées et étendues, ce qui réduit le besoin de duplication de code.
- **Abstraction** : Les détails d'implémentation sont cachés, permettant aux utilisateurs d'interagir avec les objets sans connaître leur fonctionnement interne.

**Inconvénients**

- **Complexité** : La POO peut introduire une complexité supplémentaire dans la conception et la compréhension du code, surtout pour les petits projets.
- **Performance** : L'utilisation intensive des classes et des objets peut parfois avoir un impact sur la performance, en raison de la surcharge associée à la gestion des objets.

La programmation orientée objet est un puissant paradigme de développement qui permet de créer des logiciels modulaires et réutilisables. En exploitant les concepts de classes, d'héritage, de polymorphisme et d'encapsulation, les développeurs peuvent créer des applications plus maintenables et plus faciles à comprendre.

Méthodes spéciales et surcharge d'opérateurs
--------------------------------------------

Les méthodes spéciales (ou "dunder") en Python, également appelées méthodes magiques, sont des fonctions définies dans les classes qui permettent de définir le comportement d'un objet en réponse à certaines opérations. Elles sont entourées de doubles underscores (par exemple, `__init__`). La surcharge d'opérateurs consiste à redéfinir le comportement des opérateurs (comme `+`, `-`, `*`, etc.) pour les objets personnalisés en utilisant ces méthodes spéciales.

Méthodes Spéciales Courantes
-----------------------------

1. **Constructeur (`__init__`)** :
   - La méthode `__init__` est appelée automatiquement lors de la création d'une instance d'une classe. Elle permet d'initialiser les attributs de l'objet.

   .. code-block:: python

       class Point:
           def __init__(self, x, y):
               self.x = x
               self.y = y

       p = Point(3, 4)
       print(p.x, p.y)  # Affiche "3 4"

2. **Représentation en chaîne (`__str__` et `__repr__`)** :
   - `__str__` définit la représentation en chaîne d'un objet pour les utilisateurs. `__repr__` est utilisé pour la représentation en chaîne pour le débogage et doit renvoyer une chaîne qui pourrait être utilisée pour recréer l'objet.

   .. code-block:: python

       class Personne:
           def __init__(self, nom):
               self.nom = nom

           def __str__(self):
               return f"Personne: {self.nom}"

           def __repr__(self):
               return f"Personne({self.nom!r})"

       p = Personne("Alice")
       print(p)  # Affiche "Personne: Alice"
       print(repr(p))  # Affiche "Personne('Alice')"

3. **Surcharge des opérateurs** :
   - Les opérateurs peuvent être surchargés en définissant des méthodes spéciales correspondantes.

   - **Addition (`__add__`)** :
     - La méthode `__add__` permet de définir le comportement de l'opérateur `+` pour les objets de votre classe.

     .. code-block:: python

         class NombreComplexe:
             def __init__(self, re, im):
                 self.re = re
                 self.im = im

             def __add__(self, other):
                 return NombreComplexe(self.re + other.re, self.im + other.im)

             def __str__(self):
                 return f"{self.re} + {self.im}i"

         z1 = NombreComplexe(1, 2)
         z2 = NombreComplexe(3, 4)
         z3 = z1 + z2
         print(z3)  # Affiche "4 + 6i"

   - **Égalité (`__eq__`)** :
     - La méthode `__eq__` permet de définir le comportement de l'opérateur `==` pour les objets de votre classe.

     .. code-block:: python

         class Point:
             def __init__(self, x, y):
                 self.x = x
                 self.y = y

             def __eq__(self, other):
                 return self.x == other.x and self.y == other.y

         p1 = Point(1, 2)
         p2 = Point(1, 2)
         p3 = Point(3, 4)

         print(p1 == p2)  # Affiche True
         print(p1 == p3)  # Affiche False

4. **Autres méthodes spéciales** :
   - `__len__` : Définit le comportement de la fonction `len()`.
   - `__getitem__` : Permet l'accès à un élément via des indices (par exemple, `obj[key]`).
   - `__setitem__` : Permet de définir un élément via des indices.
   - `__delitem__` : Permet de supprimer un élément via des indices.
   - `__iter__` : Rend un objet itérable en renvoyant un itérateur.
   - `__next__` : Définit le comportement de l'itérateur pour renvoyer l'élément suivant.

Exemple d'itérabilité personnalisée :

     .. code-block:: python

        class Compteur:
            def __init__(self, limite):
                self.limite = limite
                self.current = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.current < self.limite:
                    self.current += 1
                    return self.current
                else:
                    raise StopIteration

        compteur = Compteur(3)
        for nombre in compteur:
            print(nombre)  # Affiche 1, 2, 3

Générateurs
-----------

Les générateurs sont une fonctionnalité puissante de Python qui permet de créer des itérateurs de manière simple et efficace. Ils permettent de produire des séquences de valeurs sans avoir à les stocker toutes en mémoire, ce qui les rend particulièrement utiles pour gérer de grandes quantités de données ou des flux de données.

**Définition d'un Générateur**

Un générateur est une fonction qui utilise le mot-clé `yield` au lieu de `return`. Lorsqu'un générateur est appelé, il renvoie un itérateur qui peut être utilisé pour générer des valeurs une par une, plutôt que de calculer toutes les valeurs à l'avance.

Voici un exemple de générateur qui produit une séquence de nombres carrés :

.. code-block:: python

    def generate_squares(n):
        for i in range(n):
            yield i ** 2

**Utilisation d'un Générateur**

Pour utiliser un générateur, vous pouvez l'itérer avec une boucle `for`, ou utiliser la fonction `next()` pour obtenir les valeurs une à une.

.. code-block:: python

    squares = generate_squares(5)

    for square in squares:
        print(square)  # Affiche 0, 1, 4, 9, 16

    # Ou en utilisant next()
    squares = generate_squares(3)
    print(next(squares))  # Affiche 0
    print(next(squares))  # Affiche 1
    print(next(squares))  # Affiche 4
    # print(next(squares))  # Lève une exception StopIteration

**Avantages des Générateurs**

1. **Mémoire Efficace** :
   - Les générateurs ne chargent pas toutes les valeurs en mémoire, ce qui les rend particulièrement utiles pour travailler avec des ensembles de données volumineux.

2. **Exécution Paresseuse** :
   - Les générateurs ne calculent les valeurs que lorsque cela est nécessaire, ce qui peut améliorer les performances et réduire le temps d'exécution dans certains cas.

3. **Code Plus Lisible** :
   - Les générateurs permettent d'écrire du code plus clair et plus concis en remplaçant les classes d'itérateurs par des fonctions simples.

**Exemple de Générateur avec État**

Les générateurs peuvent également maintenir un état entre les appels grâce à leur nature. Voici un exemple d'un générateur qui produit une séquence infinie de nombres naturels :

.. code-block:: python

    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1

    counter = count_up_to(3)
    for number in counter:
        print(number)  # Affiche 1, 2, 3

Les générateurs sont un outil précieux en Python pour créer des itérateurs légers et efficaces. Ils facilitent le traitement des flux de données et permettent de conserver la mémoire tout en maintenant un code clair et facile à comprendre. Grâce aux générateurs, il est possible d'écrire des programmes qui gèrent de grandes quantités de données de manière efficace et élégante.
