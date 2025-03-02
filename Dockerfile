# Utiliser une image de base Python
FROM python:3.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du répertoire local dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application va fonctionner
EXPOSE 8000

# Définir la commande de démarrage de l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
