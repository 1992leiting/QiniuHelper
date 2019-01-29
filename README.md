> 这个小软件基于Python的QT库（即PyQt5）和七牛云官方Python API编写，目的是对七牛云对象存储空间进行简单管理、并带有图床功能，尽量使用PyQt提供的API（虽然部分API例如操作系统剪贴板读写等在Python和PyQt中都有）、并避免依赖特定操作系统下独有的第三方库来实现；因此，不出意外该软件发布之后在Windows/Linux/Mac下都可以运行（目前只在Windows和Mac环境下调试运行）。

# 特性

- 可以获取特定七牛云空间下的文件列表，并且提供文件名前缀筛选（七牛云API支持）
- 文件列表提供排序功能（但由于QT的tableWidget功能限制，只能按照字符串排序，所以文件大小排序暂时未实现，但是文件名排序和创建时间排序可以使用）
- 拖动本地文件到特定区域，自动上传文件
- 上传文件完成后自动拷贝文件链接到剪贴板（链接分为文件外链和Markdown使用的图片链接，设置中可以关闭自动拷贝链接功能）
- 在文件列表中选中文件，可以直接下载或者复制外链、Markdown链接
- 可以监控剪贴板内容，当检测到有截图时，会提示是否需要上传（设置中可以关闭监控），上传图片格式为png，文件名为当前时间

# 截图

![vital/screenshot_20190117_09-26-05.png](http://qiniu.leiting6.cn/vital/screenshot_20190117_09-26-05.png)

![vital/screenshot_20190117_09-27-39.png](http://qiniu.leiting6.cn/vital/screenshot_20190117_09-27-39.png)



# 安装&运行

由于软件采用Python进行编写，并且不使用依赖操作系统的第三方库，因此拥有比较好的兼容性。使用方法大概分为两种。

## Python环境下启动

1. 在你的操作系统上安装完整的Python环境，这里推荐Python3.6, Windows下记得安装时勾选“add to path‘，这个选项会把Python启动器加到系统的环境变量中。[点击跳转Python官网](https://www.python.org/getit/)

2. 打开系统的命令行工具，使用pip3工具安装第三方库。

   ```
   pip3 install pyqt5
   pip3 install qiniu
   pip3 install Pillow
   pip3 install configparser
   ```



3. 在命令行工具中将当期目录切换到本软件脚本所在目录，

   - Windows下

     ```
     cd /d ....\QiniuHelper
     ```

   - Mac/Linux下

     ```
     cd ..../QiniuHelper
     ```

   然后使用Python解释器运行主程序脚本：```python QiniuHelper.py```


## 使用打包好的可执行文件

## Windows可执行文件

使用pyinstaller打包成可执行文件，因为要放入PyQt5库文件和其他依赖，体积相对于C家族编写的软件来说非常大，暂时没有办法解决。

~~[下载地址](https://kod.leiting6.cn/index.php?share/folder&user=1&sid=rGiXqIwf#%2F%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E5%8C%85%2FWindows%E8%BD%AF%E4%BB%B6%2FQiniuHelper%2F)~~

~~[备用下载地址](https://pan.baidu.com/s/13zg05Jv1wSW2Kt11ONdggQ)~~

因为经常更新，不会每次都打包完整包，因此推荐大家自行打包或者安装python环境来运行。

轻打包教程：[我的博客](https://leiting6.cn/Python%E7%9B%B8%E5%85%B3/PyQt5%E5%B0%8F%E6%8A%80%E5%B7%A7%E6%95%B4%E7%90%861%EF%BC%9APython%E9%A1%B9%E7%9B%AE%E8%BD%BB%E6%89%93%E5%8C%85%E6%88%90%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6/)

## Mac可执行文件

Mac上打包一直有问题，未生成可执行文件。

## Linux可执行文件

尚未在Linux平台调试。

# 后续更新

- 修复已知的一些bug，做健壮性的改善；
- 增加跟多文件操作，比如重命名、删除、移动等；
- 有可能的话会增加对其他家对象存储的支持（七牛云的免费额度并不大且必须绑定个人域名）。

欢迎使用并反馈问题！

# 历史更新
## 2019-01-29
更改剪贴板监控方式，修复上传完文件后不能自动复制链接的bug（剪贴板监控间隔为3秒）
## 2019-02-26
修复某些设置项不生效的bug