Title: MissionPlanner-仿真界面分析
Date: 2015-4-1 13:48:13 
Tags: APM, MP
modifed: 2015-4-1 14:11:56 
state: draft

<!-- PELICAN_BEGIN_SUMMARY -->
地面站软件Mission Planner的仿真界面的主要代码文件GCSViews下的Simulation.cs文件。本文详细对Simulation文件的代码内容进行分析。
<!-- PELICAN_END_SUMMARY -->

文件Simulation.cs中包含了：

Simulation类

命名空间： MissionPlaner.GCSView

父类：MyUserControl

方法：

- Simulation():构造仿真界面，包含有各个组件
- ~Simulation():
- Simulation_Load(o, e):
- ConnectcomPort_Click(o, e):
- mainloop():
- CHKdisplayall_CheckedChanged(o, e):选择时，绘制四个通道（pitch, roll, rudder, throttle）的信号值。
- GPSrate_SelectedIndexChanged(o, e):更新整形参数GPS_rate。
- updateGains():当roll、pitch、rudder、throttle文本框的增益发生变化（默认值为10000）时，更新整形变量rollgain、pitchgain、ruddergain、throttlegain。
- BUT_startfgquad_Click(o, e):配置FlightGear程序参数（包含了端口号、包类型UDP、IP地址等），并启动程序。
- xmlconfig(bool):写入系统的哈希表config中。
- but_advsettings_Click(o, e):修改Sim和SITL的IP地址和端口，然后执行xmlconfig(true)函数。
- SaveSettings_Click(o, e):执行xmlconfig(true)函数。
- ConnectComPort_Click(o, e):开始仿真按钮事件，

### 命名空间 ###

#### MissionPlanner.HIL ####

- **Vector3**：该类实现了常规3维向量的一般算法。
- **Matrix3**:该类实现了常规3行3列矩阵的一般算法。
- **Utils**:该类中提供了常用的姿态、变量换算、位置计算常用算法。
- **Wind**：继承Utils，表示风的模型类。
- **Aircraft**：继承自Utils，实现了简单的固定翼模型类。
- **Motor**：继承自Utils，实现了不同构型的简单的电机类。
- **MultiCopter**：继承自Aircraft，实现了简单的旋翼模型类。
- **XPlane**：继承自Utils和IDisposable，实现了与XPlane通信等相关操作的模型类。

*(over)*