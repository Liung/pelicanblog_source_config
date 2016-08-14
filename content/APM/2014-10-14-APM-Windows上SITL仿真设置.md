Title: APM-Windows上SITL仿真设置
Date: 2014-10-14 13:56:44 
Tags: APM,飞控板,硬件

### 简介 ###
<!-- PELICAN_BEGIN_SUMMARY -->
SITL（software in the loop）仿真可以让你在没有任何硬件的情况下运行ArduPlane，Copter或者Rover。它使用通用的C++编译器来完成autopilot的代码编译工作，从而可以让你从运行过程中不需要任何硬件就能完成代码的测试。

本页面详细说明了如何在windows平台上设置SITL。文中使用的相关命令在装有**VMware ver 5.0.2 build -1031769** 和 **Ubuntu 12.10**的Windows8平台上测试通过。
<!-- PELICAN_END_SUMMARY -->

需要注意的是：在完成本页面操作请先将[Ardupilot代码]({filename}2014-08-29-APM-获取源码.md)下载到你的电脑上，并且可以使用[arduino]({filename}2014-09-06-APM-Windows平台上用Arduino编译ArduPilot.md)或者[Make方法]({filename}2014-09-07-APM-Windows平台上用Make方法编译Pixhawk和PX4.md)编译。

![img1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_SITL_running_Copter.png)

----------
### Step #1 安装VMWare并创建Ubuntu虚拟机###
1. 下载并安装[VMware](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0)（搜索VMware Player或者windows平台VMware Player Plus）
1. 下载[Ubuntu ISO](http://www.ubuntu.com/download/desktop/thank-you?release=latest&bits=32&distro=desktop&status=zeroc)镜像文件
1. 开始运行VMware，选择 Player>File>New Virtual Machine，建立一个新虚拟机


----------

- 填写用户全称，虚拟机的用户名和密码。当你登陆你的虚拟机时将会用到。
- 命名你的虚拟机（例如 ArduCopter-SITL）
- 设置硬盘空间-保持默认20GB的最大空间，并选择“分割虚拟硬盘为多文件”
- 在“新虚拟机向导”的下一页面，电机“自定义硬件”按钮。
- 在硬件栏设置内存：3GB，处理器：4，硬盘容量：20GB，网络适配器：NAT

----------

![img2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_VMSettings_Hardware.png)

----------
### Step #2 初次运行VM###
**1、**双击启动刚刚创建的虚拟机

**2、**当遇到任何像 “Cannot connect to the XXX device because no corresponding device is available on the host”的问题时点"No"

**3、**在登陆界面输入密码

**4、**当提示升级时选择不升级

**5、**打开火狐浏览器确保虚拟机能够连接网络

![img3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_TestNetworkWithFirefox-300x205.png)

**6、**双击右上角设置时钟，选择地图中你的位置，然后“设置时间”为“自动从网络获取”

![img4](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_setTimezone-300x212.png)

**7、**设置终端窗口快捷方式：点击左上角的Home图标，键入“终端（terminal）”，然后将终端应用拖拽到左边的起始栏

![img5](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_TerminalShortcut-1024x488.png)

----------
### Step #3 设置Windows和Ubuntu虚拟机的共享文件###
**1、**确保VM已经关闭电源：在绿色按钮的下拉菜单中选择“Power Off”（如果不是灰色）

![img6](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_PowerOff-300x200.png)

**2、**在VMware虚拟机界面选择Player>Manage>Virtual Machine Settings ... > Options Tab>Shared Folders

- 选中“Always enabled”，点击Add
- 将“Host Path”设置导航到安装有ardupilot软件的文件夹位置
- 选中“Enable this share”

![img7](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/Ubuntu_VMSettings_SetupSharedFolder.png)

**3、**启动VM，进入系统

**4、**打开终端，键入“`ls/mnt/hgfs`”，然后你应该能看到你刚刚设置共享的文件

**5、**输入“`ln -s /mnt/hgfs/<foldername>`”(<foldername>替换成上面你设置的共享文件名)，用以在主目录创建一个符号链接。

----------
### Step #4 在你的VM上安装所需模块###
打开终端，然后输入下面命令：
`sudo apt-get update` <--用来从软件中心升级一系列包

`sudo apt-get install <name>`安装下列文件（回复'y'确保你有足够的剩余空间可以使用）

- dos2unix
- python-wxgtk2.8
- python-matplotlib
- python-opencv
- python-pip
- g++
- g++-4.7
- gawk
- git
- ccache

    sudo pip install pymavlink
    sudo pip install mavproxy

如果你想运行ArduPlane，那么你还需要安装：

- libexpat1-dev
- auto.conf
- libtool
- automake

----------
### Step #5 按照如下Linux说明###
现在你已经有了Linux的VM虚拟机，你可以参照[Liunx平台软件仿真]({filename}2014-10-14-APM-Linux上SITL仿真设置.md)说明。

----------
### 连接Mission Planner ###
除了使用Mavproxy地面站外(使用Python写的地面站)，还可能要和Mission Planner链接，这就需要在启动命令后面添加上`--viewerip=xxx.x.x.x`,也就是你电脑的IP地址，通过在cmd界面键入`ipconfig`来查看你电脑的IP

注意：你可能需要尝试图片中的各个IP地址，直到地面站可以正常通信为止

![img8](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/SITL_ipconfig.png)

那么，在Ubuntu虚拟机的终端就可以键入如下命令：

    ./Tools/autotest/autotest.py build.ArduCopter fly.ArduCopter logs.ArduCopter --map --viewerip=192.168.184.1

接下来首先将Mission Planner的连接方式从“COM Port”改为“UDP”

![img9](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/12/SITL_connectWithMP.png)

----------
### 数据存储器（Dataflash）日志 ###
当模拟开始后，以“ArduCopter.flashlog”或“CopterAVC.flashlog”命名的数据日志文件将会在“buildlogs”文件夹自动创建，该目录和ardupilot目录（包含有ArduCopter、ArduPlane和libraries目录的上层目录）处于同一级别。由于命名的不便，在打开Mission Planner之前，你需要先将这些文件改为以“.log”结尾。

----------
### 链接 ###

1. [APM官网原文链接](dev.ardupilot.com/wiki/setting-up-sitl-on-windows/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*