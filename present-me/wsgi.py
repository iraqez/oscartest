"""
WSGI config for oscartest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

from osenv import osenv

from django.core.wsgi import get_wsgi_application

osenv

application = get_wsgi_application()
