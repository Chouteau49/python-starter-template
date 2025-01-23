import argparse


class Args:
    """
    Classe pour gérer les arguments de la ligne de commande.
    """

    def __init__(self):
        """
        Initialise le parser d'arguments.
        """
        self.parser = argparse.ArgumentParser(
            description="Template projet python")
        self._add_arguments()

    def _add_arguments(self):
        """
        Ajoute les arguments au parser.
        """
        self.parser.add_argument(
            '--config', type=str, help='Chemin vers le fichier de configuration', default='config/config.ini')
        self.parser.add_argument(
            '--logging', type=str, help='Chemin vers le fichier de configuration des logs', default='config/logging.ini')
        # Ajoutez d'autres arguments ici si nécessaire

    def parse(self):
        """
        Parse les arguments de la ligne de commande.
        """
        return self.parser.parse_args()
