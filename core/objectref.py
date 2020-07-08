# -*- coding: UTF-8 -*-
# yqq

from __future__ import print_function
import weakref
import os
from collections import defaultdict
from time import time
from operator import itemgetter


NoneType = type(None)

live_refs = defaultdict(weakref.WeakKeyDictionary)


class ObjectRef(object):
    """Inherit from this class (instead of object) to a keep a record of live
    instances"""

    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        # print('hello')
        obj = object.__new__(cls)
        live_refs[cls][obj] = time()
        # print(cls.__name__)
        return obj


def format_live_refs(ignore=NoneType):
    s = "Live References" + os.linesep + os.linesep
    now = time()
    for cls, wdict in live_refs.iteritems():
        if not wdict:
            continue
        if issubclass(cls, ignore):
            continue
        oldest = min(wdict.itervalues())
        s += "%-30s %6d   oldest: %ds ago" % (cls.__name__, len(wdict), now - oldest) + os.linesep
    return s


def print_live_refs(*a, **kw):
    print(format_live_refs(*a, **kw))


def get_oldest(class_name):
    for cls, wdict in live_refs.iteritems():
        print(cls.__name__)
        if cls.__name__ == class_name:
            if wdict:
                return min(wdict.iteritems(), key=itemgetter(1))[0]


def iter_all(class_name):
    for cls, wdict in live_refs.iteritems():
        if cls.__name__ == class_name:
            return wdict.iterkeys()
