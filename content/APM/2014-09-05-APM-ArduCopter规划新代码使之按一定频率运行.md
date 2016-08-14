Title: APM-规划新代码使之按一定频率运行
Date: 2014-9-5 12:08:26 
Tags: APM,APM:Copter,飞控板,硬件

本页面将向你介绍如何规划你的新代码块使之可以按需运行。

---
###用代码调度器运行你的代码
在给定时间间隔内来运行你的代码的最灵活的方式就是使用调度器。这可以通过将你的函数添加到文件[ArduCopter.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde)中的[`scheduler_tasks`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L788)数组来完成。需要表明的是：实际上该文件中有两个任务列表，[上面的任务列表](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L788)是针对高频CPUs（如Pixhawk），[下面的](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L856)是针对低频CPUs（如APM2）。

<!-- PELICAN_BEGIN_SUMMARY -->
添加一个任务是相当的简单，你只要在列表添加新的一行代码就可以了（列表中位置越靠前意味着拥有更高的级别）。任务项中的第一列代表了函数名，第二列是以2.5ms为单位的数字（或者APM2中以10ms为单位）。所以，如果你想要你的函数执行频率为400Hz，那么该列就需要填写为“1”，如果想要50Hz，那么就需要改为“8”。任务项的最后一列代表该函数预计运行花费的微秒（百万分之一秒）时间。这可以帮助调度器来预估在下一个主循环开始之前有否有足够的时间来运行你的函数。
<!-- PELICAN_END_SUMMARY -->

```
/*
  scheduler table - all regular tasks apart from the fast_loop()
  should be listed here, along with how often they should be called
  (in 10ms units) and the maximum time they are expected to take (in
  microseconds)
 */
static const AP_Scheduler::Task scheduler_tasks[] PROGMEM = {
    { update_GPS,            2,     900 },
    { update_nav_mode,       1,     400 },
    { medium_loop,           2,     700 },
    { update_altitude,      10,    1000 },
    { fifty_hz_loop,         2,     950 },
    { run_nav_updates,      10,     800 },
    { slow_loop,            10,     500 },
    { gcs_check_input,	     2,     700 },
    { gcs_send_heartbeat,  100,     700 },
    { gcs_data_stream_send,  2,    1500 },
    { gcs_send_deferred,     2,    1200 },
    { compass_accumulate,    2,     700 },
    { barometer_accumulate,  2,     900 },
    { super_slow_loop,     100,    1100 },
      { my_new_function,      10,     200 },  //here,添加你的任务项
    { perf_update,        1000,     500 }
};
```

---
###作为循环的一部分运行你的代码
为了代替在代码调度器中加入一个新的函数入口，你还可以在现有的任何时间循环事件中添加你的函数。除了在fast-loop循环中添加外，这种方法对比起上面的代码调度器方法并没有什么实质性好处。但当你的代码添加到fast-loop循环中时，就意味着它将以最高的优先级别来执行（它几乎能100%达到所确保的400hz运行速度）。

- [**fast_loop**](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L990):APM2上运行频率100hz，Pixhawk上400Hz
- [**fifty_hz_loop**](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L1119):运行频率50hz
- [**ten_hz_logging_loop**](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L1101):运行频率10hz
- [**three_hz_loop**](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L1138):运行频率3.3hz
- [**on_hz_loop**](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L1159):运行频率1hz

所以举个例子，如果你想让你的代码运行频率为10hz，那么你就要将它添加到[ArduCopter.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde)文件的[`ten_hz_logging_loop()`](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/ArduCopter.pde#L1101)函数声明中。

```
// ten_hz_logging_loop
// should be run at 10hz
static void ten_hz_logging_loop()
{
    if (g.log_bitmask & MASK_LOG_ATTITUDE_MED) {
        Log_Write_Attitude();
    }
    if (g.log_bitmask & MASK_LOG_RCIN) {
        DataFlash.Log_Write_RCIN();
    }
    if (g.log_bitmask & MASK_LOG_RCOUT) {
        DataFlash.Log_Write_RCOUT();
    }
    if ((g.log_bitmask & MASK_LOG_NTUN) && mode_requires_GPS(control_mode)) {
        Log_Write_Nav_Tuning();
    }

        // 在这里添加你的新代码
        my_new_function();
}
```

---
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/code-overview-scheduling-your-new-code-to-run-intermittently/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*