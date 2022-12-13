import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pyrebase import pyrebase

import createAcc_gui
from login import Ui_MainWindow
from ui import main

firebaseConfig = {  'apiKey': "AIzaSyATVvfrqvGFbFv3_qK7i1Bgwh7VhiqBfxo",
    'authDomain': "sorting-algorithm-cac72.firebaseapp.com",
    'databaseURL': "https://sorting-algorithm-cac72-default-rtdb.firebaseio.com",
    'projectId': "sorting-algorithm-cac72",
    'storageBucket': "sorting-algorithm-cac72.appspot.com",
    'messagingSenderId': "690254571021",
    'appId': "1:690254571021:web:118dec6a6146b4a89a1744",
    'measurementId': "G-8HG19LNSMM"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Login')
        self.ui.setupUi(self)
        self.create=createAcc_gui.CreateAcc()
        self.app= main.MainWindow()
        self.ui.loginButton.clicked.connect(self.loginFunction)
        self.ui.createButton.clicked.connect(self.gotoCreate)

    def loginFunction(self):
        email = self.ui.userName.text()
        password = self.ui.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            self.close()
            self.app.show()
        except:
            self.ui.control.setText('Login Failed')

    def gotoCreate(self):
        self.close()
        self.create.show()


if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
