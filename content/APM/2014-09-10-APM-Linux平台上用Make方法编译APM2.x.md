Title: APM-Linux平台上用Make方法编译APM2.x
Date: 2014-9-10 17:18:44 
Tags: APM,飞控板,硬件


### 快速开始 ###
<!-- PELICAN_BEGIN_SUMMARY -->
对于Ubuntu平台，采用下面步骤来编译代码。对于Linux其他平台，请参阅下面的更深入的说明
<!-- PELICAN_END_SUMMARY -->

#### 1、安装 ####
安装git

```
sudo apt-get -qq -y install git
```

“克隆”源码

```
git clone https://github.com/diydrones/ardupilot.git
```

运行 install-prereqs-ubuntu.sh 脚本

```
ardupilot/Tools/scripts/install-prereqs-ubuntu.sh -y
```

重载路径(注销并再次登陆使其写入系统配置文件中)

```
. ~/.profile
```

#### 2、编译 ####
编译ArduCopter

```
cd ardupilot/ArduCopter
make configure
make
```

编译ArduPlane

```
cd ardupilot/ArduPlane
make configure
make
```

----------
### 深入介绍 ###
为了在Linux上编译Ardupilot固件，你需要一个针对板子芯片的类型相同的特定编译器。如果你使用的是基于Ubuntu发布框架的debian系统，可以使用下面命令获取你所需要的核心包：

```
sudo apt-get install gcc-avr avrdude avr-libc binutils-avr
```

此外，使用SITL系统和开发者工具还需要一些其他的辅助工具。

```
sudo apt-get install python-serial python-wxgtk2.8 python-matplotlib python-opencv python-pexpect python-scipy
```

安装完成之后，你就可以切换到你需要编译的的飞行器目录，通过运行`make`来编译你想要的代码。具体编译目标列表请查看mk/targets.mk。

#### Ubuntu Linux ####
Ubuntu上针对APM1/APM2(arduino)系统的编译还需要下面的工具。

```
gawk make git arduino-core g++
```

编译PX4平台的Ardupilot，首先需要安装PX4工具链，并下载PX4源代码。查看**PX4 工具链安装页面 **([Here!](https://pixhawk.ethz.ch/px4/dev/toolchain_installation_lin))

安装这些需要的工具最简单的方法是运行`ardupilot/Tools/scripts/install-prereqs-ubuntu.sh`脚本，来自动安装所需包和工具。

#### Building using make ####
1. 在第一次编译代码前，需要在sketch（i.e. ArduPlane, ArduCopter, etc…）目录运行`make configure`.它将在代码库的顶层目录创建一个`config.mk`文件，你可以查看该文件内的默认设置。
2. 在sketch目录，运行 `make`来编译APM2。`make apm1` 将编译为APM1平台文件，`make px4`将编译为px4平台文件.二进制文件保存在`/tmp/sketchname.build`目录。

3. 运行`make upload`加载固件. 需要在 `config.mk`文件中设置正确的默认串行端口.

----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-the-code-onlinux/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*