from pathlib import Path

from environs import Env

root_dir = Path(__file__).resolve(strict=True).parent.parent

env = Env()
env.read_env(str(root_dir / ".env"))


class Setting:
    """Environment variable class."""
    CELERY_BROKER = env("CELERY_BROKER", "redis://localhost:6379/0")

    CELERY_TIMEZONE = env("CELERY_TIMEZONE", "UTC")

    TASK_VALIDATE_MINUTES = env.int("TASK_VALIDATE_MINUTES")

    EMAIL_HOST = env("EMAIL_HOST")

    EMAIL_HOST_USER = env("EMAIL_HOST_USER")

    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

    EMAIL_PORT = env("EMAIL_PORT")

    DATABASE_URL = env("DATABASE_URL")
