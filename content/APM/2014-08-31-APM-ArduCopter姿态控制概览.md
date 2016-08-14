Title: APM-ArduCopter姿态控制概览
Date: 2014-8-31 21:53:09 
Tags: APM,飞控板,硬件

<!-- PELICAN_BEGIN_SUMMARY -->
在从版本AC3.1向AC3.2的过渡中，姿态控制逻辑运算作为“the onion”（洋葱头）工程的一部分进行了重构。下面来展示重构后的程序执行流程。
<!-- PELICAN_END_SUMMARY -->

---
###手动飞行模式

**自稳模式（Stabilize Mode）、特技模式（Acro Mode）、浮动模式（Drift Mode）**

![flight-mode](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/AC_CodeOverview_ManualFlightMode.png)

在主循环执行过程中（比如Pixhawk的运行频率为400Hz，APM2.x为100Hz），系统依次执行如下操作：

- 调用最高层次级别文件flight-mode.pde中的`update_flight_mode()`函数。该函数监测当前飞行器的飞行模式（使用变量`control_mode`），然后执行相应飞行模式下的`<flight mode>_run()`函数（如自稳模式的[`stabilize_run`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_stabilize.pde#L20)，返航模式（RTL）的[`rtl_run`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_rtl.pde#L23)等）。执行`<flight mode>_run`的结果是，系统将会找到与飞行模式相对应的命名为`control_<flight mode>.pde`飞行控制文件（比如：[`control_stabilize.pde`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_stabilize.pde)，[`control_rtl.pde`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_rtl.pde)等）。

- `<flight mode>_run`函数负责将用户的输入（从`g.rc_1.control_in`，`g.rc_2.control_in`等读入）转换为此时飞行模式下的倾斜角（lean angle）、滚转速率（rotation rate）、爬升率（climb rate）等。举个例子：[AltHold](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_althold.pde#L22)(定高，altitude hold)模式中将用户的滚转和俯仰输入转换为倾斜角（单位：角度/°），将偏航输入转换为滚转速率（单位：°/s），将油门输入转换为爬升率（单位：cm/s）。

- `<flight mode>_run`函数最后还必须要完成的就是将**预期角度、速率等参数**传送给姿态控制和/或方位控制库（它们都放在[AC_AttitiudeControl](https://github.com/diydrones/ardupilot/tree/master/libraries/AC_AttitudeControl)文件夹内）。

- [AC_AttitiudeControl](https://github.com/diydrones/ardupilot/tree/master/libraries/AC_AttitudeControl)库提供了5中可能的方法来调整飞行器的姿态，下面来说明最通用的三种方法：

------>1) [`angle_ef_roll_pitch_rate_ef_yaw()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_AttitudeControl.h#L98):该函数需要一个地轴系坐标下滚转和偏航角度，一个地轴系坐标下的偏航速率。例如：传递给该函数三个参数分别为，`roll = -1000， pitch = -1500， yaw = 500`代表飞行器此时向左倾斜10°，低头15°，向右偏航速率为5°/s。

------>2) [`angle_ef_roll_pitch_yaw()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_AttitudeControl.h#L102):该函数接受地轴系下的滚转、俯仰和偏航角。和上面的函数类似，不过参数`yaw = 500`代表飞行器北偏东5°

------>3) [`rate_bf_roll_pitch_yaw()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_AttitudeControl.h#L108):该函数接受一个**体轴系**下的滚转、俯仰和偏航角速率（°/s）。例如：传递给该函数三个参数：`roll = -1000， pitch = -1500， yaw = 500`代表飞行器此时左倾速率10°/s，低头速率15°/s，绕Z轴速率为5°/s。

当上述这些函数调用之后，就会接着调用[`AC_AttitudeControl::rate_controller_run()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_AttitudeControl.h#L114)函数，将上面所列举的函数的输出转化为滚转、偏航和俯仰输入，并使用[`set_roll,set_pitch,set_yaw` 和 `set_throttle`](https://github.com/diydrones/ardupilot/blob/master/libraries/AP_Motors/AP_Motors_Class.h#L99)方法将这些输入发送给[**AP_Motors**](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Motors)库。

- [AC_PosControl](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_PosControl.h)库用来控制飞行器的3D方位。不过通常只用来调整比较简单的Z轴方向（如姿态控制），这是因为许多需要复杂3D方位调整的飞行模式(例如[悬停Loiter](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_loiter.pde#L30))使用的是[AC_WPNav](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_WPNav/AC_WPNav.h)库。总之，AC_PosControl库中常用的方法有：

------>1) `set_alt_target_from_climb_rate()`:将爬升率（cm/s）作为参数，用来更新一个需要调整的相对高度目标。

------>2)  `set_pos_target()`:接受一个以系统中的`home`位置作为参考点的3D位置矢量（单位：cm）。


如果调用了AC_PosControl中的任何一个方法，那么在该飞行模式下就必须调用函数[`AC_PosControl::update_z_controller()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_PosControl.h#L134)。这样的话，就可以启用Z轴的方位控制PID循环，并向[**AP_Motors**](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Motors)库发送低级别的油门信息。同样，如果调用了xy轴的函数，那就就必须调用[`AC_PosControl::update_xy_controller()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AC_AttitudeControl/AC_PosControl.h#L202)函数。

- **AP_Motors**库含有“电机混合模式”代码。这些代码负责将从**AC_AttitudeControl**和**AC_PosControl**库发送过来的滚转、俯仰、偏航角度和油门值信息转换为电机的相对输出值（例如：PWM值）。因此，这样高级别的库就必须要使用如下函数：

------>1) [`set_roll(),set_pitch(),set_yaw()`](https://github.com/diydrones/ardupilot/blob/master/libraries/AP_Motors/AP_Motors_Class.h#L99)：接受在[-4500,4500]角度范围内的滚转、俯仰和偏航角。这些参数不是期望角度或者速率，更准确的讲，它仅仅是一个数值。例如，set_roll(-4500)将代表飞行器尽可能快的向左滚转。

------>2) `set_throttle()`:接受一个范围在[0,1000]的相对油门值。0代表电机关闭，1000代表满油门状态。

虽然对于不同飞行器构型（如四旋翼，Y6，传统直升机等）的控制代码中有许多不同的类，但这些类中都有一个相同的函数`output_armed`，负责将这些滚转、俯仰、偏航和油门值转换为PWM类型输入值。这转换的过程中，会应用到**stability patch**（译者注：翻译成中文感觉不妥，类似于控制飞行器稳定性分析程序代码块），用来控制由于飞行器构型限制所引起的轴系的优先级问题（例如四旋翼的四个电机不可能在做最大速度滚转时四个电机的油门同时达到最大，因为必须一部分电机输出小于另一部分才能引起滚转）。在执行函数`output_armed`的最后，还将调用`hal.rcout->write()`，把期望PWM值传递给**AP_HAL**层。

- AP_HAL库（硬件抽象层）提供了针对所有飞控板统一的借口。实际控制中，`hal.rc_out_write()`函数将接受到的来自于AP_Motors类中指定的PWM值，输出至飞控板对应的PWM端口（pin端）。

---
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/apmcopter-programming-attitude-control-2/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*