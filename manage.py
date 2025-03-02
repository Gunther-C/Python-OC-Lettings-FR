import os
import sys
import subprocess
import webbrowser
import logging

logger = logging.getLogger(__name__)


def main():
    """
    Configures the Django settings and runs the command line utility.
    Configure les paramètres de Django et exécute l'utilitaire de ligne de commande.
    Args:  None
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.error("Impossible d'importer Django. Couldn't import Django.", exc_info=True)
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def debug():
    """
    Runs flake8 to generate an HTML report and opens it in the web browser.
    Exécute flake8 pour générer un rapport HTML et l'ouvre dans le navigateur web.
    Args: None
    """
    try:
        subprocess.run(["flake8", "--format=html", "--htmldir=flake8_rapport"])
        try:
            chemin = os.getcwd()
            fichier_html = f"{chemin}/flake8_rapport/index.html"
            webbrowser.open(fichier_html)
        except ValueError as er:
            print("Erreur lors de l'ouverture du fichier :", er)
    except subprocess.CalledProcessError as e:
        print("subprocess :", e)


if __name__ == '__main__':
    debug()
