import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from pyrebase import pyrebase

import login_gui
from create import Ui_MainWindow
from ui import main

firebaseConfig = {'apiKey': "AIzaSyATVvfrqvGFbFv3_qK7i1Bgwh7VhiqBfxo",
                  'authDomain': "sorting-algorithm-cac72.firebaseapp.com",
                  'databaseURL': "https://sorting-algorithm-cac72-default-rtdb.firebaseio.com",
                  'projectId': "sorting-algorithm-cac72",
                  'storageBucket': "sorting-algorithm-cac72.appspot.com",
                  'messagingSenderId': "690254571021",
                  'appId': "1:690254571021:web:118dec6a6146b4a89a1744",
                  'measurementId': "G-8HG19LNSMM"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class CreateAcc(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Login')
        self.ui.setupUi(self)
        self.app= main.MainWindow()
        #self.login = login_gui.LoginWindow()
        self.ui.createButton.clicked.connect(self.createFunction)

    def createFunction(self):
        email = self.ui.mail.text()
        if self.ui.password.text() == self.ui.confirimPassword.text():
            password = self.ui.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                self.close()
                self.app.show()
            except:
                self.invalid.setVisible(True)


if __name__ == "__main__":
    app = QApplication([])
    window = CreateAcc()
    window.show()
    sys.exit(app.exec_())
