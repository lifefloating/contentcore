# -*- coding: utf-8 -*-
# Created by yqq

def long2hex(lx):
    return hex(lx)[2:-1]

def hex2long(hx):
    hx = '0x%sL' % hx
    return long(hx, 16)