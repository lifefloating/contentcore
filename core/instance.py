# -*- coding: utf-8 -*-
# Created by yqq



from contentcore.service import *

_instance = None


class Creator:
    """
    数据库服务实例
    """

    def __init__(self):
        # print('instance init')
        pass
        # logger.debug('init instance service')

    _services = dict()

    @property
    def queues(self):
        """获取queues服务"""
        name = 'QUEUES'
        service = self._services.get(name)
        if service is None:
            service = PriorityQueue()
            self._services[name] = service
        return service

    @property
    def segment(self):
        """获取segment服务"""
        name = 'SEGMENT'
        service = self._services.get(name)
        if service is None:
            service = SegmentService()
            self._services[name] = service
        return service

    @property
    def simhash(self):
        """获取simhash服务"""
        name = 'SIMHASH'
        service = self._services.get(name)
        if service is None:
            service = SimhashService()
            self._services[name] = service
        return service

    @property
    def hashdb(self):
        """获取simhash服务"""
        name = 'HASHDB'
        service = self._services.get(name)
        if service is None:
            service = HashDbService()
            self._services[name] = service
        return service

    @property
    def dupfilter(self):
        """获取dupfilter服务"""
        return self.dupfilter_service()

    def dupfilter_service(self, **kwargs):
        """获取dupfilter服务"""
        name = 'DUPFILTER'
        if kwargs:
            name = '%s_%s' % (name, kwargs)
        service = self._services.get(name)
        if service is None:
            service = DupFilterService(**kwargs)
            self._services[name] = service
        return service

    @property
    def randpool(self):
        """获取dupfilter服务"""
        return self.randpool_service()

    def randpool_service(self, **kwargs):
        """获取dupfilter服务"""
        name = 'RANDPOOL'
        if kwargs:
            name = '%s_%s' % (name, kwargs)
        service = self._services.get(name)
        if service is None:
            service = RandPoolService(**kwargs)
            self._services[name] = service
        return service

    @property
    def cache(self):
        """获取CACHE服务"""
        return self.cache_service()

    def cache_service(self, **kwargs):
        """获取CACHE服务"""
        name = 'CACHE'
        if kwargs:
            name = '%s_%s' % (name, kwargs)
        service = self._services.get(name)
        if service is None:
            service = CacheService(**kwargs)
            self._services[name] = service
        return service

    def extend(self, name, extend=1, **kwargs):
        """获取扩展服务"""
        name = name.upper()
        service = self._services.get(name)
        if service is None:
            service = SettingService(name, extend=extend, **kwargs)
            self._services[name] = service
        return service


def instance():
    """
    >>> services = instance()
    >>> dupfilter_default = services.dupfilter
    >>> dupfilter = services.dupfilter_service(key='test')
    >>> dupfilter.add('hello')
    >>> dupfilter.get('hello1')

    >>> dupfilter.get('hello')
    True
    >>> dupfilter.clear()
    >>> dupfilter.get('hello')

    :return:
    """
    global _instance
    if not _instance:
        _instance = Creator()
    return _instance


__all__ = ['instance']

if __name__ == "__main__":
    import doctest

    doctest.testmod()
