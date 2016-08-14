Title: APM-MacOS平台上用Arduino编译APM2.x
Date: 2014-9-8 9:02:28 
Tags: APM,飞控板,硬件

<!-- PELICAN_BEGIN_SUMMARY -->
在MacOS平台上针对AVR芯片的Ardupilot的源码编译可以有两种选择。第一种是使用特殊版的Arduino编译环境。你可以在[http://firmware.diydrones.com/](http://firmware.diydrones.com/)的工具目录下获得。第二种选择是使用`make`命令行工具进行编译。
<!-- PELICAN_END_SUMMARY -->

如果你选择Arduino工具，当你安装完成之后，你还需要做下面这些事情：

- 在Ardupilot菜单下选择你的飞控板类型
- 在菜单File-->>属性Preferences下设置Sketchbook位置到你的Ardupilot源码目录
- 关闭并重启Arduino

----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-the-code-on-mac/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*