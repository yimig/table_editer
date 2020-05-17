# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_form(object):
    def setupUi(self, main_form):
        main_form.setObjectName("main_form")
        main_form.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_form.sizePolicy().hasHeightForWidth())
        main_form.setSizePolicy(sizePolicy)
        main_form.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(main_form)
        self.centralwidget.setStyleSheet("font-family:Microsoft Yahei;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_2.setStyleSheet("background-color: rgb(33, 115, 70);\n"
"padding-top:0px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 20))
        self.widget_3.setStyleSheet("border-radius:0px;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_save = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_save.setStyleSheet("QPushButton\n"
"{\n"
"    border-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(14, 92, 47);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(33, 115, 70);\n"
"    background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_3.addWidget(self.btn_save, 1, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_add.setStyleSheet("QPushButton\n"
"{\n"
"    border-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(14, 92, 47);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(33, 115, 70);\n"
"    background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_3.addWidget(self.btn_add, 1, 1, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_search.setStyleSheet("QPushButton\n"
"{\n"
"    border-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(14, 92, 47);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(33, 115, 70);\n"
"    background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_3.addWidget(self.btn_search, 1, 3, 1, 1)
        self.btn_del = QtWidgets.QPushButton(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_del.setStyleSheet("QPushButton\n"
"{\n"
"    border-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(14, 92, 47);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(33, 115, 70);\n"
"    background-color: rgb(243, 243, 243);\n"
"}")
        self.btn_del.setObjectName("btn_del")
        self.gridLayout_3.addWidget(self.btn_del, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1)
        self.lb_title = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_title.sizePolicy().hasHeightForWidth())
        self.lb_title.setSizePolicy(sizePolicy)
        self.lb_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_title.setObjectName("lb_title")
        self.gridLayout_5.addWidget(self.lb_title, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_content = QtWidgets.QTableWidget(self.widget_4)
        self.tw_content.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom:1px solid #D4D4D4;")
        self.tw_content.setObjectName("tw_content")
        self.gridLayout.addWidget(self.tw_content, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_4, 2, 0, 1, 1)
        self.wg_search = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wg_search.sizePolicy().hasHeightForWidth())
        self.wg_search.setSizePolicy(sizePolicy)
        self.wg_search.setMinimumSize(QtCore.QSize(0, 0))
        self.wg_search.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-bottom:1px solid #D2D2D2;")
        self.wg_search.setObjectName("wg_search")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wg_search)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.le_keyword = QtWidgets.QLineEdit(self.wg_search)
        self.le_keyword.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid #C6C6C6;")
        self.le_keyword.setObjectName("le_keyword")
        self.gridLayout_2.addWidget(self.le_keyword, 0, 1, 1, 1)
        self.btn_begin_search = QtWidgets.QPushButton(self.wg_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_begin_search.sizePolicy().hasHeightForWidth())
        self.btn_begin_search.setSizePolicy(sizePolicy)
        self.btn_begin_search.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_begin_search.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius:0px;\n"
"    background-color: rgb(225, 225, 225);\n"
"    border-bottom:0px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(198, 198, 198);\n"
"    border-color: rgb(150, 150, 150);\n"
"    border-bottom:0px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(177, 177, 177);\n"
"    border-bottom:0px;\n"
"}")
        self.btn_begin_search.setObjectName("btn_begin_search")
        self.gridLayout_2.addWidget(self.btn_begin_search, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.wg_search)
        self.label_2.setStyleSheet("border-bottom:0px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.wg_search, 1, 0, 1, 1)
        main_form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_form)
        self.statusbar.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.statusbar.setObjectName("statusbar")
        main_form.setStatusBar(self.statusbar)

        self.retranslateUi(main_form)
        QtCore.QMetaObject.connectSlotsByName(main_form)

    def retranslateUi(self, main_form):
        _translate = QtCore.QCoreApplication.translate
        main_form.setWindowTitle(_translate("main_form", "Excel Lite"))
        self.btn_save.setStatusTip(_translate("main_form", "保存文档"))
        self.btn_save.setText(_translate("main_form", "保存"))
        self.btn_add.setStatusTip(_translate("main_form", "添加一条数据"))
        self.btn_add.setText(_translate("main_form", "添加"))
        self.btn_search.setStatusTip(_translate("main_form", "搜索文档"))
        self.btn_search.setText(_translate("main_form", "搜索"))
        self.btn_del.setStatusTip(_translate("main_form", "删除一条数据"))
        self.btn_del.setText(_translate("main_form", "删除"))
        self.lb_title.setStatusTip(_translate("main_form", "文档标题"))
        self.lb_title.setText(_translate("main_form", "工作簿 - Excel"))
        self.tw_content.setStatusTip(_translate("main_form", "文档内容"))
        self.le_keyword.setStatusTip(_translate("main_form", "搜索关键字"))
        self.btn_begin_search.setStatusTip(_translate("main_form", "执行搜索"))
        self.btn_begin_search.setText(_translate("main_form", "搜索"))
        self.label_2.setText(_translate("main_form", "查找内容："))
