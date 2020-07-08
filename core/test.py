# -*- coding: utf-8 -*-
# Created by yqq

import doctest
import os
import sys


def doctest_start(package, project_dir):
    sys.path.append(project_dir)
    doctest_package(package, project_dir)


def doctest_package(package, project_dir):
    package = os.path.join(project_dir, package)
    files = os.listdir(package)
    for f in files:
        fp = os.path.join(package, f)
        sp = fp.replace(project_dir, '')[1:]
        if os.path.isfile(fp) and f.endswith('.py'):
            cls = sp[:-3].replace('/', '.')
            if cls.endswith('__init__'):
                cls = cls[:-9]
            pos = cls.rfind('.')
            pg = cls[:pos]
            name = cls[pos+1:]
            m = __import__(cls, globals(), locals(), '.', -1)
            print('===================>>test:%s' % m)
            h = doctest.testmod(m=m, verbose=True)

            assert h.failed == 0, 'failed:%s' % h.failed

        elif os.path.isdir(fp):
            doctest_package(sp, project_dir)