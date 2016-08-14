Title: APM-Linux上SITL仿真设置
Date: 2014-10-15 14:06:42 
Tags: APM,飞控板,硬件

### 简介 ###
<!-- PELICAN_BEGIN_SUMMARY -->
SITL（software in the loop）仿真可以让你在没有任何硬件的情况下运行ArduPlane，Copter或者Rover。它使用通用的C++编译器来完成autopilot的代码编译工作，从而可以让你从运行过程中不需要任何硬件就能完成代码的测试。<!-- PELICAN_END_SUMMARY -->

本页面详细说明了如何在Linux平台上设置SITL。文中使用的相关命令在 **Ubuntu 12.10** 和 **Ubuntu 13.04**  平台上测试通过。

![img0](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/04/SITL_Linux.png)

----------
### 相关细节 ###
HITL（Hardware In The Loop）模拟对于APM代码测试工作相当有用，但是对于某些任务存在一些限制。这些限制包括：

- 不能运行所有的autopilot代码，因为当硬件放置在桌面上时，底层驱动不能兼容所有的飞行测试输入量。
- 不能使用一系列对正常C++调试非常有用的高级编程工具（例如调试器和内存监视器）

内建有ArduPilot的SITL克服了上述限制，它仍然运行相同的代码，但是它是作为PC上的本地可执行程序，并且使用了一些C++技巧，在注册层来模拟APM飞控板的硬件。所以，这些底层的硬件驱动（例如ADC， 陀螺仪，加速度计和GPS）就像真实飞行环境一样正常运行。

APM的SITL环境在如下系统中开发并测试：

- Windows： Windows 7
- Linux： Ubuntu 13.04 或 之后版本

### 关于虚拟机 ###
如果你尝试在虚拟机上运行SITL，你可能会发现定时器非常糟糕以至于很难飞行。具体表现为飞行非常不稳定或者经常撞机。那么，你可以通过以下方法来改善这种情况：

- 设置虚拟机使用尽可能多的CPU数量
- 不使用ardupilot中EKF（旧的DCM代码对于差的传感器定时处理相对灵活）。设置方法：在mavproxy终端键入“`param set AHRS_EKF_USE 0`”

----------
### 安装步骤 ###
请遵循以下步骤

#### Step 1： 下载ardupilot ####
如果没有ardupilot的git库本地备份，请打开终端并运行：

    git clone git://github.com/diydrones/ardupilot.git

#### Step 2： JSBSim ####
如果你想要运行固定翼模拟器，那么你就需要JSBSim包。在同一目录下（home目录）运行下面命令：

    git clone git://github.com/tridge/jsbsim.git
    apt-get install libtool automake autoconf libexpat1-dev

#### Step 3： 安装所需包 ####

    sudo apt-get install python-matplotlib python-serial python-wxgtk2.8 python-lxml
    sudo apt-get install python-scipy python-opencv ccache gawk git python-pip
    sudo pip install pymavlink MAVProxy

#### Step 4： 将目录添加到搜索路径 ####
添加下面几行到home目录中“.bashrc”的文件尾部（注意文件名以**.**开始）

    export PATH=$PATH:$HOME/ardupilot/Tools/autotest
    export PATH=$PATH:$HOME/MAVProxy
    export PATH=$PATH:$HOME/mavlink/pymavlink/examples
    export PATH=$PATH:$HOME/jsbsim/src
    export PATH=/usr/lib/ccache:$PATH

然后使用“**.**”命令在终端重载路径文件

    . ~/.bashrc

#### Step 5： 编译JSBSim，运行如下命令 ####
如果要运行SITL中的固定翼版本，那么你需要安装JSBSim。（Copter 和 Rover 不需要）

    cd jsbsim
    ./autogen.sh
    make

#### Step 6： 启动SITL模拟器 ####
开始运行模拟器，首先需要将目录切换到对应飞行器目录。例如，对于固定翼需要将目录切换到ardupilot/ArduPlane。

使用sim_vehicle.sh启动模拟器。第一次启动时需要加-w命令选项来清除之前的EEPROM数据，加载当前你的飞行器的正确默认参数，并使用“make configure”来生成配置文件。

    make configure
    sim_vehicle.sh -w

当默认参数加载完成，就可以正常启动模拟器了。

    sim_vehicle.sh --console --map --aircraft test

sim_vehicle.sh有许多有用参数选项。请使用-h项查看可用的选项哦~

#### Step 7： 加载任务 ####
让我们来开始加载测试任务吧~

    wp load ../Tools/autotest/ArduPlane-Missions/CMAC-toff-loop.txt

这个任务写入了绕我本地领域的一个飞行循环。现在开始起飞~在MAVProxy中运行“`auto`”，你的虚拟飞行器现在开始起飞啦~啦~~哦~

#### Step 8： 学习MAVProxy ####
想要学习SITL之外的东西？那就开始学习使用MAVProxy吧。这个是[MAVProxy文档](http://tridge.github.io/MAVProxy/)。飞行愉快哦~0-0.

----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/setting-up-sitl-on-linux/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*