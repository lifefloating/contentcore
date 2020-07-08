# -*- coding: utf-8 -*-
# Created by yqq

from contentcore.service.queue import BaseQueue
from contentcore.service.segment import Segment
from contentcore.service.dupfilter import DupFilter
from contentcore.service.simhash import SimHash
from contentcore.service.hashdb import HashDb

__all__ = ['BaseQueue',
           'Segment',
           'DupFilter',
           'SimHash',
           'HashDb',
           'PriorityQueue',
           'SettingService',
           'SegmentService',
           'DupFilterService',
           'SimhashService',
           'HashDbService',
           'RandPoolService',
           'CacheService']

# 定义的各项带基本配置服务

from contentcore.core.factory import priority_queue as _priority_queue

# 优先队列
PriorityQueue = _priority_queue


# 扩展服务

from contentcore.core.factory import setting_service as _setting_service

SettingService = _setting_service

# 分词服务
from contentcore.core.factory import segment as _segment_service

SegmentService = _segment_service

# 去重服务
from contentcore.core.factory import dupfilter as _dupfilter_service

DupFilterService = _dupfilter_service

#
# simhash
from contentcore.core.factory import simhash as _simhash_service

SimhashService = _simhash_service

# hashdb
from contentcore.core.factory import hashdb as _hash_service

HashDbService = _hash_service

# randpool
from contentcore.core.factory import randpool as _randpool_service

RandPoolService = _randpool_service


# cache
from contentcore.core.factory import cache as _cache_service

CacheService = _cache_service

