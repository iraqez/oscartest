from .settings import DATABASES, ALLOWED_HOSTS



DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'dev-present-me',
    'USER': 'postgres',
    'PASSWORD': 'workfree',
    'HOST': 'localhost', # Set to empty string for localhost.
    'PORT': '5432', # Set to empty string for default.
    }
}