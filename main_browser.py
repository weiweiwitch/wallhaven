# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_browser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl, Qt, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineDownloadItem

from lib.Browser import Browser


class Ui_MainWindow(object):
    def setIcon(self, icon: QIcon):
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setUi(self)

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1550, 840)
        self.MainWindow.setMinimumSize(QtCore.QSize(1200, 500))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.browser = Browser(self.centralwidget)
        self.browser.setObjectName("browser")
        self.horizontalLayout.addWidget(self.browser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        self.load_web()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def load_web(self):
        # 禁用右键
        # self.browser.setContextMenuPolicy(Qt.NoContextMenu)
        self.page = self.browser.page()
        # 清除缓存
        # self.page.profile().clearHttpCache()
        self.page.setBackgroundColor(Qt.transparent)
        self.page.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        url = QUrl("http://localhost:1746/index.html#/online")
        self.browser.load(url)
        # self.download(QUrl("http://mirrors.aliyun.com/centos/7/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso"), filename='tttt')

    def download(self, url, filename):
        print(self)
        self.browser.page().download(QUrl(url), filename=filename)
        print("4")
        self.browser.page().profile().downloadRequested.connect(self.downloadFucntion)

    def downloadFucntion(self, downloadItem: QWebEngineDownloadItem):
        print("xxx")
        print(downloadItem.savePageFormat())
        print(downloadItem.path())
        print(downloadItem.url())
        print(downloadItem.totalBytes())
        print(downloadItem.totalBytes())
        print(downloadItem.downloadFileName())
        print(downloadItem.downloadDirectory())
        downloadItem.accept()


from PyQt5 import QtWebEngineWidgets
