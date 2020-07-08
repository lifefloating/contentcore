# -*- coding: utf-8 -*-
from debuglog import logger

__all__ = ['Mmh3SimHash']

from contentcore.service.simhash import SimHash
from contentcore import settings
import simhash

try:
    import cPickle as pickle
except ImportError:
    import pickle

_SIMHASH_CACHE_LIB = {}


class Mmh3SimHash(SimHash):
    """
    simhash比较

    测试hashcode生成
    >>> sim = Mmh3SimHash()
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
    >>> lx = [x3]
    >>> sx = set(lx)
    >>> sim.remove(sx)
    >>> sim.hamming(x4)
    (34, 261717332990784154696618402931915064554L)

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

    __slots__ = ('adds', 'hamming', 'hashcode', 'similarity','remove')

    def adds(self, hashcode_set, size=128, db=None):
        """
        增加数据至hashcode lib
        :param hashcode_set:
        :param size:
        :param db:
        :return:
        """
        # 获取lib
        db = self._full_db(size=size, db=db)
        lib = self._cache_lib(db=db)
        # 增加lib数据

        if not isinstance(hashcode_set, set):
            raise TypeError(u'hashcode_set必须为set集合')

        lib = lib | hashcode_set
        # 保存lib
        self._save_lib(lib, db=db)
        # 清除缓存
        self._cache_lib_remove(db=db)

    def remove(self, hashcode_set, size=128, db=None):
        # 获取lib
        db = self._full_db(size=size, db=db)
        lib = self._cache_lib(db=db)
        # 增加lib数据

        if not isinstance(hashcode_set, set):
            raise TypeError(u'hashcode_set必须为set集合')

        lib = lib - hashcode_set
        # 保存lib
        self._save_lib(lib, db=db)
        # 清除缓存
        self._cache_lib_remove(db=db)

    def hamming(self, hashcode, size=128, db=None):
        """
        继续与已存的hashcode lib最近的数据
        :param hashcode:
        :param size:
        :param db:
        :return:
        """
        size = Mmh3SimHash.resize(size)
        db = self._full_db(size=size, db=db)
        lib = self._cache_lib(db)
        return simhash.hamming_lib(hashcode, lib)

    def hashcode(self, content, size=128):
        """
        获取hashcode值
        :param content:
        :param size:
        :return:
        """
        size = Mmh3SimHash.resize(size)
        return simhash.simhash_instance(content=content, size=size).hash

    def similarity(self, hashcode1, hashcode2):
        """
        计算两个数的相似度，实际为除法计算
        :param hashcode1:
        :param hashcode2:
        :return:
        """
        a = float(hashcode1)
        b = float(hashcode2)
        if a > b:
            return b / a
        else:
            return a / b

    def __init__(self, **kwargs):
        super(Mmh3SimHash, self).__init__(**kwargs)
        default_setting = settings.SIMHASH_CONTENT_PARAMS
        self.hash_db = kwargs.get('hash_db') or default_setting.get('hash_db')
        # self.hash128 = kwargs.get('hash128') or default_setting.get('hash128')
        # self.hash64 = kwargs.get('hash64') or default_setting.get('hash64')
        # self.hash32 = kwargs.get('hash32') or default_setting.get('hash32')

    def _full_db(self, size=128, db=None):
        """
        通过给定的size获取db，如果已给定db，则使用给定的db
        :param size:
        :param db:
        :return:
        """
        size = Mmh3SimHash.resize(size)
        if db:
            db = '%s_%s_%s' % (self.hash_db, size, db)
        else:
            db = getattr(self, 'hash%s' % size)
        return db

    def _load_lib(self, db):
        """
        加载指定的lib
        :param db:
        :return:
        """
        try:
            with open(db, 'rb') as f:
                return pickle.load(f)
        except Exception, e:
            logger.warn(u'默认返回set()，因载入hash数据库%s:%s' % (db, e))
            return set()

    def _save_lib(self, lib, db):
        """
        保存Lib至指定的路径
        :param lib:
        :param db:
        :return:
        """
        with open(db, 'wb') as f:
            pickle.dump(lib, f)

    def _cache_lib(self, db):
        """
        获取缓存lib，如果没有缓存，则读取并缓存
        :param db:
        :return:
        """
        global _SIMHASH_CACHE_LIB

        lib = _SIMHASH_CACHE_LIB.get(db)

        if lib is None:
            lib = self._load_lib(db)
            _SIMHASH_CACHE_LIB[db] = lib
        return lib

    def _cache_lib_remove(self, db):
        """
        清除指定的缓存lib
        :param db:
        :return:
        """
        global _SIMHASH_CACHE_LIB
        if db in _SIMHASH_CACHE_LIB:
            del _SIMHASH_CACHE_LIB[db]

    @staticmethod
    def resize(size):
        """
        只支持32.64.128 hashcode
        :param size:
        :return:
        """
        if size in (32, 64, 128):
            return size
        else:
            return 128


if __name__ == "__main__":
    import doctest

    doctest.testmod()
