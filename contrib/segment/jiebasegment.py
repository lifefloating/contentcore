# -*- coding: utf-8 -*-
from collections import Counter

import jieba


__all__ = ['JiebaSegment']

from contentcore.service.segment import Segment
from contentcore import settings


class JiebaSegment(Segment):
    """
    结巴分词
    >>> seg = JiebaSegment()
    >>> ex = seg.cut('我是中国人', remove_stop=False)
    >>> ('/'.join(ex)).decode()
    u'\u6211/\u662f/\u4e2d\u56fd/\u4eba'
    >>> ex = seg.cut('我是中国人')
    >>> ('/'.join(ex)).decode()
    u'\u4e2d\u56fd/\u4eba'
    >>> ex = seg.cut_count('中国人民是中国人')
    >>> '/'.join([e[0] for e in ex])
    u'\u4e2d\u56fd/\u4eba'
    >>> '/'.join([str(e[1]) for e in ex])
    '2/1'

    """

    def __init__(self, **kwargs):
        super(JiebaSegment, self).__init__(**kwargs)
        default_setting = settings.SEGMENT_CONTENT_PARAMS
        self._jieba_dict = kwargs.get('dict') or default_setting.get('dict')
        self._stopwords_dict = kwargs.get('stopwords') or default_setting.get('stopwords')
        log_level = kwargs.get('log_level') or default_setting.get('log_level')
        if log_level:
            jieba.setLogLevel(log_level)

    _stopwords = None
    _load_dict = False

    @property
    def stopwords(self):
        if not self._stopwords:
            with open(self._stopwords_dict, 'r') as f:
                self._stopwords = [unicode(s) for s in f.read().split('\n')]
        return self._stopwords

    def cut_count(self, content, size=128):
        seg_list = self.cut(content)
        if len(seg_list) > 128:
            seg_list = [word for word in seg_list if len(word) >= 2]
        c = Counter(seg_list)
        words = c.most_common(size)
        return words

    def cut(self, content, remove_stop=True):
        """
        分词
        :param content:
        :param remove_stop:
        :return:
        """
        if not self._load_dict and self._jieba_dict:
            jieba.load_userdict(self._jieba_dict)
            self._load_dict = True
            # logger.debug('loaded dict')
        seg_list = [w for w in jieba.cut(content, cut_all=False) if w.strip()]
        # logger.debug(' '.join(seg_list))
        if remove_stop:
            stop_tiny = list(set(seg_list) & set(self.stopwords))
            # logger.debug(' '.join(stop_tiny))
            seg_list = [s for s in seg_list if s not in stop_tiny]
        # logger.debug(' '.join(seg_list))
        return seg_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()