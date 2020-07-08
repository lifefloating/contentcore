# -*- coding: utf-8 -*-
# Created by yqq

import logging
import os

DEBUG = True

SERVICE_PROJECT_PATH = os.path.dirname(__file__)

# SEGMENT

SEGMENT_CONTENT_CLS = 'contentcore.contrib.segment.jiebasegment.JiebaSegment'
SEGMENT_CONTENT_PARAMS = {

    'dict': os.path.join(SERVICE_PROJECT_PATH, 'data/segment/jiebadict'),
    'stopwords': os.path.join(SERVICE_PROJECT_PATH, 'data/segment/stopwords'),
    'log_level': logging.ERROR,
}

DUPFILTER_CONTENT_CLS = 'contentcore.contrib.dupfilter.bloomfilter.BloomFilter'
DUPFILTER_CONTENT_PARAMS = {

    "capacity": 10000000,
    "error_rate": 0.1,
    "filename": os.path.join(SERVICE_PROJECT_PATH, 'data/dupfilter/testdb'),
    "enabled": True
}

SIMHASH_CONTENT_CLS = 'contentcore.contrib.simhash.mmh3simhash.Mmh3SimHash'
SIMHASH_CONTENT_PARAMS = {

    'hash_db': os.path.join(SERVICE_PROJECT_PATH, 'data/simhash/test_hash_test')
}


# QUEUE REDIS

QUEUE_CONTENT_CLS = 'contentcore.contrib.queue.redisqueue.RedisQueue'
QUEUE_CONTENT_PARAMS = {

    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 15,
    'collection': 'queue_test'

}


HASHDB_CONTENT_CLS = 'contentcore.contrib.hashdb.redishashdb.RedisHashDb'
HASHDB_CONTENT_PARAMS = {

    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 15,
    'collection': 'hashdb_test'

}
RANDPOOL_CONTENT_CLS = 'contentcore.contrib.randpool.redisrandpool.RedisRandPool'
RANDPOOL_CONTENT_PARAMS = {

    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 14,
    'collection': 'randpool_test'

}

CACHE_CONTENT_CLS = 'contentcore.contrib.cache.rediscache.RedisCache'
CACHE_CONTENT_PARAMS = {

    'host': '127.0.0.1',
    'port': 6379,
    'password': '',
    'db': 13,
    'collection': 'redis_cache_test'

}
EXTEND_CONTENTS = {}






