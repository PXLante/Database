# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Create a user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateNewUser(object):


    def setupUi(self, CreateNewUser):
        CreateNewUser.setObjectName("CreateNewUser")
        CreateNewUser.resize(628, 442)
        self.centralwidget = QtWidgets.QWidget(CreateNewUser)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateUsertext = QtWidgets.QTextBrowser(self.centralwidget)
        self.CreateUsertext.setGeometry(QtCore.QRect(190, 40, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateUsertext.sizePolicy().hasHeightForWidth())
        self.CreateUsertext.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(117, 175, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 175, 13))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.CreateUsertext.setPalette(palette)
        self.CreateUsertext.setObjectName("CreateUsertext")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.NameLabel.setObjectName("NameLabel")
        self.NamelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NamelineEdit.setGeometry(QtCore.QRect(80, 130, 221, 21))
        self.NamelineEdit.setText("")
        self.NamelineEdit.setObjectName("NamelineEdit")
        self.AgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.AgeLabel.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.AgeLabel.setObjectName("AgeLabel")
        self.AgeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeLineEdit.setGeometry(QtCore.QRect(80, 210, 221, 21))
        self.AgeLineEdit.setText("")
        self.AgeLineEdit.setObjectName("AgeLineEdit")
        self.TypeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.TypeLabel_2.setGeometry(QtCore.QRect(360, 110, 47, 13))
        self.TypeLabel_2.setObjectName("TypeLabel_2")
        self.TypeScroller = QtWidgets.QComboBox(self.centralwidget)
        self.TypeScroller.setGeometry(QtCore.QRect(360, 130, 221, 22))
        self.TypeScroller.setObjectName("TypeScroller")
        self.TypeScroller.addItem("")
        self.TypeScroller.addItem("")
        self.PhoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.PhoneLabel.setGeometry(QtCore.QRect(360, 190, 91, 16))
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.PhoneLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PhoneLineEdit.setGeometry(QtCore.QRect(360, 210, 221, 21))
        self.PhoneLineEdit.setText("")
        self.PhoneLineEdit.setObjectName("PhoneLineEdit")
        self.EmailLabel = QtWidgets.QLabel(self.centralwidget)
        self.EmailLabel.setGeometry(QtCore.QRect(220, 260, 47, 13))
        self.EmailLabel.setObjectName("EmailLabel")
        self.EmailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailLineEdit.setGeometry(QtCore.QRect(220, 280, 221, 21))
        self.EmailLineEdit.setText("")
        self.EmailLineEdit.setObjectName("EmailLineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 340, 431, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveUser = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SaveUser.setObjectName("SaveUser")
        self.horizontalLayout.addWidget(self.SaveUser)
        self.QuitUser = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.QuitUser.setObjectName("QuitUser")

        self.QuitUser.clicked.connect(CreateNewUser.hide)

        self.horizontalLayout.addWidget(self.QuitUser)
        CreateNewUser.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreateNewUser)
        self.statusbar.setObjectName("statusbar")
        CreateNewUser.setStatusBar(self.statusbar)

        self.retranslateUi(CreateNewUser)
        QtCore.QMetaObject.connectSlotsByName(CreateNewUser)

    def retranslateUi(self, CreateNewUser):
        _translate = QtCore.QCoreApplication.translate
        CreateNewUser.setWindowTitle(_translate("CreateNewUser", "Create a New User"))
        self.CreateUsertext.setHtml(_translate("CreateNewUser", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CREATE NEW USER</span></p></body></html>"))
        self.NameLabel.setText(_translate("CreateNewUser", "Name"))
        self.AgeLabel.setText(_translate("CreateNewUser", "Age"))
        self.TypeLabel_2.setText(_translate("CreateNewUser", "Type"))
        self.TypeScroller.setItemText(0, _translate("CreateNewUser", "Student"))
        self.TypeScroller.setItemText(1, _translate("CreateNewUser", "Teacher"))
        self.PhoneLabel.setText(_translate("CreateNewUser", "Phone Number"))
        self.EmailLabel.setText(_translate("CreateNewUser", "Email"))
        self.SaveUser.setText(_translate("CreateNewUser", "Save"))
        self.QuitUser.setText(_translate("CreateNewUser", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewUser = QtWidgets.QMainWindow()
    ui = Ui_CreateNewUser()
    ui.setupUi(CreateNewUser)
    CreateNewUser.show()
    sys.exit(app.exec_())

