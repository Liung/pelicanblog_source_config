Title: APM-Windows7上的MAVProxy使用
Date: 2014-10-16 13:54:19 
Tags: APM,飞控板,硬件

### 简介 ###
本说明取自于Ben Dellar在DIY Drones上的一篇[优秀的指导手册](http://diydrones.com/profiles/blogs/step-by-step-guide-to-mavproxy-on-windows-7-live-forward-your-uav?xg_source=activity)

<!-- PELICAN_BEGIN_SUMMARY -->
MAVProxy是一款强大的地面站软件，它极大的扩充了GUI界面的地面站。比如Mission Planner，APM Planner等。驱动我探索MAVProxy的最大动力在于，它对通过网络的UDP协议获取到的UAV信息和不同设备上的多种地面站软件的交互具有强大的兼容性。<!-- PELICAN_END_SUMMARY -->例如，你可以在笔记本上运行你的地面站软件，并通过天线或者wifi和手机/平板连接，从而可以在固定的天线转向之前轻松重新定位发送信号（you can run a ground station on a laptop next to your antenna and forward via wifi to a smartphone/tablet which lets you easily relocate to launch into wind before heading back to your fixed antenna.我也不是很明白 ：>）。我也曾经在一次长距离飞行中将遥测数据通过网络（4G VPN）发送给几千米之外充当观测员的朋友，这样，他就可以实时监测整个飞行，从而随时可以确定飞行器的位置信息。

本手册将指导你如何成功设置MAVProxy从而可以通过命令行与网络界面通信。当然，也有许多其他方法可以让它运行，并且，为了能够使用一些高级方法，可能还需要其他的安装包，具体信息请看官方文档：[http://tridge.github.io/MAVProxy/](http://tridge.github.io/MAVProxy/)。免责声明，所有信息归Andrew Tridgell及MAVProxy和这里用到的其他软件开发者所有。

![img0](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/05/Mavproxy_usage.png)


----------
### Step 1： 检查是否能够连接你的UAV ###
在开始任何事情之前请确保你的飞行器和地面站连接正常。检查连接到你的电脑上的端口及波特率（后面需要这些信息）。

----------
### Step 2：安装Python ###
下载并安装[Python2.7-WindowsX86 MSI](https://www.python.org/download/releases/2.7/)，不需要关心OS/CPU类型。安装并采用默认安装位置：C:\Python27\

----------
### Step 3：安装Pyserial ###
下载并安装[Pyserial 2.7 – Win32 for Python 2.x (2.4…2.7) ](https://pypi.python.org/pypi/pyserial/2.7)， 使用默认安装位置：**C:\Python27\ directory**

----------
### Step 4：安装并设置MAVProxy ###
下载最新版的[MAVProxy](https://pypi.python.org/pypi/MAVProxy) .tar.gz 文件（如果没有合适的解压缩工具，请安装[WinRAR](http://www.rarlab.com/download.htm)）到**C:\Python27\**

解压完成之后就会出现**C:\Python27\MAVProxy-1.3.3\MAVProxy **目录和**mavproxy.py**文件

右击**mavproxy.py**文件选择IDLE打开。在文件第20行`sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ‘..’))`去掉前面的#，如下图所示：

![img1](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/05/Mavproxyedit.png)

----------
### Step 5：安装pymavlink ###
下载最新版[pymavlink](https://pypi.python.org/pypi/pymavlink)，并解压到**C:\Python27\MAVProxy-1.3.3\MAVProxy**

这将会在上面的目录中出现一个类似“pymavlink-1.1.29”的文件夹，将文件夹改名为pymavlink。

----------
### Step 6：准备运行 ###
检查你的无线模块是否通过USB连到电脑上，飞行器模块和APM是否上电，确保所有地面站软件都已经关闭。

打开命令终端窗口（start->cmd,then press enter），输入`cd “C:\Python27\MAVProxy-1.3.3\MAVProxy” `并按回车。命令窗口将会切到该目录下。

然后输入`mavproxy.py –master=”com14″ –baudrate 57600`（替换成你的本地连接端口和波特率），按回车。

如果一切正常，MAVProxy就会启动，并出现一些基本的飞行数据，如模式及当前航点。偶尔一些数据可能会出现干扰并显示出一些奇怪的字符，但这并不影响总体的可靠性和性能。

![img3](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/05/mavproxy_running.png)

命令窗口输入`mode FBWA`，按回车。就会看到MAVLink报告模式改变并通知你的飞行器将切换到该模式下。

如果你想在命令行测试更多的命令，可以在[这里](http://tridge.github.io/MAVProxy/)找到MAVLink的所有命令。

----------
### Step 7：网络收发 ###
为了和PC上的本地程序通过网络收发MAV数据，我们可以简单的在在命令启动MAVProxy时添加额外的参数。

为了和地面站软件连接（如Mission Planner），可以使用下述命令启动MAVProxy：`mavproxy.py –master=”com14″ –baudrate 57600 –out 127.0.0.1:14550`并按回车。

然后打开Mission Planner，选择UDP，点击连接。当点击完默认弹出的端口号（14550）提示OK后，就能看到Mission Planner开始下载参数并连接到你的UAV上。

最后，你还可以添加任何发送遥测数据流到任何电脑的地面站软件的IP地址信息。

1. 在本地网络/wifi环境中，需要确保本地PC上没有防火墙阻止向地面站的输入数据流的发送。
1. 在mavproxy.py命令的后面添加： –out IP_ADDRESS:14550。你还可以添加许多单独的-out参数，这取决于你运行了多少地面站软件。
1. 设置每个地面站在端口14550监听UDP包

----------
### Step 8: 使用批处理文件简单启动 ###
为了简化MAVProxy的启动，我（原作者）已经写了一个简单的5行批处理文件：

[Mavproxy Startup Batch File](http://api.ning.com/files/LAl787uzrCCKik-3pTnOKtXuYtVXVMkpLenY6ZJqdXwGtQI-7IYZxf*Lqb*X*iWsM48fW6B0IXNiJP24esqUxLduGtyOQbKY/StartMavproxy.bat)

你可以编辑参数为你的本地端口，波特率及需要传送数据的IP地址等。

简单的保存并双击就可以启动MAVProxy（假设你已经遵循了上述的操作）

----------
####链接

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/mavproxy-on-windows-7/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*