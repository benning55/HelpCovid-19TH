"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

runs = os.environ.get('TYPE')

if runs == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


application = get_wsgi_application()
