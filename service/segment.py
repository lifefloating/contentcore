# -*- coding: utf-8 -*-
# Created by yqq


__all__ = ['Segment']
from abc import ABCMeta, abstractmethod


class Segment(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def cut(self, content, remove_stop=True):
        """
        普通分词
        :param content:
        :param remove_stop:是否移除停用词
        :return:
        """

    @abstractmethod
    def cut_count(self, content, size=128):
        """
        去除停用词分词返回统计数据
        :param content:
        :return:
        """
