# Utiliser une image Python de base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port de l'application
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
