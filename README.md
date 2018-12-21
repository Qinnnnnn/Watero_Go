# Watero Go

[![](https://img.shields.io/pypi/v/watero-go.svg)](https://pypi.org/project/watero-go/)
[![](https://img.shields.io/github/license/Qinnnnnn/Watero_Go.svg)](https://github.com/Qinnnnnn/Watero_Center/blob/master/LICENSE)
![](https://img.shields.io/badge/python-3.7-blue.svg)
* Watero Go是Watero Center部署于服务器的Agent服务
* Watero Go用于采集节点数据并上报Watero Center，同时接收Watero Center推送的控制信息
* [Watero Center](https://github.com/Qinnnnnn/Watero_Center)是一项数据接收、转发和投递集成服务

## 如何使用

#### 环境配置

* Python 3.7

#### 安装模块

```bash
pip install watero_go
```

依赖
* requests
* psutil

#### 启动服务

1. 导入Watero_Go模块
2. 配置Watero Center公网地址和服务端口
3. 调用相应的API上报日志数据和建立控制通道
