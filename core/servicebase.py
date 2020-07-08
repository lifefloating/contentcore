# -*- coding: utf-8 -*-
# Created by yqq


from abc import ABCMeta, abstractmethod


class DbServiceBase(object):
    """
    数据的相关基于操作实现
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, **kwargs):
        """
        初使化
        :return:
        """

    @abstractmethod
    def add(self, documents):
        """
        增加存储
        :param documents:
        :return:num
        """

    @abstractmethod
    def get(self, _id=None):
        """
        指定获取某记录
        :param _id:
        :return:document or None
        """

    @abstractmethod
    def update(self, documents):
        """
        更新数据，根据_id为主键，修改documents
        :param documents:
        :return:num
        """
    @abstractmethod
    def update_values(self, documents,):
        """
        更新指定数据列
        :param documents:
        :return:
        """


    @abstractmethod
    def save(self, documents):
        """
        保存数据
        :param documents:
        :return:
        """

    @abstractmethod
    def list(self, pagesize=100, page=1):
        """
        分页获取document信息
        :param pagesize:
        :param page:
        :return:list
        """

    @abstractmethod
    def count(self):
        """
        统计记录数
        :return:num
        """

    @abstractmethod
    def remove(self, documents):
        """
        根据_id删除记录集
        :param documents:
        :return:num
        """
    @abstractmethod
    def fetch(self, *ids):
        """
        获取指定_id序列的记录集
        :param ids:
        :return:
        """
    @abstractmethod
    def filter(self, **kv):
        """
        获取指定kv序列的记录集
        :param kv:
        :return:
        """