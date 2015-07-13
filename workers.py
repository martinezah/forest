import json
import redis
import requests

from settings import (REDIS_HOST, REDIS_PORT, REDIS_DB, AWS_KEY, AWS_SECRET)

class BaseWorker():
    TYPE = None

    def __init__(self):
        if self.TYPE is None:
            raise NotImplementedError()
        self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def run(self, req):
        response = {}
        try:
            response['request'] = json.loads(req)
        except ValueError:
            return {'error':'could not parse request'}
        request = response['request']
        # validate request
        # get site config
        # check wait times
        url = request['url']
        rr = requests.get(url)
        response = self.process(rr)
        return json.dumps(response)

    def process(self, rr):
        raise NotImplementedError()
        
class IndexWorker(BaseWorker):
    TYPE = 'index'

    def process(self, rr):
        return rr.status_code
        
class ScrapeWorker(BaseWorker):
    TYPE = 'scrape'

    def process(self, rr):
        return rr.status_code
        
class DownloadWorker(BaseWorker):
    TYPE = 'download'

    def process(self, rr):
        return rr.status_code
