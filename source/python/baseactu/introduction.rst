Rappels Clés
===============

Les mathématiques financières sont une branche des mathématiques appliquées qui traite des problèmes liés aux marchés financiers, aux investissements, aux emprunts et à la gestion des risques. Voici quelques concepts clés :

Valeur actuelle et valeur future
------------------------------------

La valeur actuelle (VA) est la valeur aujourd'hui d'une somme d'argent qui sera reçue ou payée à une date future. La valeur future (VF) est la valeur à une date future d'une somme d'argent investie ou empruntée aujourd'hui.

**Formules de base**

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

**Exemple de calcul**

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

**Intérêts simples**

Les intérêts simples sont calculés uniquement sur le montant initial investi ou emprunté.

.. math::

    I_{\text{simple}} = P \cdot r \cdot t

où:

-   *I_simple* : Intérêts simples
-   *P* : Principal (montant initial)
-   *r* : Taux d'intérêt
-   *t* : Temps

**Intérêts composés**

Les intérêts composés sont calculés sur le montant initial ainsi que sur les intérêts accumulés des périodes précédentes.

.. math::

    I_{\text{compose}} = P \cdot (1 + r)^t - P

où:

-   *I_compose* : Intérêts composés
-   *P* : Principal (montant initial)
-   *r* : Taux d'intérêt
-   *t* : Temps

**Exemple de calcul**

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

    (1 + r_{\text{effectif}}) = \left(1 + \frac{r_{\text{nominal}}}{m}\right)^m

où:

-   *r_nominal* : Taux d'intérêt nominal
-   *r_effectif* : Taux d'intérêt effectif
-   *m* : Nombre de périodes de capitalisation par an

**Exemple de calcul**

.. code-block:: python

    # Calcul du taux d'intérêt effectif
    taux_nominal = 0.06
    periodes_par_an = 4

    taux_effectif = (1 + taux_nominal / periodes_par_an) ** periodes_par_an - 1
    print(f'Taux d\'Intérêt Effectif: {taux_effectif}')

Taux d'escompte nominal et taux d'escompte effectif
--------------------------------------------------------

**Taux d'escompte nominal**

Le taux d'escompte nominal est le taux utilisé pour calculer les escomptes sur une base annuelle sans tenir compte de la fréquence de l'escompte.

### Taux d'escompte effectif

Le taux d'escompte effectif prend en compte la fréquence de l'escompte, reflétant ainsi le taux réel appliqué sur une période donnée.

La relation entre le taux d'escompte nominal (d_nominal) et le taux d'escompte effectif (d_effectif) est donnée par :

.. math::

    (1 - d_{\text{effectif}}) = \left(1 - \frac{d_{\text{nominal}}}{m}\right)^m

où:

-   *d_nominal* : Taux d'escompte nominal
-   *d_effectif* : Taux d'escompte effectif
-   *m* : Nombre de périodes d'escompte par an

**Exemple de calcul**

.. code-block:: python

    # Calcul du taux d'escompte effectif
    taux_escompte_nominal = 0.06
    periodes_par_an = 4

    taux_escompte_effectif = 1 - (1 - taux_escompte_nominal / periodes_par_an) ** periodes_par_an
    print(f'Taux d\'Escompte Effectif: {taux_escompte_effectif}')

.. Calcul des annuités
.. ===================

.. Une annuité est une série de paiements égaux effectués à intervalles réguliers sur une période de temps. Les calculs d'annuités sont couramment utilisés pour les emprunts, les hypothèques et les investissements.

.. Annuités ordinaires et annuités anticipées
.. ------------------------------------------

.. Il existe deux types d'annuités : les annuités ordinaires (paiements effectués à la fin de chaque période) et les annuités anticipées (paiements effectués au début de chaque période).

.. ### Formules de base

.. La valeur actuelle d'une annuité ordinaire est :

.. .. math::

..     VA_{\text{annuite}} = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right)

.. La valeur actuelle d'une annuité anticipée est :

.. .. math::

..     VA_{\text{annuite}} = PMT \cdot \left( \frac{1 - (1 + r)^{-n}}{r} \right) \cdot (1 + r)

.. où:
.. - *VA_{\text{annuite}}* : Valeur actuelle de l'annuité
.. - *PMT* : Paiement périodique
.. - *r* : Taux d'intérêt par période
.. - *n* : Nombre de périodes

.. **Exemple de calcul**

.. .. code-block:: python

..     # Calcul de la valeur actuelle d'une annuité ordinaire
..     paiement_periodique = 1000
..     taux_interet = 0.05
..     nombre_periodes = 10

..     valeur_actuelle_annuite = paiement_periodique * ((1 - (1 + taux_interet) ** -nombre_periodes) / taux_interet)
..     print(f'Valeur Actuelle de l\'Annuite: {valeur_actuelle_annuite}')

.. Rentes viagères
.. ===============

.. Une rente viagère est une série de paiements effectués régulièrement à une personne jusqu'à son décès. Les rentes viagères sont utilisées pour les plans de retraite, les assurances vie, et les régimes de pension. Cette section couvre les types de rentes viagères, leurs formules de calcul, et des exemples concrets.

.. Types de rentes viagères
.. -------------------------

.. Il existe plusieurs types de rentes viagères, notamment les rentes viagères simples, les rentes viagères réversibles, et les rentes viagères différées.

.. ### Rente viagère simple

.. Les paiements sont effectués régulièrement à une personne jusqu'à son décès.

.. ### Rente viagère réversible

.. Les paiements sont effectués à une personne et continuent après son décès à une autre personne désignée (bénéficiaire), souvent à un taux réduit.

.. ### Rente viagère différée

.. Les paiements commencent après une certaine période de différé et continuent jusqu'au décès de l'ass