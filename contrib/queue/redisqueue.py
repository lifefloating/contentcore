# -*- coding: utf-8 -*-
# Created by yqq

__all__ = ['RedisQueue']

"""
列队基类

"""

import json

import redis

from contentcore.service.queue import BaseQueue
from contentcore import settings


class RedisQueue(BaseQueue):
    """
    Redis有序集合实现优先队列
    >>> q = RedisQueue()
    >>> q.clear()
    >>> q.names()
    []
    >>> q.push('push.com', [1,2,3,4,5,6,7])
    7
    >>> q.count('push.com')
    7
    >>> q.names()
    ['queue_test:push.com']
    >>> q.pop('push.com')
    [(1, 0.0)]
    >>> q.push('push.com', [9], 1)
    1
    >>> q.pop('push.com')
    [(9, 1.0)]
    >>> q.push('pop.com', [1,2,3,4,5,6,7])
    7
    >>> q.count('pop.com')
    7
    >>> q.push('pop.com',[11,22,33],9)
    3
    >>> q.pop('pop.com', 1)
    [(11, 9.0)]
    >>> q.names()
    ['queue_test:push.com', 'queue_test:pop.com']
    >>> q.clear('push.com')
    >>> q.names()
    ['queue_test:pop.com']
    >>> q.clear()
    >>> q.names()
    []
    """

    def __init__(self, **kwargs):
        super(RedisQueue, self).__init__(**kwargs)
        default_setting = settings.QUEUE_CONTENT_PARAMS
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

    def count(self, name):
        return self.server.zcard(self._pq_name(name))

    def push(self, name, values, priority=0):
        q = self._pq_name(name)
        vss = list()
        for v in values:
            vss.append(json.dumps(v))
            vss.append(-priority)
        self.server.zadd(q, *vss)
        return len(values)

    def names(self):
        return self.server.keys(self._pq_name('*'))

    def clear(self, name=None):
        if name:
            q = self._pq_name(name)
            if self.server.exists(q):
                self.server.delete(q)
        else:
            names = self.names()
            if names:
                self.server.delete(*names)

    def optimize(self):
        qs = list()

        for q in self.server.keys(self._pq_name('*')):
            if not self.server.zcard(q):
                qs.append(q)

        self.server.delete(qs)

    def pop(self, name, num=1, remove=True):
        assert num >= 1, u'num必须大于等于1'
        result = self.server.zrange(self._pq_name(name), 0, num - 1, withscores=True)
        if remove:
            self.server.zremrangebyrank(self._pq_name(name), 0, num - 1)

        # logger.debug(result)
        return [(json.loads(item[0]), item[1] if item[1] >= 0 else -item[1]) for item in result]


if __name__ == "__main__":
    import doctest

    doctest.testmod()