标记	时间	需求类型	需求详情		问题		代码实现

##################################
	2018/7/15	NOC Coresight工具环境搭建	NOC Coresight环境搭建				NOC Coresight环境搭建
1、python3.5.4安装，不要用python3.5.0安装，因为3.5.0安装后会提示pip为7.0.1的，所以会要求更新pip，而3.5.4安装后pip直接就是10.0.1的；
2、安装PyQt5，在pypi上搜索PyQt，安装PyQt5-5.11.2的版本；然后搜索sip，安装sip-4.19.12版本。安装后就可以使用PyQt开发图形界面了；
3、pyinstaller使用
3.1、pip install pyinstaller方式安装，需要添加环境变量python3.5/scripts，因为scripts下有pyinstaller可运行程序；然后打包xxx.py文件，打包会产生_pycache_、build文件、dist文件；
3.2、直接下载pyinstaller3.3.1，不要安装，手动安装pywin32、profile、future，然后就可以直接用pyinstaller.py来打包了；
3.3、打包的时候去掉黑色的DOS窗口
pyinstaller  XXX.py  -F --noconsole
3.4、pyintaller打包PyQt的程序，出现找不到PyQt5.sip的错误，所以，在.py中导入pyQt5.QtWidgets的同时，导入PyQt5.sip，再重新打包就没事了；


##################################
	2018/8/10	QT Designer使用	QT Designer使用				QT Designer使用
1、使用qt designer软件新建一个界面，父类选择为MainWindow，这个界面的名字也命名为MainWindow，添加一些控件后保存;
2、保存后的文件里面，有main.cpp、mainwindow.cpp、mainwindow.h、mainwindow.ui、utitle.pro、utitle.pro.user这几个文件，需要的是mainwindow.ui这个文件;
3、打开mainwindow.ui文件，有一个控件是这样的:
<widget class=QToolButton name=toolButton>
  <property name=geometry >
   <rect>
     <x>300</x>
     <y>10<y>
     <width>91</width>
     <height>30</height>
   </rect>
 </property>
  <property name=text>
      <string>提交</string>
  </property>
</widget>

4、ui转换为py文件使用，DOS命令下，输入pyuic5 -o mainwindow.py mainwindow.ui，将ui转换为py文件，转换后格式为:
from PyQt5 import QtCore,QtGui,QtWidgets
Class Ui_MainWindow(object):
  def setupUi(self,MainWindow):
     MainWindow.setObjectName(mainwindow)
     MainWindow.resize(600,600)
     self.centralwidget = QtWidgets.QtWidget(MainWindow)
     self.pushButton = QtWidgets.QPushButton(self.centralwidget)


							
5.直接使用ui文件

from PyQt5.Qwidgets import QApplication,QMainWindow

from PyQt5.uic import loadUi

Class MainWindow(QMainWindow):
   def __init__(self,parent=None):
    super(MainWindow,self).__init__(parent)
    loadUi(mainwindow.ui,self)
    self.setFixedSize(500,300)

   def on_toolButton_pressed(self):
     print(toolButton pressed)
    
if __name__ == __main__:
  app = QApplication(sys.argv)
  mainwindow = MainWindow()
  mainwindow.show()
  sys.exit(app.exec_())
这里on_toolButton_pressed信号槽触发函数，定义格式为on+组件名称+动作，这里“提交”按钮的组件姓名是toolButton，动作是pressed.

							6、使用转换后的py文件

from PyQt5 import Qwidgets

if __name__ == __main__:
  app = Qwidgets.QApplication(sys.argv)
  mainwindow = Qwidgets.MainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(mainwindow)
  mainwindow.show()
  sys.exit(app.exec_())

