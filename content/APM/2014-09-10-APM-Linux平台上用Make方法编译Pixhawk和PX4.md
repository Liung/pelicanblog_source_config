Title: APM-Linux平台上用Make方法编译Pixhawk/PX4
Date: 2014-9-10 17:24:31 
Tags: APM,飞控板,硬件


### 快速开始 ###
<!-- PELICAN_BEGIN_SUMMARY -->
对于Ubuntu平台，采用下面步骤来编译代码。对于Linux其他平台，请参阅下面的更深入的说明
<!-- PELICAN_END_SUMMARY -->

#### 1、安装 ####
**安装git**

```
sudo apt-get -qq -y install git
```

**“克隆”源码**

```
git clone https://github.com/diydrones/ardupilot.git
```

**运行 install-prereqs-ubuntu.sh 脚本**

```
ardupilot/Tools/scripts/install-prereqs-ubuntu.sh -y
```

重载路径(注销并再次登陆使其写入系统配置文件中)

```
. ~/.profile
```

#### 2、编译 ####
**编译ArduCopter**

```
cd ardupilot/ArduCopter
make configure
make px4-v2
```

**编译ArduPlane**

```
cd ardupilot/ArduPlane
make configure
make px4-v2
```

----------
### 深入介绍 ###
为了在Linux平台上编译PX4，你需要下面这些工具及Git代码库：

- gcc-arm交叉编译器[[here](http://firmware.diydrones.com/Tools/PX4-tools/)]
- ardupilot的git代码库[[github.com/diydrones/ardupilot](https://github.com/diydrones/ardupilot)]
- PX4NuttX的git代码库[[https://github.com/diydrones/PX4NuttX](https://github.com/diydrones/PX4NuttX)]
- PX4Firmware的git代码库[[github.com/diydrones/PX4NuttX](https://github.com/diydrones/PX4Firmware)]
- GNU make，gawk和相关的linux标准编译工具
- Ubuntu平台你将需要安装genromfs工具包

需要注意的是你需要使用diydrones的github账户下的PX4nuttx和PX4Firmware代码库，而不是PX4下的。因为来自于PX4的代码库没有使用APM相关代码进行过验证。

#### 设置权限 ####
你需要将你当前用户添加到dialout群组中：

```
sudo usermod -a -G dialout $USER
```

注销并再次登陆是群组操作生效。

还有，值得注意的是确保没有安装modemmanager包（调制解调器管理），并且modem-manager进程没有运行。

#### 目录结构 ####
Ardupilot、PX4Nuttx和PX4Firmware的git代码需要放在同一个目录下。因为目录中的makefile文件将在Ardupilot目录的上层目录寻找PX4Nuttx和PX4Firmware。

#### 编译器 ####
需要指定gcc-arm交叉编译器链接上述文件。

首先，你需要解压编译器：

```
tar -xjvf gcc-arm-none-eabi-4_6-2012q2-20120614.tar.bz2
```
然后编辑$HOME/.bashrc文件，在文件末尾添加如下链接，将原始代码中的bin目录添加到你的环境变量中`%PATH`.

```
export PATH=$PATH:/home/your_username/bin/gcc-arm-none-eabi-4_6-2012q2/bin
```

#### 快速编译工具ccache ####
安装ccache工具将极大加速你的编译时间。一旦你安装了它（例如通过“`sudo apt-get install ccache`”）你应该像这样链接编译器到/usr/lib/ccache。

```
cd /usr/lib/ccache
sudo ln -s /usr/bin/ccache arm-none-eabi-g++
sudo ln -s /usr/bin/ccache arm-none-eabi-gcc
```
然后像前面一样将/usr/lib/ccache加入你的环境变量里`%PATH`

#### 编译 ####
当你下载好了上述三个git代码库并配置完成编译器，就可以在你的飞行器目录开始编译工作。例如，编译ArduPlane：

```
cd ardupilot/ArduPlane
make configure
make px4
```

编译完成后将生成两个文件：ArduPlane-v1.px4 和 ArduPlane-v2.px4。v1文件针对PX4V1平台，V2针对PX4v2平台（Pixhawk）。

同样可以使用`make px4-v1`或者`make px4-v2`来编译对应平台文件。

第一次编译时间可能有点漫长，因为它需要编译整个px4的文件架构。之后的编译过程将变得非常快（特别是你正确地设置了ccache）。

#### 加载固件 ####
使用下面的命令将固件加载到飞控板上：

```
make px4-v1-upload
```

或

```
make px4-v2-upload
```

当通过USB向你的PX4加载代码提示“waiting for bootloader”之后。

如果在擦出阶段上传总是失败，检查是否运行了modemmanager，它可以控制PX4的USB端口。如果是，尝试移除modemmanager来获得帮助。

#### 清理 ####
更新完成git代码后，你可能需要一个干净的编译结果。使用下面命令来实现：

```
make px4-clean
```

这将会移除编译过程的PX4Nuttx文件架构信息以便于重新编译。

----------
####链接####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-px4-for-linux-with-make/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*