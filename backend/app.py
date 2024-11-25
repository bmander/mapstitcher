# backend/app.py
from flask import Flask
from tasks import celery

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'message': 'MapStitcher API'}

@app.route('/test-celery')
def test_celery():
    """Test endpoint to ensure Celery is working."""
    result = celery.send_task('tasks.example', args=[4, 4])
    return {'task_id': result.id, 'status': 'queued'}