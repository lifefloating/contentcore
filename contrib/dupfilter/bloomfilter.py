# -*- coding: utf-8 -*-

import pybloomfilter
# from pybloom import BloomFilter
__all__ = ['BloomFilter']

from contentcore.service.dupfilter import DupFilter
from contentcore import settings


class BloomFilter(DupFilter):

    def get(self, key):
        """
        检查key是否已存在
        :param key:
        :return:
        """
        if key in self.bloom_filter:
            return True

    def add(self, key):
        """
        增加key到过滤库
        :param key:
        :return:
        """
        self.bloom_filter.add(key)

    def clear(self):
        self.bloom_filter.clear_all()

    bloom_filter = None
    enabled = True

    def __init__(self, **kwargs):
        super(BloomFilter, self).__init__(**kwargs)
        default_setting = settings.DUPFILTER_CONTENT_PARAMS
        filename = kwargs.get('filename') or default_setting.get('filename')
        key = kwargs.get('key') or default_setting.get('key') or 'default'
        filename = '%s_%s' % (filename, key)
        self.enabled = kwargs.get('enabled') or default_setting.get('enabled')
        try:
            self.bloom_filter = pybloomfilter.BloomFilter.open(filename)
        except:
            capacity = kwargs.get('capacity') or default_setting.get('capacity')
            error_rate = kwargs.get('error_rate') or default_setting.get('error_rate')
            self.bloom_filter = pybloomfilter.BloomFilter(capacity=capacity, error_rate=error_rate, filename=filename)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
