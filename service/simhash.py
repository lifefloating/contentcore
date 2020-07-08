# -*- coding: utf-8 -*-
# Created by yqq

__all__ = ['SimHash']
from abc import ABCMeta, abstractmethod


class SimHash(object):
    def __init__(self, **kwargs):
        """
        SimHash比较
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def adds(self, hashcode_set, size=128, db=None):
        """
        增加hashcode列表到库
        :param hashcode_set:
        :param size:
        :param db:
        :return:
        """
    @abstractmethod
    def remove(self, hashcode_set, size=128, db=None):
        """
        清除hashcode
        :param hashcode_set:
        :param size:
        :param db:
        :return:
        """

    @abstractmethod
    def hamming(self, hashcode, size=128, db=None):
        """
        获取hamming距离最小的值
        :param hashcode:
        :return:
        """

    @abstractmethod
    def hashcode(self, content, size=128):
        """
        获取给定内容的hashcode
        :param content:
        :param size:
        :return:
        """

    @abstractmethod
    def similarity(self, hashcode1, hashcode2):
        """
        比较两个数的相似度
        :param hashcode1:
        :param hashcode2:
        :return:
        """


