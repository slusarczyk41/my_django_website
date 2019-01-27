from os import environ
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = environ["SECRET_KEY"],

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0',
    'dataguy.pl',
    'dataguy',
    'modernhippie.eu',
]
