# Python + Celery + Docker

<h3 align="left"></h3>
<p align="left"> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://redis.io" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg" alt="redis" width="40" height="40"/> </a> </p>

Application for scheduled tasks with celery.

## Description

Dervices to check website status, adding log in json file as well as alert sent to email

## Installation

Add env.example variable file.

```
  .envs -> path
  └── .local ->file
  └── .postgres ->file
     
```

## docker 

```
    docker-compose -f local.yml build

    docker-compose -f local.yml up

```

## celery extra

```
    celery -A celery_service worker -l INFO

    celery -A celery_service beat -l INFO

```

## Celery beat task settings

Scheduled task settings

Edit file /celery_service/task_json/task.json

```
  {
    "name_task_beat_schedule": {
        "task": "tasks.task.check_page", # task to execute
        "schedule": {  # execution schedule 
            "minute":0, # int or str
            "hour":"*/1"
        }
    },
     "check-status-page-day": {
        "task": "tasks.task.sent_report",
        "schedule": {
            "hour":"1",
            "day_of_week": "1"
        },
      "kwargs": {"status":  200},
      "args": [1,2]
    }

}
```
 Finally the dictionary for beat schedule is generated

```
from celery.schedules import crontab

app.conf.beat_schedule = {
'check-status-page': {
	'task': 'tasks.task.check_page',
	 'schedule': crontab(minute=0, hour="*/1")
	 },
'check-status-page-day': {
	'task': 'tasks.task.check_page',
	'schedule': crontab(minute="*/5")
	}
}
```

### Example

<table class="docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 52%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><strong>Example</strong></p></td>
<td><p><strong>Meaning</strong></p></td>
</tr>
<tr class="row-odd"><td><p><code class=""><span class="pre"><span class="highlighted">crontab</span>(minute=0,</span> <span class="pre">hour=0)</span></code></p></td>
<td><p>Execute daily at midnight.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre"><span class="highlighted">crontab</span>(minute=0,</span> <span class="pre">hour='*/3')</span></code></p></td>
<td><p>Execute every three hours:
midnight, 3am, 6am, 9am,
noon, 3pm, 6pm, 9pm.</p></td>
</tr>
<tr class="row-odd"><td><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre"><span class="highlighted">crontab</span>(minute=0,</span></code></dt><dd><p><code class="docutils literal notranslate"><span class="pre">hour='0,3,6,9,12,15,18,21')</span></code></p>
</dd>
</dl>
</td>
<td><p>Same as previous.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre"><span class="highlighted">crontab</span>(minute='*/15')</span></code></p></td>
<td><p>Execute every 15 minutes.</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre"><span class="highlighted">crontab</span>(day_of_week='sunday')</span></code></p></td>
<td><p>Execute every minute (!) at Sundays.</p></td>
</tr>


</tbody>
</table>


    
## Documentation

[docs.celeryq.dev - Periodic Tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html?highlight=crontab#crontab-schedules)



## Connect with me  
<div align="center">
<a href="https://github.com/larenas-d" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 5px;" />
</a>
<a href="https://diego-larenas.gropoz.com" target="_blank">
<img src=https://img.shields.io/badge/website-%2308090A.svg?&style=for-the-badge alt=devto style="margin-bottom: 5px;" />
</a>
<a href="https://www.linkedin.com/in/diego-larenas-7704411b6/" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 5px;" />
</a>
 
</div> 


