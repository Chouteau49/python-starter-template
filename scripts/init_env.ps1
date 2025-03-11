# Chemins des répertoires
$CONFIG_DIR = "./config"
$EXAMPLES_DIR = "./config_samples"

# Création du répertoire config s'il n'existe pas
if (-Not (Test-Path -Path $CONFIG_DIR)) {
    New-Item -ItemType Directory -Path $CONFIG_DIR
    Write-Output "Répertoire $CONFIG_DIR créé."
}

# Copie des fichiers de configuration depuis config_examples
Copy-Item -Path "$EXAMPLES_DIR/config.ini.sample" -Destination "$CONFIG_DIR/config.ini"
Copy-Item -Path "$EXAMPLES_DIR/logging.ini.sample" -Destination "$CONFIG_DIR/logging.ini"

Write-Output "Fichiers de configuration copiés dans $CONFIG_DIR."
