# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labelimg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5.QtCore import QRect,QSize,QMetaObject,QCoreApplication
from PyQt5.QtWidgets import QWidget,QGroupBox,QLabel,QHBoxLayout,QPushButton,QTextBrowser,QMenuBar,QMenu,QStatusBar,QAction
from PyQt5.QtGui import QIcon
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.setWindowIcon(QIcon("robot.png"))
        MainWindow.resize(690, 675)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QRect(10, 230, 671, 391))
        self.groupBox.setObjectName("groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setGeometry(QRect(10, 20, 640, 360))
        self.label.setMouseTracking(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QRect(10, 130, 671, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 651, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.last = QPushButton(self.horizontalLayoutWidget)
        self.last.setMinimumSize(QSize(0, 45))
        self.last.setObjectName("last")
        self.horizontalLayout.addWidget(self.last)
        self.next = QPushButton(self.horizontalLayoutWidget)
        self.next.setMinimumSize(QSize(0, 45))
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.save = QPushButton(self.horizontalLayoutWidget)
        self.save.setMinimumSize(QSize(0, 45))
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.reset = QPushButton(self.horizontalLayoutWidget)
        self.reset.setMinimumSize(QSize(0, 45))
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QRect(10, 10, 671, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Message = QTextBrowser(self.groupBox_3)
        self.Message.setGeometry(QRect(10, 20, 651, 81))
        self.Message.setObjectName("Message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 690, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.menu.addAction(self.actionOpenFile)
        self.Refreshfolder = QAction(MainWindow)
        self.Refreshfolder.setObjectName("Refreshfolder")
        self.menu.addAction(self.Refreshfolder)
        self.menubar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "图片显示"))
        self.groupBox_2.setTitle(_translate("MainWindow", "快捷栏"))
        self.last.setText(_translate("MainWindow", "上一个(A)"))
        self.last.setShortcut(_translate("MainWindow", "A"))
        self.next.setText(_translate("MainWindow", "下一个(D)"))
        self.next.setShortcut(_translate("MainWindow", "D"))
        self.save.setText(_translate("MainWindow", "保存(S)"))
        self.save.setShortcut(_translate("MainWindow", "S"))
        self.reset.setText(_translate("MainWindow", "重置(R)"))
        self.reset.setShortcut(_translate("MainWindow", "R"))
        self.groupBox_3.setTitle(_translate("MainWindow", "消息"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionOpenFile.setText(_translate("MainWindow", "打开"))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Q"))
        self.Refreshfolder.setText(_translate("MainWindow", "刷新当前文件夹下项目列表"))
        self.Refreshfolder.setShortcut(_translate("MainWindow", "E"))