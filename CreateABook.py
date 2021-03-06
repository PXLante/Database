# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Create a book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')




class Ui_CreateNewBook(object):




########################################################################################################################
# Functions for inserting values into .db tables

    def addBook(self):
        conn = sqlite3.connect('attempt1.db')
        c = conn.cursor()


        theBook = self.BooklineEdit.text()
        theAuthor = self.AuthorLineEdit.text()
        theGenre = str(self.GenreScroller.currentText())
        theISBN = self.ISBNLineEdit.text()


        c.execute("INSERT INTO bookDB (book, author, genre, ISBN) VALUES (?, ?, ?, ?)",
                   (theBook, theAuthor, theGenre, theISBN))
        conn.commit()
        c.close()
        conn.close()







########################################################################################################################
# UI Function. Builds the GUI. Contains references to buttons. Calls other functions.

    def setupUi(self, CreateNewBook):
        CreateNewBook.setObjectName("CreateNewBook")
        CreateNewBook.resize(628, 442)
        self.centralwidget = QtWidgets.QWidget(CreateNewBook)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateBooktext = QtWidgets.QTextBrowser(self.centralwidget)
        self.CreateBooktext.setGeometry(QtCore.QRect(190, 40, 231, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateBooktext.sizePolicy().hasHeightForWidth())
        self.CreateBooktext.setSizePolicy(sizePolicy)
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
        self.CreateBooktext.setPalette(palette)
        self.CreateBooktext.setObjectName("CreateBooktext")
        self.BookLabel = QtWidgets.QLabel(self.centralwidget)
        self.BookLabel.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.BookLabel.setObjectName("BookLabel")
        self.BooklineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BooklineEdit.setGeometry(QtCore.QRect(80, 130, 221, 21))
        self.BooklineEdit.setText("")
        self.BooklineEdit.setObjectName("BooklineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 340, 431, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveBook = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SaveBook.setObjectName("SaveBook")

        self.SaveBook.clicked.connect(self.addBook)
        self.SaveBook.clicked.connect(CreateNewBook.hide)

        self.horizontalLayout.addWidget(self.SaveBook)
        self.QuitBook = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.QuitBook.setObjectName("QuitBook")

        self.QuitBook.clicked.connect(CreateNewBook.hide)

        self.horizontalLayout.addWidget(self.QuitBook)
        self.AuthorLabel = QtWidgets.QLabel(self.centralwidget)
        self.AuthorLabel.setGeometry(QtCore.QRect(360, 110, 47, 13))
        self.AuthorLabel.setObjectName("AuthorLabel")
        self.AuthorLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthorLineEdit.setGeometry(QtCore.QRect(360, 130, 221, 21))
        self.AuthorLineEdit.setText("")
        self.AuthorLineEdit.setObjectName("AuthorLineEdit")
        self.GenreLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenreLabel.setGeometry(QtCore.QRect(80, 190, 47, 13))
        self.GenreLabel.setObjectName("GenreLabel")
        self.GenreScroller = QtWidgets.QComboBox(self.centralwidget)
        self.GenreScroller.setGeometry(QtCore.QRect(80, 210, 211, 22))
        self.GenreScroller.setObjectName("GenreScroller")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.GenreScroller.addItem("")
        self.ISBNLabel = QtWidgets.QLabel(self.centralwidget)
        self.ISBNLabel.setGeometry(QtCore.QRect(360, 190, 91, 16))
        self.ISBNLabel.setObjectName("ISBNLabel")
        self.ISBNLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ISBNLineEdit.setGeometry(QtCore.QRect(360, 210, 221, 21))
        self.ISBNLineEdit.setText("")
        self.ISBNLineEdit.setObjectName("ISBNLineEdit")
        CreateNewBook.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreateNewBook)
        self.statusbar.setObjectName("statusbar")
        CreateNewBook.setStatusBar(self.statusbar)

        self.retranslateUi(CreateNewBook)
        QtCore.QMetaObject.connectSlotsByName(CreateNewBook)

    def retranslateUi(self, CreateNewBook):
        _translate = QtCore.QCoreApplication.translate
        CreateNewBook.setWindowTitle(_translate("CreateNewBook", "Create a New User"))
        self.CreateBooktext.setHtml(_translate("CreateNewBook", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CREATE NEW BOOK</span></p></body></html>"))
        self.BookLabel.setText(_translate("CreateNewBook", "Book"))
        self.SaveBook.setText(_translate("CreateNewBook", "Save"))
        self.QuitBook.setText(_translate("CreateNewBook", "Quit"))
        self.AuthorLabel.setText(_translate("CreateNewBook", "Author"))
        self.GenreLabel.setText(_translate("CreateNewBook", "Genre"))
        self.GenreScroller.setItemText(0, _translate("CreateNewBook", "Other"))
        self.GenreScroller.setItemText(1, _translate("CreateNewBook", "Action and Adventure"))
        self.GenreScroller.setItemText(2, _translate("CreateNewBook", "Biography"))
        self.GenreScroller.setItemText(3, _translate("CreateNewBook", "Classic"))
        self.GenreScroller.setItemText(4, _translate("CreateNewBook", "Comics/Graphic Novel"))
        self.GenreScroller.setItemText(5, _translate("CreateNewBook", "Crime/Detective"))
        self.GenreScroller.setItemText(6, _translate("CreateNewBook", "Fable"))
        self.GenreScroller.setItemText(7, _translate("CreateNewBook", "Fairy tale"))
        self.GenreScroller.setItemText(8, _translate("CreateNewBook", "Fantasy"))
        self.GenreScroller.setItemText(9, _translate("CreateNewBook", "Folktale"))
        self.GenreScroller.setItemText(10, _translate("CreateNewBook", "Historical Fiction"))
        self.GenreScroller.setItemText(11, _translate("CreateNewBook", "Horror"))
        self.GenreScroller.setItemText(12, _translate("CreateNewBook", "Humor"))
        self.GenreScroller.setItemText(13, _translate("CreateNewBook", "Legend"))
        self.GenreScroller.setItemText(14, _translate("CreateNewBook", "Magical Realism"))
        self.GenreScroller.setItemText(15, _translate("CreateNewBook", "Meta Fiction"))
        self.GenreScroller.setItemText(16, _translate("CreateNewBook", "Mystery"))
        self.GenreScroller.setItemText(17, _translate("CreateNewBook", "Mythology"))
        self.GenreScroller.setItemText(18, _translate("CreateNewBook", "Picture Book"))
        self.GenreScroller.setItemText(19, _translate("CreateNewBook", "Science Fiction"))
        self.GenreScroller.setItemText(20, _translate("CreateNewBook", "Suspense/Thriller"))
        self.ISBNLabel.setText(_translate("CreateNewBook", "ISBN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewBook = QtWidgets.QMainWindow()
    ui = Ui_CreateNewBook()
    ui.setupUi(CreateNewBook)
    CreateNewBook.show()
    sys.exit(app.exec_())

