"""
WSGI config for oscartest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
from osenv import osenv

from django.core.wsgi import get_wsgi_application

osenv
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "present-me.dev_settings")

application = get_wsgi_application()
