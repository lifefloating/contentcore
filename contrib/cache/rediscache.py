# -*- coding: utf-8 -*-
# Created by yqq

import redis

from contentcore.service.cache import Cache
from contentcore import settings


class RedisCache(Cache):
    """
    RedisCache

    >>> cache = RedisCache()
    >>> cache.set('a',1)
    >>> cache.get('a')
    '1'

    """

    def __init__(self, **kwargs):
        super(RedisCache, self).__init__(**kwargs)
        default_setting = settings.CACHE_CONTENT_PARAMS
        host = kwargs.get('host') or default_setting.get('host')
        port = kwargs.get('port') or default_setting.get('port')
        password = kwargs.get('password') or default_setting.get('password')
        db = kwargs.get('db') or default_setting.get('db')
        pool = kwargs.get('pool')
        self._name = '%s:{0}' % (kwargs.get('collection') or default_setting.get('collection'))

        if not pool:
            pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
        self.server = redis.Redis(connection_pool=pool)

    def _pq_name(self, name):
        return self._name.format(name)

    def clear(self):
        pass

    def delete(self, key):
        self.server.delete(self._pq_name(key))

    def expire(self, key, expire):
        pass

    def set(self, key, value, expire=7200):
        self.server.set(self._pq_name(key), value, expire)

    def delete_pattern(self, key_pattern):
        pass

    def get(self, key, default=None):
        return self.server.get(self._pq_name(key)) or default


__all__ = ['RedisCache']
