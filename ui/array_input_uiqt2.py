# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'array_input_uiqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 238)
        MainWindow.setMinimumSize(QtCore.QSize(442, 238))
        MainWindow.setMaximumSize(QtCore.QSize(442, 238))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("#MainWindow{\n"
"background-color: rgb(167, 167, 167);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.takearray_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.takearray_textedit.setGeometry(QtCore.QRect(30, 20, 381, 111))
        self.takearray_textedit.setStyleSheet("background-color: rgb(231, 217, 234);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.takearray_textedit.setObjectName("takearray_textedit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 140, 381, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clear_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.clear_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.clear_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("#clear_btn{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color: rgb(f, f, f);\n"
"color: white;\n"
"}\n"
"\n"
"#clear_btn:hover{\n"
"background-color: \n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:0.625, y2:0.761, stop:0 rgba(48, 33, 14, 255), stop:1 rgba(0, 108, 80, 255));\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.add_array_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.add_array_btn.setMinimumSize(QtCore.QSize(0, 42))
        self.add_array_btn.setMaximumSize(QtCore.QSize(16777215, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(True)
        self.add_array_btn.setFont(font)
        self.add_array_btn.setStyleSheet("#add_array_btn {\n"
"background-color: rgb(102, 61, 54);\n"
"border-radius: 10px ;\n"
"color: white;\n"
"}\n"
"\n"
"#add_array_btn:hover {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.625, y2:0.761, stop:0 rgba(48, 33, 14, 255), stop:1 rgba(0, 108, 80, 255));\n"
"}")
        self.add_array_btn.setObjectName("add_array_btn")
        self.horizontalLayout.addWidget(self.add_array_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.takearray_textedit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.takearray_textedit.setPlaceholderText(_translate("MainWindow", "Please enter a string of numbers with a comma between the numbers. For example \'21, 42, 1, 4\'."))
        self.clear_btn.setText(_translate("MainWindow", "CLEAR"))
        self.add_array_btn.setText(_translate("MainWindow", "ADD ARRAY"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
