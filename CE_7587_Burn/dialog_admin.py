# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dia_admin(object):
    def setupUi(self, dia_admin):
        dia_admin.setObjectName("dia_admin")
        dia_admin.resize(270, 131)
        self.lblName = QtWidgets.QLabel(dia_admin)
        self.lblName.setGeometry(QtCore.QRect(10, 21, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.lblPsw = QtWidgets.QLabel(dia_admin)
        self.lblPsw.setGeometry(QtCore.QRect(14, 55, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.lblPsw.setFont(font)
        self.lblPsw.setObjectName("lblPsw")
        self.edtName = QtWidgets.QLineEdit(dia_admin)
        self.edtName.setGeometry(QtCore.QRect(120, 20, 111, 21))
        self.edtName.setMaxLength(20)
        self.edtName.setObjectName("edtName")
        self.edtPsw = QtWidgets.QLineEdit(dia_admin)
        self.edtPsw.setGeometry(QtCore.QRect(120, 54, 111, 21))
        self.edtPsw.setMaxLength(20)
        self.edtPsw.setObjectName("edtPsw")
        self.btnOK = QtWidgets.QPushButton(dia_admin)
        self.btnOK.setGeometry(QtCore.QRect(80, 90, 91, 31))
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(dia_admin)
        QtCore.QMetaObject.connectSlotsByName(dia_admin)

    def retranslateUi(self, dia_admin):
        _translate = QtCore.QCoreApplication.translate
        dia_admin.setWindowTitle(_translate("dia_admin", "授权登陆"))
        self.lblName.setText(_translate("dia_admin", "用户名："))
        self.lblPsw.setText(_translate("dia_admin", "密    码："))
        self.btnOK.setText(_translate("dia_admin", "确定"))