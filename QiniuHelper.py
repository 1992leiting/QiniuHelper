import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow as MW
import qiniu_api as qnapi
import ini_parser as inip
import datetime
from PIL import ImageGrab
from mainwindow_st import Ui_MainWindow_setting as MWST
import os

'''
全局变量
'''
version = 'v1.0'
about_string = '欢迎使用七牛云助手\n'  + \
               '它可以作为七牛云对象存储的文件管理器，也可以作为图床使用\n\n' +\
               '作者: Ting Lei\n' +\
               '版本: ' + version +'\n' +\
               '博客: https://leiting6.cn\n' +\
               '简书: https://www.jianshu.com/u/e096f464b471\n\n' +\
               '遇到bug欢迎反馈!'

ak = ''
sk = ''
bucket = ''
prefix = ''
domain = ''

ini_file = 'config.ini'
setting_section = 'setting'
auto_lock_flag = 0
auto_copy_flag = 1
auto_copy_content = '1'
monitor_clipboard_flag = 1
auto_copy_contents = ['Markdown', 'Link']


def recover_ini_file():
    if os.path.exists('config.ini'):
        return
    with open(ini_file, 'w') as f:
        f.write('[%s]' % setting_section)
    # inip.add_section(ini_file, setting_section)
    inip.write_key_val(ini_file, setting_section, 'ak', 'None')
    inip.write_key_val(ini_file, setting_section, 'sk', 'None')
    inip.write_key_val(ini_file, setting_section, 'bucket', 'None')
    inip.write_key_val(ini_file, setting_section, 'domain', 'None')
    inip.write_key_val(ini_file, setting_section, 'prefix', 'None')
    inip.write_key_val(ini_file, setting_section, 'autoCopy', '-1')
    inip.write_key_val(ini_file, setting_section, 'autoLock', '0')
    inip.write_key_val(ini_file, setting_section, 'monitorClipboard', '-1')
    inip.write_key_val(ini_file, setting_section, 'copyContent', 'Markdown')
    print('ini file recovered')


def remove_all_tablewidget_lines(table):
    row_cnt = table.rowCount()
    print('Removing rows, cnt: %d' % row_cnt)
    for _ in range(0, row_cnt):
        table.removeRow(0)


def get_button_image(status):
    if status:
        return 'on.png'
    else:
        return 'off.png'


def upload_file(key, local_file):
    if not os.path.exists(local_file):
        local_file = '/' + local_file
        if not os.path.exists(local_file):
            ui.show_statusbar_message('内部错误,要上传的文件不存在!')
            return
    file_name = local_file.split('/')[-1]
    ui.statusbar.showMessage('正在上传: ' + local_file)
    try:
        rt = qnapi.qiniu_upload(ak, sk, bucket, prefix, key, local_file)
    except KeyError as e:
        ui.show_statusbar_message('检查空间名称发现错误,请检查设置是否正确!')
        return
    '''try:
        rt = qnapi.qiniu_upload(ak, sk, bucket, prefix, key, local_file)
    except Exception as e:
        local_file = '/' + local_file
        rt = qnapi.qiniu_upload(ak, sk, bucket, prefix, key, local_file)'''
    ui.refresh_file_list()
    if rt is None:
        # ui.show_statusbar_message('上传成功,文件列表已刷新')
        pass
    else:
        ui.show_statusbar_message('上传出现异常!')
        return
    # 上传完成后根据设置复制外链或者MD链接
    if auto_copy_flag:
        if domain == '' and domain is  None:
            ui.show_statusbar_message('没有提供域名，无法复制相关链接')
            return
        if auto_copy_content == 'Markdown':
            ui.link_option('md', prefix+'/'+file_name)
            ui.show_statusbar_message('文件上传成功,Markdown链接已拷贝到剪贴板')
        elif auto_copy_content == 'Link':
            ui.link_option('link', prefix+'/'+file_name)
            ui.show_statusbar_message('文件上传成功,外链已拷贝到剪贴板')
        else:
            print('copy content error: ' + auto_copy_content)
            ui.show_statusbar_message('拷贝链接参数错误!')


class ThreadHandleIniSettings(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadHandleIniSettings, self).__init__(parent)
        self.finished.connect(ui.handle_settings)

    def run(self):
        if not os.path.exists(ini_file):
            print('ini file not exist, recovering...')
            recover_ini_file()
            ui_st.setupFunction(MainWindow_st)


class LineEditEx(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(None, parent)
        self.setGeometry(50, 50, 100, 20)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)  # 开启可拖放事件

    def dragEnterEvent(self, QDragEnterEvent):
        e = QDragEnterEvent  # type:QDragEnterEvent
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        global ak, sk, bucket, prefix
        # self.setText(e.mimeData().text()) #如果之前设置ignore 为False 这里将不会生效
        local_file = e.mimeData().text().lstrip('file:').strip('/')
        print(local_file)
        key = local_file.split('/')[-1]
        ui.statusbar.showMessage('正在上传: ' + local_file)
        upload_file(key, local_file)


class MainUIst(MWST):
    def __init__(self):
        self.settings = None

    def setupFunction(self, MainWindow_st):
        '''
        固定窗口大小并提示欢迎信息
        '''
        mw_size = MainWindow_st.size()
        MainWindow_st.setFixedSize(mw_size)

        '''
        读取ini文件信息并初始化各个控件
        '''
        global auto_lock_flag, auto_copy_flag, auto_copy_content, monitor_clipboard_flag
        global ini_file, setting_section
        self.settings = inip.get_dict_from_ini('config.ini', 'setting')
        auto_lock_flag = int(self.settings['autoLock'])
        auto_copy_flag = int(self.settings['autoCopy'])
        auto_copy_content = self.settings['copyContent']
        monitor_clipboard_flag = int(self.settings['monitorClipboard'])

        self.set_auto_lock('r', auto_lock_flag)
        self.set_auto_copy('r', auto_copy_flag)
        self.set_auto_copy_content('r')
        self.set_monitor_clipboard('r', monitor_clipboard_flag)

        '''
        按键链接
        '''
        self.pushButton_AutoLock.clicked.connect(lambda: self.set_auto_lock('w', ~int(auto_lock_flag)))
        self.pushButton_AutoCopy.clicked.connect(lambda: self.set_auto_copy('w', ~int(auto_copy_flag)))
        self.pushButton_MonitorClipboard.clicked.connect(lambda: self.set_monitor_clipboard('w', ~int(monitor_clipboard_flag)))
        self.comboBox_CopyContent.currentIndexChanged.connect(lambda: self.set_auto_copy_content('w'))

    def set_auto_lock(self, option, val):
        global auto_lock_flag, ini_file, setting_section
        if 'w' in option:
            inip.write_key_val(ini_file, setting_section, 'autoLock', str(val))
            auto_lock_flag = val
        if 'r' in option:
            self.settings = inip.get_dict_from_ini(ini_file, setting_section)
            auto_lock_flag = int(self.settings['autoLock'])
        icon_img = get_button_image(auto_lock_flag)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_img), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AutoLock.setIcon(icon)
        print('set auto lock, cur val: %d' % int(auto_lock_flag))

    def set_auto_copy(self, option, val):
        global auto_copy_flag, ini_file
        if 'w' in option:
            inip.write_key_val(ini_file, setting_section, 'autoCopy', str(val))
            auto_copy_flag = int(val)
        if 'r' in option:
            self.settings = inip.get_dict_from_ini(ini_file, setting_section)
            auto_copy_flag = int(self.settings['autoCopy'])
        self.comboBox_CopyContent.setEnabled(auto_copy_flag)
        icon_img = get_button_image(auto_copy_flag)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_img), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_AutoCopy.setIcon(icon)
        print('set auto copy, cur val: %d' % int(auto_copy_flag))

    def set_auto_copy_content(self, option):
        global auto_copy_content, ini_file, auto_copy_contents
        if 'w' in option:
            auto_copy_content = self.comboBox_CopyContent.currentText()
            inip.write_key_val(ini_file, setting_section, 'copyContent', auto_copy_content)
        if 'r' in option:
            self.settings = inip.get_dict_from_ini(ini_file, setting_section)
            auto_copy_content = self.settings['copyContent']
            index = self.comboBox_CopyContent.findText(auto_copy_content)
            print('index: %d' % index)
            if index != -1:
                print('copy content: ' + auto_copy_content)
                self.comboBox_CopyContent.setCurrentIndex(index)

    def set_monitor_clipboard(self, option, val):
        global monitor_clipboard_flag, ini_file
        if 'w' in option:
            inip.write_key_val(ini_file, setting_section, 'monitorClipboard', str(val))
            monitor_clipboard_flag = int(val)
        if 'r' in option:
            self.settings = inip.get_dict_from_ini(ini_file, setting_section)
            monitor_clipboard_flag = int(self.settings['monitorClipboard'])
        icon_img = get_button_image(monitor_clipboard_flag)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_img), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_MonitorClipboard.setIcon(icon)
        print('set monitor clipboard flag, cur val: %d' % int(monitor_clipboard_flag))


class MainUI(MW):
    def __init__(self):
        self.lock_flag = 0
        self.settings = None
        self.thread_prepare_settings = None
        self.lock_buttons = None
        self.lock_table = None
        self.lock_edit = None
        self.clipboard = None
        self.widget_msg = None
        self.timer = QtCore.QTimer()
        self.lineEdit_DragDrop = None

    def setupFunction(self, MainWindow):
        '''
        设置窗口标题，固定窗口大小并提示欢迎信息
        '''
        MainWindow.setWindowTitle('七牛云助手 - ' + version)
        mw_size = MainWindow.size()
        MainWindow.setFixedSize(mw_size)
        # self.statusbar.showMessage('欢迎使用七牛云助手,请先设置参数并点击锁定按钮.')
        self.show_statusbar_message('欢迎使用七牛云助手,请先设置参数并点击锁定按钮')
        '''
        处理拖放控件，继承LineEditEx，并赋予mainwoindows.py中相同的参数
        '''
        rect = self.lineEdit_DragDrop.geometry()
        self.lineEdit_DragDrop = LineEditEx(self.centralwidget)
        self.lineEdit_DragDrop.setText("拖放文件自动上传或者点击按钮从剪贴板上传")
        self.lineEdit_DragDrop.setGeometry(rect)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_DragDrop.setFont(font)
        self.lineEdit_DragDrop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_DragDrop.setReadOnly(True)
        self.lineEdit_DragDrop.setObjectName("lineEdit")
        self.lineEdit_DragDrop.setEnabled(False)

        '''
        设置需要锁定管控的控件
        '''
        self.lock_buttons = [self.pushButton_ClipBoard,
                             self.pushButton_Refresh,
                             self.pushButton_Download,
                             self.pushButton_CopyLink,
                             self.pushButton_CopyMD]
        self.lock_table = self.tableWidget_Settings
        self.lock_edit = self.lineEdit_DragDrop

        '''
        设置剪贴板监控
        '''
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.monitor_clipboard)

        '''
        创建消息窗口
        '''
        self.widget_msg = QtWidgets.QWidget(self.centralwidget)
        self.widget_msg.setObjectName("widget_msg")

        '''
        设置定时器清空状态栏
        '''
        self.timer.timeout.connect(lambda: self.show_statusbar_message(''))

        '''
        设置按键连接
        '''
        self.pushButton_Lock.clicked.connect(self.lock)
        self.pushButton_Refresh.clicked.connect(self.refresh_file_list)
        self.pushButton_CopyLink.clicked.connect(lambda: self.link_option('link', ''))
        self.pushButton_Download.clicked.connect(lambda: self.link_option('download', ''))
        self.pushButton_CopyMD.clicked.connect(lambda: self.link_option('md', ''))
        self.pushButton_ClipBoard.clicked.connect(lambda: self.clipboard_option('save_image', ''))
        self.action_GlobalSetting.triggered.connect(self.show_setting_window)
        self.action_About.triggered.connect(self.show_about)
        self.action_Exit.triggered.connect(MainWindow.close)

        self.show_statusbar_message('读取ini...')
        self.thread_prepare_settings = ThreadHandleIniSettings()
        self.thread_prepare_settings.start()

    '''
    处理ini设置
    '''
    def handle_settings(self):
        print('handle settings')
        self.settings = inip.get_dict_from_ini('config.ini', 'setting')
        self.tableWidget_Settings.item(0, 0).setText(self.settings['ak'])
        self.tableWidget_Settings.item(1, 0).setText(self.settings['sk'])
        self.tableWidget_Settings.item(2, 0).setText(self.settings['bucket'])
        self.tableWidget_Settings.item(3, 0).setText(self.settings['domain'])
        self.tableWidget_Settings.item(4, 0).setText(self.settings['prefix'])

    '''
    锁定设置
    '''
    def lock(self):
        global ak, sk, bucket, domain, prefix
        self.lock_flag = ~self.lock_flag

        # 如果是锁定状态
        if self.lock_flag:
            # 读取参数
            self.tableWidget_Settings.setCurrentItem(None)
            ak, sk, bucket, domain, prefix = self.tableWidget_Settings.item(0, 0).text(), \
                                            self.tableWidget_Settings.item(1, 0).text(), \
                                            self.tableWidget_Settings.item(2, 0).text(), \
                                            self.tableWidget_Settings.item(3, 0).text(), \
                                            self.tableWidget_Settings.item(4, 0).text()
            # 检查必填数据
            if ak == '' or sk == '' or bucket == '':
                # self.statusbar.showMessage('缺少必填参数项!')
                self.show_statusbar_message('缺少必填参数项!')
                self.lock_flag = 0
                return
            # 检查域名是否为http开头
            if not domain.startswith('http') :
                domain = 'http://' + domain
                self.tableWidget_Settings.item(3, 0).setText(domain)

            # 写入ini文件
            inip.write_key_val(ini_file, setting_section, 'ak', ak)
            inip.write_key_val(ini_file, setting_section, 'sk', sk)
            inip.write_key_val(ini_file, setting_section, 'bucket', bucket)
            inip.write_key_val(ini_file, setting_section, 'domain', domain)
            inip.write_key_val(ini_file, setting_section, 'prefix', prefix)

            # 管控相关控件
            self.lock_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            for bt in self.lock_buttons:
                bt.setEnabled(True)
            self.lock_edit.setEnabled(True)
            # 设置按钮
            self.pushButton_Lock.setText('已锁定')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_Lock.setIcon(icon)

            # self.statusbar.showMessage('参数已录入.')
            self.show_statusbar_message('参数已录入')
            self.refresh_file_list()

        # 如果不是锁定状态
        else:
            # 管控相关控件
            self.lock_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked |
                                            QtWidgets.QAbstractItemView.EditKeyPressed |
                                            QtWidgets.QAbstractItemView.AnyKeyPressed)
            for bt in self.lock_buttons:
                bt.setEnabled(False)
            self.lock_edit.setEnabled(False)
            # 设置按钮
            self.pushButton_Lock.setText('已解锁')
            print('set bt text: unlock')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_Lock.setIcon(icon)
            # 情况文件列表
            remove_all_tablewidget_lines(self.tableWidget_FileList)
            self.show_statusbar_message('已解除锁定,现在可以对设置进行编辑')

    def refresh_file_list(self):
        # 使用tableWidget_FileLst前，先删除所有行
        remove_all_tablewidget_lines(self.tableWidget_FileList)

        f_name, f_size, f_time = qnapi.qiniu_get_file_list(ak, sk, prefix, bucket)
        if f_name is None or f_size is None or f_time is None:
            # self.statusbar.showMessage('获取数据错误,请检查设置和网络!')
            self.show_statusbar_message('获取数据错误,请检查设置和网络!')
            return

        f_cnt = len(f_name)
        print('Showing file list, cnt: %d' % f_cnt)
        # 每处理一条文件数据，新建一行，并初始化每个单元格为tableWidgetItem属性
        for i in range(0, f_cnt):
            self.tableWidget_FileList.insertRow(i)
            for j in range(0, 3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_FileList.setItem(i, j, item)
            # 获取单个文件名、文件大小和上传时间
            cur_fname, cur_fsize, cur_ftime = f_name[i], int(f_size[i]), f_time[i]
            item0, item1, item2 = self.tableWidget_FileList.item(i, 0), \
                                  self.tableWidget_FileList.item(i, 1), \
                                  self.tableWidget_FileList.item(i, 2)
            # 文件名处理：去除引号
            item0.setText(cur_fname.strip('"'))
            # 文件大小处理：原始大小单位为B，根据实际数值转换为KB/MB/GB
            f_size_unit = 'B'  # 默认文件大小单位为B
            if 1024 <= cur_fsize < 1024*1024:
                cur_fsize = int(cur_fsize / 1024)
                f_size_unit = 'KB'
            elif 1048576 <= cur_fsize < 1024*1024*1024:
                cur_fsize = int(cur_fsize/1024/1024)
                f_size_unit = 'MB'
            elif cur_fsize >= 1024*1024*1024:
                cur_fsize = int(cur_fsize/1024/1024/1024)
                f_size_unit = 'GB'
            item1.setText(str(cur_fsize)+' '+f_size_unit)
            # 创建时间处理：时间在qiniu_api里面已经格式化过，这里直接用
            item2.setText(cur_ftime)

    def link_option(self, option, file_name):
        print('link option: ' + option)
        item = self.tableWidget_FileList.currentItem()
        if item is None:
            if file_name == '':
                self.show_statusbar_message('请先在文件列表中选中文件!')
                return
        else:
            if file_name == '':
                row = self.tableWidget_FileList.currentRow()
                file_name = self.tableWidget_FileList.item(row, 0).text()
            else:
                print('item selected and file name given, use item name')
        if option == 'download':
            qnapi.qiniu_download(ak, sk, domain, file_name)
        elif option == 'link':
            url = qnapi.qiniu_get_private_url(ak, sk, domain, file_name)
            self.clipboard_option('copy_text', url)
            print(url)
        elif option == 'md':
            md_link = '![' + file_name + '](' + domain + '/' + file_name + ')'
            self.clipboard_option('copy_text', md_link)
            print(md_link)
        else:
            print('link option para error')

    def clipboard_option(self, option, content):
        clipboard = QtWidgets.QApplication.clipboard()

        # 拷贝链接到剪贴板
        if option == 'copy_text':
            clipboard.setText(content)

        # 保存图片并上传操作
        elif option == 'save_image':
            if not self.check_clipboard_image():    # 检测剪贴板中是不是图片
                return
            image_file = r'tmp.png'
            image_format = image_file.split('.')[-1]
            print('PIL saving tmp...')
            pic = ImageGrab.grabclipboard()
            pic.save(image_file)
            cur_time = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
            key = 'screenshot_' + cur_time + '.' + image_format
            print('qiniu uploading...')
            rt = qnapi.qiniu_upload(ak, sk, bucket, prefix, key, image_file)
            print('updating list...')
            ui.refresh_file_list()
            if rt is None:
                # ui.statusbar.showMessage('上传成功, 文件列表已刷新')
                self.show_statusbar_message('上传成功,文件列表已刷新')
                # os.remove('tmp.bmp')
                # self.clipboard.clear()
            else:
                # ui.statusbar.showMessage('上传出现异常!')
                self.show_statusbar_message('上传出现异常!')

    '''
    监控剪贴板，如果剪贴板数据发生改变并且是图片，则询问是否上传图片
    '''
    def monitor_clipboard(self):
        # 如果当前状态不是锁定的，则不监控动作为空
        if not self.lock_flag:
            return
        if self.check_clipboard_image():
            print('Img copied')
            bt = QtWidgets.QMessageBox.question(self.widget_msg,
                                                '提示',
                                                '是否上传剪贴板图片?',
                                                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
                                                QtWidgets.QMessageBox.Ok)
            if bt == QtWidgets.QMessageBox.Ok:
                # print('Save img from clipboard')
                self.clipboard_option('save_image', '')
            else:
                return

    def check_clipboard_image(self):
        md = self.clipboard.mimeData()
        print('clipboard format: ', end='')
        print(md.formats())
        if md.hasImage():
            return 1
        else:
            print('no img in clipboard')
            return 0

    def show_statusbar_message(self,string):
        self.statusbar.showMessage('   ' + string)
        self.timer.start(3000)

    def show_setting_window(self):
        MainWindow_st.show()
        
    def show_about(self):
        global about_string
        wgt = QtWidgets.QWidget(self.centralwidget)
        QtWidgets.QMessageBox.about(wgt, "关于", about_string)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    recover_ini_file() # 检查ini文件是否存在

    # 设置窗口
    MainWindow_st = QtWidgets.QMainWindow()
    MainWindow_st = QtWidgets.QMainWindow()
    ui_st = MainUIst()
    ui_st.setupUi(MainWindow_st)
    ui_st.setupFunction(MainWindow_st)

    # 主窗口
    MainWindow = QtWidgets.QMainWindow()
    ui = MainUI()
    ui.setupUi(MainWindow)
    ui.setupFunction(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
