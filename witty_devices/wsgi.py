"""
WSGI config for witty_devices project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Check if env.py exists and import it to load environment variables
if os.path.exists("env.py"):
    import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'witty_devices.settings')

application = get_wsgi_application()
