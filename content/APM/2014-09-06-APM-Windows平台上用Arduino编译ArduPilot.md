Title: APM-Windows平台上用Arduino编译ArduPilot
Date: 2014-9-6 15:34:19 
Tags: APM,飞控板,硬件

<!-- PELICAN_BEGIN_SUMMARY -->
**版本要求： Copter 3.1， Plane 2.76**

**硬件要求： APM 2.0,2.5,2.6**
<!-- PELICAN_END_SUMMARY -->

![apm](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image001.jpg)

----------
### Step 1 安装Git-SCM ###
软件链接： [http://git-scm.com/download/win](http://git-scm.com/download/win)

在安装过程中请按照下面的截图勾选相应的选项。

![img1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image004.jpg)

![img2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image006.jpg)

在欢迎界面和许可证界面点击Next按钮

----------
![img3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image008.jpg)

![img4](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image018.jpg)

在选择组件点击Next按钮，然后点击Finish按钮。

----------
![img5](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image014.jpg)

![img6](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image016.jpg)

在替换用户文件界面点击Next按钮，然后等待Git完成安装。

----------
![img7](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image012.jpg)

![img8](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image010.jpg)

如上图，选择切换到window风格（checkout windows-style），然后点击Next按钮，选择从windows命令界面运行Git，点击Next按钮。

----------
### Step 2 下载源码 ###

首先在你电脑的C盘，建立一个名为GIT的文件夹。

用windows资源管理器到该文件夹下。

![img9](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image020.jpg)

----------
然后在文件夹空白地方右击选择git Bash选项。

![img10](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image022.jpg)

----------
此时，屏幕上会弹出下面的窗口。

![img11](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image024.jpg)

----------
在该命令窗口中，键入：

    git clone git://github.com/diydrones/ardupilot.git

![img26](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image026.jpg)

----------
当命令执行完毕之后，应该像下面这样...

![img12](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image028.jpg)

----------
### Step 3 安装MHV_AVR_Tools到软件默认位置 ###
软件链接：[http://firmware.diydrones.com/Tools/Arduino/MHV_AVR_Tools_20121007.exe](http://firmware.diydrones.com/Tools/Arduino/MHV_AVR_Tools_20121007.exe)

![img13](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image030.jpg)

![img14](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image038.jpg)

安装引导界面点击Next按钮然后选择Install按钮开始安装

----------
![img15](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image036.jpg)

![img16](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image034.jpg)

在选择组件界面两项都勾选，然后点击Next按钮，选择安装到默认位置。

----------
![img17](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image032.jpg)

在许可证界面点击同意（I Agree）完成安装。

----------
### Step 4 安装Ardupilot-Arduino ###
接下来下载特定版本的 ArduPilot Arduino 压缩包。

这里有一个新版本的，采用GCC 4.7.2编译。

地址：[http://firmware.diydrones.com/Tools/Arduino/ArduPilot-Arduino-1.0.3-gcc-4.8.2-windows.zip](http://firmware.diydrones.com/Tools/Arduino/ArduPilot-Arduino-1.0.3-gcc-4.8.2-windows.zip)

我将该文件解压到我电脑上的C盘。


----------
### Step 5 配置Arduino ###
打开放置Arduino的文件夹

![img18](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image0401.jpg)

----------
双击Arduino图标

![img19](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image040.jpg)

当Arduino打开之后，到文件（file）菜单栏

![img20](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image042.png)

----------
点击属性

![img21](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image044.png)

设置Sketchbook到你电脑上GIT文件夹下的Ardupilot目录

同样选择编译和加载选项，这样在执行相应功能时就可以查看到详细信息。

不要选择启动时自动升级功能（该版本是针对Ardupilot的特殊版本）

点击OK，然后关闭Arduino

----------
### Step 6 通过USB连接你的APM ###
重新打开Arduino，然后在file菜单栏中点击Sketchbook，选择你想要加载到你的APM2.x上的程序代码（比如这里选择ArduCopter,其它采用同样的方法设置）。

![img22](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image047.jpg)

----------
一旦文件加载完成，点击Ardupilot菜单，选择HAL板下的Ardupilot Mega 2.x

![img23](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image049.jpg)

----------
然后点击Tools菜单，选择Board 选项卡下的 Arduino Mega 2560 or Mega ADK

![img24](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image051.jpg)

----------
接下来重新选择Tools菜单，设置你的APM连接到电脑上的端口号Serial Port

![img25](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image053.jpg)

----------
在这个例子中为COM4，你可以在你的电脑的设备管理器中，在端口Ports中查看APM对应的端口。

![img27](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image055.jpg)

----------
### Step 7 配置Arducopter ###
点击文件APM_Config.h选项卡。

设置你的飞行器构型（例如`#define FRAME_CONFIG HEXA_FRAME`）

在该文件中可以启用/不启用相应的功能。

例如：如果在编译过程中想让auto tune 功能失效，那么你可以简单的将该行取消注释

    //# AUTOTUNE              DISABLED            // 不启用该功能可以节省7k的闪存空间

改为：

    # AUTOTUNE              DISABLED            // 不启用该功能可以节省7k的闪存空间

默认是启用该功能。

源代码中所有注释掉的功能都不是默认的，你需要做的就是通过取消注释来改变系统的默认选项

保存该文件然后选择文件Arducopter

接下来就可以准备开始编译了。

但一般来讲我会先选择校验（verify）代码。

![img28](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image057.jpg)

----------
### Step 8 将代码加载到你的Ardupilot板上 ###
点击编译按钮

![img29](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image058.png)

----------
这可能会花费一些时间...

当出现下面提示时表明编译完成...

![img30](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/11/image061.jpg)

----------
最后用地面站软件Mission Planner确认能否正常使用

----------
### 注意 ###
你自己配置并编译过的代码是没有经过测试的，请仅仅将它用来做测试之用。如果你没有足够的把握，建议你使用Mission Planner来加载预先编译过的代码。

----------
### 升级你的代码 ###
请确认你电脑上的代码为最新版，否则就用git来升级你的代码到最新版本。

----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-ardupilot-with-arduino-windows/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*