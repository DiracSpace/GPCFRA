# coding: utf-8

import os

from photovault.infrastructure.settings.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/db.sqlite3',
    }
}

# TODO: setup cache