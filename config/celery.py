import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# Create a new Celery application instance.
app = Celery("config")
# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
