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
class NtripServerByCors(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
       
        self.host = "192.168.1.53"
        self.port = 3333
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))

        while True:
            data =sock.recv(1024)
            if not data:
                break
            # 处理接收到的数据
            # print(data)
            line = data.decode("utf-8")
            parts = line.split(",")
            if(parts[0]=="$GPGGA"):
                # print(line)
                # print(parts[6])
                if(parts[6]==""):
                    print("搜索信号")
                    ws = []
                    ls = []
                    hs = []
                    n = 0
                    continue
                if(parts[6]=="0"):
                    print("未定位")
                if(parts[6]=="1"):
                    print("单点定位")

                if(parts[6]=="2"):
                    print("差分GPS定位解")
                if(parts[6]=="3"):
                    print("PPS定位解")
                if(parts[6]=="4"):
                    print("RTK固定解")
                if(parts[6]=="5"):
                    print("RTK浮点解")
                if(parts[6]=="6"):
                    print("估算模式")
                w = float(parts[2])
                w = self.DDmm2D(w)
                l = float(parts[4])
                l = self.DDmm2D(l)
                h =float(parts[9])+float(parts[11])
                print("("+str(w)+","+str(l)+","+str(h)+")")

              

    def DDmm2D(self,ddmm):
        dd = str(ddmm).split(".")[0][0:-2]
        mm = str(ddmm).split(".")[0][-2:]+"."+str(ddmm).split(".")[1]
        dd = float(dd)
        mm = float(mm)
        d = dd + mm/60
        return d



def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = NtripServerByCors("ntripServerByCors")   # 创建ROS2节点对象并进行初始化
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
