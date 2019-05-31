#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File : hardware.py
Author : Zerui Qin
CreateDate : 2018-12-06 10:00:00
LastModifiedDate : 2018-12-06 10:00:00
Note : 获取本机MAC地址
"""

import uuid


def get_mac_address(is_format=True):
    """
    获取本机MAC地址
    :param is_format: Boolean - 是否以冒号分隔MAC地址
    :return: str - MAC地址
    """
    node = uuid.getnode()  # 获取硬件编码
    mac_addr = uuid.UUID(int=node).hex[-12:].upper()  # 获取大写MAC地址，不包含分割符
    if is_format:
        mac_addr_list = list()
        flag = 0
        for i in mac_addr:
            mac_addr_list.append(i)
            flag = flag + 1
            if flag == 2:
                mac_addr_list.append(':')
                flag = 0
        mac_addr_list.pop(-1)
        mac_addr_format = ''.join(mac_addr_list)
        return mac_addr_format
    else:
        return mac_addr
