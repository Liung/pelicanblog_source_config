Title: APM-使用Git和GitHub进行APM代码管理
Date: 2015-2-3 19:27:42 
Tags: APM, Git, GitHub

### 如何开始使用Git进行APM源码操作 ###
目前APM源代码在线托管在[https://github.com/diydrones/ardupilot](https://github.com/diydrones/ardupilot)上。如果你需要了解更多关于forking/cloning该项目的一些细节，请阅读[这篇在线指南](http://dev.ardupilot.com/wiki/git_github_guide/wiki/where-to-get-the-code/)。

----------
### 教程：使用Git向APM贡献代码 ###
<!-- PELICAN_BEGIN_SUMMARY -->
这篇指南假定你已具有GitHub账户。如果使用的是Windows平台，本指南假设你已经下载并安装了[GitHub的windows客户端](https://windows.github.com/)程序。如果你使用Mac OSX或者是Linux的任意一种发布版本，本指南假定你已经安装了git并能够使用终端进行目录切换和输入命令操作。
<!-- PELICAN_END_SUMMARY -->


----------
### 创建分支并更改代码 ###
分支作为将开发分离为不同路径的方法，之后可以和一个单独分支（经常命名为“master”）中进行合并。参考下面“学习Git”部分的更多资源，或快速浏览这篇[简短说明](http://gitready.com/beginner/2009/01/25/branching-and-merging.html)。这一部分，你可以创建代码分支并对代码进行更改。

分支命名取决于你，但是选择一个简短且描述性的名字是非常有用的。本指南中的代码分支命名为“apm_git_tutorial”。

对于OSX/Linux终端命令，假设你目前的工作目录位于你“克隆”到的代码库的根目录中。

1、创建分支。

- OSX/Linux终端：`git checkout -b apm_git_tutorial`
- Windows(GitHub GUI):在安装GitHub的Windows应用程序中，点击窗口右上角的“master”按钮，输入“aom_git_tutorial”并点击下拉列表中的"+创建分支amp_git_tutorial”：

![github for windows](http://dev.ardupilot.com/wp-content/uploads/sites/6/2014/04/APM-Git-Github-Windows-Branch.jpg)

2、更改代码。对于本指南，在你喜欢的文本编辑器中代开`Tools/GIT_Test/GIT_Success.txt`文件，在文件末行输入你的名字并保存。

3、使用`git status`查看那些文件发生改变

- OSX/Linux终端：`git status`

4、确认分支上的改动。该命令将你的改动提交到git历史中。请查看下面更多信息，为方便起见已经忽略了对于提交你的改动到官方发布版的确认请求操作。当你确定改动时，你需要添加一段修改的日志信息，说明改动中你做了什么。请阅读下方更多如何操作相关信息。鉴于本指南旨在全面的说明操作，你可以仅仅使用命令行第一句命令：`Added name to GIT_Success.txt`：

- OSX/Linux终端：

```
git add Tools/GIT_Test/Git_Success.txt
git commit -m'Added name to GIT_Success.txt'
```

5、推送分支到GitHub。该操作将会复制你本地分支的文件到GitHub上新的分支上。推送分支是对于其他GitHUb上的合作者或向官方发布版提交补丁支持的一个前提条件。

- OSX/Linux终端：`git push origin amp_git_tutorial`

恭喜你！你已经完成了从更改代码到向官方项目提交相关的正常进程中的所有工作内容。下一步的[确认推送请求](http://dev.ardupilot.com/wiki/submitting-patches-back-to-master/)，将把让你的改变内容添加到主项目中。


----------
### rebase-base： 保持你的代码最新 ###
当你进行项目开发时，上游的ArduPilot代码库的master主分支有可能已经升级，所以你应该[保持你fork的代码库和本地分支最新](http://robots.thoughtbot.com/keeping-a-github-fork-updated)。如果使用的是Windows版的Github，启动“Git Shell”工具，该工具在你安装GitHub的Windows客户端时已经默认安装，使用下面的命令：

1、保证你的本地代码库连接到你fork的代码库：

    git remote add upstream https://github.com/diydrones/ardupilot.git

2、获取上游主分支的改动：

    git fetch upstream

3、重新将上游主分支的当前分支作为基准：

    git rebase upstream/master

----------
#### 链接 ####

1. [APM官网原文链接](http://dev.ardupilot.com/wiki/git_github_guide/)
1. [APM开发人员参考手册目录列表]({filename}2014-08-29-APM-开发人员参考手册目录列表.md)

*(over)*