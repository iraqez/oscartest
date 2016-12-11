from .dev_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGES = (
    ('ru', gettext_noop('Russian')),
    ('uk', gettext_noop('Ukrainian')),
    ('en', gettext_noop('English')),
)
