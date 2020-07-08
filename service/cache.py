# -*- coding: utf-8 -*-
# Created by yqq

__all__ = ['Cache']
from abc import ABCMeta, abstractmethod


class Cache(object):
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, key, value, expire=7200):
        """
        设置缓存
        :param key:
        :param value:
        :param expire:
        :return:
        """

    @abstractmethod
    def get(self, key, default=None):
        """
        获取缓存
        :param key:
        :param default:
        :return:
        """

    @abstractmethod
    def delete(self, key):
        """
        删除缓存
        :param key:
        :return:
        """

    @abstractmethod
    def delete_pattern(self, key_pattern):
        """
        批量删除缓存
        :param key_pattern:
        :return:
        """

    @abstractmethod
    def clear(self):
        """
        清除所有缓存
        :return:
        """

    @abstractmethod
    def expire(self, key, expire):
        """
        更改缓存时间
        :param key:
        :param expire:
        :return:
        """
