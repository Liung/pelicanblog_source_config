Title: APM-Windows平台使用Make方法编译Pixhawk和PX4
Date: 2014-9-7 13:59:57 
Tags: APM,硬件

### Windows平台 ###
<!-- PELICAN_BEGIN_SUMMARY -->
**1、** 安装[Github for Windows](http://windows.github.com/)

**2、**  确保你的github上设置行结束符不发生改变。

- 当你安装完成Git，顺带也安装了“Git shell（or Bash）”。点击“Git shell（or Bash）”图标，然后在弹出的Git “MINGW32”终端窗口键入：

```git config --global core.autocrlf false```

**3、**“克隆”（clone）Ardupilot，PX4Firmware和PX4NuttX代码库到你的本地电脑上：

<!-- PELICAN_END_SUMMARY -->

- 到 [GitHub/diydrones/ardupilot](https://github.com/diydrones/ardupilot) 的web页面点击“Clone in Desktop”按钮
- 到[ GitHub/diydrones/PX4Firmware ](https://github.com/diydrones/PX4Firmware)的web页面点击“Clone in Desktop”按钮
- 到[ GitHub/diydrones/PX4NuttX ](https://github.com/diydrones/PX4NuttX)的web页面点击“Clone in Desktop”按钮
- ![img1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/BuildingTheCode_PX4OnWindows1.png)

**4、**运行[ px4_toolchain_installer_v12_win.exe ](http://www.inf.ethz.ch/personal/lomeier/downloads/px4_toolchain_installer_v12_win.exe)下载并安装PX4工具链（在[该页面](http://pixhawk.org/firmware/downloads#px4_arm_toolchain)的底部搜索“PX4 Toolchain Installer”）

**5、**创建并定制config.mk文件：

- win7平台可以在开始>>所有程序>>PX4 Toolchain找到PX4Console并运行，或直接运行该C:\px4\toolchain\msys\1.0\px4_console.bat文件。
- 切换到步骤三中Ardupilot固件的文件目录，然后进入ArduCopter目录（确保这里**A**rdu**C**opter中的A和C要大写）。上述操作可以在命令行中如下执行：

```cd /c/Users/<username>/Documents/GitHub/ardupilot/ArduCopter```

- 通过在终端键入下列命令创建config.mk文件。系统将会出现这样的 &#8220;WARNING &#8211; 信息：包含有准确文件位置信息的config.mk文件已经写入。

```make configure```

如果步骤三中创建PX4Firmware和PX4NuttX仓库时使用了相同的名字和位置，那么就不需要更改config.mk文件。但是如果名字或者位置有一个不同，那你就需要用诸如[NotePad++](http://notepad-plus-plus.org/download/v6.4.5.html)等文本编辑器打开config.mk，并将PX4_ROOT和/或NUTTX_SRC值设置与实际位置匹配。

![img2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/BuildingTheCode_PX4OnWindows2.png)

**6、**打开PX4控制台开始编译固件，首先切换到ArduCopter目录，然后输入下面命令执行编译

-  ```make px4```                <– 将会编译四旋翼的PX4和PixHawk固件
-  ```make px4-v2```           <– 将会编译四旋翼的PixHawk固件
-  ```make px4-v2-hexa```  <–将会编译六旋翼的PixHawk固件(其它可支持的后缀参数包括“octa”和"heli")
-  ```make clean```             <– 清理（“clean”） ardupilot 文件目录
-  ```make px4-clean```      <– 清理（“clean”）PX4Firmware 和 PX4NuttX  文件目录以便于下次重新编译
-  ```make px4-v2-upload```  <– 编译并上传四旋翼的Pixhawk固件(如果使用该命令，那么就不需要执行下面的步骤七了)

编译好的固件以.px4文件扩展名结尾，位于在ArduCopter目录

![img3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/PX4_ArduCopter_Build.png)

**7、**使用Mission Planner 加载固件的方法：初始设置（Initial Setup）>>安装固件（Install Firmware）界面点击“Load custom firmware”链接

### 加快编译时间的一些小建议 ###
杀毒防护软件有可能会减慢编译时间，特别对PX4尤为明显，所以建议包含有Ardupilot、PX4Firmware和PX4NuttX源代码的文件夹不在你的杀毒软件实时扫描范围内。

当执行完`make px4-clean`后的第一次编译将会非常的慢，这是因为要重新编译链接每一个文件。


----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-px4-with-make/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*