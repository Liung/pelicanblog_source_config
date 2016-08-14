Title: APM-添加新的飞行模式
Date: 2014-9-5 11:01:10 
Tags: APM,APM:Copter,飞控板,硬件

<!-- PELICAN_BEGIN_SUMMARY -->
这部分将涵盖一些怎样创建一个新的高级别的飞行模式的基本操作步骤（类似于自稳，悬停等），这些新模式处于“the onion”（洋葱头工程）中的高级别代码控制部分，如之前[姿态控制页面]({filename}2014-08-31-APM-ArduCopter姿态控制概览.md)描述的一样。不过遗憾的是本页面并没有提供给你关于所创建的理想飞行模式需要的所有信息，但是希望这将是一个好的开始。
<!-- PELICAN_END_SUMMARY -->

---
**Step #1**：在文件[defines.h](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/defines.h#L88)中用`#define`定义你自己新的飞行模式,然后将飞行模式数量`NUM_MODES`加1。

        // Auto Pilot modes
        #define STABILIZE 0 // hold level position
        #define ACRO 1 // rate control
        #define ALT_HOLD 2 // AUTO control
        #define AUTO 3 // AUTO control
        #define GUIDED 4 // AUTO control
        #define LOITER 5 // Hold a single location
        #define RTL 6 // AUTO control
        #define CIRCLE 7 // AUTO control
        #define LAND 9 // AUTO control
        #define OF_LOITER 10 // Hold a single location using optical flow sensor
        #define DRIFT 11 // DRIFT mode (Note: 12 is no longer used)
        #define SPORT 13 // earth frame rate control
        #define FLIP 14 // flip the vehicle on the roll axis
        #define AUTOTUNE 15 // autotune the vehicle's roll and pitch gains
        #define POSHOLD 16 // position hold with manual override
        
        #define NEWFLIGHTMODE 17    // 描述你所定义的模式内容
        #define NUM_MODES 18        //模式数+1
    
---
**Step #2**：类似于相似的飞行模式的[control_stabilize.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_stabilize.pde)或者[control_loiter.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/control_loiter.pde)文件，创建新的飞行模式的`<new flight mode>.pde`控制sketch文件。该文件中必须包含一个`_init()`初始化函数和`_run()`运行函数。

```
/// -*- tab-width: 4; Mode: C++; c-basic-offset: 4; indent-tabs-mode: nil -*-

/*
 * control_newflightmode.pde - init and run calls for new flight mode
 */

// newflightmode_init - initialise flight mode
static bool newflightmode_init(bool ignore_checks)
{
    // do any required initialisation of the flight mode here
    // this code will be called whenever the operator switches into this mode

    // return true initialisation is successful, false if it fails
    // if false is returned here the vehicle will remain in the previous flight mode
    return true;
}

// newflightmode_run - runs the main controller
// will be called at 100hz or more
static void newflightmode_run()
{
    // if not armed or throttle at zero, set throttle to zero and exit immediately
    if(!motors.armed() || g.rc_3.control_in <= 0) {
        attitude_control.relax_bf_rate_controller();
        attitude_control.set_yaw_target_to_current_heading();
        attitude_control.set_throttle_out(0, false);
        return;
    }

    // convert pilot input into desired vehicle angles or rotation rates
    //   g.rc_1.control_in : pilots roll input in the range -4500 ~ 4500
    //   g.rc_2.control_in : pilot pitch input in the range -4500 ~ 4500
    //   g.rc_3.control_in : pilot's throttle input in the range 0 ~ 1000
    //   g.rc_4.control_in : pilot's yaw input in the range -4500 ~ 4500

    // call one of attitude controller's attitude control functions like
    //   attitude_control.angle_ef_roll_pitch_rate_yaw(roll angle, pitch angle, yaw rate);

    // call position controller's z-axis controller or simply pass through throttle
    //   attitude_control.set_throttle_out(desired throttle, true);
}
```

---
**Step #3**：在文件[flight_mode.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/flight_mode.pde#L269)文件的`set_mode()`函数中增加一个新飞行模式的`case`（C++中switch..case语法）选项，然后调用上面的`_init()`函数。

    // set_mode - change flight mode and perform any necessary initialisation
    static bool set_mode(uint8_t mode)
    {
        // boolean to record if flight mode could be set
        bool success = false;
        bool ignore_checks = !motors.armed();   // allow switching to any mode if disarmed.  We rely on the arming check to perform
    
        // return immediately if we are already in the desired mode
        if (mode == control_mode) {
            return true;
        }
    
        switch(mode) {
            case ACRO:
                #if FRAME_CONFIG == HELI_FRAME
                    success = heli_acro_init(ignore_checks);
                #else
                    success = acro_init(ignore_checks);
                #endif
                break;
            
            //这里添加case选型：指定飞行模式，然后条用_init()函数
            case NEWFLIGHTMODE:
                success = newflightmode_init(ignore_checks);
                break;
        }
    }

---
**Step #4**：在文件[flight_mode.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/flight_mode.pde#L269)文件的`update_flight_mode()`函数中增加一个新飞行模式的`case`选项，然后调用上面的`_run()`函数。

    // update_flight_mode - calls the appropriate attitude controllers based on flight mode
    // called at 100hz or more
    static void update_flight_mode()
    {
        switch (control_mode) {
            case ACRO:
                #if FRAME_CONFIG == HELI_FRAME
                    heli_acro_run();
                #else
                    acro_run();
                #endif
                break;

            //这里添加case选型：指定飞行模式，然后条用_run()函数
            case NEWFLIGHTMODE:
                success = newflightmode_run();
                break;
        }
    }

---
**Step #5**：在文件[flight_mode.pde](https://github.com/diydrones/ardupilot/blob/master/ArduCopter/flight_mode.pde#L269)文件的`print_flight_mode()`函数中增加可以输出新飞行模式字符串的`case`选项。

    static void
    print_flight_mode(AP_HAL::BetterStream *port, uint8_t mode)
    {
        switch (mode) {
        case STABILIZE:
            port->print_P(PSTR("STABILIZE"));
            break;

        //这里增加case选型，执行输出当前飞行模式
        case NEWFLIGHTMODE:
            port->print_P(PSTR("NEWFLIGHTMODE"));
            break;

---
**Step #6**：在文件[Parameters.pde]()中向`FLTMODE1` ~ `FLTMODE6`参数中正确的增加你的新飞行模式到`@Values`列表中。

    // @Param: FLTMODE1
    // @DisplayName: Flight Mode 1
    // @Description: Flight mode when Channel 5 pwm is 1230, <= 1360
    // @Values: 0:Stabilize,1:Acro,2:AltHold,3:Auto,4:Guided,5:Loiter,6:RTL,7:Circle,8:Position,9:Land,10:OF_Loiter,11:ToyA,12:ToyM,13:Sport,17:NewFlightMode  //列表末尾添加新的正确形式飞行模式
    // @User: Standard
    GSCALAR(flight_mode1, "FLTMODE1",               FLIGHT_MODE_1),

    // @Param: FLTMODE2
    // @DisplayName: Flight Mode 2
    // @Description: Flight mode when Channel 5 pwm is >1230, <= 1360
    // @Values: 0:Stabilize,1:Acro,2:AltHold,3:Auto,4:Guided,5:Loiter,6:RTL,7:Circle,8:Position,9:Land,10:OF_Loiter,11:ToyA,12:ToyM,13:Sport,17:NewFlightMode  //列表末尾添加新的正确形式飞行模式
    // @User: Standard
    GSCALAR(flight_mode2, "FLTMODE2",               FLIGHT_MODE_2),

---
**Step #7**：如果你想让你的新飞行模式出现的Mission Planner的平视显示器HUD和飞行模式组件中，你可以在[Mission Planner的问题列表](https://github.com/diydrones/MissionPlanner/issues)中提出你的请求。

![MP_HUD](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/FlightMode.png)

---
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/apmcopter-adding-a-new-flight-mode/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*