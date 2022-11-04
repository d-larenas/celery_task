import json
from pathlib import Path
import datetime
from logs import get_log, set_log
import pandas as pd
from celery.schedules import crontab
from celery_service.task_load_json import get_beat_schedule


def validate_log(response, url):
    log_list = get_log()
    set_log(response["datetime"]["date"], response["datetime"]["time"], response["status"], response["message"], url)
    try:
        df = pd.DataFrame(log_list)
        result_filter = df.loc[df["url"] == url].to_dict('records')
    except KeyError:
        result_filter = []
    if result_filter:
        if result_filter[0]["date"] == response["datetime"]["date"]:
            return True
    return False



ss = get_beat_schedule()
d = 2