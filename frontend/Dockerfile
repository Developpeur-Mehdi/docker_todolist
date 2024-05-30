FROM node:18.19

WORKDIR /app

# Copier les fichiers de dépendances avant d'exécuter npm install
COPY frontend/package*.json ./

# Installer Angular CLI globalement
RUN npm install -g @angular/cli

# Installer les dépendances du projet
RUN npm install

# Copier tous les fichiers du projet
COPY frontend/ ./

# Commande pour démarrer l'application Angular
CMD ["ng", "serve", "--host", "0.0.0.0"]

