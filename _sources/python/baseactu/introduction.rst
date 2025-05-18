Rappels Clés : Mesures de l'intérêt
===============================

Introduction
--------------
Les mesures d'intérêt jouent un rôle fondamental dans la finance et l'économie. Comprendre les différents types d'intérêt et savoir calculer la valeur des investissements est essentiel pour les étudiants en actuariat.

L'intérêt
-----------
L'intérêt est la compensation accordée au détenteur d'un capital qui accepte de s'en dessaisir temporairement pour le mettre à la disposition d'une personne physique ou morale.

Le taux d'intérêt effectif
----------------------------
Le taux d'intérêt effectif :math:`i` est le montant d'intérêt produit par le placement d'un capital unitaire (1 €) sur une période (i.e. par unité de temps).

Fonction d'accumulation et valeur accumulée
---------------------------------------------
Pour un placement d'une valeur initiale de 1 €, soit la fonction d'accumulation :math:`a(t)`.

- :math:`a(0) = 1`
- :math:`a(t)` est croissante (si :math:`i > 0`) et continue lorsque l'intérêt est accumulé de manière continue.
- Aussi, :math:`i = a(1) - 1 = a(1) - a(0)` et :math:`a(1) = 1 + i`.

Pour un placement d'une valeur initiale :math:`K`, la valeur accumulée :math:`A(t)` est donnée par :math:`A(t) = K a(t)`.

- Il vient :math:`i = \frac{a(1) - a(0)}{a(0)} = \frac{A(1) - A(0)}{A(0)} = \frac{I_1}{A(0)}`,
  où :math:`I_1` est le montant d'intérêt produit au cours de la première période. Ainsi, le taux d'intérêt effectif :math:`i` est le rapport entre le montant d'intérêt produit au cours de la première période :math:`I_1` et le montant initial du placement :math:`A(0)`.

Le taux d'intérêt effectif :math:`i_t`
---------------------------------------
Le taux d'intérêt effectif peut varier avec le temps. Ainsi, le taux d'intérêt effectif relatif à l'intervalle de temps unitaire (période) \([t - 1; t]\) est dénoté :math:`i_t`. Celui-ci est donné par

- :math:`i_t = \frac{I_t}{A(t - 1)} = \frac{A(t) - A(t - 1)}{A(t - 1)} = \frac{a(t) - a(t - 1)}{a(t - 1)}`.

Comportement de :math:`a(t)`
-----------------------------
Il existe deux types d'intérêt :

- Intérêt simple : Un placement est dit à intérêts simples si les intérêts qu'il produit sont proportionnels à la durée du placement.
- Intérêt composé : Un placement est dit à intérêts composés si les intérêts qu'il produit sont périodiquement capitalisés, c'est-à-dire incorporés au capital pour produire eux-mêmes des intérêts.

Intérêt simple
-----------------
La valeur accumulée en :math:`t` par le placement s'élève à :math:`a(t) = 1 + it ; t \geq 0`.

- Les intérêts ne sont pas incorporés périodiquement au capital pour produire eux-mêmes des intérêts.

Le taux d'intérêt effectif :math:`i_t` est donné par

- :math:`i_t = \frac{a(t) - a(t - 1)}{a(t - 1)} = \frac{i}{1 + i (t - 1)}`.

Ainsi, en intérêt simple, le taux d'intérêt effectif varie d'une année à l'autre. Celui-ci décroît au cours du temps. En général, seuls les placements de courte durée (inférieure à un an) sont à intérêts simples.

Intérêt composé
------------------
La valeur accumulée en :math:`t` par le placement s'élève à :math:`a(t) = (1 + i)^t ; t \geq 0`.

- Les intérêts sont incorporés périodiquement au capital pour produire eux-mêmes des intérêts.

Le taux d'intérêt effectif :math:`i_t` est donné par

- :math:`i_t = \frac{a(t) - a(t - 1)}{a(t - 1)} = i`.

Ainsi, en intérêt composé, le taux d'intérêt effectif reste constant au cours du temps. En général, les placements dont la durée est supérieure à une année sont toujours à intérêt composé.

Exercice 1
------------
Soit :math:`K = 1000` €. Calculer les valeurs de :math:`A(t)` en :math:`t = 3` mois, :math:`t = 1` an et :math:`t = 3` ans pour un taux d'intérêt annuel simple de 8%. Refaire les mêmes calculs avec un taux d'intérêt annuel composé de 8%.

.. code-block:: python

    def simple_interest(K, r, t):
        return K * (1 + r * t)

    def compound_interest(K, r, t):
        return K * (1 + r)**t

    # Parameters
    K = 1000
    annual_rate = 0.08

    # Simple Interest
    A_simple_3_months = simple_interest(K, annual_rate, 3/12)
    A_simple_1_year = simple_interest(K, annual_rate, 1)
    A_simple_3_years = simple_interest(K, annual_rate, 3)

    # Compound Interest
    A_compound_3_months = compound_interest(K, annual_rate, 3/12)
    A_compound_1_year = compound_interest(K, annual_rate, 1)
    A_compound_3_years = compound_interest(K, annual_rate, 3)

    print("Simple Interest - 3 Months:", A_simple_3_months)
    print("Simple Interest - 1 Year:", A_simple_1_year)
    print("Simple Interest - 3 Years:", A_simple_3_years)
    print("Compound Interest - 3 Months:", A_compound_3_months)
    print("Compound Interest - 1 Year:", A_compound_1_year)
    print("Compound Interest - 3 Years:", A_compound_3_years)

Valeur présente (valeur actualisée)
-------------------------------------
Désormais, les placements considérés seront principalement à intérêts composés (sauf indication contraire). La valeur en :math:`t = 1` de :math:`1` € investi en :math:`t = 0` au taux :math:`i` est :math:`a(1) = 1 + i`.

- En pratique, :math:`1 + i` est appelé facteur de capitalisation et est noté :math:`u`.

Ainsi, la valeur en :math:`t` de :math:`1` € investi en :math:`t = 0` au taux :math:`i` est

- :math:`a(t) = (1 + i)^t = u^t`.

Inversement, le capital qu'il faut placer en :math:`t = 0` au taux :math:`i` pour que sa valeur accumulée en :math:`t = 1` soit de :math:`1` € est :math:`1 / (1+i)`.

- En pratique, :math:`1 / (1+i)` est appelé facteur d'actualisation et est noté :math:`v`.

Aussi, la valeur présente de :math:`1` € au temps :math:`t` est :math:`v^t`.

Exercice 2
------------
Soit un taux d'intérêt annuel :math:`i = 5\%`. Pierre investit :math:`K` le 6/10/2014. Sachant qu'au 6/01/2021 Pierre aura 30000 €, trouver :math:`K` si :

(a) Le placement est à intérêts composés.
(b) Le placement est à intérêts simples.
(c) Le placement est à intérêts composés jusqu'au 6/10/2020 et à intérêts simples pour la période restante.

.. code-block:: python

    from datetime import date

    def years_between(d1, d2):
        return (d2 - d1).days / 365.25

    def present_value_future_compound_value(FV, r, t):
        return FV / (1 + r)**t

    # Dates and Parameters
    invest_date = date(2014, 10, 6)
    future_date = date(2021, 1, 6)
    future_value = 30000
    annual_rate = 0.05

    # Calculate time in years
    time_years = years_between(invest_date, future_date)

    # Calculate Present Value for Compounded Interest
    PV_compound = present_value_future_compound_value(future_value, annual_rate, time_years)

    print("Present Value for Compounded Interest:", PV_compound)

Taux d'intérêt nominal
-------------------------
Le taux d'intérêt nominal est le taux d'intérêt annuel annoncé, qui ne tient pas compte de la capitalisation des intérêts. Lorsque les intérêts sont capitalisés plusieurs fois par an, le taux d'intérêt effectif est plus élevé que le taux nominal.

La relation entre le taux d'intérêt nominal :math:`i_{nom}` et le taux d'intérêt effectif :math:`i_{eff}` pour une capitalisation :math:`m` fois par an est donnée par :

.. math::

    (1 + i_{eff}) = (1 + i_{nom} / m)^m

Exercice 3
----------
Soit :math:`K = 1000` €. Calculer les valeurs de :math:`A(t)` en :math:`t = 1` an pour :

(a) Un taux d'intérêt annuel :math:`i = 6%`.
(b) Un taux d'intérêt mensuel :math:`i = 0.5%`.

.. code-block:: python

    def nominal_to_effective(nominal_rate, periods):
        return (1 + nominal_rate / periods)**periods - 1

    K = 1000
    annual_rate = 0.06
    monthly_rate = 0.005

    A_annual = K * (1 + annual_rate)
    A_monthly = K * (1 + nominal_to_effective(monthly_rate, 12))

    print("Annual Interest:", A_annual)
    print("Monthly Interest:", A_monthly)

Taux d'escompte effectif
-------------------------
Le taux d'escompte effectif, noté :math:`d`, est utilisé pour calculer le montant net que reçoit un investisseur lorsque les intérêts sont payés en avance. L'escompte est une réduction appliquée à un montant futur pour obtenir sa valeur présente.

### Formule
La relation entre le taux d'escompte :math:`d` et le taux d'intérêt effectif :math:`i` est :

.. math::

    d = \frac{i}{1 + i}

Inversement, pour obtenir le taux d'intérêt effectif à partir du taux d'escompte :

.. math::

    i = \frac{d}{1 - d}

Exemple : Si un placement offre un taux d'intérêt effectif de 5%, le taux d'escompte correspondant est :

.. math::

    d = \frac{0.05}{1 + 0.05} = 0.04762 \quad \text{(ou 4,762%)}

Taux d'escompte nominal
----------------------------

Le taux d'escompte nominal, noté :math:`d(m)`, est utilisé lorsque l'escompte est fractionné. Par exemple, si l'escompte est appliqué mensuellement, le taux d'escompte nominal mensuel est donné par :

.. math::

    d(m) = m \left[1 - (1 - d)^{1/m}\right]

Exercice 4
------------
Soit un taux d'escompte effectif annuel de 12%. Calculer le taux d'escompte nominal mensuel correspondant et le taux d'intérêt effectif annuel équivalent.

.. code-block:: python

    def effective_to_nominal_discount(effective_rate, periods):
        return periods * (1 - (1 - effective_rate)**(1 / periods))

    def discount_to_interest(discount_rate):
        return discount_rate / (1 - discount_rate)

    # Parameters
    annual_effective_discount = 0.12
    periods = 12

    # Calculate nominal discount rate and equivalent interest rate
    monthly_nominal_discount = effective_to_nominal_discount(annual_effective_discount, periods)
    annual_effective_interest = discount_to_interest(annual_effective_discount)

    print("Monthly Nominal Discount Rate:", monthly_nominal_discount)
    print("Equivalent Annual Effective Interest Rate:", annual_effective_interest)

Force d'intérêt et d'escompte
------------------------------
La force d'intérêt, notée :math:`\delta`, est une mesure continue de la croissance d'un investissement. Elle est particulièrement utile lorsque les intérêts sont composés en continu.

La relation entre la force d'intérêt et le taux d'intérêt effectif est donnée par :

.. math::

    \delta = \ln(1 + i)

De manière similaire, la force d'escompte est utilisée pour les calculs de valeur présente lorsque les escomptes sont appliqués de manière continue. La relation est :

.. math::

    \delta = -\ln(1 - d)

Exemple : Si le taux d'intérêt effectif est de 5%, la force d'intérêt est :

.. math::

    \delta = \ln(1 + 0.05) \approx 0.04879

Exercice 5
------------
Soit un taux d'intérêt effectif :math:`i = 5%`. Trouver le taux d'intérêt nominal :math:`i (m)` équivalent pour :math:`m = 2`, :math:`6`, :math:`12`, :math:`52`, :math:`365`.

.. code-block:: python

    import math

    def effective_to_nominal(effective_rate, periods):
        return periods * (math.exp(effective_rate / periods) - 1)

    # Parameters
    effective_rate = 0.05
    periods_list = [2, 6, 12, 52, 365]

    # Calculate nominal rates
    nominal_rates = {periods: effective_to_nominal(effective_rate, periods) for periods in periods_list}

    for periods, nominal_rate in nominal_rates.items():
        print(f"Nominal Rate for {periods} periods: {nominal_rate:.6f}")

Conclusion
------------
La compréhension des mesures d'intérêt est fondamentale pour les actuaires et les professionnels de la finance. Les concepts d'intérêt simple et composé, la valeur présente, ainsi que les taux nominaux et effectifs, sont des outils essentiels pour évaluer et gérer les investissements. Les exercices pratiques en Python permettent d'appliquer ces concepts théoriques à des situations réelles, renforçant ainsi la compréhension et la compétence des étudiants en actuariat.
