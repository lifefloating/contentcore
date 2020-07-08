# -*- coding: utf-8 -*-
# Created by yqq

"""
把字典转为属性形式调用

"""
__all__ = ['Parameter']


class Parameter(dict):
    """
    把字典转为属性形式调用
    >>> o = Parameter(a=1)
    >>> o.a
    1
    >>> o['a']
    1
    >>> o.a = 2
    >>> o['a']
    2
    >>> del o.a
    >>> o.a

    """

    def __getattr__(self, key):
        return self.get(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError(k)


if __name__ == "__main__":
    import doctest
    doctest.testmod()