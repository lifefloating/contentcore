# -*- coding: utf-8 -*-
# Created by yqq

__all__ = ['RedisHashDb']

import redis

from contentcore.service.hashdb import HashDb
from contentcore import settings
from debuglog import logger
import json

class RedisHashDb(HashDb):
    """
    基于redis的hash存储
    >>> h = RedisHashDb()
    >>> h.hset('baidu', 'a', 1)
    >>> h.hset('baidu', 'b', 2)
    >>> h.hset('baidu', 'c', 3)
    >>> h.hget('baidu', 'a')
    '1'
    >>> h.hget('baidu', 'c')
    '3'
    >>> h.hset('baidu', 'a', 11)
    >>> h.hget('baidu', 'a')
    '11'
    >>> h.delete('baidu','a')
    >>> h.hget('baidu', 'a')

    >>> h.hget('baidu', 'c')
    '3'
    >>> h.delete('baidu', k=None)
    >>> h.hget('baidu', 'c')

    """

    def __init__(self, **kwargs):
        super(RedisHashDb, self).__init__(**kwargs)
        default_setting = settings.HASHDB_CONTENT_PARAMS
        host = kwargs.get('host') or default_setting.get('host')
        port = kwargs.get('port') or default_setting.get('port')
        password = kwargs.get('password') or default_setting.get('password')
        db = kwargs.get('db') or default_setting.get('db')
        pool = kwargs.get('pool')
        self._name = '%s_{0}' % (kwargs.get('collection') or default_setting.get('collection'))

        if not pool:
            pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
        self.server = redis.Redis(connection_pool=pool)

    def _pq_name(self, name):

        return self._name.format(name)

    def hset(self, name, k, v):
        q = self._pq_name(name)
        self.server.hset(q, k, v)

    def hget(self, name, k):
        q = self._pq_name(name)
        return self.server.hget(q, k)

    def delete(self, name, k):
        q = self._pq_name(name)
        if k:
            if not isinstance(k, list):
                k = [k]
            self.server.hdel(q, *k)
        else:
            self.server.delete(q)

    def getall(self, name):
        q = self._pq_name(name)

        return self.server.hgetall(q)

if __name__ == "__main__":
    import doctest

    doctest.testmod()