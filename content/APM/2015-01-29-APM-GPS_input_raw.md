Title: APM-GPS原始输出
Date: 2015-1-29 15:39:21 
Tags: APM

### 原始GPS输出 ###
<!-- PELICAN_BEGIN_SUMMARY -->
本页面用来说明GPS模块原始的输出形式。如果你在GPS的正常测试过程中遇到问题，那么这些命令可能有助于你进行调试。
<!-- PELICAN_END_SUMMARY -->

*大多数用户不推荐，仅用于GPS底层硬件调试*

如果你想要以ASCII格式查看GPS输出，在测试命令窗口将该行：

    Serial.print(incoming,BYTE); // will output Byte values

改为:

    Serial.print(incoming,ASCII); // will output ASCII values

----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/gps_input_raw/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*