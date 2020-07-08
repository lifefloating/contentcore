# -*- coding: utf-8 -*-

import hashlib
import time
import uuid


def hash_uuid():
    return hashlib.md5('%s.%s' % (str(uuid.uuid4()), time.time())).hexdigest()


if __name__ == "__main__":
    import doctest

    doctest.testmod()