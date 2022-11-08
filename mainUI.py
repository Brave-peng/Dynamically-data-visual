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
        Form.resize(1011, 661)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 110, 571, 381))
        self.label.setText("")
        self.label.setObjectName("label")
        self.inportButton = QtWidgets.QPushButton(Form)
        self.inportButton.setGeometry(QtCore.QRect(160, 530, 81, 41))
        self.inportButton.setObjectName("inportButton")
        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(270, 530, 81, 41))
        self.playButton.setObjectName("playButton")
        self.stopButton = QtWidgets.QPushButton(Form)
        self.stopButton.setGeometry(QtCore.QRect(380, 530, 81, 41))
        self.stopButton.setObjectName("stopButton")
        self.reverseButton = QtWidgets.QPushButton(Form)
        self.reverseButton.setGeometry(QtCore.QRect(490, 530, 81, 41))
        self.reverseButton.setObjectName("reverseButton")
        self.exitButton = QtWidgets.QPushButton(Form)
        self.exitButton.setGeometry(QtCore.QRect(740, 530, 81, 41))
        self.exitButton.setObjectName("exitButton")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(610, 540, 91, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.inportButton.setText(_translate("Form", "导入数据"))
        self.playButton.setText(_translate("Form", "正向播放"))
        self.stopButton.setText(_translate("Form", "暂停"))
        self.reverseButton.setText(_translate("Form", "数据倒播"))
        self.exitButton.setText(_translate("Form", "退出"))

