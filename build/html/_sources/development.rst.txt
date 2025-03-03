.. -*- coding: utf-8 -*-

Développement
=============

Informations sur le développement de Python-OC-lettings-FR.

Prérequis
---------
- Python 3.x
- pip
- Un environnement virtuel (recommandé)

Installer les dépendances
-------------------------
Pour installer les dépendances nécessaires au développement, exécutez la commande suivante :

    pip install -r requirements.txt

Lancer les tests
----------------
Pour exécuter les tests unitaires et vérifier que tout fonctionne correctement, utilisez la commande suivante :

    pytest

Test de couverture :

    coverage run -m pytest

    coverage report

Créer un rapport Flake8
-----------------------
Pour créer un rapport Flake8,
remplacez la fonction `main` par la fonction `debug` dans le fichier `manage.py` (Lancez).

    python manage.py

`Cela va générer un rapport HTML dans votre navigateur.`

Bonnes pratiques
----------------
- **Convention de nommage** : Utilisez des noms de variables et de fonctions explicites.
- **Commentaire et documentation** : Documentez votre code avec des commentaires clairs et précis.
- **Revue de code** : Effectuez des revues de code régulières pour maintenir la qualité du code.

Contribuer au projet
--------------------
Si vous souhaitez contribuer au projet, veuillez suivre les étapes suivantes :

1. Fork le dépôt GitHub.
2. Clonez votre fork localement :
    git clone https://github.com/votre-utilisateur/Python-OC-lettings-FR.git

3. Créez une branche pour votre fonctionnalité ou correction :
    git checkout -b ma-nouvelle-fonctionnalite

4. Développez votre fonctionnalité et ajoutez des tests.
5. Poussez vos modifications et créez une Pull Request :
    git push origin ma-nouvelle-fonctionnalite

Merci de suivre les directives de contribution et de respecter les conventions de codage du projet.
