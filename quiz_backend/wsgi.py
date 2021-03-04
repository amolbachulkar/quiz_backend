"""
WSGI config for quiz_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_backend.settings')

# Override default port for `runserver` command
#from django.core.management.commands.runserver import Command as runserver
#runserver.default_port = "8080"

application = get_wsgi_application()
