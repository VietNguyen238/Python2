"""
WSGI config for NguyenQuocViet_65_ST21A2A project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NguyenQuocViet_65_ST21A2A.settings')

application = get_wsgi_application()
