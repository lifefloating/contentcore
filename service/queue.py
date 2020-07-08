# -*- coding: utf-8 -*-
# Created by yqq

"""
列队基类
"""

__all__ = ['BaseQueue']
from abc import ABCMeta, abstractmethod


class BaseQueue(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def pop(self, name, num):
        """
        指定键名出列
        :param name: 键名
        :param num: 数量
        :return:list
        """

    @abstractmethod
    def push(self, name, values, priority=0):
        """
        指定键名入列
        :param name:
        :param values:
        :param priority:
        :return:num
        """

    @abstractmethod
    def count(self, name):
        """
        统计指定键名队列长度
        :param name:
        :return:num
        """

    @abstractmethod
    def names(self):
        """
        获取所有键名
        :return:[]
        """

    @abstractmethod
    def optimize(self):
        """
        优化队列
        :return:None
        """

    @abstractmethod
    def clear(self, name=None):
        """
        清空数据
        :param name:
        :return:None
        """