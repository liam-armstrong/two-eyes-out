import os, random
from .settings import *

SECRET_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'secret.txt')
def keygenFn():
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except FileNotFoundError:
        try:
            print("YES")
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = open(SECRET_FILE, 'w+')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)
