from .dev_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGES = (
    ('uk', gettext_noop('Ukrainian')),
    ('ru', gettext_noop('Russian')),
 #   ('en', gettext_noop('English')),
)
