from .common import *
from .keygen import *

DEBUG = False
keygenFn()
with open(SECRET_FILE, 'r') as secretfile:
  SECRET_KEY = secretfile.read()

ALLOWED_HOSTS = ['159.203.33.149']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': '2eo_DB',
        'PORT': 5432,
    }
}