#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import rclpy                                     # ROS2 Python接口库
from rclpy.node import Node                      # ROS2 节点类
import time
from std_msgs.msg import ByteMultiArray 
import socket
import base64
import math
"""
创建一个HelloWorld节点, 初始化时输出“hello world”日志
"""
class NtripClient(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
        self.sub = self.create_subscription(ByteMultiArray , "chatter", self.listener_callback, 100)        # 创建订阅者对象（消息类型、话题名、订阅者回调函数、队列长度） 



    def listener_callback(self, msg):                             # 创建回调函数，执行收到话题消息后对数据的处理
        # self.get_logger().info('I heard: "%s"' % msg.data)        # 输出日志信息，提示订阅收到的话题消息

        # print(msg.data)
        b=b''.join(msg.data)
        print(b)

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = NtripClient("ntripClient")   # 创建ROS2节点对象并进行初始化
    rclpy.spin(node)  
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
