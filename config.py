from os import getenv

REDIS_HOST = getenv('REDIS_HOST', 'redis://localhost')
