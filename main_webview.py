# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_webview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import os
os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "9000"
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QFileInfo, QUrl, Qt
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from lib.WebBridge import WebBridge
from lib.wallhavenapi import WallhavenApiV1, Sorting, TopRange


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1550, 840)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 500))
        MainWindow.setStyleSheet("*{\n"
                                 "    font: normal 14px \"楷体\";\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget{\n"
                                 "    background-color: rgba(39,42,44,.45);\n"
                                 "    border-image: url(:/images/mian_bg.jpg);\n"
                                 "    \n"
                                 "}\n"
                                 "\n"
                                 "#left_widget{\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(168, 168, 168,.15), stop:1 rgba(39,42,44,.15));\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#my_bg_label,#more_info{\n"
                                 "    font: normal 16px \"楷体\";\n"
                                 "    color:#aaa;\n"
                                 "    padding:5px 20px;\n"
                                 "}\n"
                                 "\n"
                                 "#logo_label{\n"
                                 "    margin-left:12px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar {\n"
                                 "    height:0px;\n"
                                 "    width:0px;\n"
                                 "}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_widget = QtWidgets.QWidget(self.centralwidget)
        self.left_widget.setEnabled(True)
        self.left_widget.setMinimumSize(QtCore.QSize(200, 0))
        self.left_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_widget.setBaseSize(QtCore.QSize(43, 7))
        self.left_widget.setStyleSheet("QListWidget{\n"
                                       "    background: transparent;\n"
                                       "    outline:0px;\n"
                                       "    border:none;\n"
                                       "    font: normal 16px \"楷体\";\n"
                                       "    color:#c6c6c6;\n"
                                       "    padding:5px 85px 5px 45px;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "QListWidget::Item{\n"
                                       "    margin-top:10px;\n"
                                       "    background: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QListWidget::Item:hover,\n"
                                       "QListWidget::Item:selected {\n"
                                       "    color:#fff;\n"
                                       "}\n"
                                       "\n"
                                       "QListWidget::Item:selected {\n"
                                       "    border-bottom:2px solid qlineargradient(spread:reflect, x1:0, y1:0.016, x2:1, y2:1, stop:0.46438 rgba(0, 156, 218, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.left_widget.setObjectName("left_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.left_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 841))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.logo_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMaximumSize(QtCore.QSize(150, 150))
        self.logo_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.logo_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.logo_label.setAutoFillBackground(False)
        self.logo_label.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhPreferNumbers)
        self.logo_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo_label.setText("")
        self.logo_label.setTextFormat(QtCore.Qt.AutoText)
        self.logo_label.setPixmap(QtGui.QPixmap(":/images/logo.svg"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.logo_label.setIndent(-1)
        self.logo_label.setOpenExternalLinks(False)
        self.logo_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_4.addWidget(self.logo_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.my_bg_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.my_bg_label.setStyleSheet("")
        self.my_bg_label.setObjectName("my_bg_label")
        self.verticalLayout.addWidget(self.my_bg_label)
        self.my_bg_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.my_bg_list.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.my_bg_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.my_bg_list.setObjectName("my_bg_list")
        item = QtWidgets.QListWidgetItem()
        self.my_bg_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.my_bg_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.my_bg_list.addItem(item)
        self.verticalLayout.addWidget(self.my_bg_list)
        self.more_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.more_info.setStyleSheet("")
        self.more_info.setObjectName("more_info")
        self.verticalLayout.addWidget(self.more_info)
        self.more_info_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.more_info_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.more_info_list.setObjectName("more_info_list")
        item = QtWidgets.QListWidgetItem()
        self.more_info_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.more_info_list.addItem(item)
        self.verticalLayout.addWidget(self.more_info_list)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5.addWidget(self.left_widget)
        self.contentWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.contentWidget.setMinimumSize(QtCore.QSize(1250, 0))
        self.contentWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.contentWidget.setStyleSheet("#contentWidget{\n"
                                         "    background-color: rgba(39,42,44,.25);\n"
                                         "}\n"
                                         "\n"
                                         "#page1_title,#page2_title,#page3_title,#page4_title,#page5_title{\n"
                                         "    padding:5px 0;\n"
                                         "    color:#fff;\n"
                                         "    font: normal 18px \"楷体\";\n"
                                         "}")
        self.contentWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contentWidget.setLineWidth(0)
        self.contentWidget.setObjectName("contentWidget")
        self.online_page = QtWidgets.QWidget()
        self.online_page.setMinimumSize(QtCore.QSize(1250, 0))
        self.online_page.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.online_page.setStyleSheet("background: transparent;")
        self.online_page.setObjectName("online_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.online_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.page1_title = QtWidgets.QLabel(self.online_page)
        self.page1_title.setMinimumSize(QtCore.QSize(0, 28))
        self.page1_title.setMaximumSize(QtCore.QSize(16777215, 28))
        self.page1_title.setStyleSheet("background-color: rgba(39,42,44,.35);")
        self.page1_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page1_title.setObjectName("page1_title")
        self.verticalLayout_2.addWidget(self.page1_title)
        self.online_bg_webwidget = QtWebEngineWidgets.QWebEngineView(self.online_page)
        self.online_bg_webwidget.setObjectName("online_bg_webwidget")
        self.verticalLayout_2.addWidget(self.online_bg_webwidget)
        self.contentWidget.addWidget(self.online_page)
        self.list_page = QtWidgets.QWidget()
        self.list_page.setMinimumSize(QtCore.QSize(1250, 0))
        self.list_page.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.list_page.setStyleSheet("background: transparent;")
        self.list_page.setObjectName("list_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.list_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.page2_title = QtWidgets.QLabel(self.list_page)
        self.page2_title.setStyleSheet("background-color: rgba(39,42,44,.35);")
        self.page2_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page2_title.setObjectName("page2_title")
        self.verticalLayout_3.addWidget(self.page2_title)
        self.list_page_list_widget = QtWidgets.QListWidget(self.list_page)
        self.list_page_list_widget.setObjectName("list_page_list_widget")
        self.verticalLayout_3.addWidget(self.list_page_list_widget)
        self.contentWidget.addWidget(self.list_page)
        self.download_page = QtWidgets.QWidget()
        self.download_page.setMinimumSize(QtCore.QSize(1250, 0))
        self.download_page.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.download_page.setStyleSheet("background: transparent;")
        self.download_page.setObjectName("download_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.download_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.page3_title = QtWidgets.QLabel(self.download_page)
        self.page3_title.setStyleSheet("background-color: rgba(39,42,44,.35);")
        self.page3_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page3_title.setObjectName("page3_title")
        self.verticalLayout_4.addWidget(self.page3_title)
        self.download_page_list_widget = QtWidgets.QListWidget(self.download_page)
        self.download_page_list_widget.setObjectName("download_page_list_widget")
        self.verticalLayout_4.addWidget(self.download_page_list_widget)
        self.contentWidget.addWidget(self.download_page)
        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setMinimumSize(QtCore.QSize(1250, 0))
        self.setting_page.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.setting_page.setObjectName("setting_page")
        self.page4_title = QtWidgets.QLabel(self.setting_page)
        self.page4_title.setGeometry(QtCore.QRect(0, 0, 1250, 28))
        self.page4_title.setMinimumSize(QtCore.QSize(1250, 0))
        self.page4_title.setMaximumSize(QtCore.QSize(1250, 2000))
        self.page4_title.setStyleSheet("background-color: rgba(39,42,44,.35);")
        self.page4_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page4_title.setObjectName("page4_title")
        self.contentWidget.addWidget(self.setting_page)
        self.about_page = QtWidgets.QWidget()
        self.about_page.setMinimumSize(QtCore.QSize(1250, 0))
        self.about_page.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.about_page.setObjectName("about_page")
        self.page5_title = QtWidgets.QLabel(self.about_page)
        self.page5_title.setGeometry(QtCore.QRect(0, 0, 1254, 28))
        self.page5_title.setStyleSheet("background-color: rgba(39,42,44,.35);")
        self.page5_title.setAlignment(QtCore.Qt.AlignCenter)
        self.page5_title.setObjectName("page5_title")
        self.contentWidget.addWidget(self.about_page)
        self.horizontalLayout_5.addWidget(self.contentWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.init_frame()
        self.contentWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.my_bg_label.setText(_translate("MainWindow", "我的壁纸"))
        __sortingEnabled = self.my_bg_list.isSortingEnabled()
        self.my_bg_list.setSortingEnabled(False)
        item = self.my_bg_list.item(0)
        item.setText(_translate("MainWindow", "在线壁纸"))
        item = self.my_bg_list.item(1)
        item.setText(_translate("MainWindow", "轮换列表"))
        item = self.my_bg_list.item(2)
        item.setText(_translate("MainWindow", "下载中心"))
        self.my_bg_list.setSortingEnabled(__sortingEnabled)
        self.more_info.setText(_translate("MainWindow", "更多"))
        __sortingEnabled = self.more_info_list.isSortingEnabled()
        self.more_info_list.setSortingEnabled(False)
        item = self.more_info_list.item(0)
        item.setText(_translate("MainWindow", "设置"))
        item = self.more_info_list.item(1)
        item.setText(_translate("MainWindow", "关于"))
        self.more_info_list.setSortingEnabled(__sortingEnabled)
        self.page1_title.setText(_translate("MainWindow", "在线壁纸"))
        self.page2_title.setText(_translate("MainWindow", "轮换列表"))
        self.page3_title.setText(_translate("MainWindow", "下载中心"))
        self.page4_title.setText(_translate("MainWindow", "设置"))
        self.page5_title.setText(_translate("MainWindow", "关于"))

    # ===============================================================
    def init_frame(self):
        self.online_bg_webwidget.setContextMenuPolicy(Qt.NoContextMenu)
        page = self.online_bg_webwidget.page()
        page.setBackgroundColor(Qt.transparent)
        page.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        # 通信
        self.webChannel = QWebChannel()
        self.webBridge = WebBridge()
        self.webChannel.registerObject("webBridge", self.webBridge)
        page.setWebChannel(self.webChannel)
        page.profile().clearHttpCache()
        url = QUrl(QFileInfo("page/online_wallpaper.html").absoluteFilePath())
        url2 = QUrl("https://wallhaven.cc/toplist")
        self.online_bg_webwidget.load(url)
        self.webBridge.SigSaveParamsFromWeb.connect(self.saveParamsFromWeb)
        self.webBridge.SigLoadMoreData.connect(self.load_data)

    def saveParamsFromWeb(self, strParameter):
        try:
            params = json.loads(f"""{strParameter}""")
        except BaseException as e:
            print(e)
        print(params)

    def load_data(self, page):
        wallhaven_api = WallhavenApiV1(api_key=os.getenv('APIKEY', None), verify_connection=True,
                                       base_url="http://wallhaven.cc/api/v1",
                                       requestslimit_timeout=(15, 5))
        search_data = wallhaven_api.search(top_range=TopRange.one_day, sorting=Sorting.toplist, page=page)
        print(search_data)
        sleep(5)
        self.webBridge.SigLoadPageDataFromQt.emit(json.dumps(search_data))

    def bind_event(self):
        """绑定事件"""
        self.my_bg_list.setCurrentRow(0)
        self.my_bg_list.itemClicked.connect(self.my_bg_list_change)
        self.more_info_list.itemClicked.connect(self.more_info_list_change)

    def my_bg_list_change(self):
        """侧边栏壁纸监听"""
        self.more_info_list.clearSelection()
        self.contentWidget.setCurrentIndex(self.my_bg_list.currentRow())

    def more_info_list_change(self):
        """侧边栏更多监听"""
        self.my_bg_list.clearSelection()
        self.contentWidget.setCurrentIndex(3 + self.more_info_list.currentRow())


