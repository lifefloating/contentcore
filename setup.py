# -*- coding: utf-8 -*-
# Created by yqq

from os.path import dirname, join

from setuptools import setup, find_packages

project_dir = dirname(__file__)

with open(join(project_dir, 'VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name="contentcore",
    maintainer='yqq',
    platforms=["any"],
    maintainer_email='imshuazi@126.com',
    version=version,
    description="内容处理包",
    author="yqq",
    url="https://github.com/lifefloating/express-scaffold",
    license="GPL",
    include_package_data=True,
    packages=find_packages(exclude=()),
    long_description=open(join(project_dir, 'README.md')).read(),

    install_requires=['pybloomfiltermmap', 'redis', 'jieba', 'mmh3', 'debug-log', 'six'],
)