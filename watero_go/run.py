#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File : run.py
Author : Zerui Qin
CreateDate : 2019-05-22 23:48:29 
Note : 
"""

import threading

from .agent_client import AgentClient


def bundle_send(p_data_service):
    try:
        h_status = p_data_service.heartbeat()
        r_status = p_data_service.resource()
    except Exception as e:
        pass
    timer = threading.Timer(60, bundle_send, args=[p_data_service, ])
    timer.start()


if __name__ == '__main__':
    client = AgentClient('v1')
    data_service = client.get_service('base_service')
    data_service.auth()
    bundle_send(data_service)
