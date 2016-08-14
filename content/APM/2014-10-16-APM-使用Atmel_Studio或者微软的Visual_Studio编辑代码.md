Title: APM-使用Atmel Studio 或者微软的Visual Studio编辑代码
Date: 2014-10-16 13:54:19 
Tags: APM,飞控板,硬件

![1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/04/Atmel-Studio-+-Visual-Micro-300x238.jpg)

### 简介 ###
<!-- PELICAN_BEGIN_SUMMARY -->
对APM代码开发需要一款高鲁棒性的开发环境？请尝试使用Atmel Studio 6.2或者带有[Visual Micro](http://www.visualmicro.com/)插件的微软Visual Studio吧。使用这些工具你可以编辑、编译、上载你的APM代码，其中，编译与上传代码与Ardupilot Arduino的编译方法一致。本指南带你开始这方面的内容。
<!-- PELICAN_END_SUMMARY -->

**预览**：Atmel Studio或微软的Visual Studio提供了高鲁棒性的集成开发环境（IDE）。但是，Ardupilot是建立在特殊版本的Ardupilot Arduino IDE上，所以没有相关插件来设置正确的工程结构关系和提供上传工具，这些代码是不能在这些环境中正常工作的。使用Arduino找到不同函数与类型的源文件是非常困难的，有时寻找在主代码初始设置体与循环体中的函数或者类的原始定义代码文件，需要通过多个文件与目录来人工搜索。

**解决方案**：Visual Micro能够解决上述的大部分问题。Visual Micro作为Atmel Studio或Visual Studio软件的一个插件，具有如下特性：

- 兼容Arduino代码结果关系，库，文件命名与sketch程序块（配合高鲁棒性的studio IDE）
- 能够将Arduino sketch代码上传到任何类型的Arduino板和APM飞控板
- 解决方案面板中显示所有文件，方便任何文件的打开、浏览与编辑
- 可以前往[Visual Micro](http://www.visualmicro.com/)网站了解更多细节
- Visual Micro具有对标准的Arduino sketches代码文件的调试功能。但是APM代码已经移除或更改了许多标准Arduino特性(例如`Serial.print()`)和硬件串口特性。Visual Micro调试器不能对APM正常工作。但是，这不能让我们放弃使用Atmel Studio或者Visual Studio IDE

这里来一步一步地介绍设置Atmel Stduio或者Visual Studio来浏览、编辑、编译和上传APM代码。特别感谢Tim Leek对于开发出Visual Micro这样棒的插件以及对本文档撰写提供的帮助。

----------
### 安装软件 ###
如果你之前没有使用过Atmel Studio或Visual Studio Pro软件，但曾经使用Arduino IDE编译过APM代码，那么本指南对你来说是一个很好的开始。文中给出了其它相关详细信息的wiki页面链接，但不包含Visual Studio和Atmel Studio特性的介绍，因此你需要自己学习相关知识。[Visual Micro](http://www.visualmicro.com/)网站介绍了如何针对Arduino安装Visual Micro以及如何设置Ateml Studio和Visual Studio来使用Arduino sketches代码文件和不同类型板子工作，但是没有明确涉及到如何支持APM飞控板的相关说明。一旦这些信息明确，那么设置工作变得非常简单。这里列入了所需要的一些关键步骤的简短总结：

- 假定：

　　　　■ 特殊版本的Ardupilot Arduino已经安装，并且已经测试能够正常编译与上传代码。详细细节点击[这里](http://dev.ardupilot.com/wiki/building-ardupilot-with-arduino-windows/)，这里假定该软件安装在C:\ArduPilot-Arduino-1.0.3-windows

　　　　■ 需要安装[Atmel Studio](http://www.atmel.com/tools/ATMELSTUDIO.aspx)（免费版）和带有许可证的Visual Studio 2008、2010或2012完整版。Visual Micro不能在Visual Studio的Express版正常运行。本例中使用了Visual Studio 2008

　　　　■ 需要下载Ardupilot源码。对于本教程，假定APM源码存放在C:\Users\Public\Documents\ardupilot-ArduCopter-3.1.3。[这里](http://ardupilot.com/downloads/?category=29)可以得到最新发布的源码压缩文件“APM：Plane x.x.x”，或使用[GitHub](http://dev.ardupilot.com/wiki/where-to-get-the-code/)克隆一份当前代码到本地。如果你需要特定发布版本，请到[diydrones/ardupilot](https://github.com/diydrones/ardupilot)代码仓库中，选择想要的ardupilot分支，然后点击**download zip**。

- 下载并安装了[Visual Micro](http://www.visualmicro.com/)网站的Visual Micro，并且完成[软件安装](http://www.visualmicro.com/post/2011/10/04/How-to-test-a-new-installation-of-Arduino-for-Visual-Studio.aspx)部分内容。参考网站说明。
- 对Arduino使用[本说明](http://www.visualmicro.com/post/2011/10/04/How-to-test-a-new-installation-of-Arduino-for-Visual-Studio.aspx)进行了Visual Micro测试。继续进行之前确保能够正常工作。
- 下载并安装APM飞控板相关信息文件。该步骤在编译和上传APM代码中是必须的。

　　　　■ 前往Visual Micro论坛的[Apm-安装指导](http://www.visualmicro.com/post/2013/05/02/APM-Installation-Guide.aspx)页面。阅读相关内容并下载[boards.txt](http://www.visualmicro.com/downloads/APM_Sketchbook_Hardware.zip)文件

　　　　■ 将“boards.txt”文件放到包含有“Arduino/hardware”文件夹的“APM”目录中。无论你的Arduino IDE存放在什么地方，你的Arduino文件（本例中位于C:\ArduPilot-Arduino-1.0.3-windows）应该具有如下结构：

![2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/04/VisualMicroHardware.jpg)

　　　　■ 运行Atmel Studio或Visual Studio，针对APM设置如下：（本例中使用APM2）

　　　　　　　　-->★ Tools>>Visual Micro>>Boards：选择Arduino Mega 2560 （APM2）

　　　　　　　　-->★ Tools>>Options>>Visual Micro：窗口右侧，选择Applications & Locations>>Application Ide Locations>>Click to configure Ide locations。在对话窗口：

　　　　　　　　　　　　---->☆　在下拉选项中选择Auduino为“1.0.x”

　　　　　　　　　　　　---->☆ 选择IDE的文件位置：C:\ArduPilot-Arduino-1.0.3-windows （或者你自己Arduino IDE的路径）

　　　　　　　　　　　　---->☆ 设置sketchbook位置：C:\Users\Public\Documents\ardupilot-ArduCopter-3.1.3 （或选择你自己Ardupilot代码路径）

　　　　　　　　　　　　---->☆ 注意：该文件包含了APMover2、ArduCopter、ArduPlane、docs、FollowMe、libraries、mk、Tools。下图是该部分教程的截图：

![3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/04/VisualMicroSetup-278x300.jpg)

　　　　■ 打开arducopter.pde文件： File>>Open>>Sketch Project: 然后选择ArduCopter\arducopter.pde (或者你自己电脑上代码文件中的arducopter.pde文件)

　　　　■ 编译代码： Build>>Clean Solution then Build>>Build Solution。代码编译应该不会出现错误。取决于你使用的源代码内容，可能会得到“Sketch too big …”信息。你可以通过在文件APM_Config.h中注释掉一些编译选项来减少编译后文件的大小。**Important：**每次改变`#define statement`（或者注释/取消注释代码）时，必须执行Build>>Clean Solution followed by Build>>Rebuild Solution。更多细节请查看**相关提示与注意**部分。

----------
### 上传代码 ###
当你完成代码编译并没有出现错误时，就可以上传代码到APM。

- 首先，要做：Tools>>Options>>Visual Micro -Micro Debug – Advanced设置自动调试（Automatic debugging）为False，然后摁下F5键开始不带调试上传。摁下Ctrl+F5执行保存操作。
- 使用USB连接你的APM和电脑
- 在Tools>>Visual Micro>>Serial Port，设置检测到的APM的USB端口号。如果USB端口没有检测到，那么检查Arduino安装，按照说明增加正确的驱动器。如果Arduino IDE可以正常工作，那么Visual Studio/Visual Studio也就能正常工作了。
- 摁下F5，将编译好的二进制固件加载到APM飞控板中

作者采用了3.1.3发布版本进行代码编译与上传到APM板和飞行测试，飞行测试中分别进行了自稳、定高、悬停模式测试，测试结果与通过Mission Planner加载对应版本的固件一致。但是，还是要注意编译自己从源码下载的代码可能会造成某些意外结果。你必须配置所有的选项`define`和其他代码是否正确。时刻小心，在使用Visual Micro的Visual Studio编译过程中顺利与快乐~

----------
### 相关提示与注意 ###
本次编译与上传代码到APM的整个过程都在作者电脑上进行。还有许多其他方法来配置Arduino、Atmel Studio，Visual Studio、Visual Micro。这些方法留给读者研究。举例来讲，你可以在任何位置安装Ardupilot Arduino IDE，而不仅仅局限于上文中的位置。不过建议使用上面的方法来验证整个软件等设置是否可用。

**减少Arducopter空间使之可以编译的方法**：在Visual Studio或Atmel Studio的资源方案解决面板（这里里除了所有文件资源），打开文件Arducopter/Header Files/APM_Copfit.h，取消注释一些诸如`#Define XXX DISABLED`语句，例如，禁用一些对于你的APM不用的功能：MOUNT, OPTIFLOW, CAMERA, CONFIG_CONAR和/或者PARACHUTE。每次更改`Define`语句时，必须在执行Build>>Clean Solution完后紧接着执行Build>>Rebuild Solution

**从刚下载的源码克隆库中直接编译的错误**：第一次设置应用位置（例如刚克隆了一份源码到本地后）或者改变了使用的IDE时，你可能即使选择正确的Arduino版类型的情况下依然得到一些编译错误信息。为了避免错误能够正常完成编译，仅需要重新选择正确的飞控板类型。查看**多版本的Arduino**部分内容。

**快速编译 VS 改变defines**:Visual Micro有一个默认选择快速编译。这个功能作为默认设置。IDE会监测文件的改变，如果文件没有变化，那么就不会再编译未发生改变的这部分文件。这个特性存在一些负面影响：如果某些define声明语句发生改变，可能会影响到其他文件的调用，但是这部分文本（代码）并没有明确的改变，这些由于define声明改变而影响的文件不会再次编译就会造成混乱。不过，可以采用两个方法来避免这个问题：

　　　　●　每次改变define声明或者取消注释/注释一些define语句，执行下面动作：

　　　　　　　　-->■ Build>>Clean>>Solution     （该操作会清除之前编译的缓存）

　　　　　　　　-->■ Build>>Rebuild

　　　　　　　　-->■ 接下来所有编译（假定再没有define语句发生变化）可以使用快速编译方法：Build>>Build Solution

　　　　● 或者，如果你想每次编译都喜欢等待一些时间，那么你可以改变Visual Micro的配置选项

　　　　　　　　-->■ Tools>>Options，选择Visual Micro。使用滚轮滚动到编译器优化（Compiler Optimistation）。（英式英语中采用这种翻译）

　　　　　　　　-->■ 设置核心代码改变和代码库变化选项为False

**多版本的Arduino**：需要提醒的是Arduino只有一个安装位置相当重要，所有的参数将被存储到这个文件C:\Users\….\AppData\Roaming\Arduino\preferences.txt中。每次启动任何一个Arduino程序（标准版），Ardupilot Arduino或之前在Visual Micro设置过的文件可能会发生改变。所以每次改变IDE后检查所有的IDE设置非常重要，可以避免IDE的参数设置为上次IDE使用的参数。

**在Visual Micro中索引标准的Arduino**：正常情况下，Visual Micro会所以一个标准的Arduino，来代替针对APM的HAL类型的Ardupilot Arduino特殊版。你可以配置Visual Studio或Atmel Studio索引标准Arduino安装位置，这样的话代码可以正常的编译但不能正常的上传APM代码到飞控板中。而且编译的大小不相同，并且没有连接Mission Planner。强烈建议仅仅当编译APM代码时所引导特殊版的Ardupilot Arduino安装位置。

**使用Arduino声明与库**：最好不使用标准Arduino的语法声明。较新的Ardupilot的HAL版本针对APM已经移除了大部分（并非所有）标准arduino函数声明和标准库。比如你不能加入`analogRead(sensorPin)`函数声明。所以，当你试着使用标准Arduino语言的方法编辑APM代码时，它大部分是无用的。对于APM有着很多的等效函数与语句声明，但你不得不搜索代码样例。

**编译老版本Ardupilot**：如果你仍然使用是2.9.1b版本或者比HAL更老的版本，那么你可以充分利用带有Visual Micro 的Atmel Studio或Visual Studio IDE。仅需按照如下执行：

　　　　●　下载[Ardupilot Arduino that supports the 2.x.x revisions](https://code.google.com/p/ardupilot-mega/downloads/detail?name=ArduPilot-Arduino-1.0.3-windows.zip&can=2&q=)。不要对当前版本存在疑惑，实质上他们大部分都一样仅有少量不同

　　　　●　安装Ardupilot Arduino到一个单独文件目录，并且添加apm/boards.txt文件到hardware文件夹（和之前介绍的一样）

　　　　●　在Atmel（或Visual） Studio的Tools>>Options>>Visual Micro，设置应用程序和Arduino位置，参考位置为之前安装的支持2.x.x版Ardupilot Arduino且包含2.x.x源代码的文件夹。你可以在[diydrones/ardupilot](https://github.com/diydrones/ardupilot)代码库中得到2.9.1b版源代码（通过选择需要的Ardupilot分支，点击下载zip）

　　　　●　设置Tools>>Visual Micro>>Boards为APM Arduino Mega 2560



----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/building-ardupilot-apm-with-visual-studio-visual-micro/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*