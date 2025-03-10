#!/bin/bash

# Chemins des répertoires
CONFIG_DIR="./config"
EXAMPLES_DIR="./config_samples"

# Création du répertoire config s'il n'existe pas
if [ ! -d "$CONFIG_DIR" ]; then
    mkdir "$CONFIG_DIR"
    echo "Répertoire $CONFIG_DIR créé."
fi

# Copie des fichiers de configuration depuis config_examples
cp "$EXAMPLES_DIR/config.ini.sample" "$CONFIG_DIR/config.ini"
cp "$EXAMPLES_DIR/logging.ini.sample" "$CONFIG_DIR/logging.ini"

echo "Fichiers de configuration copiés dans $CONFIG_DIR."