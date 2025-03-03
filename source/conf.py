import os
import sys
import django

sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

project = 'Python-OC-lettings-FR'
copyright = '2025, Gunther'
author = 'Gunther'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

html_theme = 'alabaster'
html_static_path = ['_static']

source_encoding = 'utf-8'
