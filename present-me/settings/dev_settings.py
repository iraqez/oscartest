from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'dev-present-me',
#     'USER': 'postgres',
#   #  'PASSWORD': 'workfree',
#     'HOST': 'db', # Set to empty string for localhost.
#     'PORT': '5432', # Set to empty string for default.
#     }
# }

# LANGUAGES = (
#     ('uk', gettext_noop('Ukrainian')),
#     ('ru', gettext_noop('Russian')),
#  #   ('en', gettext_noop('English')),
# )