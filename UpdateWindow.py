# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):
        UpdateWindow.setObjectName("UpdateWindow")
        UpdateWindow.resize(338, 223)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(UpdateWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(UpdateWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.InsertWindowName = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.InsertWindowName.setFont(font)
        self.InsertWindowName.setAlignment(QtCore.Qt.AlignCenter)
        self.InsertWindowName.setObjectName("InsertWindowName")
        self.verticalLayout.addWidget(self.InsertWindowName)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.BldnLabel = QtWidgets.QLabel(self.frame)
        self.BldnLabel.setObjectName("BldnLabel")
        self.horizontalLayout_5.addWidget(self.BldnLabel)
        self.BldnInput = QtWidgets.QLineEdit(self.frame)
        self.BldnInput.setObjectName("BldnInput")
        self.horizontalLayout_5.addWidget(self.BldnInput)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Bldn_hLabel = QtWidgets.QLabel(self.frame)
        self.Bldn_hLabel.setObjectName("Bldn_hLabel")
        self.horizontalLayout_6.addWidget(self.Bldn_hLabel)
        self.Bldn_hInput = QtWidgets.QLineEdit(self.frame)
        self.Bldn_hInput.setObjectName("Bldn_hInput")
        self.horizontalLayout_6.addWidget(self.Bldn_hInput)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ApprLabel = QtWidgets.QLabel(self.frame)
        self.ApprLabel.setObjectName("ApprLabel")
        self.horizontalLayout_7.addWidget(self.ApprLabel)
        self.ApprInput = QtWidgets.QLineEdit(self.frame)
        self.ApprInput.setObjectName("ApprInput")
        self.horizontalLayout_7.addWidget(self.ApprInput)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.PhoneLabel = QtWidgets.QLabel(self.frame)
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.horizontalLayout_8.addWidget(self.PhoneLabel)
        self.PhoneInput = QtWidgets.QLineEdit(self.frame)
        self.PhoneInput.setObjectName("PhoneInput")
        self.horizontalLayout_8.addWidget(self.PhoneInput)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.SaveButton = QtWidgets.QPushButton(self.frame)
        self.SaveButton.setObjectName("SaveButton")
        self.verticalLayout.addWidget(self.SaveButton)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(UpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateWindow)

    def retranslateUi(self, UpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateWindow.setWindowTitle(_translate("UpdateWindow", "Изменить"))
        self.InsertWindowName.setText(_translate("UpdateWindow", "Изменение текущей строки"))
        self.BldnLabel.setText(_translate("UpdateWindow", "Дом"))
        self.Bldn_hLabel.setText(_translate("UpdateWindow", "Строение"))
        self.ApprLabel.setText(_translate("UpdateWindow", "Квартира"))
        self.PhoneLabel.setText(_translate("UpdateWindow", "Телефон"))
        self.SaveButton.setText(_translate("UpdateWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateWindow = QtWidgets.QDialog()
    ui = Ui_UpdateWindow()
    ui.setupUi(UpdateWindow)
    UpdateWindow.show()
    sys.exit(app.exec_())