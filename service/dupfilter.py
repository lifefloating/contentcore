# -*- coding: utf-8 -*-
# Created by yqq

__all__ = ['DupFilter']
from abc import ABCMeta, abstractmethod


class DupFilter(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key):
        """
        检查key是否在过滤器中
        :param key:
        :return:
        """

    @abstractmethod
    def add(self, key):
        """
        增加key到过滤器
        :param key:
        :return:
        """

    @abstractmethod
    def clear(self):
        """
        清空库
        :return:
        """