Title: APM-使用Eclipse进行ArduPilot Mega开发
Date: 2014-10-16 13:54:19 
Tags: APM,飞控板,硬件


### 综述 ###
<!-- PELICAN_BEGIN_SUMMARY -->

1. Eclipse是一款精致地多语言集成开发平台
1. Eclipse CDT（C++开发工具）实现了支持在Eclipse平台进行C/C++开发
1. Eclipse CDT工具可以帮助管理与组织大型C++工程，比如ArduPilot Mega的固件开发工程
1. 本指南用来说明如何将最近的ArduPilot Mega 固件开发工程设置为Eclipse CDT工程
1. 提醒：这些操作都在Eclipse Kepler（4.3.0）版本上进行。


<!-- PELICAN_END_SUMMARY -->

----------
### 当前编译相关信息 ###
1. 基于make的编译系统支持在Windows，MacOS，Liunx平台进行APM编译
1. 但是，你仍然可以使用安装的Arduino IDE进行，因为在编译过程中也使用到了它的工具链的一部分
1. 位于ardupilot-mega工程文件顶层目录的文件README.txt记录了编译说明相关信息
1. 在Readme.txt文件中关于使用Eclipse的编译说明仍然可以使用，但是相对复杂一些


----------
### 安装Eclipse和CDT组件 ###
如果你已经安装了Eclipse，但是没有安装CDT组件，那么你可以直接跳到下一部分内容。

- 下载并安装最新版本的[Java Runtime Environment（Java运行时环境）](http://java.com/en/download/index.jsp)
- 对于C/C++开发者下载并安装最新版本的Eclipse IDE。

　　A.前往[下载页面](http://www.eclipse.org/downloads/)

　　B.在“安装包选型”中点击“Eclipse IDE for C/C++ Developer”

- 将下载的压缩包解压到你的桌面上。

![1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/ExtractEclipse1.png)

![2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/ExtractDesktop1.png)

![3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/ExtractToDesktop1.png)

- 如果Eclipse不能正常运行并弹出“不能找到Java JDK or JRE”相关信息，请阅读**问题排查**部分内容


----------
### 在Eclipse安装程序中添加C开发工具 ###
- 如果你按照上一部分的说明下载了Eclipse，那么你可以跳过该部分

　　A.因为你安装的Eclipse中已经带有CDT组件

- 如果你还没有加载C开发工具（或者还不能够正确加载）

　　A. 前往[http://www.eclipse.org/cdt/downloads.php](http://www.eclipse.org/cdt/downloads.php)的**CDT 8.2.0 for Eclipse Kepler**部分

　　B. 运行Eclipse 工程，选择**Windows**下拉菜单中的**参数（Preference）**选项

![4](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/Eclipse-Preferences.png)

- 单击参数窗口的**Install/Unpdate**左侧小三角箭头，选择**可用站点（Availabel Sorftware Sites）**，然后选择添加按钮

　　A.在添加站点（**Add Site**）窗口的**Name**栏键入**CDT**

　　B.然后从CDT的下载页面复制URL链接**http://download.eclipse.org/tools/cdt/releases/kepler**到**Location**栏

　　C.在添加站点（**Add Site**）窗口点击**OK**，然后在**参数（Preference）**窗口点击**OK**

![5](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseLoadCDT.png)


----------
### 创建工作空间 ###
- 运行Eclipse：

　　A.导航到桌面的Eclipse目录

　　B.双击eclipse.exe

- 当Eclipse窗口打开：

　　A.选择**Window**菜单项中的**Preference**选项

　　B.在**Preference**窗口点击**C/C++**的左侧箭头，然后选择**File Types**

　　C.如果列表中没有“*.pde”条目，使用**New**按钮打开**C/C++文件类型**窗口

　　D.在**Pattern**栏键入***.pde**，在**Type**下拉选项中选择**C++ Source File**

　　E.在**C/C++ File Type**窗口点击**OK**，然后点击**Preference**窗口的**OK**按钮

　　F.这样就解决了Eclipse中pde文件与C++的关联

![6](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipsePrefPDE.png)

- Eclipse的代码分析功能不能够正确的解析arduino的.pde文件。为了避免编辑arduino代码时出现上百个“undeclared（未声明）”和“unused（未使用）”错误信息，禁用代码解析带来的错误

　　A.选择**Window**菜单项中的**Preference**选项

　　B.点击**C/C++**选项卡左侧的小三角展开内容，选择**Code Analysis**

　　C.取消选中**Syntax and Semantic Errors**，然后点击**OK**按钮

![7](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/UntitledEclipsePrefTurnOffErrors.png)


----------
### 创建Ardupilot Mega工程 ###
**1、**运行**Eclipse**软件，单击左上方的**File**菜单，在下拉菜单中选择**Import**选项。

**2、**在**Import**窗口，通过点击C/C++左边的小三角展开选项。

**3、**选择**Existing Code as Makefile Project**（译者注：某些版本的Eclipse，可能是**Makefile Project with Existing Code**），点击**Next**按钮进入导入代码选项窗口。

![8](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseSelectExistCodeAsMake.png)

**4、**在**New Project**的文件导航窗口，选择ardupilot-mega代码的顶层目录到**Existing Code Location**文本栏，然后点击**Finish**按钮。

![9](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseImportArduPilot.png)

**5、**为了针对你特定类型的载具和飞控板类型编译相应代码，需要对编译配置进行更改。

　　　　**A、**选择Eclipse软件页面左上侧的如Java页面部件的菜单项（打开视图窗口）。

　　　　**B、**在弹出的视图窗口中选择**C/C++(default)**项，点击**OK**按钮。


　　　　**C、**在工程管理器页面你的工程（下图的**ardupilot-master**）上右击

![10](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseOpenPerspectiveCC++.png)

**6、**在弹出菜单中选择**Properties**

**7、**属性窗口（Properties）选择**C/C++ Build**（当前选项卡应该是**Builder Settings**）

**8、**在**C/C++ Build**窗口，编辑**Build directory**文本栏内容为你想要编译的载具目录。

　　　　A、例如，将`${workspace_loc:/ardupilot-master}`变为`${workspace_loc:/ardupilot-master/ArduPlane}`

![11](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseBuildSettings.png)


**9、**现在，选择**Behavior**选项卡

**10、**在**Build（Incremental Build）**项，用你的编译目标（编译参数）替换**all**，如果你想编译近期的APM飞控板，那么可以改为**apm2**

**11、**这里还可以填写其他的编译目标（编译参数），包括SIL和各种旋翼构型

**12、**可以在不同飞行器目录中的Makefiles文件中查看可用的参数类型（目标类型）

**13、**最后点击**C/C++ Build**窗口底部的**OK**按钮

![12](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/EclipseSetBuildTarget.png)

----------
### 编译ArduPilot工程 ###



----------
### 可用插件 ###
1、**AVR Eclipse 插件**可能在Eclipse中进行APM编程非常有用

　　A、 现在，它在窗口底部区域添加了一个AVR Device管理器，有助于找到AVR注册者的相关名称

2、**EGit插件**能够在Eclipse进行版本控制，并允许你尽可能的在不脱离IDE的情况下对代码进行升级、比较和提交操作

----------
### 问题排查 ###
1、当启动Eclipse时得到“不能找到Java JRE或者JDK”相关错误信息，你需要编辑Eclipse.ini配置文件，设置Java安装包的正确路径

2、定位到你的Java安装位置，可能位于：**C:/program files/java/jdk1.7.0_07/bin/java**

3、用文本编辑器，如NotePad++，代开Eclipse.ini配置文件，添加Java安装路径到出现**-vm**的下一行

![13](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/08/JavaPathInEclipseIni.png)

4、编辑完成后保存**Eclipse.ini**文件，然后点击**Eclipse.exe**重启Eclipse

5、（在完成编辑Eclipse.ini文件，启动Eclipse之前可能还需要重启电脑）


----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/editing-the-code-with-eclipse/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*