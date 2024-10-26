"""
WSGI config for test_mgmt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from api import admin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_mgmt.settings')

application = get_wsgi_application()

# Load site configuration
admin.site.reload_settings()
