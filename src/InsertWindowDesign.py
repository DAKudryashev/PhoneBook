# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InsertDialogWindow(object):
    def setupUi(self, InsertDialogWindow):
        InsertDialogWindow.setObjectName("InsertDialogWindow")
        InsertDialogWindow.resize(400, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(InsertDialogWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(InsertDialogWindow)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FamiliyLabel = QtWidgets.QLabel(self.frame)
        self.FamiliyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FamiliyLabel.setObjectName("FamiliyLabel")
        self.horizontalLayout.addWidget(self.FamiliyLabel)
        self.FamilyComboBox = QtWidgets.QComboBox(self.frame)
        self.FamilyComboBox.setObjectName("FamilyComboBox")
        self.horizontalLayout.addWidget(self.FamilyComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NameLabel = QtWidgets.QLabel(self.frame)
        self.NameLabel.setObjectName("NameLabel")
        self.horizontalLayout_2.addWidget(self.NameLabel)
        self.NameComboBox = QtWidgets.QComboBox(self.frame)
        self.NameComboBox.setObjectName("NameComboBox")
        self.horizontalLayout_2.addWidget(self.NameComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.OtcLabel = QtWidgets.QLabel(self.frame)
        self.OtcLabel.setObjectName("OtcLabel")
        self.horizontalLayout_3.addWidget(self.OtcLabel)
        self.OtcComboBox = QtWidgets.QComboBox(self.frame)
        self.OtcComboBox.setObjectName("OtcComboBox")
        self.horizontalLayout_3.addWidget(self.OtcComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StreetLabel = QtWidgets.QLabel(self.frame)
        self.StreetLabel.setObjectName("StreetLabel")
        self.horizontalLayout_4.addWidget(self.StreetLabel)
        self.StreetComboBox = QtWidgets.QComboBox(self.frame)
        self.StreetComboBox.setObjectName("StreetComboBox")
        self.horizontalLayout_4.addWidget(self.StreetComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.InsertSaveButton = QtWidgets.QPushButton(self.frame)
        self.InsertSaveButton.setObjectName("InsertSaveButton")
        self.verticalLayout.addWidget(self.InsertSaveButton)
        self.verticalLayout_3.addWidget(self.frame)

        self.retranslateUi(InsertDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(InsertDialogWindow)

    def retranslateUi(self, InsertDialogWindow):
        _translate = QtCore.QCoreApplication.translate
        InsertDialogWindow.setWindowTitle(_translate("InsertDialogWindow", "Добавить"))
        self.InsertWindowName.setText(_translate("InsertDialogWindow", "Добавление нового контакта"))
        self.FamiliyLabel.setText(_translate("InsertDialogWindow", "Фамилия"))
        self.NameLabel.setText(_translate("InsertDialogWindow", "Имя"))
        self.OtcLabel.setText(_translate("InsertDialogWindow", "Отчество"))
        self.StreetLabel.setText(_translate("InsertDialogWindow", "Улица"))
        self.BldnLabel.setText(_translate("InsertDialogWindow", "Дом"))
        self.Bldn_hLabel.setText(_translate("InsertDialogWindow", "Строение"))
        self.ApprLabel.setText(_translate("InsertDialogWindow", "Квартира"))
        self.PhoneLabel.setText(_translate("InsertDialogWindow", "Телефон"))
        self.InsertSaveButton.setText(_translate("InsertDialogWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InsertDialogWindow = QtWidgets.QDialog()
    ui = Ui_InsertDialogWindow()
    ui.setupUi(InsertDialogWindow)
    InsertDialogWindow.show()
    sys.exit(app.exec_())