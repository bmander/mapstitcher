# backend/tasks.py
from celery import Celery
from celery.signals import worker_ready
import os

# Create celery app
celery = Celery(
    'mapstitcher',
    broker=os.getenv('REDIS_URL', 'redis://redis:6379/0'),
    backend=os.getenv('REDIS_URL', 'redis://redis:6379/0')
)

# Configure Celery
celery.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

@worker_ready.connect
def at_start(sender, **kwargs):
    print("Celery worker is ready!")

@celery.task(name='tasks.example')
def example_task(x, y):
    """Example task that adds two numbers."""
    return x + y