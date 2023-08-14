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
class GetCoordinatePoint(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
       
        corsHost = "124.223.125.136"
        corsPort = 8002
        mountPoint = "RTCM32_GRECJ2"
        username = "tsnrn8v9"
        password = "98193837"
        lat = 35.103973106
        lon = 117.409903771
        self.connectCors(corsHost, corsPort, mountPoint, username,
                        password, lat, lon)



    def getGGA(self,lat, lon):
        lat = math.floor(lat) * 100 + (lat - math.floor(lat)) * 60
        lon = math.floor(lon) * 100 + (lon - math.floor(lon)) * 60
        ggaTime = time.strftime("%H%M%S", time.gmtime(time.time()))
        gga = "GPGGA," + ggaTime + "," + \
            str(lat) + ",N," + str(lon) + ",E,3,15,2,100,M,2,M,6,0"
        # 计算校验码
        checkNum = ord(gga[0])
        for i in range(1, len(gga)):
            checkNum = checkNum ^ ord(gga[i])
        gga = "$" + gga + "*" + hex(checkNum)[2:].upper() + "\r\n"
        return gga

    def connectCors(self,corsHost, corsPort, mountPoint, username, password, lat=35.103973106, lon=117.409903771):

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((corsHost, corsPort))
        except Exception:
            print("连接cors失败")
            return 0

        request = f"GET /{mountPoint} HTTP/1.0\r\n"
        request += f"Host: {corsHost}:{corsPort}\r\n"
        request += f"User-Agent: NTRIP connect\r\n"
        request += f'Authorization: Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}\r\n'
        request += "Ntrip-Version: Ntrip/2.0\r\n"
        request += "\r\n"
        client_socket.sendall(request.encode())

        # 接收并打印服务器响应
        response = client_socket.recv(1024)
        print(response)

        # 第三步：计算并发送GGA数据

        gga = self.getGGA(lat, lon)
        client_socket.send(gga.encode('utf-8'))



        self.host = "192.168.1.53"
        self.port = 2222
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.connect((self.host, self.port))
        # 接收并打印流数据
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
          
            print(data)
            self.s_socket.send(data)

            # self.get_logger().info('I heard: "%s"' % msg.data)  
     
            gga = self.getGGA(lat, lon)
            client_socket.send(gga.encode('utf-8'))

        # 关闭连接
        client_socket.close()


def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = GetCoordinatePoint("getCoordinatePoint")   # 创建ROS2节点对象并进行初始化
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
