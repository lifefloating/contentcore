# -*- coding: utf-8 -*-
# Created by yqq

"""
列队基类
"""

__all__ = ['HashDb']
from abc import ABCMeta, abstractmethod


class HashDb(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def hset(self, name, k, v):
        """
        设置数据集name的k=v
        :param name:
        :param k:
        :param v:
        :return:
        """

    @abstractmethod
    def hget(self, name, k):
        """
        获取数据集name的k的v
        :param name:
        :param k:
        :return:
        """

    @abstractmethod
    def delete(self, name, k):
        """
        删除数据集name的k
        如果k=None则删除数据集name
        :param name:
        :param k:
        :return:
        """

    @abstractmethod
    def getall(self, name):
        """
        获取所有kv
        """