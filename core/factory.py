# -*- coding: utf-8 -*-
# Created by yqq

from contentcore import settings
from contentcore.service.queue import BaseQueue
from contentcore.service.segment import Segment
from contentcore.service.dupfilter import DupFilter
from contentcore.service.simhash import SimHash
from contentcore.service.hashdb import HashDb
from contentcore.service.randpool import RandPool
from contentcore.service.cache import Cache

from contentcore.core import gcls


def hashdb(cls=None, **kwargs):
    """
    >>> h = hashdb()
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

    :param cls:
    :param kwargs:
    :return:
    """
    instance = HashDb
    if isinstance(instance, type(HashDb)):
        instance = settings_service_base('HASHDB', cls, instance, **kwargs)
    return instance


def priority_queue(cls=None, **kwargs):
    """
    >>> q = priority_queue()
    >>> q.clear()
    >>> q.names()
    []

    :param cls:
    :param kwargs:
    :return:
    """
    instance = BaseQueue
    if isinstance(instance, type(BaseQueue)):
        instance = settings_service_base('QUEUE', cls, instance, **kwargs)
    return instance


def segment(cls=None, **kwargs):
    """
    >>> seg = segment()
    >>> ex = seg.cut('我是中国人', remove_stop=False)
    >>> ('/'.join(ex)).decode()
    u'\u6211/\u662f/\u4e2d\u56fd/\u4eba'
    >>> ex = seg.cut('我是中国人')
    >>> ('/'.join(ex)).decode()
    u'\u4e2d\u56fd/\u4eba'
    >>> ex = seg.cut_count('中国人民是中国人')
    >>> '/'.join([e[0] for e in ex])
    u'\u4e2d\u56fd/\u4eba'
    >>> '/'.join([str(e[1]) for e in ex])
    '2/1'

    :param cls:
    :param kwargs:
    :return:
    """
    instance = Segment
    if isinstance(instance, type(Segment)):
        instance = settings_service_base('SEGMENT', cls, instance, **kwargs)
    return instance


def dupfilter(cls=None, **kwargs):
    """
    去重服务
    :param cls:
    :param kwargs:
    :return:

    >>> bf = dupfilter()
    >>> url1 = 'http://a.com/1'
    >>> bf.add(url1)
    >>> bf.add(url1)
    >>> bf.add(url1)
    >>> url2 = 'http://a.com/2'
    >>> bf.get(url1)
    True
    >>> bf.get(url2)
    >>> bf.add('a')
    >>> bf.add('b')
    >>> bf.add('c')
    >>> bf.get('c')
    True
    """
    instance = DupFilter
    if isinstance(instance, type(DupFilter)):
        instance = settings_service_base('DUPFILTER', cls, instance, **kwargs)
    return instance


def simhash(cls=None, **kwargs):
    """
    去重服务
    :param cls:
    :param kwargs:
    :return:

    TODO 此处测试代码用的是基于mmh3的hashcode处理测试，如果改为其它hashcode为simhash需要重新更改代码

    测试hashcode生成
    >>> sim = simhash()
    >>> sim.hashcode('hello')
    340282366920938463463374607431768211455L
    >>> sim.hashcode('hello', size=128)
    340282366920938463463374607431768211455L
    >>> sim.hashcode('hello', size=64)
    18446744073709551615L
    >>> sim.hashcode('hello', size=32)
    4294967295
    >>> sim.hashcode('hello', size=1)
    340282366920938463463374607431768211455L


    测试hashcode增加与Hamming计算

    size=128(default)

    >>> x1 = sim.hashcode('hello')
    >>> x1
    340282366920938463463374607431768211455L
    >>> x2 = sim.hashcode('hello world')
    >>> x2
    261717332990784154696618402931915064554L
    >>> x3 = sim.hashcode('hello world china')
    >>> x3
    306994206956801177407236076499246237423L
    >>> lx = [x1,x2,x3]
    >>> sx = set(lx)
    >>> sim.adds(sx)
    >>> x4 = sim.hashcode('hello world china abc')
    >>> x4
    136769891227086872778960038052162946151L
    >>> sim.hamming(x4)
    (26, 306994206956801177407236076499246237423L)

    size = 32

    >>> x1 = sim.hashcode('hello', size=32)
    >>> x1
    4294967295
    >>> x2 = sim.hashcode('hello world', size=32)
    >>> x2
    4220927227
    >>> x3 = sim.hashcode('hello world china', size=32)
    >>> x3
    4288560891
    >>> lx = [x1,x2,x3]
    >>> sx = set(lx)
    >>> sim.adds(sx, size=32)
    >>> x4 = sim.hashcode('hello world china abc', size=32)
    >>> x4
    3147699963
    >>> sim.hamming(x4, size=32)
    (4, 4288560891)


    size = 64, db = test
    >>> x1 = sim.hashcode('hello', size=64)
    >>> x1
    18446744073709551615L
    >>> x2 = sim.hashcode('hello world', size=64)
    >>> x2
    8198091784597505258
    >>> x3 = sim.hashcode('hello world china', size=64)
    >>> x3
    8495894650748389103
    >>> lx = [x1,x2,x3]
    >>> lx
    [18446744073709551615L, 8198091784597505258, 8495894650748389103]
    >>> sx = set(lx)
    >>> sx
    set([8198091784597505258, 18446744073709551615L, 8495894650748389103])
    >>> sim.adds(sx, size=64, db='test')
    >>> x4 = sim.hashcode('hello world china abc', size=64)
    >>> x4
    8396815455723963495
    >>> sim.hamming(x4, size=64, db='test')
    (9, 8495894650748389103)


    # similar

    >>> similar = sim.similarity(8396815455723963495, 8495894650748389103)
    >>> similar
    0.9883379915715294
    """
    instance = SimHash
    if isinstance(instance, type(SimHash)):
        instance = settings_service_base('SIMHASH', cls, instance, **kwargs)
    return instance


def settings_service_base(name, cls=None, instance=None, **kwargs):
    """
    获取settings中配置的service服务
    service cls 配置项为 NAME_CONTENT_CLS
    service params 配置项为 NAME_CONTENT_PARAMS
    :param cls:
    :param name:
    :param instance:
    :param kwargs:
    :return:

    >>> service = settings_service_base('QUEUE', None, BaseQueue)
    >>> service.clear()
    >>> service.names()
    []

    """
    if not cls:
        cls = getattr(settings, '{0}_CONTENT_CLS'.format(name))
    if kwargs == {}:
        kwargs = getattr(settings, '{0}_CONTENT_PARAMS'.format(name))
    if cls:
        instance = gcls.get(cls)(**kwargs)
    return instance


def setting_service(name, cls=None, extend=0, **kwargs):
    """
    获取配置服务
    :param name:
    :param cls:
    :param base:
    :param kwargs:
    :return:

    >>> q = setting_service('QUEUE')
    >>> q.names()
    []
    >>> from contentcore import settings
    >>> settings.EXTEND_CONTENTS = dict(QUEUE_CONTENT_CLS = 'contentcore.contrib.queue.redisqueue.RedisQueue', QUEUE_CONTENT_PARAMS = {'host': '127.0.0.1', 'port': 6379, 'password': '', 'db': 15})
    >>> q = setting_service('QUEUE', extend=1)
    >>> q.names()
    []
    """

    if extend:
        fun = settings_service_extend
    else:
        fun = settings_service_base
    return fun(name, cls, **kwargs)


def settings_service_extend(name, cls=None, instance=None, **kwargs):
    """
    获取settings中配置的extend service服务
    service cls 配置项为 NAME_CONTENT_CLS
    service params 配置项为 NAME_CONTENT_PARAMS
    :param cls:
    :param name:
    :param instance:
    :param kwargs:
    :return:
    >>> from contentcore import settings
    >>> settings.EXTEND_CONTENTS = dict(QUEUE_CONTENT_CLS = 'contentcore.contrib.queue.redisqueue.RedisQueue', QUEUE_CONTENT_PARAMS = {'host': '127.0.0.1', 'port': 6379, 'password': '', 'db': 15,})
    >>> service = settings_service_extend('QUEUE', None, BaseQueue)
    >>> service.names()
    []

    """
    extend_settings = getattr(settings, 'EXTEND_CONTENTS')
    if not cls:
        cls = extend_settings.get('{0}_CONTENT_CLS'.format(name))
    if kwargs == {}:
        kwargs = extend_settings.get('{0}_CONTENT_PARAMS'.format(name))

    if cls:
        instance = gcls.get(cls)(**kwargs)
    return instance


def randpool(cls=None, **kwargs):
    """
    :param cls:
    :param kwargs:
    :return:
    """
    instance = RandPool
    if isinstance(instance, type(RandPool)):
        instance = settings_service_base('RANDPOOL', cls, instance, **kwargs)
    return instance


def cache(cls=None, **kwargs):
    """
    Cache
    :param cls:
    :param kwargs:
    :return:
    """
    instance = Cache
    if isinstance(instance, type(Cache)):
        instance = settings_service_base('CACHE', cls, instance, **kwargs)
    return instance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
