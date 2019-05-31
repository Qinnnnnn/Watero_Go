#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File : agent_client.py
Author : Zerui Qin
CreateDate : 2018-12-20 10:00:00
LastModifiedDate : 2018-12-20 10:00:00
Note : Agent客户端类, 获取Agent相关服务
"""

from watero_go.services.base_service import BaseService
from watero_go.utils.error import ServiceException
from watero_go.utils.mapping import Service


class AgentClient:
    """
    Agent客户端
    """

    def __init__(self, p_api_version, p_host='http://api.clevermoon.tk', p_port=5000):
        """
        初始化
        :param p_api_version: API版本: v1, v2, etc...
        :param p_host: Center服务公网地址
        :param p_port: Center服务端口号
        """
        self.api_version = p_api_version
        self.host = p_host
        self.port = p_port
        self.url_prefix = self.host + ':' + str(self.port) + '/api/' + self.api_version

    def get_service(self, p_service):
        """
        获取Agent相关服务
        :param p_service: 服务名称
        :return:
        """
        if p_service == Service.BASE_SERVICE.value:
            return BaseService(self.url_prefix)
        else:
            raise ServiceException(p_service)
