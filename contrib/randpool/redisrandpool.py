# -*- coding: utf-8 -*-
# Created by yqq

"""
随机

"""

import redis

from contentcore.service.randpool import RandPool
from contentcore import settings
from debuglog import logger
__all__ = ['RandPool']


class RedisRandPool(RandPool):

    """
    基于redis的hash存储
    >>> r = RedisRandPool()
    >>> rs = ['1','2','3']
    >>> [r.add('k_%s' % s,s) for s in rs]
    [None, None, None]
    >>> v = r.rand()
    >>> logger.debug(v)
    >>> v in rs
    True
    >>> r.count()
    3L



    """

    def __init__(self, **kwargs):
        super(RedisRandPool, self).__init__(**kwargs)
        default_setting = settings.RANDPOOL_CONTENT_PARAMS
        host = kwargs.get('host') or default_setting.get('host')
        port = kwargs.get('port') or default_setting.get('port')
        password = kwargs.get('password') or default_setting.get('password')
        db = kwargs.get('db') or default_setting.get('db')
        pool = kwargs.get('pool')
        self._name = '%s:{0}' % (kwargs.get('collection') or default_setting.get('collection'))

        if not pool:
            pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
        self.server = redis.Redis(connection_pool=pool)

    def _pool_name(self, name):
        return self._name.format(name)

    def add(self, k, v, expire=None):
        if expire > 0:
            self.server.set(self._pool_name(k), v, expire)
        else:
            self.server.set(self._pool_name(k), v)
        logger.info('add:%s=%s' % (k,v))

    def rand(self):
        key = self.server.randomkey()
        logger.debug(key)
        if key:
            return self.server.get(key)

    def remove(self, k):
        self.server.delete(self._pool_name(k))

    def count(self):
        return self.server.dbsize()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
