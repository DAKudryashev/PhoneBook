# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateParentWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateParentDialogWindow(object):
    def setupUi(self, UpdateParentDialogWindow):
        UpdateParentDialogWindow.setObjectName("UpdateParentDialogWindow")
        UpdateParentDialogWindow.resize(400, 107)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(UpdateParentDialogWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(UpdateParentDialogWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UpdateWindowName = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UpdateWindowName.setFont(font)
        self.UpdateWindowName.setText("")
        self.UpdateWindowName.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdateWindowName.setObjectName("UpdateWindowName")
        self.verticalLayout.addWidget(self.UpdateWindowName)
        self.ParentInput = QtWidgets.QLineEdit(self.frame)
        self.ParentInput.setObjectName("ParentInput")
        self.verticalLayout.addWidget(self.ParentInput)
        self.SaveParentButton = QtWidgets.QPushButton(self.frame)
        self.SaveParentButton.setObjectName("SaveParentButton")
        self.verticalLayout.addWidget(self.SaveParentButton)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(UpdateParentDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateParentDialogWindow)

    def retranslateUi(self, UpdateParentDialogWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateParentDialogWindow.setWindowTitle(_translate("UpdateParentDialogWindow", "Изменить"))
        self.SaveParentButton.setText(_translate("UpdateParentDialogWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateParentDialogWindow = QtWidgets.QDialog()
    ui = Ui_UpdateParentDialogWindow()
    ui.setupUi(UpdateParentDialogWindow)
    UpdateParentDialogWindow.show()
    sys.exit(app.exec_())