Title: APM-增加新的MAVLink通讯协议消息
Date: 2014-9-5 14:41:58 
Tags: APM,飞控板,硬件

###综述
<!-- PELICAN_BEGIN_SUMMARY -->
地面站之间的数据和指令通信都是通过串行接口使用[MAVLink协议](http://en.wikipedia.org/wiki/MAVLink)来传递的。本页面将提供关于添加新的MAVLink信息的一些高级建议。

这些指令仅在Liunx上测试完成（通过Windows上虚拟机运行的Ubuntu）。关于设置虚拟机的方法在[SITL(软件层面仿真)页面](http://dev.ardupilot.com/wiki/code-overview-adding-a-new-mavlink-message/wiki/setting-up-sitl-on-windows/)有相关介绍。如果你要运行SITL，你最好遵循下面的一些建议。这些指令不能直接在Windows或者Mac平台上本地运行。
<!-- PELICAN_END_SUMMARY -->

---
**Step #1**：确保你已经安装了最新的ardupilot代码，同时也检查一下mavproxy是否是最新版本。mavproxy工具可以通过在终端窗口运行下面命令进行升级。

```
sudo pip install --upgrade mavproxy
```

---
**Step #2**：先确定你所要添加的信息的类型，以及如何和已有的[MavLink消息](https://pixhawk.ethz.ch/mavlink/)兼容。

比如：你可能会想要向飞行器发送一个新的导航指令，让它可以在任务中期（自动模式中）模仿一个特技动作（比如翻筋斗）。在这个例子中，你需要一个类似于`MAV_CMD_NAV_WAYPOINT`（可以在[MAVLink消息页面](https://pixhawk.ethz.ch/mavlink/)搜索`MAV_CMD_NAV_WAYPOINT`）一样的新的导航指令`MAV_CMD_NAV_TRICK`。

又或者你想要从飞行器发送一个新的传感器数据类型到地面站,可能类似于[SCALED_PRESSURE](https://pixhawk.ethz.ch/mavlink/#SCALED_PRESSURE)消息。

---
**Step #3**：在[common.xml](https://github.com/diydrones/ardupilot/blob/master/libraries/GCS_MAVLink/message_definitions/common.xml)和[ardupilotmega.xml](https://github.com/diydrones/ardupilot/blob/master/libraries/GCS_MAVLink/message_definitions/ardupilotmega.xml)文件中添加你的信息的定义声明。

如果你希望将该指令添加到MAVLink协议中，那么你应该添加该指令到../ardupilot/libraries/GCS_MAVLink/message_definitions/common.xml文件中。如果你仅仅个人使用或者仅仅和ArduCopter，ArduPlane，ArduRover搭配使用，那么它就应该被添加到ardupimega.xml文件中。

---
**Step #4**：重新生成你的所有inlcude文件，确保添加的信息在主代码中可以被识别。

首先将目录切换到ardupilot文件夹下，然后执行下面命令：

```
./libraries/GCS_MAVLink/generate.sh
```

成功执行后，你应该看到下面这些文件都应经被更新。

```
../libraries/GCS_MAVLink/include/mavlink/v1.0/ardupilotmega/ardupilotmega.h
../libraries/GCS_MAVLink/include/mavlink/v1.0/ardupilotmega/version.h
../libraries/GCS_MAVLink/include/mavlink/v1.0/common/version.h
```

文件version.h仅简单的更新了文件的日期和时间，但是ardupilotmega.h文件已经应该有了你的新消息的定义声明。

---
**Step #5**：在飞行器主代码中添加函数方法用来控制向/从地面站发送/接收指令。

这些顶层代码指令绝大部分包含在飞行器的[GCS_MAVLink.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/GCS_Mavlink.pde)文件中或在[../libraries/GCS_MAVLink/GCS](https://github.com/diydrones/ardupilot/blob/master/libraries/GCS_MAVLink/GCS.h)类中。

在我们想要添加一个新的导航指令的例子中（比如执行特技动作），应该需要下面信息：

- 扩展[AP_Mission库](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Mission)中的`mission_cmd_to_mavlink()`和`mavlink_to_mission_cmd()`方法，将mavproxy的指定转换到一个`AP_Mission::Mission_Command`结构体中。
- 在飞行器的[commands_logic.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/commands_logic.pde)文件中分别添加`start_command()`函数和`verify_command()`函数的一个`case`分支，用来校验新的消息指令`MAV_CMD_NAV_TRICK`是否接收到。这些需要你调用自己创建的两个新函数`do_trick()`和`verify_trick()`（具体参考下面）。
- 创建两个新函数`do_trick()`和`verify_trick()`，用来控制飞行器如何执行特技动作（这可能需要调用[control_auto.pde]()中的另一个函数来设置`auto_mode`变量，然后调用新方法`auto_trick_start()`）。当指令第一次被唤醒时将使用`do_trick()`函数。`verify_trick()`函数将会以10hz频率（或者更高）被重复调用直到特技动作完成，当特技动作执行完毕之后`verify_trick()`函数应该返回`True`。

---
**Step #6**：考虑是否发布你的代码到主代码仓库中。

你可以发邮件到[drones-discuss email list](https://groups.google.com/forum/#!forum/drones-discuss)并且/或者[发送一个pull请求](http://dev.ardupilot.com/wiki/code-overview-adding-a-new-mavlink-message/wiki/submitting-patches-back-to-master/)。如果你发送一个pull提交请求，最好将改变的部分分成至少三个部分的提交确认（commits,与git指令相关，包括pull、push等）。一个是.xml文件的改变提交确认（Setp #3），另一个是重新生成文件的（Step #4），剩下的还有一个或者更多是关于飞行器主代码变化的提交确认。

---
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/code-overview-adding-a-new-mavlink-message/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*