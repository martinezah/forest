'''
settings.py should begin with:

    from defaults import *

followed by overrides of specific settings
'''

# Redis
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# AWS
AWS_KEY = None
AWS_SECRET = None

# Timeouts
DEFAULT_SITE_WAIT_TIME = 10
DEFAULT_URL_WAIT_TIME = 86400 
