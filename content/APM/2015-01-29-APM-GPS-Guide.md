Title: APM-GPS指南
Date: 2015-1-29 14:36:02 
Tags: APM

<!-- PELICAN_BEGIN_SUMMARY -->
<!-- PELICAN_END_SUMMARY -->

### GPS指南 ###

    //  *EXPLAINED*   
    // Diydrones is a Open source site and different people use different quipement,
    // because of this there are different GPS modules available to use and APM needs to be told wich one you have purchased.
    //  
    //  *INSTRUCTIONS*
    // Look at the list of GPS modules below, look for your specific module and define it as follows
    // example" #define GPS_PROTOCOL GPS_PROTOCOL_UBLOX " please note that only the "GPS_PROTOCOL_UBLOX " part of the statement changes 
    // and your's should look identical after editing.
    //   
    //   *AVAILABLE OPPTIONS*
    // GPS_PROTOCOL_NONENo GPS attached
    // GPS_PROTOCOL_IMU X-Plane interface or ArduPilot IMU.
    // GPS_PROTOCOL_MTK MediaTek-based GPS.
    // GPS_PROTOCOL_MTK16   MediaTek GPS with firmware 1.6
    // GPS_PROTOCOL_UBLOX   UBLOX GPS
    // GPS_PROTOCOL_SIRFSiRF-based GPS in Binary mode.  NOT TESTED
    //  ******************
    //   *SELECTED OPPTION*
    #define GPS_PROTOCOL GPS_PROTOCOL_UBLOX
    //  ******************

----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/gps_guide/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*