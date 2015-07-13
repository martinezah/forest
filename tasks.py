import celery

import workers

from settings import (REDIS_HOST, REDIS_PORT, REDIS_DB)

CELERY_REDIS_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_DB)
app = celery.Celery('tasks', broker=CELERY_REDIS_URL, backend=CELERY_REDIS_URL)

_workers = { }

@app.task
def download(msg):
    if not _workers.get('download'):
        _workers['download'] = workers.DownloadWorker()
    return _workers['download'].run(msg)

@app.task
def scrape(req):
    if not _workers.get('scrape'):
        _workers['scrape'] = workers.ScrapeWorker()
    return _workers['scrape'].run(msg)

@app.task
def index(req):
    if not _workers.get('index'):
        _workers['index'] = workers.IndexWorker()
    return _workers['index'].run(msg)
