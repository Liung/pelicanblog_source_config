Title: APM-MAVLink命令集
Date: 2015-1-29 17:45:52 
Tags: APM, MAVLink

### APM 2.0 命令集 ###
<!-- PELICAN_BEGIN_SUMMARY -->
APM 2.0版本已经采用部分MAVLink消息协议。[这里](http://diydrones.com/group/arducopterusergroup/forum/topics/mavlink-tutorial-for-absolute-dummies-part-i?xg_source=activity)有一份“傻瓜式指南”直接对MAVLink进行操作。<!-- PELICAN_END_SUMMARY -->

APM命令集以14个字节形式存储，字节对应的含义如下表所示：

Byte #|Address|Data type|Function
:---|:---:|:---:|:---:
0|0x00|byte|Command ID
1|0x01|byte|Options
2|0x02|byte|Parameter 1
3|0x03|long|Parameter 2
4|0x04|..|
5|0x05|..|
6|0x06|..|
7|0x07|long|Parameter 3
8|0x08|..|
9|0x09|..|
10|0x0A|..|
11|0x0B|long|Parameter 4
12|0x0C|..|
13|0x0D|..|
14|0x0E|..|



----------
**导航命令-这些参数都包含有lat和lon**

导航参数具有最高的优先级。对于ID比导航命令更高的命令，当下次导航命令接收到时未被执行的命令将直接被丢弃，所以规划/队列命令集具有差异。

例如，当航点到达时，正准备执行CMD_MAV_CONDITION命令时又紧接着接收到||ox10命令（导航命令），这时未被执行的CMD_MAV_CONDITION和CMD_MAV_DO命令会直接跳过，加载下一个导航命令。

Command ID hex/decimal|Name|Parameter 1|Altitude|Latitude|Longitude|notes
---|---|---|---|---|---|---
0x10 / 16|MAV_CMD_NAV_WAYPOINT|-|altitude|lat|lon|
0x11 / 17|MAV_CMD_NAV_LOITER_UNLIM|(indefinitely)|altitude|lat|lon|
0x12 / 18|MAV_CMD_NAV_LOITER_TURNS|turns|altitude|lat|lon|
0x13 / 19|MAV_CMD_NAV_LOITER_TIME|time (seconds*10)|altitude|lat|lon|
0x14 / 20|MAV_CMD_NAV_RETURN_TO_LAUNCH|-|altitude|lat|lon|
0x15 / 21|MAV_CMD_NAV_LAND|-|altitude|lat|lon|
0x16 / 22|MAV_CMD_NAV_TAKEOFF|takeoff pitch|altitude|-|-|NOTE: for command 0x16 the value takeoff pitch specifies the minimum pitch for the case with airspeed sensor and the target pitch for the case without.
0x17 / 23|MAV_CMD_NAV_TARGET|-|altitude|lat|lon|



----------
**微型飞行器相关命令-这些命令具有终止和完成任务标准，例如“到达航点”或者“到达指定高度”**


Command ID|Name|Parameter 1|Parameter 2|Parameter 3|Parameter 4|notes
---|---|---|---|---|---|---
0x70 / 112|MAV_CMD_CONDITION_DELAY|-|-|time (seconds)|-|
0x71 / 113|MAV_CMD_CONDITION_CHANGE_ALT|rate (cm/sec)|alt (finish)|-|-|Note: rate must be >
||||||10 cm/sec due to integer math
0x72 / 114|MAV_CMD_CONDITION_DISTANCE|-|-|distance (meters)|-|




----------
**实时命令（Now Comands）-这些命令集如果检测到存在新的可用实时命令将立刻执行**

**注意：当前DO_XXX命令集需要该命令之后存在一个缓冲航点**


Command ID|Name|Parameter 1|Parameter 2|Parameter 3|Parameter 4|notes
---|---|---|---|---|---|---
0xB1 / 177|MAV_CMD_DO_JUMP|index|-|repeat count|-|Note: The repeat count must be greater than 1 for the command to execute. Use a repeat count of 1 if you intend a single use.
0xB2 / 178|MAV_CMD_DO_CHANGE_SPEED|Speed type|Speed (m/s)|Throttle (Percent)|-|"(0Airspeed| 1"
||||||
||||||Ground Speed)(-1 indicates no change)(-1 indicates no change)
0xB3 / 179|MAV_CMD_DO_SET_HOME|Use current|altitude|lat|lon|"(1use current location| 0"
||||||
||||||use specified location)
0xB4 / 180|MAV_CMD_DO_SET_PARAMETER|Param number|Param value|(NOT CURRENTLY IMPLEMENTED IN APM)||
0xB5 / 181|MAV_CMD_DO_SET_RELAY|Relay number|On/off (1/0)|-|-|
0xB6 / 182|MAV_CMD_DO_REPEAT_RELAY|Relay number|Cycle count|Cycle time (sec)|-|"Note: Max cycle time = 60 sec| A repeat relay or repeat servo command will cancel any current repeating event"
0xB7 / 183|MAV_CMD_DO_SET_SERVO|Servo number (5-8)|On/off (1/0)|-|-|
0xB6 / 184|MAV_CMD_DO_REPEAT_SERVO|Servo number (5-8)|Cycle count|Cycle time (sec)|-|"Note: Max cycle time = 60 sec| A repeat relay or repeat servo command will cancel any current repeating event"


----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/mavlink-commands/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*