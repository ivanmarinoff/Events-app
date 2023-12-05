import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library_online_catalog.settings") - for deploy on render.com
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library_online_catalog.library.settings")

application = get_wsgi_application()
