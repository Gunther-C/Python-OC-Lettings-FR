.. -*- coding: utf-8 -*-

Utilisation
===========

Instructions d'utilisation pour Python-OC-lettings-FR.

Configuration initiale
----------------------
Pour configurer l'application après l'installation, suivez les étapes suivantes :

1. Ouvrez le fichier de configuration `settings.py` et ajustez les paramètres selon vos besoins.
2. Créez un super utilisateur pour accéder à l'interface d'administration :

    python manage.py createsuperuser

Lancer l'application
---------------------
Pour lancer l'application, utilisez la commande suivante :

    python manage.py runserver

Accéder à l'application
-----------------------
Une fois le serveur en cours d'exécution, vous pouvez accéder à l'application en ouvrant un navigateur
et en naviguant à l'adresse suivante :

    http://127.0.0.1:8000/

Fonctionnalités principales
----------------------------
- **Gestion des locations** : Créez, modifiez et supprimez des annonces de locations.
- **Gestion des utilisateurs** : Gérez les profils d'utilisateurs et les autorisations.
- **Interface d'administration** : Utilisez l'interface d'administration pour gérer l'ensemble du site.
