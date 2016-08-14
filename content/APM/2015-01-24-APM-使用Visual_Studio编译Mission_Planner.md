Title: APM-使用Visual Studio编译Mission Planner
Date: 2015-1-24 14:19:53 
Tags: APM,Mission Planner

### 简介 ###

<!-- PELICAN_BEGIN_SUMMARY -->
Mission Planner（简称MP）是一款Windows平台使用（可通过mono实现Mac平台上的跨平台使用）的开源地面站软件，主要开发语言采用C#。该软件是目前使用最普遍的一款地面站软件，它不仅面向各种载具提供了完备地功能性设置，还提供了飞行任务规划、飞行实时监测、飞行后日志文件分析等功能。
<!-- PELICAN_END_SUMMARY -->

本页面将介绍如何在自己的电脑上使用微软的Visual Studio2013软件编译Mission Planner。能够顺利的完成编译工作不仅对你想要在Mission Planner上需要添加的某些变化或者面向社区的改进等非常有用，而且可以对于开发编译个人定制地面站软件是一个很好的指导。

深入研究之前的一些警告：

- 使用个人改变/编译Mission Planner版的风险由本人承担
- Mission Planner具有非常复杂的库包含关系，不推荐概念模糊就改编代码。这里列出了你需要对MP做出可信改变的一些基本技术能力：

　　● 具备C#编程技术与相关经验（至少有C++相关经验）

　　● 具有微软VS开发环境相关经验。MP不是学习VS的入门应用。

　　● 具有Windows的API（应用程序接口），包括理解数据流、进程、线程等相关知识。

- VS的相关支持，C#编程相关以及Windows API相关技术可能不会从DIY Drones社区获得。你需要从其他资源获得帮助与支持。


----------
### 系统需求 ###

你需要：

- Windows XP, Vista, 7, 8
- 足够的硬盘空间、内存、处理器用来运行VS（具体内容见下文）
- 网络连接通畅
- Visual Studio 2013社区版


----------
### 安装Visual Studio 和 DirectX ###

第一步安装[Visual Studio 2013](http://www.visualstudio.com/)，并且保证在Windows系统中能够正常运行。

- 下载并安装MS Visual Studio 2013社区版（[点击这里](http://www.visualstudio.com/)）
- 重启电脑
- 从开始按钮中运行Visual Studio
- 当安装完成后，尝试改变Mission Planner之前先使用一个简单的“Hello World”例子测试一下你安装的软件能否正常使用。

通过下载并运行 [DirectX End-User Runtime Web Installer](http://www.microsoft.com/en-us/download/confirmation.aspx?id=35)，完成DirectX的安装。


----------
### 从Github中得到源代码 ###

Mission Planner源代码储存在Github网站上。你可以遵循之前如何获取[ardupilot飞行代码](http://dev.ardupilot.com/wiki/buildin-mission-planner/wiki/where-to-get-the-code/)的介绍在 [https://github.com/diydrones/MissionPlanner](https://github.com/diydrones/MissionPlanner)代码库中获取得到Mission Planner源代码。


----------
### 在Visual Studio中打开Mission Planner ###

![img1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/MPBuild_OpenSolution-1024x703.png)

- 运行Visual Studio
- 点击 文件 >> 打开 >> 工程 / 解决方案
- 导航到Mission Planner文件夹，选择ArdupilotMega.sla文件打开
- Visual Studio应该打开包含有Mission Planner和其他一些相关引用（如“3DR Radio”, “Updater”等）的相关解决方案（solution）,可以在“解决方案”资源管理器面板看到（上图黄色高亮区域）
- 设置“Solution Configuration”为“Debug”或者“Release”（可在工具菜单下找到相关命令）
- 设置“Solution Platforms”为“x86″
- 在“解决方案”管理器面板中，在Mission Planner项右击选择属性，在Signing（签名）选型卡中取消选中“Sign the ClickOnce manifests”(为ClickOnce清单签名)

![img2](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/MPBuild_UncheckSigning-1024x641.png)

Mission Planner有如下几个工程项目组成，你可以通过在解决方案面板中打开“Mission Planner”和“Libs”文件夹看到。

- MissionPlanner (主代码)
- AviFile
- BaseClasses
- BSE.Windows.Forms
- Core
- GeoUtility
- GMap.Net.Core
- GMap.Net.WindowsForms
- KMLib
- MAVLink
- MetaDataExtractor
- MissionPlanner.Comms
- MissionPlanner.Controls
- MissionPlanner.Utils
- px4uploader
- SharpKml
- ZedGraph

----------
### 编译Mission Planner ###

在尝试编译Mission Planner之前，还必须在你的电脑上安装官方安装版Mission Planner。这是因为有一些动态库文件.dll没有包含在Git代码库中。

![img3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/MPBuild_BatchBuild-1024x741.png)

选择Build >> Batch Build…（生成 >> 批生成），“Select All”（全选），然后点击“Rebuild”（重新生成）。第一次尝试编译Mission Planner时可能会出现一些错误，所以多尝试几次。

如果一些错误仍然存在，那么试着使用下面这些方法：

- 对于缺失dlls相关的错误:

　　● 解决方案面板中，在MissionPlanner工程上右击选择属性，参考路径。

　　● 在文件选择窗口，选择已经安装的Mission Planner文件目录，其可能为： C:\Program Files (x86)\Mission Planner 或者 C:\Program Files\Mission Planner

　　● 点击添加文件夹按钮，然后将已安装的Mission Planner文件目录输入到参考目录框中。

　　● 点击(选择)编译事件。移除所有预编译pre-build和编译后（Post build）选项。

　　● 点击 (选择)编译。

- 对于缺失索引相关错误，可以查看每个列出的错误对应的工程名。然后选择相应工程的属性，和之前一样添加已安装版Mission Planner安装目录。这样应该可以减少此类错误。
- 如果在工程BSE.Windows.Forms中遇到类似“..could not locate the Code Analysis tool at”。你可以在BSE.Windows.Forms属性选项中的Code Analysis通过取消勾选代码分析选型来解决。

解决编译错误时一些有用的帮助:

- 在VS中，当你进行编译或者预编译一个解决方案时，选择菜单项[BUILD] [Configuration Manager]，将会显示出每次哪个项目将被编译。
- 选择编译那些未被选中的项目: (例如 3DRRadio, Updater, wix)
- 选择 [Build], [Clean Solution] 然后 [Build], [Rebuild solution].
- 所有的工程应该都可以被正确编译.


当编译中没有错误发生时，那么你就可以准备开始浏览并编辑源代码了。


----------
### 编译SimpleExample ###

![img4](http://dev.ardupilot.com/wp-content/uploads/sites/6/2013/06/MPBuild_SimpleExampleRun-1024x582.png)

“SimpleExample”方案作为一个微型应用，用来说明一个C#程序如何与载具连接，并且控制它解锁与上锁。这个简单的例子与完整的Mission Planner相比具有更少的依赖性，因此编译工作相当容易理解。

首先，从Visual Studio的 File >> Open >> Project/Solution 中打开Solution面板。然后在MissionPlanner代码目录选择`ExtLibs/SimpleExample.sln`

选择 Build >> Build Solution 选项，确保程序能够成功的被编译。

完成上述工作后，接下来第一步先要检查能够正常连接到你的飞行控制板，并且使用已安装的Mission Planner软件能够正常解锁，然后断开常规的Mission Planner，点击“Start”按钮使用debug模式运行程序。当面板“Florm1”弹出后，选择正确的COM端口和波特率（一般115200），点击“Connect”按钮。如果连接成功，点击“Arm/Disarm”按钮尝试解锁你的载具。


----------
### 编辑与调试Mission Planner (与其它温馨提示) ###


编辑与调试代码相关细节超出了本Wiki的范畴。调试结果可能会造成一些警告，你应该认真了解这些警告产生的原因并采取一些必要措施来解决。下面这些简单的调试例子可以让你有个很好的开始：

- 编译MP时不要连接你的APM。你应该首先复制一些.xml文件到bin/degub文件夹。请查看下面的详细内容。
- 首先确保VS软件配置为调试模式（相对于发布release）。可以在主菜单中的工具菜单或者配置管理器中进行相关设置。
- 选择菜单 DEBUG, Start Debugging.   (或者按下 F5 键).  Mission Planner应该可以正常的运行，但是由于一些重要的配置文件处于丢失状态，所以此时不推荐连接APM。

　　● 如果开始调试后，程序出现启动画面后挂起状态，并且得到如下信息：“Managed Debugging Assistant ‘LoaderLock’ has detected a problem …… “‘  and/or the debugger has paused at the line  Application.Run(new MainV2()); in ArdupilotMega.Program。这时应该选择：[Debug],  [Exceptions].打开[Managed Debugging Assistants].  取消勾选‘Loader Lock’。

- 关闭MP。(或者在VS中选择菜单DEBUG, Stop Debugging)。
- 接下来可以尝试在程序中设置断点：

　　● 在VS的资源方案管理器中展开 ArdupilotMega 项目，这样你可以一目了然地查看包含的所有对象。

　　● 滚动到MainV2.cs文件，文件对象上右击选择显示代码。

　　● 在MainV2.cs的代码窗口，鼠标滚动到public MainV2()模块那一行。
  
　　● `splash.Text = “Mission Planner ” + Application.ProductVersion + ” ” + strVersion; `  (about line number 169)

　　● 点击行首（左侧深灰色边条）设置断点（红色圆点）。

　　● 点击调试（按键F5）。

　　● 可以观察到MP正常开始启动并出现启动画面，然后程序停止运行。当你点击断点，Visual Studio将会显示代码并高亮断点。需要注意的是此时你不能移除启动屏幕，所以你需要重新调整VS窗口来观察断点位置。

　　● 将鼠标移动到代码中不同的变量和对象上，会看到需要变量的当前值或当前对象的包含项。

　　● 按下F5，Mission Planner会继续运行。

- 编辑与调试代码更深入的细节留给用户自己探究。


----------
### 使用修改过的Mission Planner ###


如果你对Mission Planner做了一下改变，你可能想要使用你自己版本的MP。这里我们将提供给你一些关于这方面的初步的信息。你可以使用你本地编译过的版本，但是VS中编译输出的文件位于不同位置，这需要一些额外的步骤。有一些和Mission Planner安装相关的文件没有包含在Github上的代码库中，而仅在Mission Planner安装包文件中提供。所以你需要复制这些文件到你正在使用的Visual Studio工程文件文件的正确位置。可以从下面步骤入手：

- 使用你自己硬盘中改变/编译过的Mission Planner版本。
- 这些步骤假定VS处在调试模式。
- 为了使你VS中MP的版本和APM能够连接，你需要复制一些文件从你之前MP的安装目录(C:\Program Files (x86)\APM Planner  or C:\Program Files\APM Planner)复制到你的VS工程编译文件输出目录。

　　● 从MP安装版的根目录(C:\Program Files\APM Planner)复制（不是移动）所有的xml文件(例如 files with the extension .xml)到需要调试的Mission Planner方案存储路径中的bin/Debug目录下。这样就会设置你编译的版本与你的APM当前配置文件相一致(旋翼VS固定翼，其他选项等)。

　　● 例如， 如果你的工程目录为MPGitClone，那么复制.xml文件到MPGitClone\bin\Debug。复制过程中可能会提示是否要替换已存在的文件。选择替换所有文件，此步骤之前你应该进行深入分析并确保你的MP在实际情况下能够正常工作。

　　● 如果你在发布模式下编译Mission Planner，那么文件应该复制到bin/Release目录下。该操作目前还没有进行测试。

- 这里有一些相关提示：

　　● 当使用自己版本的日志文件存储目录将会位于/bin/Debug或者bin/Release文件目录下。这可以在Mission Planner 1.2.63和之后的版本中改变。

　　● 如果你想通过快捷方式来运行个人版本的Mission Planner而又不运行Visual Studio软件，可以创建一个快捷方式链接到bin/Debug或bin/Release子目录下的程序ArdupilotMegaPlanner10.exe。

- 此时当运行本地个人版本Mission Planner时，你应该已经可以和你的APM相连接。包含状态的飞行数据应该可以正常工作，并且可以上载APM参数，终端应该也可以正常保存和浏览日志信息。和之前提到过的一样，使用本地硬盘的个人版Mission Planner，飞行规划也应该可以工作。


----------
### 代码主分支中确认你的改动 ###

衷心提出和Ardupilot飞行代码一样的建议，如下几个要点：

- Github上注册账户
- 通过 [https://github.com/diydrones/MissionPlanner](https://github.com/diydrones/MissionPlanner) 点击右上角的Fork按钮，创建个人账户的Mission Planner的镜像代码。
- “克隆”私人库代码（上一步中Fork的库）到本地电脑上。
- 在私人库中建立新分支，提交改变并push到Github的私人仓库中。
- 使用Github网站页面创建分支推送请求。
- Mission Planner维护人员(Michael Oborne)将会收到关于你推送的通知邮件。他会尽可能仔细地审查你的代码请求，并积极地向你反馈相关信息。如果请求通过，那么你的代码将会被添加到主分支master中。


----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/buildin-mission-planner/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*