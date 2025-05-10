import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# Create a new Celery application instance.
app = Celery("config")
# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# # Define a periodic task to run every day at 00:00.
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('add') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s("add"), name="add every 10 seconds")
#     # Calls test('multiply') every 30 seconds.
#     sender.add_periodic_task(
#         30.0, test.s("multiply"), name="multiply every 30 seconds"
#     )
