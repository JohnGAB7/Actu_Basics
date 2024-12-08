Calcul des annuités
===================

Une annuité est une série de paiements égaux effectués à intervalles réguliers sur une période de temps. Les annuités sont couramment utilisées pour les emprunts, les hypothèques, les plans de retraite, et les investissements. Cette section couvre les différents types d'annuités, leurs formules de calcul, et des exemples concrets.

Types d'annuités
----------------

Il existe plusieurs types d'annuités, notamment les annuités ordinaires, les annuités anticipées, les annuités perpétuelles, et les annuités différées.

### Annuité ordinaire

Les paiements sont effectués à la fin de chaque période.

### Annuité anticipée

Les paiements sont effectués au début de chaque période.

### Annuité perpétuelle

Les paiements sont effectués indéfiniment.

### Annuité différée

Les paiements commencent après une certaine période de différé.

Formules de calcul des annuités
-------------------------------

### Valeur actuelle d'une annuité ordinaire

La valeur actuelle d'une annuité ordinaire (VA) est la somme des valeurs actuelles de tous les paiements futurs.

.. math::

    VA = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right)

où:
- *VA* : Valeur actuelle de l'annuité
- *PMT* : Paiement périodique
- *r* : Taux d'intérêt par période
- *n* : Nombre de périodes

### Valeur actuelle d'une annuité anticipée

La valeur actuelle d'une annuité anticipée est calculée en ajustant la valeur actuelle d'une annuité ordinaire.

.. math::

    VA = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right) \cdot (1 + r)

### Valeur future d'une annuité ordinaire

La valeur future d'une annuité ordinaire (VF) est la somme des valeurs futures de tous les paiements effectués.

.. math::

    VF = PMT \cdot \left( \frac{(1 + r)^n - 1}{r} \right)

où:
- *VF* : Valeur future de l'annuité
- *PMT* : Paiement périodique
- *r* : Taux d'intérêt par période
- *n* : Nombre de périodes

### Valeur future d'une annuité anticipée

La valeur future d'une annuité anticipée est calculée en ajustant la valeur future d'une annuité ordinaire.

.. math::

    VF = PMT \cdot \left( \frac{(1 + r)^n - 1}{r} \right) \cdot (1 + r)

### Valeur actuelle d'une annuité perpétuelle

Une annuité perpétuelle est une série de paiements qui continue indéfiniment. Sa valeur actuelle est calculée comme suit :

.. math::

    VA = \frac{PMT}{r}

Exemples de calculs des annuités
--------------------------------

### Exemple de calcul de la valeur actuelle d'une annuité ordinaire

Supposons qu'un investisseur souhaite connaître la valeur actuelle d'une série de paiements annuels de 1 000 € sur 10 ans, avec un taux d'intérêt annuel de 5 %.

.. code-block:: python

    # Calcul de la valeur actuelle d'une annuité ordinaire
    paiement_periodique = 1000
    taux_interet = 0.05
    nombre_periodes = 10

    valeur_actuelle_annuite = paiement_periodique * ((1 - (1 + taux_interet) ** -nombre_periodes) / taux_interet)
    print(f'Valeur Actuelle de l\'Annuite: {valeur_actuelle_annuite}')

### Exemple de calcul de la valeur future d'une annuité ordinaire

Supposons qu'un investisseur souhaite connaître la valeur future d'une série de paiements annuels de 1 000 € sur 10 ans, avec un taux d'intérêt annuel de 5 %.

.. code-block:: python

    # Calcul de la valeur future d'une annuité ordinaire
    paiement_periodique = 1000
    taux_interet = 0.05
    nombre_periodes = 10

    valeur_future_annuite = paiement_periodique * ((1 + taux_interet) ** nombre_periodes - 1) / taux_interet
    print(f'Valeur Future de l\'Annuite: {valeur_future_annuite}')

### Exemple de calcul de la valeur actuelle d'une annuité perpétuelle

Supposons qu'un investisseur souhaite connaître la valeur actuelle d'une série de paiements annuels de 1 000 € indéfiniment, avec un taux d'intérêt annuel de 5 %.

.. code-block:: python

    # Calcul de la valeur actuelle d'une annuité perpétuelle
    paiement_periodique = 1000
    taux_interet = 0.05

    valeur_actuelle_annuite_perpetuelle = paiement_periodique / taux_interet
    print(f'Valeur Actuelle de l\'Annuite Perpetuelle: {valeur_actuelle_annuite_perpetuelle}')

Calculs d'annuités avec tables de mortalité
--------------------------------------------

Dans certaines applications actuarielles, les calculs d'annuités prennent en compte la probabilité de survie de l'individu, basée sur des tables de mortalité.

### Exemple de calcul de la valeur actuelle d'une annuité viagère

Supposons qu'un individu souhaite connaître la valeur actuelle d'une rente viagère de 10 000 € par an, avec un taux d'intérêt de 3 %, en utilisant une table de mortalité simplifiée.

.. code-block:: python

    import numpy as np

    # Données d'exemple
    age = 65
    paiement_annuel = 10000
    taux_interet = 0.03
    esperance_vie = 20  # Hypothèse simplifiée

    # Calcul de la valeur actuelle d'une rente viagère
    valeur_actuelle_rente = paiement_annuel * ((1 - (1 + taux_interet) ** -esperance_vie) / taux_interet)
    print(f'Valeur Actuelle de la Rente Viagère: {valeur_actuelle_rente}')

Ces exemples montrent comment calculer les différentes valeurs des annuités en utilisant des formules mathématiques et des exemples pratiques en Python. La compréhension de ces concepts est essentielle pour les professionnels de la finance, les actuaires, et toute personne impliquée dans les décisions d'investissement ou de planification financière.
