# ACTU-BASICS

Site documentation de la chaine educative **ACTU-BASICS**
(statistiques, probabilites, actuariat) : *Eveiller par les chiffres* -
*Enlightening through numbers*.

Site en ligne : https://johngab7.github.io/Actu_Basics/

## Contenu

- **Parcours Actuariat** (A0 a A9, 11 modules)
- **Niveau 1 Statistiques** (23 lecons publiees)
- **Fiches telechargeables** (PDF, tableurs, R, Python)
- **References techniques** (Python, R, SQL, SAS, MATLAB, Julia)

## Construire le site localement

```bash
pip install sphinx pydata-sphinx-theme sphinx-design sphinx-tabs numpydoc
sphinx-build -b html source build/html
```

## Publication (pas de GitHub Actions)

Le HTML est construit en local puis commite dans `docs/` avec un
fichier `.nojekyll`. GitHub Pages est configure pour servir le dossier
`/docs` de la branche `main` (Settings > Pages > Deploy from a branch
> `main` / `/docs`). Aucun workflow Actions n'est utilise, ce qui
preserve les credits.

## Mise a jour du site

1. Modifier les fichiers `.rst` dans `source/`.
2. Lancer `sphinx-build -b html source build/html`.
3. Synchroniser : `rm -rf docs && mkdir docs && cp -r build/html/. docs/ && touch docs/.nojekyll`.
4. Commiter la source et `docs/` ensemble, pousser sur `main`.

## Licence et credits

Projet ACTU-BASICS par John GABARY. Depot miroir du programme editorial :
https://github.com/johngab7/le-monde-en-chiffres
