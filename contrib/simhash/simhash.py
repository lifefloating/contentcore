# -*- coding: utf-8 -*-

import mmh3
from contentcore import instance


class LvSimHash:

    def __init__(self, tokens, bits=128):
        self.bits = bits
        self.hash = self.simhash(tokens)

    def __str__(self):
        return str(self.hash)

    def simhash(self, tokens):
        v = [0] * self.bits
        for x in [x for x in tokens]:
            c = x[0]
            if self.bits == 128:
                t = mmh3.hash128(c)

            elif self.bits == 64:
                t = mmh3.hash64(c)[0]
            else:
                t = mmh3.hash(c)

            w = x[1]
            for i in range(self.bits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += w  # 查看当前bit位是否为1,是的话将该位+1
                else:
                    v[i] -= w  # 否则的话,该位-1
        fingerprint = 0
        for i in range(self.bits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint  # 整个文档的fingerprint为最终各个位>=0的和


def hamming_lib(hashcode, hashlib):
    m = 256
    ml = 0
    for i in hashlib:
        x = (hashcode ^ i)
        c = 0
        while x:
            c += 1
            x &= x - 1
        if c < m:
            m = c
            ml = i
        if m == 0:
            break
    return m, ml


def simhash_instance(content, size=128):
    if not isinstance(content, unicode):
        content = unicode(content)
    content = content.lower()
    tokens = instance().segment.cut_count(content, size=size)
    # print(tokens)
    return LvSimHash(tokens, bits=size)
