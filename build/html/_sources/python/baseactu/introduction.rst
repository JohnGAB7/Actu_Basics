Rappels Clés
=======================================

Les mathématiques financières sont une branche des mathématiques appliquées qui traite des problèmes liés aux marchés financiers, aux investissements, aux emprunts et à la gestion des risques. Voici quelques concepts clés :

Valeur actuelle et valeur future
-----------------------------------

La valeur actuelle (VA) est la valeur aujourd'hui d'une somme d'argent qui sera reçue ou payée à une date future. La valeur future (VF) est la valeur à une date future d'une somme d'argent investie ou empruntée aujourd'hui.

### Formules de base

La formule de la valeur future est :
.. math::

    VF = VA \cdot (1 + r)^n

La formule de la valeur actuelle est :
.. math::

    VA = \frac{VF}{(1 + r)^n}

où:
-   *VF* : Valeur future
-   *VA* : Valeur actuelle
-   *r* : Taux d'intérêt par période
-   *n* : Nombre de périodes

### Exemple de calcul

.. code-block:: python

    # Calcul de la valeur future
    valeur_actuelle = 1000
    taux_interet = 0.05
    nombre_periodes = 10

    valeur_future = valeur_actuelle * (1 + taux_interet) ** nombre_periodes
    print(f'Valeur Future: {valeur_future}')

Intérêts simples et composés
--------------------------------

Les intérêts peuvent être calculés de deux manières : simples ou composés.

### Intérêts simples

Les intérêts simples sont calculés uniquement sur le montant initial investi ou emprunté.

.. math::

    I_{simple} = P \cdot r \cdot t

où:
-   *I_{simple}* : Intérêts simples
-   *P* : Principal (montant initial)
-   *r* : Taux d'intérêt
-   *t* : Temps

### Intérêts composés

Les intérêts composés sont calculés sur le montant initial ainsi que sur les intérêts accumulés des périodes précédentes.

.. math::

    I_{compose} = P \cdot (1 + r)^t - P

où:
-   *I_{compose}* : Intérêts composés
-   *P* : Principal (montant initial)
-   *r* : Taux d'intérêt
-   *t* : Temps

### Exemple de calcul

.. code-block:: python

    # Calcul des intérêts simples et composés
    principal = 1000
    taux_interet = 0.05
    temps = 10

    interets_simples = principal * taux_interet * temps
    interets_composes = principal * ((1 + taux_interet) ** temps - 1)

    print(f'Intérêts Simples: {interets_simples}')
    print(f'Intérêts Composés: {interets_composes}')

Taux d'intérêt nominal et taux d'intérêt effectif
-----------------------------------------------------

### Taux d'intérêt nominal

Le taux d'intérêt nominal est le taux d'intérêt annuel indiqué qui ne prend pas en compte la capitalisation des intérêts. C'est le taux que l'on voit le plus souvent dans les publicités bancaires.

### Taux d'intérêt effectif

Le taux d'intérêt effectif, ou taux annuel effectif global (TAEG), prend en compte l'effet de la capitalisation des intérêts. Il représente le taux réel appliqué sur une période donnée.

La relation entre le taux nominal (r_nominal) et le taux effectif (r_effectif) est donnée par :
.. math::

    (1 + r_{effectif}) = (1 + \frac{r_{nominal}}{m})^m

où:
-   *r_{nominal}* : Taux d'intérêt nominal
-   *r_{effectif}* : Taux d'intérêt effectif
-   *m* : Nombre de périodes de capitalisation par an

### Exemple de calcul

.. code-block:: python

    # Calcul du taux d'intérêt effectif
    taux_nominal = 0.06
    periodes_par_an = 4

    taux_effectif = (1 + taux_nominal / periodes_par_an) ** periodes_par_an - 1
    print(f'Taux d\'Intérêt Effectif: {taux_effectif}')

Taux d'escompte nominal et taux d'escompte effectif
-------------------------------------------------------

### Taux d'escompte nominal

Le taux d'escompte nominal est le taux utilisé pour calculer les escomptes sur une base annuelle sans tenir compte de la fréquence de l'escompte.

### Taux d'escompte effectif

Le taux d'escompte effectif prend en compte la fréquence de l'escompte, reflétant ainsi le taux réel appliqué sur une période donnée.

La relation entre le taux d'escompte nominal (d_nominal) et le taux d'escompte effectif (d_effectif) est donnée par :
.. math::

    (1 - d_{effectif}) = (1 - \frac{d_{nominal}}{m})^m

où:
-   *d_{nominal}* : Taux d'escompte nominal
-   *d_{effectif}* : Taux d'escompte effectif
-   *m* : Nombre de périodes d'escompte par an

### Exemple de calcul

.. code-block:: python

    # Calcul du taux d'escompte effectif
    taux_escompte_nominal = 0.06
    periodes_par_an = 4

    taux_escompte_effectif = 1 - (1 - taux_escompte_nominal / periodes_par_an) ** periodes_par_an
    print('Taux d\'Escompte Effectif: {taux_escompte_effectif}')

.. Calcul des annuités
.. =====================

.. Une annuité est une série de paiements égaux effectués à intervalles réguliers sur une période de temps. Les calculs d'annuités sont couramment utilisés pour les emprunts, les hypothèques et les investissements.

.. Annuités ordinaires et annuités anticipées
.. --------------------------------------------

.. Il existe deux types d'annuités : les annuités ordinaires (paiements effectués à la fin de chaque période) et les annuités anticipées (paiements effectués au début de chaque période).

.. ### Formules de base

.. La valeur actuelle d'une annuité ordinaire est :
.. .. math::

..     VA_{annuite} = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right)

.. La valeur actuelle d'une annuité anticipée est :
.. .. math::

..     VA_{annuite} = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right) \cdot (1 + r)

.. où:
.. - *VA_{annuite}* : Valeur actuelle de l'annuité
.. - *PMT* : Paiement périodique
.. - *r* : Taux d'intérêt par période
.. - *n* : Nombre de périodes

.. ### Exemple de calcul

.. .. code-block:: python

..     # Calcul de la valeur actuelle d'une annuité ordinaire
..     paiement_periodique = 1000
..     taux_interet = 0.05
..     nombre_periodes = 10

..     valeur_actuelle_annuite = paiement_periodique * ((1 - (1 + taux_interet) ** -nombre_periodes) / taux_interet)
..     print('Valeur Actuelle de l\'Annuite: {valeur_actuelle_annuite}')

.. Rentes viagères
.. =================

.. Une rente viagère est une série de paiements effectués régulièrement à une personne jusqu'à son décès. Les calculs de rentes viagères sont utilisés pour les plans de retraite et les assurances vie.

.. ### Formules de base

.. La valeur actuelle d'une rente viagère peut être calculée en utilisant une table de mortalité et les probabilités de survie.

.. ### Exemple de calcul

.. .. code-block:: python

..     import numpy as np

..     # Données d'exemple
..     age = 65
..     paiement_annuel = 10000
..     taux_interet = 0.03
..     esperance_vie = 20  # Hypothèse simplifiée

..     # Calcul de la valeur actuelle d'une rente viagère
..     valeur_actuelle_rente = paiement_annuel * ((1 - (1 + taux_interet) ** -esperance_vie) / taux_interet)
..     print(f'Valeur Actuelle de la Rente Viagère: {valeur_actuelle_rente}')

.. Ces rappels de mathématiques financières, ainsi que les calculs des taux d'intérêt, des taux d'escompte, des annuités, et des rentes viagères sont essentiels pour comprendre les principes de base de l'actuariat et leur application dans les domaines des assurances et des finances.
