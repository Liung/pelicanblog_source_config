Title: APM:Copter相关库
Date: 2014-8-30 15:53:36 
Tags: APM:Copter, APM, 硬件, C++

<!-- PELICAN_BEGIN_SUMMARY -->
这些[库文件](https://github.com/diydrones/ardupilot/tree/master/libraries)也同样被ArduPlane和ArduRover所使用。下面将列出一系列高层次的库的说明和它们的函数说明。
<!-- PELICAN_END_SUMMARY -->

###核心库
- [AP_AHRS](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_AHRS)：采用DCM（方向余弦矩阵方法）或EKF（扩展卡尔曼滤波方法）预估飞行器姿态
- [AP_Common](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_InertialNav)：所有执行文件（sketch格式，arduino IDE的文件）和其他库都需要的基础核心库。
- [AP_Math](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Math)：包含了许多数学函数，特别对于矢量运算
- [AP_PID](https://github.com/diydrones/ardupilot/tree/master/libraries/AC_PID)：PID控制器库
- [AP_InertialNav](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_InertialNav)：扩展带有gps和气压计数据的惯性导航库
- [AP_AttitudeControl](https://github.com/diydrones/ardupilot/tree/master/libraries/AC_AttitudeControl)：姿态控制相关库
- [AP_WPNav](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_InertialNav)：航点相关的导航库
- [AP_Motors](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Motors)：多旋翼和传统直升机混合的电机库
- [RC_channel](https://github.com/diydrones/ardupilot/tree/master/libraries/RC_Channel)：更多的关于从APM_RC的PWM输入/输出数据转换到内部通用单位的库，比如角度
- [AP_HAL](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_HAL)，[AP_HAL_AVR](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_HAL_AVR)，[AP_HAL_PX4](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_HAL_PX4):硬件抽象层库，提供给其他高级控制代码一致的接口，而不必担心底层不同的硬件

###传感器相关库
- [AP_InertialSensor](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_InertialSensor)：读取陀螺仪和加速度计数据，并向主程序执行标准程序和提供标准单位数据（deg/s，m/s）。
- [AP_RangerFinder](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_RangeFinder)：声呐和红外测距传感器的交互库
- [AP_Baro](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Baro)：气压计相关库
- [AP_GPS](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_GPS)：GPS相关库
- [AP_Compass](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Compass)：三轴罗盘相关库
- [AP_OpticalFlow](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_OpticalFlow)：光流传感器相关库

###其他库
- [AP_Mount](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Mount)，[AP_Camera](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Camera), [AP_Relay](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Relay)：相机安装控制库，相机快门控制库
- [AP_Mission](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Mission)： 从eeprom（电可擦只读存储器）存储/读取飞行指令相关库
- [AP_Buffer](https://github.com/diydrones/ardupilot/tree/master/libraries/AP_Buffer)：惯性导航时所用到的一个简单的堆栈（FIFO，先进先出）缓冲区

这是本人做的一张关于库的导航图：

![daohang]({filename}../images/apm-libraries.png)

####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/apmcopter-programming-libraries/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*