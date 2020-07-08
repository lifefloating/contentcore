# -*- coding: utf-8 -*-

import unittest


class DocTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_service(self):
        import os
        project_dir = os.path.dirname(os.path.dirname(__file__))
        from contentcore.core import test
        test.doctest_start('contentcore', project_dir)

if __name__ == '__main__':
    unittest.main()








