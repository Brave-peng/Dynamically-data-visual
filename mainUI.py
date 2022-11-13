# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1193, 839)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inportButton = QtWidgets.QPushButton(Form)
        self.inportButton.setObjectName("inportButton")
        self.horizontalLayout_2.addWidget(self.inportButton)
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.reverseButton = QtWidgets.QPushButton(Form)
        self.reverseButton.setObjectName("reverseButton")
        self.horizontalLayout_2.addWidget(self.reverseButton)
        self.mirrowButton = QtWidgets.QPushButton(Form)
        self.mirrowButton.setObjectName("mirrowButton")
        self.horizontalLayout_2.addWidget(self.mirrowButton)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.junpLine = QtWidgets.QLineEdit(Form)
        self.junpLine.setEnabled(True)
        self.junpLine.setObjectName("junpLine")
        self.horizontalLayout_2.addWidget(self.junpLine)
        self.jumpButton = QtWidgets.QPushButton(Form)
        self.jumpButton.setObjectName("jumpButton")
        self.horizontalLayout_2.addWidget(self.jumpButton)
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inportButton.setText(_translate("Form", "导入数据"))
        self.playButton.setText(_translate("Form", "正向播放"))
        self.stopButton.setText(_translate("Form", "暂停"))
        self.reverseButton.setText(_translate("Form", "数据倒播"))
        self.mirrowButton.setText(_translate("Form", "镜像"))
        self.jumpButton.setText(_translate("Form", "跳转"))
        self.exitButton.setText(_translate("Form", "退出"))

