from .settings import *

DEBUG = True
MIDDLEWARE.remove('django.middleware.cache.UpdateCacheMiddleware')
MIDDLEWARE.remove('django.middleware.cache.FetchFromCacheMiddleware')
