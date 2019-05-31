#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File : mapping.py
Author : Zerui Qin
CreateDate : 2019-05-26 22:15:09 
Note : 
"""

from enum import Enum, unique


@unique
class Service(Enum):
    """
    服务名称
    """
    BASE_SERVICE = 'base_service'


@unique
class Route(Enum):
    """
    服务路由
    """
    AUTH = '/auth'
    HEARTBEAT = '/heartbeat'
    RESOURCE = '/resource'
