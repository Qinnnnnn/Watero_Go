#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File : setup.py
Author : Zerui Qin
CreateDate : 2018-12-06 10:00:00
LastModifiedDate : 2018-12-06 10:00:00
Note : 打包上传PyPi
"""

from setuptools import setup

setup(
    name='watero_go',
    version='0.0.1',
    author='Clever Moon',
    author_email='qzr19970105@live.com',
    url='https://github.com/Qinnnnnn/Watero_Go',
    description='节点数据采集并上传服务',
    packages=['watero_go', 'utils'],
    install_requires=['requests', 'psutil']
)
