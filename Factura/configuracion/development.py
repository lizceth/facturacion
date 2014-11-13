from __future__ import absolute_import
from os.path import join, normpath
from .base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#configuracion de la base de datos que usara el desarrollador
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'Mydata.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


INSTALLED_APPS += (
#    'debug_toolbar.apps.DebugToolbarConfig',
    'facturaciones',
)
"""
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_PATCH_SETTINGS = False
"""
INTERNAL_IPS = ('127.0.0.1',)
