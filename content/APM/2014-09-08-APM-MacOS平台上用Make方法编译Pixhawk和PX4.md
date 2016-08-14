Title: APM-MacOS平台上用Make方法编译Pixhawk/PX4
Date: 2014-9-8 9:27:32 
Tags: APM,飞控板,硬件

### MAC (10.6版本或更早) ###
**1、**在Mac OS X上安装Homebrew

**2、**使用brew命令安装下列包

    brew tap PX4/homebrew-px4
    brew update
    brew install genromfs
    brew install gcc-arm-none-eabi

**3、**使用下面命令安装pip和pyserial:

    sudo easy_install pip
    sudo pip install pyserial

**4、**现在创建你的工作目录，然后安装下面所有软件:

    mkdir -p px4
    cd px4
    git clone https://github.com/diydrones/ardupilot.git
    git clone https://github.com/diydrones/PX4Firmware.git
    git clone https://github.com/diydrones/PX4NuttX.git

**5、**然后使用下面命令为编译ArduCopter设置配置文件:

    cd ardupilot/ArduCopter
    make configure

打开ardupilot/config.mk文件，将下面的信息改为你对应的文件目录:
    
    PX4_ROOT=../PX4Firmware (改成你本地的PX4Firmware目录)
    
    NUTTX_SRC=../PX4NuttX/nuttx (nuttx目录同上)

    make   (第一次使用将会编译PX4Firmware和NuttX)
    make   (第二次将会编译ArduCopter固件)

**6、**用下面命令编译面向px4的ArduCopter:

    cd ardupilot/ArduCopter
    make px4-quad

编译完成之后，在你的ArduCopter文件目录将会发现两个文件。ArduCopter-v1.px4是针对原始PX4平台，而ArduCopter-v2.px4是针对pixhawk平台。

有时你可能升级PX4Firmware和PX4NuttX。为了确保能有正确编译，在运行之前请先使用clean选项清理编译环境：

    make px4-clean
    make px4-[frame type]

可使用的框架类型有：**quad, tri, hexa, y6, octa, octa-quad, hell**

然后连接并加载固件到你的飞行器上:

    make px4-quad-upload


----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-px4-with-make-on-mac/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*