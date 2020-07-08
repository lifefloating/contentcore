# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

"""
随机池
"""

__all__ = ['RandPool']


class RandPool(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, k, v, expire=None):
        """
        增加数据
        :param k:
        :param v:
        :return:
        """

    @abstractmethod
    def rand(self):
        """
        自动处理最近的data
        :param num:
        :return:
        """

    @abstractmethod
    def count(self):
        """
        统计指定键名队列长度
        :return:num
        """

    @abstractmethod
    def remove(self, k):
        """
        删除数据
        :return:None
        """
