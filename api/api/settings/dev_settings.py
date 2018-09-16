from .common import *
from .keygen import *

keygenFn()
DEBUG = True
with open(SECRET_FILE, 'r') as secretfile:
  SECRET_KEY = secretfile.read()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    }
}