import json
from celery.schedules import crontab
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


def load_task_json():
    """Read file json."""
    root_dir = Path(__file__).resolve(strict=True).parent
    file_path = root_dir / "task_json" / "task.json"
    try:
        with open(file_path, "r+", encoding="utf-8") as file:
            task = json.load(file)
    except FileNotFoundError:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({}, file)
        return {}
    return task


def load_beat_schedule(task_dict):
    """load dict for beat schedule."""
    beat_schedule = {}
    for task in task_dict:
        logging.info(msg=task_dict[task])
        beat_schedule[task] = {}
        beat_schedule[task]["task"] = task_dict[task]["task"]
        beat_schedule[task]["schedule"] = crontab(**task_dict[task]["schedule"])
    return beat_schedule


def get_beat_schedule():
    """Return beat schedule."""
    task_dict = load_task_json()
    beat_schedule = load_beat_schedule(task_dict)
    return beat_schedule
