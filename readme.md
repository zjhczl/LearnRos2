- [1. ros2安装与卸载](#1-ros2安装与卸载)
  - [1.1. 安装ros2](#11-安装ros2)
  - [1.2. 卸载ros2](#12-卸载ros2)
- [2. 基础工具](#2-基础工具)
  - [2.1. 节点](#21-节点)
    - [2.1.1. 启动节点](#211-启动节点)
    - [2.1.2. 获取节点信息](#212-获取节点信息)
  - [2.2. topics](#22-topics)
    - [2.2.1. 显示所有topic](#221-显示所有topic)
    - [2.2.2. 查看某个主题上发布的数据](#222-查看某个主题上发布的数据)
    - [2.2.3. 查看数据结构](#223-查看数据结构)
    - [2.2.4. 发布主题](#224-发布主题)
  - [2.3. services](#23-services)
    - [2.3.1. 获取服务列表](#231-获取服务列表)
    - [2.3.2. 查看服务类型](#232-查看服务类型)
    - [2.3.3. 服务查找](#233-服务查找)
    - [2.3.4. 查看服务参数的结构](#234-查看服务参数的结构)
    - [2.3.5. 服务调用](#235-服务调用)
  - [2.4. 参数](#24-参数)
    - [2.4.1. 获取节点参数列表](#241-获取节点参数列表)
    - [2.4.2. 参数获取](#242-参数获取)
    - [2.4.3. 设置参数值](#243-设置参数值)
    - [2.4.4. 参数转存](#244-参数转存)
    - [2.4.5. 加载参数](#245-加载参数)
    - [2.4.6. 启动时加载参数文件](#246-启动时加载参数文件)
  - [2.5. 动作](#25-动作)
    - [2.5.1. 列出所有action](#251-列出所有action)
    - [2.5.2. 查看action信息](#252-查看action信息)
    - [2.5.3. action操作类型](#253-action操作类型)
    - [2.5.4. 发送动作](#254-发送动作)
  - [2.6. ros bag](#26-ros-bag)
    - [2.6.1. 记录包](#261-记录包)
    - [2.6.2. 查看包录制信息](#262-查看包录制信息)
    - [2.6.3. 包回放](#263-包回放)
- [3. 客户端库](#3-客户端库)
  - [3.1. 用于colcon构建包](#31-用于colcon构建包)
    - [3.1.1. 安装 colcon](#311-安装-colcon)
    - [3.1.2. 创建工作区](#312-创建工作区)
    - [3.1.3. 构建工作区](#313-构建工作区)
    - [3.1.4. 运行测试](#314-运行测试)
    - [3.1.5. colcon\_cd](#315-colcon_cd)
    - [3.1.6. ~~](#316-)
  - [3.2. 创建工作区](#32-创建工作区)
    - [3.2.1. 新建文件夹](#321-新建文件夹)
    - [3.2.2. 克隆一个样本仓库](#322-克隆一个样本仓库)
    - [3.2.3. 解决依赖](#323-解决依赖)
    - [3.2.4. 使用 colcon 构建工作区](#324-使用-colcon-构建工作区)
    - [3.2.5. 源覆盖](#325-源覆盖)
    - [3.2.6. 总结](#326-总结)
  - [3.3. 创建package](#33-创建package)
    - [3.3.1. 什么是 ROS 2 包？](#331-什么是-ros-2-包)
    - [3.3.2. 一个package包含什么](#332-一个package包含什么)
    - [3.3.3. 工作区中的包](#333-工作区中的包)
    - [3.3.4. 创建package](#334-创建package)
    - [3.3.5. build package](#335-build-package)
    - [3.3.6. Source the setup file](#336-source-the-setup-file)
    - [3.3.7. 使用包](#337-使用包)
    - [3.3.8. 修改package.xml setup.py文件](#338-修改packagexml-setuppy文件)
  - [3.4. 编写简单的发布者和订阅者](#34-编写简单的发布者和订阅者)
    - [3.4.1. 编写发布者节点](#341-编写发布者节点)
    - [3.4.2. 添加入口点](#342-添加入口点)
    - [3.4.3. 构建运行节点](#343-构建运行节点)
  - [3.5. 编写简单的服务和客户端](#35-编写简单的服务和客户端)
    - [3.5.1. 建立package](#351-建立package)
    - [3.5.2. 编写节点服务](#352-编写节点服务)
    - [3.5.3. 编写客户端节点](#353-编写客户端节点)
    - [3.5.4. 构建并运行](#354-构建并运行)
      - [3.5.4.1. 启动服务](#3541-启动服务)
      - [3.5.4.2. 启动客户端](#3542-启动客户端)
  - [3.6. 创建自定义 msg 和 srv 文件](#36-创建自定义-msg-和-srv-文件)
    - [3.6.1. msg 自定义](#361-msg-自定义)
    - [3.6.2. srv定义](#362-srv定义)
    - [3.6.3. 修改CMakeLists.txt](#363-修改cmakeliststxt)
    - [3.6.4. 修改package.xml](#364-修改packagexml)
    - [3.6.5. 构建tutorial\_interfaces包](#365-构建tutorial_interfaces包)
    - [3.6.6. 在包中使用自定义的msg](#366-在包中使用自定义的msg)
    - [3.6.7. 在包中使用srv](#367-在包中使用srv)
  - [3.7. 实现自定义接口](#37-实现自定义接口)
    - [3.7.1. 背景](#371-背景)
    - [3.7.2. 创建一个package](#372-创建一个package)
    - [3.7.3. 2 创建消息文件](#373-2-创建消息文件)
    - [3.7.4. 构建一个msg文件](#374-构建一个msg文件)
  - [3.8. 在类中使用参数 (Python)](#38-在类中使用参数-python)
    - [3.8.1. 创建package](#381-创建package)
    - [编写python节点](#编写python节点)
    - [添加入口点](#添加入口点)
  - [创建和使用插件 (C++)](#创建和使用插件-c)
    - [背景](#背景)
    - [安装pluginlib](#安装pluginlib)
    - [任务](#任务)
    - [创建基本package](#创建基本package)

## 1. ros2安装与卸载
### 1.1. 安装ros2
设置语言环境
```
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```
将 ROS 2 apt 存储库添加到您的系统
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
使用 apt 添加 ROS 2 GPG 密钥
```
sudo apt update && sudo apt install curl
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
将存储库添加到您的源列表中
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
安装ros2
```
sudo apt update
sudo apt upgrade
sudo apt install ros-rolling-desktop
sudo apt install ros-rolling-ros-base
sudo apt install ros-dev-tools
```
设置环境
```
# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/rolling/setup.bash
```
将 sourcing 添加到您的 shell 启动脚本.如果您不想每次打开一个新的 shell 时都必须获取安装文件（跳过任务 1），那么您可以将命令添加到您的 shell 启动脚本中：
```
echo "source /opt/ros/rolling/setup.bash" >> ~/.bashrc
```

### 1.2. 卸载ros2
```
sudo apt remove ~nros-rolling-* && sudo apt autoremove
sudo rm /etc/apt/sources.list.d/ros2.list
sudo apt update
sudo apt autoremove
# Consider upgrading for packages previously shadowed.
sudo apt upgrade
```
## 2. 基础工具
### 2.1. 节点
ROS 中的每个节点都应该负责一个单一的模块用途（例如，一个节点用于控制车轮电机，一个节点用于控制激光测距仪等）。每个节点都可以通过主题、服务、操作或参数向其他节点发送和接收数据。
#### 2.1.1. 启动节点
```
ros2 run <package_name> <executable_name>
```
例子:
```
ros2 run turtlesim turtlesim_node
```
#### 2.1.2. 获取节点信息
```
ros2 node info <node_name>
ros2 node info /my_turtle

```
### 2.2. topics
#### 2.2.1. 显示所有topic
```
ros2 topic list
```
ros2 topic list -t将返回相同的主题列表，这次主题类型附加在括号中
#### 2.2.2. 查看某个主题上发布的数据
```
ros2 topic echo <topic_name>
ros2 topic echo /turtle1/cmd_vel
```
话题不必只是点对点的交流；它可以是一对多、多对一或多对多。另一种看待这个问题的方法是运行：
```
ros2 topic info /turtle1/cmd_vel
```
#### 2.2.3. 查看数据结构
```
ros2 interface show geometry_msgs/msg/Twist
```
#### 2.2.4. 发布主题
参数'<args>'是您将传递给主题的实际数据，采用您刚刚在上一节中发现的结构。请务必注意，此参数需要以 YAML 语法输入。像这样输入完整的命令：
```
ros2 topic pub <topic_name> <msg_type> '<args>'
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
--once是一个可选参数，意思是“发布一条消息然后退出”。

### 2.3. services
#### 2.3.1. 获取服务列表
```
ros2 service list -t
```
-t会列出所有活动服务的类型
#### 2.3.2. 查看服务类型
```
ros2 service type <service_name>
ros2 service type /clear
```
返回std_srvs/srv/Empty
#### 2.3.3. 服务查找
```
ros2 service find <type_name>
ros2 service find std_srvs/srv/Empty
```
返回/clear /reset
#### 2.3.4. 查看服务参数的结构
```
ros2 interface show <type_name>
ros2 interface show std_srvs/srv/Empty
```
#### 2.3.5. 服务调用
```
ros2 service call <service_name> <service_type> <arguments>
ros2 service call /clear std_srvs/srv/Empty
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```
### 2.4. 参数
#### 2.4.1. 获取节点参数列表
```
ros2 param list
```
#### 2.4.2. 参数获取
```
ros2 param get <node_name> <parameter_name>
ros2 param get /turtlesim background_g
```
#### 2.4.3. 设置参数值
```
ros2 param set <node_name> <parameter_name> <value>
ros2 param set /turtlesim background_r 150
```
#### 2.4.4. 参数转存
显示节点所有参数
```
ros2 param dump <node_name>
```
将参数存储成文件
```
ros2 param dump /turtlesim > turtlesim.yaml
```
#### 2.4.5. 加载参数
```
ros2 param load <node_name> <parameter_file>
ros2 param load /turtlesim turtlesim.yaml
```
#### 2.4.6. 启动时加载参数文件

```
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim.yaml
```
### 2.5. 动作
动作是 ROS 2 中的一种通信类型，用于长时间运行的任务。它们由三部分组成：目标、反馈和结果。操作基于主题和服务。它们的功能类似于服务，除了可以取消操作。他们还提供稳定的反馈，而不是返回单一响应的服务。操作使用客户端-服务器模型，类似于发布者-订阅者模型（在主题教程中描述）。“动作客户端”节点将目标发送到“动作服务器”节点，该节点确认目标并返回反馈流和结果。
#### 2.5.1. 列出所有action
```
ros2 action list -t
```
返回/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
#### 2.5.2. 查看action信息
```
ros2 action info /turtle1/rotate_absolute
```
返回:
```
Action: /turtle1/rotate_absolute
Action clients: 1
    /teleop_turtle
Action servers: 1
    /turtlesim
```
这告诉我们之前在每个节点上运行时学到的东西：节点有一个动作客户端，节点有一个用于动作的动作服务器。
#### 2.5.3. action操作类型
```
ros2 interface show turtlesim/action/RotateAbsolute
```
```
The desired heading in radians
float32 theta
---
The angular displacement in radians to the starting position
float32 delta
---
The remaining rotation in radians
float32 remaining
```
此消息的第一部分，在 之上---，是目标请求的结构（数据类型和名称）。下一部分是结果的结构。最后一部分是反馈的结构。
#### 2.5.4. 发送动作
```
ros2 action send_goal <action_name> <action_type> <values>
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
```
```
Waiting for an action server to become available...
Sending goal:
   theta: 1.57

Goal accepted with ID: f8db8f44410849eaa93d3feb747dd444

Result:
  delta: -1.568000316619873

Goal finished with status: SUCCEEDED
```
要查看此目标的反馈，请--feedback在命令中添加：ros2 action send_goal
```
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback
```
```
Sending goal:
   theta: -1.57

Goal accepted with ID: e6092c831f994afda92f0086f220da27

Feedback:
  remaining: -3.1268222332000732

Feedback:
  remaining: -3.1108222007751465

…

Result:
  delta: 3.1200008392333984

Goal finished with status: SUCCEEDED
```
### 2.6. ros bag
#### 2.6.1. 记录包
```
ros2 bag record <topic_name>
ros2 bag record /turtle1/cmd_vel
ros2 bag record -o subset /turtle1/cmd_vel /turtle1/pose
```
-o选项允许您为包文件选择一个唯一的名称。在本例中，以下字符串subset是文件名。
#### 2.6.2. 查看包录制信息
```
ros2 bag info <bag_file_name>
```
#### 2.6.3. 包回放
```
ros2 bag play subset
```
## 3. 客户端库
### 3.1. 用于colcon构建包
#### 3.1.1. 安装 colcon
```
sudo apt install python3-colcon-common-extensions
```
#### 3.1.2. 创建工作区
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
git clone https://github.com/ros2/examples src/examples -b rolling

```
目录结构
```
.
└── src
    └── examples
        ├── CONTRIBUTING.md
        ├── LICENSE
        ├── rclcpp
        ├── rclpy
        └── README.md

4 directories, 3 files
```
#### 3.1.3. 构建工作区

```
colcon build --symlink-install
```
#### 3.1.4. 运行测试
```
colcon test
```
当 colcon 成功完成构建时，输出将在install目录中。在您可以使用任何已安装的可执行文件或库之前，您需要将它们添加到您的路径和库路径中。colcon 将在目录中生成 bash/bat 文件install以帮助设置环境。这些文件会将所有必需的元素添加到您的路径和库路径中，并提供包导出的任何 bash 或 shell 命令。
```
. install/setup.bash
```
#### 3.1.5. colcon_cd
该命令colcon_cd允许您快速将 shell 的当前工作目录更改为包的目录。
#### 3.1.6. ~~
### 3.2. 创建工作区
#### 3.2.1. 新建文件夹
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
#### 3.2.2. 克隆一个样本仓库
```
git clone https://github.com/ros/ros_tutorials.git -b rolling-devel
```
#### 3.2.3. 解决依赖
在构建工作区之前，您需要解决包依赖关系。您可能已经拥有所有依赖项，但最佳做法是在每次克隆时检查依赖项。您不希望构建由于缺少依赖项而在长时间等待后失败。


```
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
rosdep install -i --from-path src --rosdistro rolling -y
```
#### 3.2.4. 使用 colcon 构建工作区
```
colcon build
```
其他有用的参数：colcon build

--packages-up-to构建你想要的包，加上它的所有依赖项，但不是整个工作区（节省时间）

--symlink-install使您不必每次调整 python 脚本时都必须重建

--event-handlers console_direct+在构建时显示控制台输出（否则可以在目录中找到log）
#### 3.2.5. 源覆盖
在采购叠加层之前，打开一个新终端非常重要，与您构建工作区的终端分开。在您构建的同一终端中获取覆盖层，或者同样在覆盖层来源处构建，可能会产生复杂的问题。

在新终端中，将你的主要 ROS 2 环境作为“底层”，这样你就可以在它“之上”构建覆盖层：
```
source /opt/ros/rolling/setup.bash
cd ~/ros2_ws
. install/local_setup.bash
```
#### 3.2.6. 总结
在本教程中，您将主要的 ROS 2 发行版安装作为底层，并通过在新工作区中克隆和构建包来创建覆盖层。正如您在修改后的 turtlesim 中看到的那样，覆盖层被添加到路径之前，并优先于底层。

建议在处理少量包时使用覆盖，这样您就不必将所有内容都放在同一个工作区中，也不必在每次迭代时都重建一个巨大的工作区。
### 3.3. 创建package
#### 3.3.1. 什么是 ROS 2 包？
一个包可以被认为是你的 ROS 2 代码的容器。如果您希望能够安装您的代码或与他人共享，那么您需要将其组织在一个包中。借助软件包，您可以发布您的 ROS 2 作品并允许其他人轻松构建和使用它。
ROS 2 中的包创建使用 ament 作为其构建系统，并使用 colcon 作为其构建工具。您可以使用官方支持的 CMake 或 Python 创建包，但确实存在其他构建类型。
#### 3.3.2. 一个package包含什么
```
package.xml包含有关包的元信息的文件

setup.py包含有关如何安装软件包的说明

setup.cfg当一个包有可执行文件时是必需的，所以可以找到它们ros2 run

/<package_name>- 与您的包同名的目录，ROS 2 工具使用它来查找您的包，包含__init__.py
```
最简单的包可能具有如下所示的文件结构：
```
my_package/
      setup.py
      package.xml
      resource/my_package
```
#### 3.3.3. 工作区中的包
一个工作区可以包含任意数量的包，每个包都在自己的文件夹中。您还可以在一个工作区（CMake、Python 等）中包含不同构建类型的包。你不能有嵌套的包。

最佳做法是在您的工作区中有一个src文件夹，并在其中创建您的包。这使工作区的顶层保持“干净”。

一个普通的工作区可能看起来像：
```
workspace_folder/
    src/
      package_1/
          CMakeLists.txt
          package.xml

      package_2/
          setup.py
          package.xml
          resource/package_2
      ...
      package_n/
          CMakeLists.txt
          package.xml
```

#### 3.3.4. 创建package
进入src目录
```
cd ~/ros2_ws/src
```
创建package
```
ros2 pkg create --build-type ament_python <package_name>
ros2 pkg create --build-type ament_python --node-name my_node my_package
```
#### 3.3.5. build package
将包放在工作区中特别有价值，因为您可以通过在工作区根目录中运行来一次构建多个包。否则，您将不得不单独构建每个包。colcon build
```
cd ~/ros2_ws
colcon build
```
只构建一个包
```
colcon build --packages-select my_package
```
#### 3.3.6. Source the setup file
```
. install/local_setup.bash
```
#### 3.3.7. 使用包
```
ros2 run my_package my_node
```
#### 3.3.8. 修改package.xml setup.py文件
```
<description>Beginner client libraries tutorials practice package</description>
<license>Apache License 2.0</license>
```
### 3.4. 编写简单的发布者和订阅者
在src目录
```
ros2 pkg create --build-type ament_python py_pubsub
```
#### 3.4.1. 编写发布者节点
导航到ros2_ws/src/py_pubsub/py_pubsub. 回想一下，这个目录是一个Python 包，与它嵌套在其中的 ROS 2 包同名。
通过输入以下命令下载示例 talker 代码：
```
wget https://raw.githubusercontent.com/ros2/examples/rolling/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
```
#### 3.4.2. 添加入口点
```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},

```
#### 3.4.3. 构建运行节点

```
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select py_pubsub
. install/setup.bash
ros2 run py_pubsub talker
```
### 3.5. 编写简单的服务和客户端
#### 3.5.1. 建立package
```
ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces
```
该--dependencies参数会自动将必要的依赖行添加到package.xml. 
因为您--dependencies在包创建期间使用了该选项，所以您不必手动将依赖项添加到package.xml.
不过，一如既往，请确保将描述、维护者电子邮件和姓名以及许可证信息添加到package.xml.
#### 3.5.2. 编写节点服务
ros2_ws/src/py_srvcli/py_srvcli目录中，创建一个名为的新文件service_member_function.py
```python
from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        # 类型 名称 回调
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
要允许命令运行您的节点，您必须将入口点添加到（位于目录中）。ros2 run setup.py


#### 3.5.3. 编写客户端节点
在该ros2_ws/src/py_srvcli/py_srvcli目录中，创建一个名为的新文件client_member_function.py并将以下代码粘贴到其中：
```python
import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
与服务节点一样，您还必须添加一个入口点才能运行客户端节点。
```
entry_points={
    'console_scripts': [
        'service = py_srvcli.service_member_function:main',
        'client = py_srvcli.client_member_function:main',
    ],
},
```
#### 3.5.4. 构建并运行
##### 3.5.4.1. 启动服务
```
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select py_srvcli
. install/setup.bash
ros2 run py_srvcli service
```
##### 3.5.4.2. 启动客户端
```
ros2 run py_srvcli client 2 3

```

### 3.6. 创建自定义 msg 和 srv 文件
因为python无法自定义msg，所以只能使用c++来实现
在ros2_ws/src目录创建用c++语言package
```
ros2 pkg create --build-type ament_cmake tutorial_interfaces
```
#### 3.6.1. msg 自定义
在tutorial_interfaces/msg您刚刚创建的目录中，创建一个新文件，Num.msg使用一行代码声明其数据结构：
```
int64 num
```
这是一条自定义消息，它传输一个名为 的 64 位整数num。

同样在tutorial_interfaces/msg您刚刚创建的目录中，创建一个名为Sphere.msg以下内​​容的新文件：
```
geometry_msgs/Point center
float64 radius
```
此自定义消息使用来自另一个消息包的消息（geometry_msgs/Point在本例中）。

#### 3.6.2. srv定义
回到tutorial_interfaces/srv您刚刚创建的目录，创建一个新文件，AddThreeInts.srv使用以下请求和响应结构调用：
```
int64 a
int64 b
int64 c
---
int64 sum
```
是您的自定义服务，它请求名为 、 和 的三个整数a，b并c以名为 的整数响应sum。
#### 3.6.3. 修改CMakeLists.txt
添加下面内容
```find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)


```
#### 3.6.4. 修改package.xml
因为接口依赖rosidl_default_generators于生成特定于语言的代码，所以您需要声明对它的依赖。标签<exec_depend>用于指定运行时或执行阶段的依赖关系，是rosidl_interface_packages包所属的依赖组的名称，使用标签声明<member_of_group>。
```
<depend>geometry_msgs</depend>

<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```
#### 3.6.5. 构建tutorial_interfaces包

```
colcon build --packages-select tutorial_interfaces
. install/setup.bash
ros2 interface show tutorial_interfaces/msg/Num
ros2 interface show tutorial_interfaces/msg/Sphere
ros2 interface show tutorial_interfaces/srv/AddThreeInts
```
#### 3.6.6. 在包中使用自定义的msg
```python
import rclpy
from rclpy.node import Node
# 引入消息
from tutorial_interfaces.msg import Num                            # CHANGE


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        #使用消息
        self.publisher_ = self.create_publisher(Num, 'topic', 10)  # CHANGE
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()                                                # CHANGE
        msg.num = self.i                                           # CHANGE
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.num)       # CHANGE
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
#### 3.6.7. 在包中使用srv

```python
from tutorial_interfaces.srv import AddThreeInts                                                           # CHANGE

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)       # CHANGE

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c                                                   # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))  # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
### 3.7. 实现自定义接口
#### 3.7.1. 背景
在之前的教程中，您学习了如何创建自定义 msg 和 srv 接口。

虽然最佳实践是在专用接口包中声明接口，但有时在一个包中声明、创建和使用一个接口会很方便。

回想一下，接口目前只能在 CMake 包中定义。但是，可以在 CMake 包中包含 Python 库和节点（使用ament_cmake_python），因此您可以在一个包中一起定义接口和 Python 节点。为了简单起见，我们将在此处使用 CMake 包和 C++ 节点。

本教程将重点介绍 msg 接口类型，但此处的步骤适用于所有接口类型。
#### 3.7.2. 创建一个package
在src目录：
```
ros2 pkg create --build-type ament_cmake more_interfaces
mkdir more_interfaces/msg
```
#### 3.7.3. 2 创建消息文件
在里面more_interfaces/msg，创建一个新文件AddressBook.msg

粘贴以下代码以创建一条消息，用于携带有关个人的信息：
```
bool FEMALE=true
bool MALE=false

string first_name
string last_name
bool gender
uint8 age
string address
```
此消息由 5 个字段组成：

first_name：字符串类型

last_name：字符串类型

性别：bool 类型，可以是 MALE 或 FEMALE

年龄：uint8类型

地址：字符串类型

请注意，可以为消息定义中的字段设置默认值。有关自定义界面的更多方法，请参阅关于 ROS 2 界面。

接下来，我们需要确保将 msg 文件转换为 C++、Python 和其他语言的源代码。
#### 3.7.4. 构建一个msg文件
打开package.xml，并添加以下行：

```
<buildtool_depend>rosidl_default_generators</buildtool_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```
请注意，在构建时，我们需要rosidl_default_generators，而在运行时，我们只需要rosidl_default_runtime.

打开CMakeLists.txt并添加以下行：
找到从 msg/srv 文件生成消息代码的包：
```
find_package(rosidl_default_generators REQUIRED)
```
声明要生成的消息列表：
```
set(msg_files
  "msg/AddressBook.msg"
)
```
通过手动添加 .msg 文件，我们确保 CMake 知道在您添加其他 .msg 文件后何时必须重新配置项目。

生成消息：
```
rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)
```
还要确保导出消息运行时依赖项：
```
ament_export_dependencies(rosidl_default_runtime)
```
现在您已准备好从 msg 定义生成源文件。我们现在将跳过编译步骤，因为我们将在下面的第 4 步中一起完成。
### 3.8. 在类中使用参数 (Python)
#### 3.8.1. 创建package
```
ros2 pkg create --build-type ament_python python_parameters --dependencies rclpy
```
因为您--dependencies在包创建期间使用了该选项，所以您不必手动将依赖项添加到package.xml或CMakeLists.txt。
不过，一如既往，请确保将描述、维护者电子邮件和姓名以及许可证信息添加到package.xml.
```
<description>Python parameter tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache License 2.0</license>
```
#### 编写python节点
在该ros2_ws/src/python_parameters/python_parameters目录中，创建一个名为的新文件python_parameters_node.py并将以下代码粘贴到其中：
```python 
import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('my_parameter', 'world')

        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        self.get_logger().info('Hello %s!' % my_param)

        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
```
#### 添加入口点
package.xml
```
maintainer='YourName',
maintainer_email='you@email.com',
description='Python parameter tutorial',
license='Apache License 2.0',
```
setup.py
```python
entry_points={
    'console_scripts': [
        'minimal_param_node = python_parameters.python_parameters_node:main',
    ],
},
```
### 创建和使用插件 (C++)
#### 背景
pluginlib 是一个 C++ 库，用于从 ROS 包中加载和卸载插件。插件是从运行时库（即共享对象、动态链接库）加载的动态可加载类。使用 pluginlib，人们不必将他们的应用程序显式链接到包含类的库——相反，pluginlib 可以在任何时候打开一个包含导出类的库，而无需应用程序事先知道该库或包含类定义的头文件。插件可用于在不需要应用程序源代码的情况下扩展/修改应用程序行为。
#### 安装pluginlib
```
sudo apt install ros-rolling-pluginlib
```

#### 任务
在本教程中，您将创建两个新包，一个定义基类，另一个提供插件。基类将定义一个通用的多边形类，然后我们的插件将定义特定的形状。
#### 创建基本package
在src目录
```
ros2 pkg create --build-type ament_cmake polygon_base --dependencies pluginlib --node-name area_node
```
创建ros2_ws/src/polygon_base/include/polygon_base/regular_polygon.hpp
```
#ifndef POLYGON_BASE_REGULAR_POLYGON_HPP
#define POLYGON_BASE_REGULAR_POLYGON_HPP

namespace polygon_base
{
  class RegularPolygon
  {
    public:
      virtual void initialize(double side_length) = 0;
      virtual double area() = 0;
      virtual ~RegularPolygon(){}

    protected:
      RegularPolygon(){}
  };
}  // namespace polygon_base

#endif  // POLYGON_BASE_REGULAR_POLYGON_HPP
```

