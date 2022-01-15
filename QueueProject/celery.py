import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QueueProject.settings')

app = Celery('QueueProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# app.conf.task_queues = (
#     Queue('sum_finder',    routing_key='default'),
# )
# app.conf.task_routes = {'calculation.tasks.*': {'queue': 'sum_finder'}}