import json
from pathlib import Path


def get_log():
    root_dir = Path(__file__).resolve(strict=True).parent.parent
    file_path = root_dir / "file_log" / "log.json"
    try:
        with open(file_path, "r+", encoding="utf-8") as file:
            log = json.load(file)
    except FileNotFoundError:
        with open(file_path,  "w", encoding="utf-8") as file:
            json.dump([], file)
        return []
    log_list = list(reversed(log))
    return log_list


def set_log(date_log, time_log, status, mgs, url):
    root_dir = Path(__file__).resolve(strict=True).parent.parent
    file_path = root_dir / "file_log" / "log.json"
    with open(file_path, "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        results.append({"date": date_log, "time": time_log, "status": status, "message": mgs, "url": url})
        f.seek(0)
        f.write(json.dumps(results))


