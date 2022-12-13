# Introduction to Algorithm course graphical interface design project input array page.
# 5 December 2021.

import sys

# import speech_recognition as sr
from PyQt5.QtCore import pyqtSignal
# Written by Orhan Ozan Yildiz.
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from array_input_uiqt2 import Ui_MainWindow


class ArrayWindow(QMainWindow):
    array_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowTitle('Enter Array')
        self.ui.setupUi(self)
        self.ui.add_array_btn.clicked.connect(self.addArray)
        #		self.ui.mic_btn.clicked.connect(self.micro)
        self.unsorted_array = []
        self.voice = []
        self.ui.add_array_btn.clicked.connect(self.close)
        self.ui.clear_btn.clicked.connect(self.clear)

    """# %%%Speech Recognition
    def micro(self):
        r = sr.Recognizer()
        microphoneValue = ""

        with sr.Microphone() as source:
            try:
                # self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                # self.statusBar().showMessage('Stop talking...')
                if len(self.unsorted_array) == 0:
                    try:
                        microphoneValue = int(microphoneValue)
                        self.voice.append(microphoneValue)
                        self.ui.takearray_textedit.setText(str(self.voice))
                        self.take_Array()
                    except:
                        QMessageBox.warning(self, "ERROR", "Try again...")
                else:
                    try:
                        self.take_Array()
                        microphoneValue = int(microphoneValue)
                        self.unsorted_array.append(microphoneValue)
                        self.ui.takearray_textedit.setText(str(self.unsorted_array))
                    except:
                        QMessageBox.warning(self, "ERROR", "Try again...")
            except sr.UnknownValueError:
                QMessageBox.information(self, "ERROR", "Sorry, Cant understand, Please say again..")
            except sr.RequestError as e:
                QMessageBox.information(self, "ERROR",
                                        "Could not request results from Google Speech Recognition service; {0}".format(
                                            e))
            except sr.RequestError:
                QMessageBox.information(self, "ERROR", "No Internet Connection...")

        # %% Signal Connection"""

    def addArray(self):
        try:
            self.take_Array()
            self.array_signal.emit(self.unsorted_array)
            self.close()
        except ValueError:
            QMessageBox.warning(self, "ERROR", "Enter the array in valid form...")

    # %%Enter Array
    def take_Array(self):
        self.unsorted_array = self.ui.takearray_textedit.toPlainText()  # .split(",")
        self.unsorted_array = self.unsorted_array.strip("[")
        self.unsorted_array = self.unsorted_array.strip("]")
        self.unsorted_array = self.unsorted_array.split(",")
        print(self.unsorted_array)
        for i in range(len(self.unsorted_array)):
            self.unsorted_array[i] = int(self.unsorted_array[i])

    def clear(self):
        self.ui.takearray_textedit.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = ArrayWindow()
    window.show()
    sys.exit(app.exec_())
