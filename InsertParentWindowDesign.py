# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsertParentWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InsertParentDialogWindow(object):
    def setupUi(self, InsertParentDialogWindow):
        InsertParentDialogWindow.setObjectName("InsertParentDialogWindow")
        InsertParentDialogWindow.resize(400, 104)
        self.horizontalLayout = QtWidgets.QHBoxLayout(InsertParentDialogWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(InsertParentDialogWindow)
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
        self.InsertWindowName.setText("")
        self.InsertWindowName.setAlignment(QtCore.Qt.AlignCenter)
        self.InsertWindowName.setObjectName("InsertWindowName")
        self.verticalLayout.addWidget(self.InsertWindowName)
        self.ParentInput = QtWidgets.QLineEdit(self.frame)
        self.ParentInput.setObjectName("ParentInput")
        self.verticalLayout.addWidget(self.ParentInput)
        self.SaveParentButton = QtWidgets.QPushButton(self.frame)
        self.SaveParentButton.setObjectName("SaveParentButton")
        self.verticalLayout.addWidget(self.SaveParentButton)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(InsertParentDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(InsertParentDialogWindow)

    def retranslateUi(self, InsertParentDialogWindow):
        _translate = QtCore.QCoreApplication.translate
        InsertParentDialogWindow.setWindowTitle(_translate("InsertParentDialogWindow", "Добавить"))
        self.SaveParentButton.setText(_translate("InsertParentDialogWindow", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InsertParentDialogWindow = QtWidgets.QDialog()
    ui = Ui_InsertParentDialogWindow()
    ui.setupUi(InsertParentDialogWindow)
    InsertParentDialogWindow.show()
    sys.exit(app.exec_())