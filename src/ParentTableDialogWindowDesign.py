# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParentTableDialogWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ParentTableWindow(object):
    def setupUi(self, ParentTableWindow):
        ParentTableWindow.setObjectName("ParentTableWindow")
        ParentTableWindow.resize(414, 635)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ParentTableWindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ParentTableWindowName = QtWidgets.QLabel(ParentTableWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ParentTableWindowName.setFont(font)
        self.ParentTableWindowName.setText("")
        self.ParentTableWindowName.setAlignment(QtCore.Qt.AlignCenter)
        self.ParentTableWindowName.setObjectName("ParentTableWindowName")
        self.verticalLayout_2.addWidget(self.ParentTableWindowName)
        self.frame = QtWidgets.QFrame(ParentTableWindow)
        self.frame.setMinimumSize(QtCore.QSize(200, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ParentTable = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParentTable.sizePolicy().hasHeightForWidth())
        self.ParentTable.setSizePolicy(sizePolicy)
        self.ParentTable.setMinimumSize(QtCore.QSize(60, 300))
        self.ParentTable.setColumnCount(2)
        self.ParentTable.setObjectName("ParentTable")
        self.ParentTable.setRowCount(0)
        self.ParentTable.horizontalHeader().setVisible(True)
        self.ParentTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.ParentTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ParentTableInsertButton = QtWidgets.QPushButton(self.frame)
        self.ParentTableInsertButton.setObjectName("ParentTableInsertButton")
        self.horizontalLayout.addWidget(self.ParentTableInsertButton)
        self.ParentTableUpdateButton = QtWidgets.QPushButton(self.frame)
        self.ParentTableUpdateButton.setObjectName("ParentTableUpdateButton")
        self.horizontalLayout.addWidget(self.ParentTableUpdateButton)
        self.ParentTableDeleteButton = QtWidgets.QPushButton(self.frame)
        self.ParentTableDeleteButton.setObjectName("ParentTableDeleteButton")
        self.horizontalLayout.addWidget(self.ParentTableDeleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ParentTableWindow)
        QtCore.QMetaObject.connectSlotsByName(ParentTableWindow)

    def retranslateUi(self, ParentTableWindow):
        _translate = QtCore.QCoreApplication.translate
        ParentTableWindow.setWindowTitle(_translate("ParentTableWindow", "Родительская таблица"))
        self.ParentTableInsertButton.setText(_translate("ParentTableWindow", "Добавить"))
        self.ParentTableUpdateButton.setText(_translate("ParentTableWindow", "Изменить"))
        self.ParentTableDeleteButton.setText(_translate("ParentTableWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ParentTableWindow = QtWidgets.QDialog()
    ui = Ui_ParentTableWindow()
    ui.setupUi(ParentTableWindow)
    ParentTableWindow.show()
    sys.exit(app.exec_())
