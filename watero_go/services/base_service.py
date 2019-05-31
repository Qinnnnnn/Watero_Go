#!/usr/bin/pythonr
# -*- coding: utf-8 -*-

"""
File : base_service.py
Author : Zerui Qin
CreateDate : 2018-12-20 10:00:00
LastModifiedDate : 2018-12-20 10:00:00
Note : Agent基础服务类, 获取Agent数据服务相关方法
"""
import time

import psutil
import requests

from watero_go.utils import hardware
from watero_go.utils.log import log_debug
from watero_go.utils.mapping import Route


class BaseService:
    """
    Agent基础服务
    """

    def __init__(self, p_url_prefix):
        """
        初始化
        :param p_url_prefix: 中心服务地址前缀
        """
        self.url_prefix = p_url_prefix
        self.mac_addr = hardware.get_mac_address()
        self.access_token = ''

    def auth(self):
        """
        Agent认证
        :return: int - 响应状态码
        """
        payload = dict()
        payload['mac_addr'] = self.mac_addr

        response = requests.get(url=self.url_prefix + Route.AUTH.value, data=payload)
        res_json = response.json()
        status = res_json['status']
        if response.status_code:  # 服务器状态码为200
            self.access_token = res_json['message']['access_token']
            log_debug.logger.info(res_json['message']['access_token'])
        elif response.status_code == 403:
            log_debug.logger.info(res_json['message'])
        return status

    def heartbeat(self):
        """
        发送Agent心跳信息
        :return: int - 响应状态码
        """
        payload = dict()
        payload['mac_addr'] = self.mac_addr
        payload['access_token'] = self.access_token
        payload['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        response = requests.post(url=self.url_prefix + Route.HEARTBEAT.value, data=payload)
        res_json = response.json()
        status = res_json['status']
        if response.status_code == 200:  # 服务器状态码为200
            log_debug.logger.info(res_json['message'])
        elif response.status_code == 403:  # 服务器状态码为403
            log_debug.logger.error(res_json['message'])
        return status

    def resource(self):
        """
        发送Agent设备资源信息
        :return: int - 响应状态码
        """
        payload = dict()
        payload['mac_addr'] = self.mac_addr
        payload['access_token'] = self.access_token
        payload['cpu_percent'] = psutil.cpu_percent()  # CPU占用率
        payload['cpu_count'] = psutil.cpu_count(logical=False)  # CPU非逻辑核心数
        payload['cpu_freq_current'] = psutil.cpu_freq()[0]  # CPU当前频率
        payload['total_memory'] = int(psutil.virtual_memory()[0] / 1024 / 1024)  # 总内存
        payload['available_memory'] = int(psutil.virtual_memory()[1] / 1024 / 1024)  # 可用内存
        payload['sensors_battery_percent'] = psutil.sensors_battery()  # 电量百分比
        payload['boot_time'] = psutil.datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
            "%Y-%m-%d %H:%M:%S")  # 启动时间
        payload['create_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        response = requests.post(url=self.url_prefix + Route.RESOURCE.value, data=payload)
        res_json = response.json()
        status = res_json['status']
        if response.status_code == 200:  # 服务器状态码为200
            log_debug.logger.info(res_json['message'])
        elif response.status_code == 403:  # 服务器状态码为403
            log_debug.logger.error(res_json['message'])
        else:
            log_debug.logger.error('Unknown error')
        return status
