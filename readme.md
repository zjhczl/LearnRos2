## ros2安装与卸载
### 安装ros2
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

### 卸载ros2
```
sudo apt remove ~nros-rolling-* && sudo apt autoremove
sudo rm /etc/apt/sources.list.d/ros2.list
sudo apt update
sudo apt autoremove
# Consider upgrading for packages previously shadowed.
sudo apt upgrade
```
## 基础工具
### 节点
ROS 中的每个节点都应该负责一个单一的模块用途（例如，一个节点用于控制车轮电机，一个节点用于控制激光测距仪等）。每个节点都可以通过主题、服务、操作或参数向其他节点发送和接收数据。
#### 启动节点
```
ros2 run <package_name> <executable_name>
```
例子:
```
ros2 run turtlesim turtlesim_node
```
#### 获取节点信息
```
ros2 node info <node_name>
ros2 node info /my_turtle

```
### topics
#### 显示所有topic
```
ros2 topic list
```
ros2 topic list -t将返回相同的主题列表，这次主题类型附加在括号中
#### 查看某个主题上发布的数据
```
ros2 topic echo <topic_name>
ros2 topic echo /turtle1/cmd_vel
```
话题不必只是点对点的交流；它可以是一对多、多对一或多对多。另一种看待这个问题的方法是运行：
```
ros2 topic info /turtle1/cmd_vel
```
#### 查看数据结构
```
ros2 interface show geometry_msgs/msg/Twist
```
#### 发布主题
参数'<args>'是您将传递给主题的实际数据，采用您刚刚在上一节中发现的结构。请务必注意，此参数需要以 YAML 语法输入。像这样输入完整的命令：
```
ros2 topic pub <topic_name> <msg_type> '<args>'
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
--once是一个可选参数，意思是“发布一条消息然后退出”。

### services
#### 获取服务列表
```
ros2 service list -t
```
-t会列出所有活动服务的类型
#### 查看服务类型
```
ros2 service type <service_name>
ros2 service type /clear
```
返回std_srvs/srv/Empty
#### 服务查找
```
ros2 service find <type_name>
ros2 service find std_srvs/srv/Empty
```
返回/clear /reset
#### 查看服务参数的结构
```
ros2 interface show <type_name>
ros2 interface show std_srvs/srv/Empty
```
#### 服务调用
```
ros2 service call <service_name> <service_type> <arguments>
ros2 service call /clear std_srvs/srv/Empty
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```
### 参数
#### 获取节点参数列表
```
ros2 param list
```
#### 参数获取
```
ros2 param get <node_name> <parameter_name>
ros2 param get /turtlesim background_g
```
#### 设置参数值
```
ros2 param set <node_name> <parameter_name> <value>
ros2 param set /turtlesim background_r 150
```
#### 参数转存
显示节点所有参数
```
ros2 param dump <node_name>
```
将参数存储成文件
```
ros2 param dump /turtlesim > turtlesim.yaml
```
#### 加载参数
```
ros2 param load <node_name> <parameter_file>
ros2 param load /turtlesim turtlesim.yaml
```
#### 启动时加载参数文件

```
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim.yaml
```
### 动作
动作是 ROS 2 中的一种通信类型，用于长时间运行的任务。它们由三部分组成：目标、反馈和结果。操作基于主题和服务。它们的功能类似于服务，除了可以取消操作。他们还提供稳定的反馈，而不是返回单一响应的服务。操作使用客户端-服务器模型，类似于发布者-订阅者模型（在主题教程中描述）。“动作客户端”节点将目标发送到“动作服务器”节点，该节点确认目标并返回反馈流和结果。
#### 列出所有action
```
ros2 action list -t
```
返回/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
#### 查看action信息
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
#### action操作类型
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
#### 发送动作
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
### ros bag
#### 记录包
```
ros2 bag record <topic_name>
ros2 bag record /turtle1/cmd_vel
ros2 bag record -o subset /turtle1/cmd_vel /turtle1/pose
```
-o选项允许您为包文件选择一个唯一的名称。在本例中，以下字符串subset是文件名。
#### 查看包录制信息
```
ros2 bag info <bag_file_name>
```
#### 包回放
```
ros2 bag play subset
```
## 客户端库
### 用于colcon构建包
#### 安装 colcon
```
sudo apt install python3-colcon-common-extensions
```
#### 创建工作区
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
#### 构建工作区

```
colcon build --symlink-install
```
#### 运行测试
```
colcon test
```
当 colcon 成功完成构建时，输出将在install目录中。在您可以使用任何已安装的可执行文件或库之前，您需要将它们添加到您的路径和库路径中。colcon 将在目录中生成 bash/bat 文件install以帮助设置环境。这些文件会将所有必需的元素添加到您的路径和库路径中，并提供包导出的任何 bash 或 shell 命令。
```
. install/setup.bash
```
#### colcon_cd
该命令colcon_cd允许您快速将 shell 的当前工作目录更改为包的目录。
#### ~~
### 创建工作区
#### 新建文件夹
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
#### 克隆一个样本仓库
```
git clone https://github.com/ros/ros_tutorials.git -b rolling-devel
```
#### 解决依赖
在构建工作区之前，您需要解决包依赖关系。您可能已经拥有所有依赖项，但最佳做法是在每次克隆时检查依赖项。您不希望构建由于缺少依赖项而在长时间等待后失败。


```
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
rosdep install -i --from-path src --rosdistro rolling -y
```
#### 使用 colcon 构建工作区
```
colcon build
```
其他有用的参数：colcon build

--packages-up-to构建你想要的包，加上它的所有依赖项，但不是整个工作区（节省时间）

--symlink-install使您不必每次调整 python 脚本时都必须重建

--event-handlers console_direct+在构建时显示控制台输出（否则可以在目录中找到log）
#### 源覆盖
在采购叠加层之前，打开一个新终端非常重要，与您构建工作区的终端分开。在您构建的同一终端中获取覆盖层，或者同样在覆盖层来源处构建，可能会产生复杂的问题。

在新终端中，将你的主要 ROS 2 环境作为“底层”，这样你就可以在它“之上”构建覆盖层：
```
source /opt/ros/rolling/setup.bash
cd ~/ros2_ws
. install/local_setup.bash
```
#### 总结
在本教程中，您将主要的 ROS 2 发行版安装作为底层，并通过在新工作区中克隆和构建包来创建覆盖层。正如您在修改后的 turtlesim 中看到的那样，覆盖层被添加到路径之前，并优先于底层。

建议在处理少量包时使用覆盖，这样您就不必将所有内容都放在同一个工作区中，也不必在每次迭代时都重建一个巨大的工作区。
### 创建package
#### 什么是 ROS 2 包？
一个包可以被认为是你的 ROS 2 代码的容器。如果您希望能够安装您的代码或与他人共享，那么您需要将其组织在一个包中。借助软件包，您可以发布您的 ROS 2 作品并允许其他人轻松构建和使用它。
ROS 2 中的包创建使用 ament 作为其构建系统，并使用 colcon 作为其构建工具。您可以使用官方支持的 CMake 或 Python 创建包，但确实存在其他构建类型。
#### 一个package包含什么
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
#### 工作区中的包
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

#### 创建package
进入src目录
```
cd ~/ros2_ws/src
```
创建package
```
ros2 pkg create --build-type ament_python <package_name>
ros2 pkg create --build-type ament_python --node-name my_node my_package
```
#### build package
将包放在工作区中特别有价值，因为您可以通过在工作区根目录中运行来一次构建多个包。否则，您将不得不单独构建每个包。colcon build
```
cd ~/ros2_ws
colcon build
```
只构建一个包
```
colcon build --packages-select my_package
```
#### Source the setup file
```
. install/local_setup.bash
```
#### 使用包
```
ros2 run my_package my_node
```
#### 修改package.xml setup.py文件
```
<description>Beginner client libraries tutorials practice package</description>
<license>Apache License 2.0</license>
```
### 编写简单的发布者和订阅者 
在src目录
```
ros2 pkg create --build-type ament_python py_pubsub
```
#### 编写发布者节点
导航到ros2_ws/src/py_pubsub/py_pubsub. 回想一下，这个目录是一个Python 包，与它嵌套在其中的 ROS 2 包同名。
通过输入以下命令下载示例 talker 代码：
```
wget https://raw.githubusercontent.com/ros2/examples/rolling/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
```
#### 添加入口点
```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},

```
#### 构建运行节点

```
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select py_pubsub
. install/setup.bash
ros2 run py_pubsub talker
```
### 编写简单的服务和客户端
#### 建立package
```
ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces
```
该--dependencies参数会自动将必要的依赖行添加到package.xml. 
因为您--dependencies在包创建期间使用了该选项，所以您不必手动将依赖项添加到package.xml.
不过，一如既往，请确保将描述、维护者电子邮件和姓名以及许可证信息添加到package.xml.
#### 编写节点服务
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


#### 编写客户端节点
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
#### 构建并运行
##### 启动服务
```
rosdep install -i --from-path src --rosdistro rolling -y
colcon build --packages-select py_srvcli
. install/setup.bash
ros2 run py_srvcli service
```
##### 启动客户端
```
ros2 run py_srvcli client 2 3

```

### 创建自定义 msg 和 srv 文件
因为python无法自定义msg，所以只能使用c++来实现
在ros2_ws/src目录创建用c++语言package
```
ros2 pkg create --build-type ament_cmake tutorial_interfaces
```
#### msg 自定义
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

#### srv定义
回到tutorial_interfaces/srv您刚刚创建的目录，创建一个新文件，AddThreeInts.srv使用以下请求和响应结构调用：
```
int64 a
int64 b
int64 c
---
int64 sum
```
是您的自定义服务，它请求名为 、 和 的三个整数a，b并c以名为 的整数响应sum。
#### 修改CMakeLists.txt
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
#### 修改package.xml
因为接口依赖rosidl_default_generators于生成特定于语言的代码，所以您需要声明对它的依赖。标签<exec_depend>用于指定运行时或执行阶段的依赖关系，是rosidl_interface_packages包所属的依赖组的名称，使用标签声明<member_of_group>。
```
<depend>geometry_msgs</depend>

<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```
#### 构建tutorial_interfaces包

```
colcon build --packages-select tutorial_interfaces
. install/setup.bash
ros2 interface show tutorial_interfaces/msg/Num
ros2 interface show tutorial_interfaces/msg/Sphere
ros2 interface show tutorial_interfaces/srv/AddThreeInts
```
#### 在包中使用自定义的msg
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
#### 在包中使用srv

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