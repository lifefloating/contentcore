# -*- coding: utf-8 -*-
# Created by yqq
from debuglog import logger


def get(cls_path):
    """
    获取
    :param cls_path:
    :return:

    >>> get(None)

    >>> get('contentcore.contrib.queue.redisqueue.RedisQueue')
    <class 'contentcore.contrib.queue.redisqueue.RedisQueue'>
    """

    if cls_path:
        pos = cls_path.rfind('.')
        package = cls_path[:pos]
        # logger.debug(package)
        name = cls_path[pos+1:]
        # logger.debug(name)
        module = __import__(package, globals(), locals(), name, -1)
        return getattr(module, name)

if __name__ == "__main__":
    import doctest
    doctest.testmod()