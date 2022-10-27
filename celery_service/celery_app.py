from celery import Celery
from celery_service.settings import Setting
from celery.schedules import crontab

app = Celery("celery service", broker=Setting.CELERY_BROKER, include=['tasks'])

app.conf.beat_schedule = {
    'check-status-page': {
        'task': 'tasks.task.check_page',
        'schedule': crontab(minute=0, hour="*/1")
    },
    'check-status-page-day': {
        'task': 'tasks.task.check_page',
        'schedule': crontab(minute="*/1")
    },

}

app.conf.timezone = Setting.CELERY_TIMEZONE
