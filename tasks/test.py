import json
from pathlib import Path
import datetime
from logs import get_log, set_log
import pandas as pd


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

response = {}
date_time = datetime.datetime.now()
time = date_time.strftime("%H:%M:%S")
date = date_time.strftime("%d-%m-%Y")
response["datetime"] = {"time": time, "date": date}
response["status"] = 500
response["message"] = "hola"
url = "https://app.gropoz.co"
ss = validate_log(response, url)


