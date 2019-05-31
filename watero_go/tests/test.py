#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
File : test.py
Author : Zerui Qin
CreateDate : 2019-05-22 23:48:29 
Note : 
"""

from watero_go.agent_client import AgentClient
import threading

def bundle_send(p_data_service):
    p_data_service.heartbeat()
    p_data_service.resource()
    timer = threading.Timer(5, bundle_send,args=[p_data_service,])
    timer.start()

if __name__ == '__main__':
    agent_client = AgentClient('v1')
    data_service = agent_client.get_service('base_service')
    data_service.auth()
    bundle_send(data_service)

