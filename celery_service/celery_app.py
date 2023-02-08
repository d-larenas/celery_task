from celery import Celery
from celery_service.settings import Setting
from .task_load_json import get_beat_schedule


app = Celery("celery service", broker=Setting.CELERY_BROKER, include=['tasks'])

app.conf.beat_schedule = get_beat_schedule()

app.conf.timezone = Setting.CELERY_TIMEZONE
