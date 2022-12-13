import csv
import math
import random
import sys
import time
import tkinter as tk
import webbrowser
from tkinter import filedialog

import numpy as np
import pandas as pd
import xlsxwriter
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
import speech_recognition as sr
from PyQt5.uic.properties import QtWidgets

from ui_functions import *
from utils_operations import binarysearch
from ui_main import Ui_MainWindow
from array_input import ArrayWindow
from utils_operations import timer
from utils_operations import fibonacci
from utils_operations import binarysearch
from utils_operations import createamatrix, matrix_mult
from utils_operations import randomized_selection

random_select = randomized_selection()
binarySearch = binarysearch()
fibonacci = fibonacci()
times = timer()
create_matrix = createamatrix()
matrix_mult = matrix_mult()

class MainWindow(QMainWindow):
    stop_array = "global"

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.AddArray = ArrayWindow()
        self.ui.array_sort.setMinimum(0)
        self.ui.array_sort.setMaximum(100)
        self.ui.lower_range.setValidator(QIntValidator(-1000000, 10000, self))
        self.ui.upper_range.setValidator(QIntValidator(10000, 1000000, self))
        self.ui.array_sort.valueChanged.connect(self.value_length)
        self.ui.set_default_values.clicked.connect(self.SetDefaultValues)
        self.ui.set_default_values.clicked.connect(self.spin_box)
        self.ui.set_default_values.clicked.connect(self.CreateBarGraph)
        self.ui.create_array.clicked.connect(self.CreateArray)
        self.ui.create_array.clicked.connect(self.spin_box)
        self.ui.enter_array.clicked.connect(self.add_array)
        self.ui.stop_btn.clicked.connect(self.stop_button)
        self.ui.skip_btn.clicked.connect(self.skip_button)
        self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
        self.ui.MplSort.canvas.axes.get_yaxis().set_visible(False)

        self.AddArray.array_signal.connect(self.add_array)
        self.AddArray.array_signal.connect(self.take_user_array)
        self.unsorted_array = []

        ## TOGGLE/BURGUER MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        # sorting Page
        self.ui.sortPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sortingPage))
        # compare Page
        self.ui.comparePageutton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.comparePage))
        # fibonacci Page
        self.ui.fibonacciPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fibonacciPage))
        # binary search Page
        self.ui.binaryPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.binaryPage))
        # Matrix Page
        self.ui.matrixPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.martixPage))
        # random Page
        self.ui.randomPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.randomPage))
        # info Page
        self.ui.infoPageButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.infoPage))

        # sorting Page Uİ
        self.ui.micro_btn.clicked.connect(self.voice)
        self.ui.create_array.clicked.connect(self.CreateBarGraph)
        self.ui.clear_btn.clicked.connect(self.clearSorting)
        self.ui.speedSlider.setFocusPolicy(Qt.NoFocus)
        self.ui.MplSort.canvas.axes.get_xaxis().set_visible(False)
        self.ui.bubble_sort.clicked.connect(self.BubbleSort)
        self.ui.insertion_sort.clicked.connect(self.InsertionSort)
        self.ui.merge_sort.clicked.connect(self.CallMerge)
        self.ui.selection_sort.clicked.connect(self.SelectionSort)
        self.ui.quick_sort.clicked.connect(self.CallQuickSort)
        self.ui.heap_sort.clicked.connect(self.HeapSort)
        self.ui.counting_sort.clicked.connect(self.CountingSort)
        self.ui.bucket_sort.clicked.connect(self.BucketSort)
        self.ui.shell_sort.clicked.connect(self.ShellSort)
        self.ui.radix_sort.clicked.connect(self.RadixSort)
        self.ui.coctail_sort.clicked.connect(self.CocktailSort)
        self.ui.comb_sort.clicked.connect(self.CallCompSort)
        self.ui.upButton.clicked.connect(self.plus)
        self.ui.downButton.clicked.connect(self.minus)

        # compare Page Uİ
        self.ui.clear_btn_comparison.clicked.connect(self.clearComparison)
        self.ui.comparisonall_button.pressed.connect(self.compare_all)
        self.ui.comparisonchoosen_button.pressed.connect(self.compare_chosen)
        self.ui.bubblesort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.insertionsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.mergesort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.selectionsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.countingsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.heapsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.bucketsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.radixsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.quicksort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.shellsort_checkBox.toggled.connect(self.checkbox_toggled)
        self.ui.MplSortComparison.canvas.axes.set_title('Time Comparison Graph')
        self.ui.MplSortComparison.canvas.axes.set_xlabel('Number of elements in array')
        self.ui.MplSortComparison.canvas.axes.set_ylabel('Time')

        # fibonacci Page Uİ
        self.ui.n_number.setValidator(QIntValidator(1, 1000, self))
        self.ui.findfibo_btn.clicked.connect(self.fibo_number)
        self.ui.findfibo_btn.clicked.connect(self.fibo_bar_graph)
        self.ui.MplFib.canvas.axes.get_xaxis().set_visible(False)
        self.ui.MplFib.canvas.axes.get_yaxis().set_visible(False)
        self.ui.mic_btn_fibo.clicked.connect(self.voiceFibo)
        self.ui.clear_btn_fibo.clicked.connect(self.clearFibo)

        # binary search Page Uİ
        self.ui.array_len.valueChanged.connect(self.valuelen)
        self.ui.createanarray_btn.clicked.connect(self.create_array)
        self.ui.sort_btn.clicked.connect(self.sortingarray)
        self.ui.find_btn.clicked.connect(self.find_number)
        self.ui.clear_btn_binary.clicked.connect(self.clearBinary)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_3.toggled.connect(self.random_array)
        self.ui.checkBox_4.toggled.connect(self.array_yourself)
        self.ui.set_default_values_binary.clicked.connect(self.set_default_array)
        self.ui.MplSort_binary.canvas.axes.get_xaxis().set_visible(False)
        self.ui.MplSort_binary.canvas.axes.get_yaxis().set_visible(False)
        self.ui.disp_unsorted_array.setReadOnly(True)
        self.ui.lower_range_binary.setValidator(QIntValidator(-1000000, 10000, self))
        self.ui.upper_range_binary.setValidator(QIntValidator(10000, 1000000, self))
        self.ui.mic_btn_binary.clicked.connect(self.voiceBinary)

        # Matrix Page Uİ
        self.ui.row_m1.returnPressed.connect(self.inputs)
        self.ui.column_m1.returnPressed.connect(self.inputs)
        self.ui.row_m2.returnPressed.connect(self.inputs)
        self.ui.column_m2.returnPressed.connect(self.inputs)

        self.ui.row_m1.setValidator(QIntValidator(0, 10, self))
        self.ui.column_m1.setValidator(QIntValidator(0, 10, self))
        self.ui.row_m2.setValidator(QIntValidator(0, 10, self))
        self.ui.column_m2.setValidator(QIntValidator(0, 10, self))

        self.ui.create_matrix_btn_1.clicked.connect(self.matrix1_user)
        self.ui.create_matrix_btn_2.clicked.connect(self.matrix2_user)
        self.ui.back_btn.clicked.connect(self.close)

        self.ui.generate_matrix_btn.clicked.connect(self.random_matrices)
        self.ui.multiply_btn.clicked.connect(self.multiplication)

        self.ui.clear_btn_matrix.clicked.connect(self.clearMatrix)
        self.ui.determinant_btn_1.clicked.connect(self.determinant1)
        self.ui.determinant_btn_2.clicked.connect(self.determinant2)
        self.ui.inverse_btn_1.clicked.connect(self.inverse1)
        self.ui.inverse_btn_2.clicked.connect(self.inverse2)
        self.ui.transpose_btn_1.clicked.connect(self.transpose1)
        self.ui.transpose_btn_2.clicked.connect(self.transpose2)
        self.ui.rank_btn_1.clicked.connect(self.rank1)
        self.ui.rank_btn_2.clicked.connect(self.rank2)
        self.ui.multiplyby_btn.clicked.connect(self.mult_scalar1)
        self.ui.multiplyby_btn_2.clicked.connect(self.mult_scalar2)
        self.visible1_false()
        self.visible2_false()
        self.ui.mic_btn_matrix.clicked.connect(self.voiceMatrix)

        #Random Page Uİ
        self.ui.array_len_2.valueChanged.connect(self.value_len_random)
        self.ui.createanarray_btn_2.clicked.connect(self.create_array_random)
        self.ui.createanarray_btn_2.clicked.connect(self.sorting_array_random)
        self.ui.set_default_values_2.clicked.connect(self.set_default_array_random)
        self.t = None
        self.msg = None
        self.x = None
        self.sorted_arrayR = None
        self.upperR = None
        self.rectsR = None
        self.lengthR = None
        self.lowerR = None
        self.msg3R = None
        self.smallestR = None
        self.numberR = None
        # Back to main menu.
        self.ui.find_btn.clicked.connect(self.find_number_random)
        self.ui.clear_btn_2.clicked.connect(self.clearRandom)
        self.ui.random_array_checkbox.setChecked(True)
        self.ui.random_array_checkbox.toggled.connect(self.random_array_random)
        self.ui.create_array_checkbox.toggled.connect(self.array_yourself_random)
        self.ui.MplSort_random.canvas.axes.get_xaxis().set_visible(False)
        self.ui.MplSort_random.canvas.axes.get_yaxis().set_visible(False)
        self.ui.lower_range_2.setValidator(QIntValidator(-1000000, 10000, self))
        self.ui.upper_range_2.setValidator(QIntValidator(10000, 1000000, self))
        self.unsorted_array = []
        self.lower_range_2 = 0
        self.upper_range_2 = 0
        self.ui.mic_btn.clicked.connect(self.voiceRandom)

        #info Page Uİ
        self.ui.logoButton.clicked.connect(self.uni_logo)
        self.ui.youtubeButton.clicked.connect(self.youtube_logo)
        self.ui.githubButton.clicked.connect(self.github_logo)
        self.ui.linkedInlBUtton.clicked.connect(self.linkedIn_logo)
        self.ui.instagramButton.clicked.connect(self.intagram_logo)


    # sorting Page Uİ
    def spin_box(self):
        self.seed_value = self.ui.spinBox.value()

    def plus(self):
        temp_min = self.ui.array_sort.minimum()
        temp_max = self.ui.array_sort.maximum()
        self.ui.array_sort.setMinimum(temp_min + 100)
        self.ui.array_sort.setMaximum(temp_max + 100)

    def minus(self):
        temp_min = self.ui.array_sort.minimum()
        temp_max = self.ui.array_sort.maximum()
        if temp_min > 0:
            self.ui.array_sort.setMinimum(temp_min - 100)
            self.ui.array_sort.setMaximum(temp_max - 100)
        else:
            QMessageBox.warning(self, "ERROR", "The range you set for the array length must be at least 0!")

    def voice(self):
        r = sr.Recognizer()
        microphoneValue = ""
        with sr.Microphone() as source:
            try:
                self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                self.statusBar().showMessage('Stop talking...')
                try:
                    if microphoneValue == 'bubble sort':
                        try:
                            self.BubbleSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'insertion sort':
                        try:
                            self.InsertionSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'merge sort':
                        try:
                            self.CallMerge()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'heap sort':
                        try:
                            self.HeapSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'selection sort':
                        try:
                            self.SelectionSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'quicksort':
                        try:
                            self.CallQuickSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'bucket sort':
                        try:
                            self.BucketSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'counting sort':
                        try:
                            self.CountingSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'radix sort':
                        try:
                            self.RadixSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'shell sort':
                        try:
                            self.ShellSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'default':
                        try:
                            self.SetDefaultValues()
                            self.CreateBarGraph()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'insert array':
                        try:
                            self.add_array()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'clear':
                        try:
                            self.clearSorting()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'time comparison':
                        try:
                            self.time_comparison_open()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'close':
                        try:
                            self.close()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'cocktail sort':
                        try:
                            self.CocktailSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    elif microphoneValue == 'comb sort':
                        try:
                            self.CallCompSort()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Create array first...")
                    else:
                        QMessageBox.warning(self, "ERROR", "Try Again...")
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

    def insert_response(self, action):
        if action.text() == "Txt File":
            try:
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("text file", "*.txt"), ("all files", "*.*")))
                text_file = open(file_path, "r")
                self.unsorted_array = text_file.read().split(',')
                for i in range(len(self.unsorted_array)):
                    self.unsorted_array[i] = int(self.unsorted_array[i])
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.ui.MplSort.canvas.axes.clear()
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff',
                                                             edgecolor="black")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
            except FileNotFoundError:
                self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")
        elif action.text() == "Csv File":
            try:
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("csv file", "*.csv"), ("all files", "*.*")))
                with open(file_path) as f:
                    reader = csv.reader(f)
                    for column in reader:
                        self.unsorted_array = column
                    for i in range(len(self.unsorted_array)):
                        self.unsorted_array[i] = int(self.unsorted_array[i])
                    t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                    self.ui.MplSort.canvas.axes.clear()
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff',
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
            except FileNotFoundError:
                self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")
        elif action.text() == "Xlsx File":
            try:
                root = tk.Tk()
                root.withdraw()
                file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("xlsx file", "*.xlsx"), ("all files", "*.*")))
                df = pd.read_excel(file_path)
                self.unsorted_array = df.columns
                self.unsorted_array = list(self.unsorted_array)
                print(self.unsorted_array)
                for i in range(len(self.unsorted_array)):
                    self.unsorted_array[i] = int(self.unsorted_array[i])
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.ui.MplSort.canvas.axes.clear()
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff',
                                                             edgecolor="black")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Please check your file...")
            except FileNotFoundError:
                self.msg = QMessageBox.critical(self, "Error", "Please choose a file...")

    def stop_button(self):
        if self.ui.stop_btn.text() == "Pause":
            self.ui.stop_btn.setText("Continue")
            self.ui.stop_btn.setStyleSheet("font: 10pt \"MS Shell Dlg 2\" white;\n"
                                           "border-radius: 10px ;\n"
                                           "background-color: rgb(0, 0, 0);\n"
                                           "color: white;")
            global stop_array
            self.stop_array = int(1)
        elif self.ui.stop_btn.text() == "Continue":
            self.ui.stop_btn.setText("Pause")
            self.ui.stop_btn.setStyleSheet("#stop_btn:hover{\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
                                           "}\n"
                                           "\n"
                                           "#stop_btn{\n"
                                           "background-color: rgba(255, 255, 255,0);\n"
                                           "}")
            global stop_array
            self.stop_array = int(0)

    def skip_button(self):
        global stop_array
        global unsorted_array
        self.ui.MplSort.canvas.axes.clear()
        self.stop_array = int(2)
        if self.stop_array == 2:
            sorted_array = self.unsorted_array
            sorted_array.sort()
            t = np.arange(len(sorted_array))
            self.ui.MplSort.canvas.axes.clear()
            self.rects = self.ui.MplSort.canvas.axes.bar(t, sorted_array, color="green")
            self.autolabelSort(self.rects)
            self.ui.MplSort.canvas.draw()

    def operation_buttons(self):
        global stop_array
        global unsorted_array
        while self.stop_array == 1:
            if self.stop_array == 0:
                if self.stop_array == 2:
                    self.ui.MplSort.canvas.axes.clear()
                    break
                break
            time.sleep(1)
            QtCore.QCoreApplication.processEvents()
            if self.stop_array == 2:
                self.ui.MplSort.canvas.axes.clear()
                break

    def add_array(self):
        self.AddArray.clear()
        self.AddArray.show()
        self.ui.MplSort.canvas.axes.clear()
        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort.canvas.draw()

    def take_user_array(self, array):
        self.unsorted_array = array
        t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        self.ui.MplSort.canvas.axes.clear()
        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
        self.autolabelSort(self.rects)
        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort.canvas.draw()

    def disable_button(self):
        self.ui.create_array.setEnabled(False)
        self.ui.bubble_sort.setEnabled(False)
        self.ui.insertion_sort.setEnabled(False)
        self.ui.merge_sort.setEnabled(False)
        self.ui.quick_sort.setEnabled(False)
        self.ui.heap_sort.setEnabled(False)
        self.ui.counting_sort.setEnabled(False)
        self.ui.bucket_sort.setEnabled(False)
        self.ui.radix_sort.setEnabled(False)
        self.ui.set_default_values.setEnabled(False)

    def enable_button(self):
        self.ui.create_array.setEnabled(True)
        self.ui.bubble_sort.setEnabled(True)
        self.ui.insertion_sort.setEnabled(True)
        self.ui.merge_sort.setEnabled(True)
        self.ui.quick_sort.setEnabled(True)
        self.ui.heap_sort.setEnabled(True)
        self.ui.counting_sort.setEnabled(True)
        self.ui.bucket_sort.setEnabled(True)
        self.ui.radix_sort.setEnabled(True)
        self.ui.set_default_values.setEnabled(True)

    def value_length(self):
        self.length = int(self.ui.array_sort.value())
        self.ui.displayarrays_sort.setText(str(self.length))

    def project_speed(self):
        self.project_speed = 0.001 * (100 - self.ui.verticalSlider.value())

    def CreateArray(self):
        self.unsorted_array = []
        try:
            try:
                self.lower = int(self.ui.lower_range.text())
                self.upper = int(self.ui.upper_range.text())
                if (self.lower == 0 and self.upper == 0) or self.length == 0:
                    self.msg = QMessageBox.critical(self, "Error",
                                                    "Fill in the required fields...!\nMake sure to set to Array Size and Range...")
                else:
                    if self.lower > self.upper:
                        self.msg = QMessageBox.critical(self, "Error",
                                                        'Upper range must be greater than lower range...')
                        self.clear()
                    else:
                        if self.ui.checkBox.isChecked():
                            random.seed(self.seed_value)
                            random.sample
                            if self.ui.checkBox_2.isChecked():
                                if abs(self.upper - self.lower) < self.length:
                                    self.msg = QMessageBox.critical(self, "Error",
                                                                    "'The length value cannot bigger than the difference on the lower and upper limit must be bigger than the length value.")
                                    self.clear()
                                else:
                                    self.unsorted_array = []
                                    while len(self.unsorted_array) < self.length:
                                        x = random.randint(self.lower, self.upper)
                                        if not np.isin(x, self.unsorted_array):
                                            self.unsorted_array.append(x)

                            else:
                                self.unsorted_array = []
                                while True:
                                    self.unsorted_array.append(random.randint(self.lower, self.upper))
                                    if len(self.unsorted_array) == self.length:
                                        break
                        else:
                            if self.ui.checkBox_2.isChecked():
                                if abs(self.upper - self.lower) < self.length:
                                    self.msg = QMessageBox.critical(self, "Error",
                                                                    "'The length value cannot bigger than the difference on the lower and upper limit must be bigger than the length value.")
                                    self.clear()
                                else:
                                    self.unsorted_array = []
                                    while len(self.unsorted_array) < self.length:
                                        x = random.randint(self.lower, self.upper)
                                        if not np.isin(x, self.unsorted_array):
                                            self.unsorted_array.append(x)

                            else:
                                self.unsorted_array = []
                                while True:
                                    self.unsorted_array.append(random.randint(self.lower, self.upper))
                                    if len(self.unsorted_array) == self.length:
                                        break
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields!")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")

    def SetDefaultValues(self):
        self.lower = random.randint(-50, 0)
        self.ui.lower_range.setText(str(self.lower))
        self.upper = random.randint(50, 300)
        self.ui.upper_range.setText(str(self.upper))
        self.length = random.randint(10, 50)
        self.ui.displayarrays_sort.setText(str(self.length))
        if self.ui.checkBox.isChecked():
            random.seed(self.seed_value)
            random.sample
            if self.ui.checkBox_2.isChecked():
                self.unsorted_array = []
                while len(self.unsorted_array) < self.length:
                    x = random.randint(self.lower, self.upper)
                    if not np.isin(x, self.unsorted_array):
                        self.unsorted_array.append(x)

            else:
                self.unsorted_array = []
                while True:
                    self.unsorted_array.append(random.randint(self.lower, self.upper))
                    if len(self.unsorted_array) == self.length:
                        break
        else:
            if self.ui.checkBox_2.isChecked():
                self.unsorted_array = []
                while len(self.unsorted_array) < self.length:
                    x = random.randint(self.lower, self.upper)
                    if not np.isin(x, self.unsorted_array):
                        self.unsorted_array.append(x)

            else:
                self.unsorted_array = []
                while True:
                    self.unsorted_array.append(random.randint(self.lower, self.upper))
                    if len(self.unsorted_array) == self.length:
                        break

    def CreateBarGraph(self):
        t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        self.ui.MplSort.canvas.axes.clear()
        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#4dffff', edgecolor="black")
        self.autolabelSort(self.rects)
        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort.canvas.draw()

    def autolabelSort(self, rects):
        for rect in self.rects:
            height = rect.get_height()
            if height > 0:
                self.ui.MplSort.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='bottom')
            else:
                self.ui.MplSort.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='top')

    def BubbleSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                for i in range(0, len(self.unsorted_array) - 1):  # loop for all array elements
                    for j in range(0, len(self.unsorted_array) - i - 1):  # second cycle for swap operations
                        if self.unsorted_array[j + 1] < self.unsorted_array[j]:  # if the left greater than right
                            self.operation_buttons()
                            self.ui.MplSort.canvas.axes.clear()
                            self.ui.MplSort.canvas.axes.set_title("Bubble Sort Animation", loc='left')
                            self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                         edgecolor="#f0f8ff")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j],
                                                                         color="#FFE4E1", edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="#FFE4E1",
                                                            edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort.canvas.draw()
                            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                            time.sleep(self.project_speed)
                            QApplication.processEvents()

                            self.unsorted_array[j], self.unsorted_array[j + 1] = self.unsorted_array[j + 1], \
                                                                                 self.unsorted_array[j]

                            self.ui.MplSort.canvas.axes.clear()
                            self.ui.MplSort.canvas.axes.set_title("Bubble Sort Animation", loc='left')
                            self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                         edgecolor="#f0f8ff")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j],
                                                                         color="#FFE4E1", edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1],
                                                                         color="#FFE4E1", edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort.canvas.draw()
                            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                            time.sleep(self.project_speed)
                            QApplication.processEvents()
                self.ui.MplSort.canvas.axes.clear()
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Fill in the required fields...!\nMake sure to set to Array Size and Range...")
            self.enable_button()

    def InsertionSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                for i in range(1, len(self.unsorted_array)):
                    j = i - 1
                    key = self.unsorted_array[i]
                    while (self.unsorted_array[j] > key) and (j >= 0):
                        self.unsorted_array[j + 1] = self.unsorted_array[j]
                        j -= 1
                        self.operation_buttons()
                        self.ui.MplSort.canvas.axes.clear()
                        self.ui.MplSort.canvas.axes.set_title("Insertion Sort Animation", loc='left')
                        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                     edgecolor="#f0f8ff")
                        self.autolabelSort(self.rects)
                        self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#FFE4E1",
                                                                     edgecolor="black")
                        self.autolabelSort(self.rects)
                        self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1],
                                                                     color="#FFE4E1", edgecolor="black")
                        self.autolabelSort(self.rects)
                        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                        self.ui.MplSort.canvas.draw()
                        self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                        time.sleep(self.project_speed)
                        QApplication.processEvents()

                    self.unsorted_array[j + 1] = key
                    self.ui.MplSort.canvas.axes.clear()
                    self.ui.MplSort.canvas.axes.set_title("Insertion Sort Animation", loc='left')
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()
                self.enable_button()

        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def CallMerge(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                array = self.unsorted_array
                self.MergeSort(array, 0, len(self.unsorted_array) - 1)
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def MergeSort(self, array, p, r):
        if p < r:  # p is the first index, r is the last index.
            q = (p + r) // 2  # q is the middle index
            self.MergeSort(array, p, q)  # recursive function for new right array created
            self.MergeSort(array, q + 1, r)  # recursive function for new right array created
            self.merge(array, p, q, r)  # merge function for sorted array to merge
        return array

    def merge(self, array, p, q, r):
        t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        n1 = q - p + 1  # left array of length is n1
        n2 = r - q  # right array of length is n2
        left_array = np.empty(n1 + 1)  # computes the length n1+1 of the subarray
        right_array = np.empty(n2 + 1)  # computes the length n2+1 of the subarray
        for i in range(n1):  # The for loop of copies the subarray divided array into left array
            left_array[i] = array[p + i]
        for j in range(n2):  # The for loop of copies the subarray divided array into right array
            right_array[j] = array[q + 1 + j]
        left_array[n1] = np.inf  # use inf value as the sentinel value
        right_array[n2] = np.inf  # use inf value as the sentinel value

        # empty subarray contains the 0 smallest elements of left array and right array
        i = 0
        j = 0
        for k in range(p, r + 1):  # the subarrays index compare
            if left_array[i] <= right_array[
                j]:  # compare left array ith index and right array jth index for sorted array
                array[k] = left_array[i]  # the smaller one is added to the arrays about to be sorted
                i += 1
                self.operation_buttons()
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[k], array[k], color="gray", edgecolor="black")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[i - 1], array[i - 1], color="red", edgecolor="black")
                self.autolabelSort(self.rects)
                # self.ui.MplSort.canvas.axes.bar(t[i+1], array[i+1], color="blue", edgecolor="black")
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                time.sleep(self.project_speed)
                QApplication.processEvents()
            else:
                array[k] = right_array[j]
                j += 1
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[k], array[k], color="gray", edgecolor="black")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[j - 1], array[j - 1], color="red", edgecolor="black")
                self.autolabelSort(self.rects)
                # self.ui.MplSort.canvas.axes.bar(t[j+1], array[j+1], color="blue", edgecolor="black")
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                time.sleep(self.project_speed)
                QApplication.processEvents()

        self.ui.MplSort.canvas.axes.clear()
        self.ui.MplSort.canvas.axes.set_title("Merge Sort Animation", loc='left')
        self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
        self.autolabelSort(self.rects)
        self.ui.MplSort.canvas.draw()

    def SelectionSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                for i in range(len(self.unsorted_array)):
                    min = i
                    for j in range(i + 1, len(self.unsorted_array)):
                        if self.unsorted_array[min] > self.unsorted_array[j]:
                            min = j

                            self.ui.MplSort.canvas.axes.clear()
                            self.ui.MplSort.canvas.axes.set_title("Selection Sort Animation", loc='left')
                            self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                         edgecolor="#f0f8ff")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="blue",
                                                                         edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[min], self.unsorted_array[min],
                                                                         color="red", edgecolor="white")
                            self.autolabelSort(self.rects)
                            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort.canvas.draw()
                            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                            time.sleep(self.project_speed)
                            QApplication.processEvents()
                    self.operation_buttons()
                    self.unsorted_array[i], self.unsorted_array[min] = self.unsorted_array[min], \
                                                                       self.unsorted_array[i]

                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Selection Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                time.sleep(self.project_speed)
                QApplication.processEvents()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def CallQuickSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                array = self.unsorted_array
                self.QuickSort(array, 0, len(self.unsorted_array) - 1)
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")

                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def QuickSort(self, array, p, r):
        if p < r:
            q = self.partition(array, p, r)
            self.QuickSort(array, p, q - 1)
            self.QuickSort(array, q + 1, r)

    def partition(self, array, p, r):
        t = np.arange(len(self.unsorted_array))
        pivot_element = array[r]
        i = p - 1
        for j in range(p, r):
            if array[j] <= pivot_element:
                i += 1

                array[i], array[j] = array[j], array[i]
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.operation_buttons()
                self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="black",
                                                             edgecolor="black")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="blue",
                                                             edgecolor="black")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
                                                             edgecolor="black")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                time.sleep(self.project_speed)
                QApplication.processEvents()

            self.ui.MplSort.canvas.axes.clear()
            self.ui.MplSort.canvas.axes.set_title("Quick Sort Animation", loc='left')
            self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                         edgecolor="#f0f8ff")
            self.autolabelSort(self.rects)
            self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="blue",
                                                         edgecolor="black")
            self.autolabelSort(self.rects)
            self.rects = self.ui.MplSort.canvas.axes.bar(t[j + 1], self.unsorted_array[j + 1], color="black",
                                                         edgecolor="black")
            self.autolabelSort(self.rects)
            self.rects = self.ui.MplSort.canvas.axes.bar(t[r], self.unsorted_array[r], color="red",
                                                         edgecolor="black")
            self.autolabelSort(self.rects)
            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
            self.ui.MplSort.canvas.draw()
            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
            time.sleep(self.project_speed)
            QApplication.processEvents()
        array[i + 1], array[r] = array[r], array[i + 1]

        return i + 1

    def Heapify(self, array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[i] < array[left]:
            largest = left
        if right < n and array[largest] < array[right]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.Heapify(array, n, largest)

    def HeapSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                n = len(self.unsorted_array)
                for i in range(n // 2 - 1, -1, -1):
                    self.Heapify(self.unsorted_array, n, i)
                    self.ui.MplSort.canvas.axes.clear()
                    self.operation_buttons()
                    self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()

                for i in range(n - 1, 0, -1):
                    self.unsorted_array[i], self.unsorted_array[0] = self.unsorted_array[0], self.unsorted_array[i]
                    self.Heapify(self.unsorted_array, i, 0)
                    self.ui.MplSort.canvas.axes.clear()
                    self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()

                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Heap Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def CountingSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                max_value = int(max(self.unsorted_array))
                min_value = int(min(self.unsorted_array))
                range_of_elements = max_value - min_value + 1

                counting_temp_array = [0 for _ in range(range_of_elements)]
                sorted_array = [0 for _ in range(len(self.unsorted_array))]

                for i in range(0, len(self.unsorted_array)):
                    counting_temp_array[self.unsorted_array[i] - min_value] += 1

                for i in range(1, len(counting_temp_array)):
                    counting_temp_array[i] += counting_temp_array[i - 1]

                for i in range(len(self.unsorted_array) - 1, -1, -1):
                    sorted_array[counting_temp_array[self.unsorted_array[i] - min_value] - 1] = self.unsorted_array[
                        i]
                    counting_temp_array[self.unsorted_array[i] - min_value] -= 1
                    self.operation_buttons()

                for i in range(len(self.unsorted_array) - 1):
                    self.ui.MplSort.canvas.axes.clear()
                    self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="red",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()

                for i in range(0, len(self.unsorted_array)):
                    self.unsorted_array[i] = sorted_array[i]
                    self.ui.MplSort.canvas.axes.clear()
                    self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()

        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def BucketSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                max_value = max(self.unsorted_array)
                size = max_value / len(self.unsorted_array)

                buckets_list = []
                for x in range(len(self.unsorted_array)):
                    buckets_list.append([])

                for i in range(len(self.unsorted_array)):
                    j = int(self.unsorted_array[i] / size)
                    if j != len(self.unsorted_array):
                        buckets_list[j].append(self.unsorted_array[i])

                    else:
                        buckets_list[len(self.unsorted_array) - 1].append(self.unsorted_array[i])

                for z in range(len(self.unsorted_array)):
                    binarysearch.insertion_sort(buckets_list[z])

                final_output = []
                for x in range(len(self.unsorted_array)):
                    final_output = final_output + buckets_list[x]
                    self.operation_buttons()

                for i in range(len(self.unsorted_array) - 1):
                    self.ui.MplSort.canvas.axes.clear()
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="black",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()

                for i in range(0, len(self.unsorted_array)):
                    self.unsorted_array[i] = final_output[i]
                    self.ui.MplSort.canvas.axes.clear()
                    self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                 edgecolor="#f0f8ff")
                    self.autolabelSort(self.rects)
                    self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="gray",
                                                                 edgecolor="black")
                    self.autolabelSort(self.rects)
                    self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort.canvas.draw()
                    self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                    time.sleep(self.project_speed)
                    QApplication.processEvents()

                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def ShellSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                n = len(self.unsorted_array)
                gap = n // 2

                while gap > 0:
                    for i in range(gap, n):
                        temp = self.unsorted_array[i]
                        j = i
                        self.ui.MplSort.canvas.axes.clear()
                        self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
                        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                     edgecolor="#f0f8ff")
                        self.autolabelSort(self.rects)
                        self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="red",
                                                                     edgecolor="black")
                        self.autolabelSort(self.rects)
                        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                        self.ui.MplSort.canvas.draw()
                        self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                        time.sleep(self.project_speed)
                        QApplication.processEvents()
                        while j >= gap and self.unsorted_array[j - gap] > temp:
                            self.unsorted_array[j] = self.unsorted_array[j - gap]
                            self.ui.MplSort.canvas.axes.clear()
                            self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
                            self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                         edgecolor="#f0f8ff")
                            self.autolabelSort(self.rects)
                            self.rects = self.ui.MplSort.canvas.axes.bar(t[j], self.unsorted_array[j], color="blue",
                                                                         edgecolor="black")
                            self.autolabelSort(self.rects)
                            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort.canvas.draw()
                            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                            time.sleep(self.project_speed)
                            QApplication.processEvents()
                            j -= gap
                        self.unsorted_array[j] = temp
                    gap //= 2
                    self.operation_buttons()

                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Shell Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def countingSort(self, array, digit):
        count = []
        result_array = []
        j = len(array) - 1
        for i in range(10):
            count.append(0)
        for i in range(len(array)):
            result_array.append(0)
        for i in range(len(array)):
            count[(array[i] // digit) % 10] += 1
        for i in range(len(count)):
            if i > 0:
                count[i] += count[i - 1]
        for i in range(len(array)):
            count[(array[j] // digit) % 10] -= 1
            result_array[count[(array[j] // digit) % 10]] = array[j]
            j -= 1
            t = np.arange(len(result_array))
            self.ui.MplSort.canvas.axes.clear()
            self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
            self.rects = self.ui.MplSort.canvas.axes.bar(t, result_array, color='#56132a', edgecolor="#f0f8ff")
            self.autolabelSort(self.rects)
            self.rects = self.ui.MplSort.canvas.axes.bar(t[i], result_array[i], color="red", edgecolor="black")
            self.autolabelSort(self.rects)
            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
            self.ui.MplSort.canvas.draw()
            self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
            time.sleep(self.project_speed)
            QApplication.processEvents()
        for i in range(len(array)):
            array[i] = result_array[i]

    def RadixSort(self):
        try:
            if len(self.unsorted_array) == 0:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
            else:
                self.disable_button()
                t = np.arange(len(self.unsorted_array))
                max_number = max(self.unsorted_array)
                digit = 1
                while max_number // digit > 0:
                    self.countingSort(self.unsorted_array, digit)
                    digit *= 10
                    self.operation_buttons()
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Counting Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

        # %% Cocktail Sort Algorithm

    def CocktailSort(self):
        try:
            if len(self.unsorted_array) != 0:
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.disable_button()
                isSwapped = True
                start = 0
                end = len(self.unsorted_array) - 1
                while (isSwapped == True):
                    isSwapped = False
                    for i in range(start, end):
                        if (self.unsorted_array[i] > self.unsorted_array[i + 1]):
                            self.unsorted_array[i], self.unsorted_array[i + 1] = self.unsorted_array[i + 1], \
                                                                                 self.unsorted_array[i]
                            isSwapped = True
                        self.ui.MplSort.canvas.axes.clear()
                        self.ui.MplSort.canvas.axes.set_title("Cocktail Sort Animation", loc="left", color="white")
                        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                                     edgecolor="#f0f8ff")
                        self.autolabelSort(self.rects)
                        self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#800000",
                                                                     edgecolor="green")
                        self.autolabelSort(self.rects)
                        self.ui.MplSort.canvas.axes.patch.set_alpha(0)

                        self.ui.MplSort.canvas.draw()
                        self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                        time.sleep(self.project_speed)
                        QApplication.processEvents()
                    if (isSwapped == False):
                        break
                    isSwapped = False
                    end = end - 1

                    for i in range(end - 1, start - 1, -1):
                        if (self.unsorted_array[i] > self.unsorted_array[i + 1]):
                            self.unsorted_array[i], self.unsorted_array[i + 1] = self.unsorted_array[i + 1], \
                                                                                 self.unsorted_array[i]
                            isSwapped = True
                        self.ui.MplSort.canvas.axes.clear()
                        self.ui.MplSort.canvas.axes.set_title("Cocktail Sort Animation", loc="left", color="white")
                        self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color=['#583d72'],
                                                                     edgecolor='blue')
                        self.autolabelSort(self.rects)
                        self.rects = self.ui.MplSort.canvas.axes.bar(t[i], self.unsorted_array[i], color="#000080",
                                                                     edgecolor="green")
                        self.autolabelSort(self.rects)
                        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                        self.ui.MplSort.canvas.draw()
                        self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                        time.sleep(self.project_speed)
                        QApplication.processEvents()
                    start = start + 1
                self.ui.MplSort.canvas.axes.clear()
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()
            else:
                self.msg = QMessageBox.critical(self, "Error", "Please make an array!")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

        # %%Comb Sort Animation

    def CallCompSort(self):
        try:
            if len(self.unsorted_array) != 0:
                t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.disable_button()
                self.CombSort(self.unsorted_array)
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Comb Sort Animation", loc='left')
                self.rects = self.ui.MplSort.canvas.axes.bar(t, self.unsorted_array, color='#56132a',
                                                             edgecolor="#f0f8ff")

                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.enable_button()

        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!\nMake sure to set to Array Size and Range")
            self.enable_button()

    def CombSort(self, array):
        t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        gap = len(array)
        swaps = True
        while gap > 1 or swaps:
            gap = max(1, int(gap / 1.25))
            swaps = False
            for i in range(len(array) - gap):
                self.ui.MplSort.canvas.axes.clear()
                self.ui.MplSort.canvas.axes.set_title("Comb Sort Animation", loc="left", color="white")
                self.rects = self.ui.MplSort.canvas.axes.bar(t, array, color='#56132a', edgecolor="#f0f8ff")
                self.autolabelSort(self.rects)
                self.rects = self.ui.MplSort.canvas.axes.bar(t[i], array[i], color="#FFE4E1", edgecolor="black")
                self.autolabelSort(self.rects)
                self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort.canvas.draw()
                self.project_speed = 0.001 * (100 - self.ui.speedSlider.value())
                time.sleep(self.project_speed)
                QApplication.processEvents()
                j = i + gap
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
                    swaps = True

    def clearSorting(self):
        self.ui.displayarrays_sort.clear()
        self.lower = 0
        self.upper = 0
        self.length = 0
        self.ui.lower_range.clear()
        self.ui.upper_range.clear()
        self.ui.array_sort.setValue(0)
        self.unsorted_array = []
        self.ui.MplSort.canvas.axes.clear()
        self.ui.MplSort.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort.canvas.draw()

    # comparison Page Uİ
    def compare_all(self):
        all_methods = times.comparison([True, True, True, True, True, True, True, True, True, True])
        algorithms = ["Bubble", "Insertion", "Merge", "Selection", "Counting", "Heap", "Bucket", "Radix", "Quick",
                      "Shell"]
        methods_list = []
        for i in algorithms:
            methods_list.append(all_methods[i])

        colors_graph = ["#e60000", "#114477", "#223300", "#F1A1D8", "#BCF199", "#F9E16D", "#03F5DF", "#B303F5",
                        "#03F512", "#064564"]
        k = 0
        self.ui.MplSortComparison.canvas.axes.clear()
        for i in methods_list:
            self.ui.MplSortComparison.canvas.axes.plot([100, 300, 500, 2000], i, color=colors_graph[k], label=algorithms[k])
            self.ui.MplSortComparison.canvas.axes.legend(algorithms, loc="upper left")
            self.ui.MplSortComparison.canvas.draw()
            k += 1

    def compare_chosen(self):
        if not (self.method_list[0] or self.method_list[1] or self.method_list[2] or self.method_list[3] or
                self.method_list[4] or self.method_list[5] or self.method_list[6] or self.method_list[7] or
                self.method_list[8]):
            QMessageBox.critical(self, "ERROR", "Please choose a method/methods to compare...")
        else:

            algorithms = []
            algorithms_counter = 0
            if self.method_list[0]:
                algorithms.append("Bubble")
                algorithms_counter += 1
            if self.method_list[1]:
                algorithms.append("Insertion")
                algorithms_counter += 1
            if self.method_list[2]:
                algorithms.append("Merge")
                algorithms_counter += 1
            if self.method_list[3]:
                algorithms.append("Selection")
                algorithms_counter += 1
            if self.method_list[4]:
                algorithms.append("Counting")
                algorithms_counter += 1
            if self.method_list[5]:
                algorithms.append("Heap")
                algorithms_counter += 1
            if self.method_list[6]:
                algorithms.append("Bucket")
                algorithms_counter += 1
            if self.method_list[7]:
                algorithms.append("Radix")
                algorithms_counter += 1
            if self.method_list[8]:
                algorithms.append("Quick")
                algorithms_counter += 1
            if self.method_list[9]:
                algorithms.append("Shell")
                algorithms_counter += 1

            chosen_methods = times.comparison(self.method_list)
            methods_list = []
            for i in algorithms:
                methods_list.append(chosen_methods[i])

            colors_graph = ["#e60000", "#114477", "#223300", "#F1A1D8", "#BCF199", "#F9E16D", "#03F5DF", "#B303F5",
                            "#03F512"]
            k = 0
            self.ui.MplSortComparison.canvas.axes.clear()
            for i in methods_list:
                # self.ui.MplWidget_fibonacci.canvas.axes.clear()
                self.ui.MplSortComparison.canvas.axes.plot([100, 300, 500, 2000], i, color=colors_graph[k], label=algorithms[k])
                self.ui.MplSortComparison.canvas.axes.legend(algorithms, loc="upper left")
                self.ui.MplSortComparison.canvas.draw()
                k += 1

    def checkbox_toggled(self):

        if self.ui.bubblesort_checkBox.isChecked():
            self.method_list[0] = True
        else:
            self.method_list[0] = False
        if self.ui.insertionsort_checkBox.isChecked():
            self.method_list[1] = True
        else:
            self.method_list[1] = False
        if self.ui.mergesort_checkBox.isChecked():
            self.method_list[2] = True
        else:
            self.method_list[2] = False
        if self.ui.selectionsort_checkBox.isChecked():
            self.method_list[3] = True
        else:
            self.method_list[3] = False
        if self.ui.countingsort_checkBox.isChecked():
            self.method_list[4] = True
        else:
            self.method_list[4] = False
        if self.ui.heapsort_checkBox.isChecked():
            self.method_list[5] = True
        else:
            self.method_list[5] = False
        if self.ui.bucketsort_checkBox.isChecked():
            self.method_list[6] = True
        else:
            self.method_list[6] = False
        if self.ui.radixsort_checkBox.isChecked():
            self.method_list[7] = True
        else:
            self.method_list[7] = False
        if self.ui.quicksort_checkBox.isChecked():
            self.method_list[8] = True
        else:
            self.method_list[8] = False
        if self.ui.shellsort_checkBox.isChecked():
            self.method_list[9] = True
        else:
            self.method_list[9] = False

    def clearComparison(self):
        self.ui.bubblesort_checkBox.setChecked(False)
        self.ui.insertionsort_checkBox.setChecked(False)
        self.ui.mergesort_checkBox.setChecked(False)
        self.ui.selectionsort_checkBox.setChecked(False)
        self.ui.countingsort_checkBox.setChecked(False)
        self.ui.heapsort_checkBox.setChecked(False)
        self.ui.bucketsort_checkBox.setChecked(False)
        self.ui.radixsort_checkBox.setChecked(False)
        self.ui.quicksort_checkBox.setChecked(False)
        self.ui.shellsort_checkBox.setChecked(False)
        self.ui.MplSortComparison.canvas.axes.clear()
        self.ui.MplSortComparison.canvas.draw()

    # fibonacci Page UI
    def voiceFibo(self):
        r = sr.Recognizer()
        microphoneValue = ""
        with sr.Microphone() as source:
            try:
                self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                self.statusBar().showMessage('Stop talking...')
                print(microphoneValue)
                try:
                    if microphoneValue == 'find':
                        try:
                            self.fibo_number()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'Fibonacci spiral':
                        try:
                            self.spiral()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'clear':
                        try:
                            self.clearFibo()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'close':
                        try:
                            self.close()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    else:
                        QMessageBox.warning(self, "ERROR", "Try Again...")
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

    def error(self):
        self.n = int(self.ui.n_number.text())
        if self.n == 0:
            self.ui.MplFib.canvas.axes.clear()
            self.ui.MplFib.canvas.draw()
            self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")
        else:
            pass

    def fibo_number(self):
        try:
            # User input with line edit.
            self.n = int(self.ui.n_number.text())
            if self.n == 0:
                self.ui.MplFib.canvas.axes.clear()
                self.ui.MplFib.canvas.axes.patch.set_alpha(0)
                self.ui.MplFib.canvas.draw()
                self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")
            else:
                # Function of finding a fibonacci number sending this number to the function in
                # my project operations file the result appears on the screen.
                self.result = fibonacci.fibonacci_number(self.n)
                self.ui.result.setText("{}. Fibonacci Number is {}".format(str(self.n), str(self.result)))
                self.fibonacci_numbers = fibonacci.fibonacci_array(self.n)
                self.ui.fibonacci_series.setText(str(self.fibonacci_numbers))
        except ValueError:
            self.msg = QMessageBox.critical(self, "Error", "Please enter a positive integer!")

    def fibo_bar_graph(self):
        self.n = int(self.ui.n_number.text())
        if self.n == 0:
            self.ui.MplFib.canvas.axes.clear()
        # self.msg=QMessageBox.critical(self,"Error","Please enter a positive integer!")
        else:
            self.x = np.arange(1, self.n + 1)  # assigning x-axis numbers to the chart
            self.y = fibonacci.fibonacci_array(self.n)  # assigning fibonacci numbers to the y-axis of the chart
            self.x_pos = [i for i, _ in enumerate(self.x)]
            self.ui.MplFib.canvas.axes.clear()  # cleaning the graphic display before each drawing
            self.rects = self.ui.MplFib.canvas.axes.bar(self.x_pos, self.y, color='#56132a', edgecolor="#f0f8ff")
            self.autolabelFibo(self.rects)
            self.ui.MplFib.canvas.axes.patch.set_alpha(0)
            self.ui.MplFib.canvas.axes.set_title('Fibonacci Graph')
            self.ui.MplFib.canvas.draw()  # plotting the graph

    def autolabelFibo(self, rects):
        for rect in self.rects:
            height = rect.get_height()
            if height > 0:
                self.ui.MplFib.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                '%d' % int(height), ha='center', va='bottom')
            else:
                self.ui.MplFib.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                '%d' % int(height), ha='center', va='top')

    def clearFibo(self):
        self.ui.n_number.clear()
        self.ui.result.clear()
        self.ui.MplFib.canvas.axes.clear()
        self.ui.MplFib.canvas.axes.patch.set_alpha(0)
        self.ui.MplFib.canvas.draw()
        self.ui.fibonacci_series.clear()


    #binary search page UI

    def voiceBinary(self):
        r = sr.Recognizer()
        microphoneValue = ""
        with sr.Microphone() as source:
            try:
                self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                self.statusBar().showMessage('Stop talking...')
                try:
                    if microphoneValue == 'set default values':
                        try:
                            self.set_default_array()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")

                    elif microphoneValue == 'create array':
                        try:
                            self.create_array()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")

                    elif microphoneValue == 'sort':
                        try:
                            self.sortingarray()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'find index':
                        try:
                            self.find_number()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'clear':
                        try:
                            self.clearBinary()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'close':
                        try:
                            self.close()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    else:
                        QMessageBox.warning(self, "ERROR", "Try Again...")
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

    def set_default_array(self):
        self.lower = random.randint(-50, 0)
        self.ui.lower_range_binary.setText(str(self.lower))
        self.upper = random.randint(50, 300)
        self.ui.upper_range_binary.setText(str(self.upper))
        self.length = random.randint(10, 50)
        self.ui.display_arraylen.setText(str(self.length))
        self.ui.array_len.setValue(self.length)
        self.unsorted_array = binarySearch.createarray(self.lower, self.upper,
                                                       self.length)  # Calling the create array function from the project operations file
        self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
        self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        self.ui.disp_unsorted_array.setText(str(self.unsorted_array))  # Display on the interface
        self.ui.MplSort_binary.canvas.axes.clear()
        self.ui.MplSort_binary.canvas.axes.set_title("Unsorted Array")
        self.rects = self.ui.MplSort_binary.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2), edgecolor="blue")
        self.autolabelBinary(self.rects)
        self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort_binary.canvas.draw()

    def random_array(self):
        self.ui.disp_unsorted_array.setReadOnly(True)
        self.ui.array_len.setEnabled(True)
        self.ui.checkBox_4.setChecked(False)
        self.ui.lower_range_binary.setEnabled(True)
        self.ui.upper_range_binary.setEnabled(True)
        self.ui.set_default_values_binary.setEnabled(True)

    def array_yourself(self):
        self.ui.disp_unsorted_array.setReadOnly(False)
        self.ui.array_len.setEnabled(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.lower_range_binary.setEnabled(False)
        self.ui.upper_range_binary.setEnabled(False)
        self.ui.set_default_values_binary.setEnabled(False)
        self.clear()

    def valuelen(self):  # Function of array size value taken from dial to show next to line edit
        self.length_array = self.ui.array_len.value()
        self.ui.display_arraylen.setText(str(self.length_array))

    def autolabelBinary(self, rects):
        for rect in self.rects:
            height = rect.get_height()
            if height > 0:
                self.ui.MplSort_binary.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='bottom')
            else:
                self.ui.MplSort_binary.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='top')

    def create_array(self):
        if self.ui.checkBox_2.isChecked():  # function written to create an array
            try:
                try:
                    self.lower = int(self.ui.lower_range_binary.text())
                    self.upper = int(self.ui.upper_range_binary.text())
                    if (self.lower != 0 and self.upper != 0) or self.length_array != 0:
                        if self.lower < self.upper:
                            if abs(self.upper - self.lower) > self.length_array:
                                self.unsorted_array = binarySearch.createarray(self.lower, self.upper,
                                                                               self.length_array)  # Calling the create array function from the project operations file
                                self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
                                self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                                self.ui.disp_unsorted_array.setText(
                                    str(self.unsorted_array))  # Display on the interface
                                self.ui.MplSort_binary.canvas.axes.clear()
                                self.ui.MplSort_binary.canvas.axes.set_title("Unsorted Array")
                                self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.unsorted_array,
                                                                             color=(0.4, 0, 0.2), edgecolor="blue")
                                self.autolabelBinary(self.rects)
                                self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
                                self.ui.MplSort_binary.canvas.draw()
                            else:
                                self.msg = QMessageBox.critical(self, "Error",
                                                                "Array length should be less than the difference between upper range and lower range.!")
                        else:
                            self.msg = QMessageBox.critical(self, "Error",
                                                            "Upper range must be greater than lower range!")
                    else:
                        self.msg = QMessageBox.critical(self, "Error", "Please set the range and array size!")
                except ValueError:
                    self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields!")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error",
                                                "Please make the operations in order!")  # If the user presses another button without pressing this button, an error is given

        if self.ui.checkBox_4.isChecked():
            self.ui.disp_unsorted_array.setReadOnly(False)
            try:
                self.unsorted_array = self.ui.disp_unsorted_array.toPlainText().split(',')
                for i in range(len(self.unsorted_array)):
                    self.unsorted_array[i] = int(self.unsorted_array[i])
                self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.ui.disp_unsorted_array.setText(str(self.unsorted_array))  # Display on the interface
                self.ui.MplSort_binary.canvas.axes.clear()
                self.ui.MplSort_binary.canvas.axes.set_title("Unsorted Array")
                self.rects = self.ui.MplSort_binary.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2),
                                                             edgecolor="blue")
                self.autolabelBinary(self.rects)
                self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort_binary.canvas.draw()
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error",
                                                "Please enter an array as valid format!")  # If the user presses another button without pressing this button, an error is given
                self.ui.disp_unsorted_array.clear()
                self.unsorted_array = []

    def sortingarray(self):
        try:
            if len(self.unsorted_array) != 0:
                self.sorted_array = binarySearch.insertionSort(
                    self.unsorted_array)  # Calling the insertion sort function from the project operations file for sorting
                self.ui.disp_sorted_array.setText(str(self.sorted_array))  # Display on the interface
                self.ui.MplSort_binary.canvas.axes.clear()
                self.ui.MplSort_binary.canvas.axes.set_title("Sorted Array")
                self.rects = self.ui.MplSort_binary.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
                                                             edgecolor="blue")
                self.autolabelBinary(self.rects)
                self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort_binary.canvas.draw()
            else:
                self.msg = QMessageBox.information(self, "Error", "Please create an array...")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error",
                                            "Please make the operations in order!")  # If the user presses another button without pressing this button, an error is given
            self.ui.disp_sorted_array.clear()

    def find_number(self):
        try:
            if len(self.sorted_array) != 0:
                self.number = int(self.ui.take_number.text())  # getting the desired number from the user
                if np.isin(self.number, self.sorted_array):  # Checking whether the desired number is in the array
                    begin_index = 0
                    end_index = len(self.sorted_array) - 1
                    while True:
                        midpoint = begin_index + (end_index - begin_index) // 2
                        # if begin_index>end_index:
                        #     self.ui.lineEdit_answer.setText("None")
                        #     break

                        if self.sorted_array[midpoint] == self.number:
                            self.ui.MplSort.canvas.axes.clear()
                            self.rects = self.ui.MplSort.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
                                                                         edgecolor=(0, .9, .9))
                            self.autolabelBinary(self.rects)
                            self.ui.MplSort.canvas.axes.bar(self.t[midpoint], self.sorted_array[midpoint], color="red",
                                                            edgecolor=(0, .9, .9))
                            self.ui.MplSort.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort.canvas.draw()
                            self.ui.result_edit.setText("Element {} found at index '{}'.".format(str(self.number),
                                                                                                 str(midpoint + 1)))  # Display of result
                            break

                        else:

                            self.ui.MplSort_binary.canvas.axes.bar(self.t[midpoint], self.sorted_array[midpoint], color="blue",
                                                            edgecolor=(0, .9, .9))
                            self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
                            self.ui.MplSort_binary.canvas.draw()
                            QApplication.processEvents()
                            time.sleep(1)
                        if self.sorted_array[midpoint] > self.number:
                            end_index = midpoint - 1
                        if self.sorted_array[midpoint] < self.number:
                            begin_index = midpoint + 1
                else:
                    self.msg3 = QMessageBox.information(self, "Error",
                                                        "Please enter a sorted array elements...")  # give an error if the requested number is not in the array
                    self.ui.MplSort_binary.canvas.axes.clear()
                    self.ui.MplSort_binary.canvas.axes.set_title("Sorted Array")
                    self.rects = self.ui.MplSort_binary.canvas.axes.bar(self.t, self.sorted_array, color=(0.4, 0, 0.2),
                                                                 edgecolor="black")
                    self.autolabelBinary(self.rects)
                    self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
                    self.ui.MplSort_binary.canvas.draw()
                    self.ui.take_number.clear()  # cleaning the section where the user entered numbers
                    self.ui.result_edit.clear()
            else:
                self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")
                self.ui.take_number.clear()
        except ValueError:
            self.msg = QMessageBox.information(self, "Error",
                                               "Please enter a valid number...")  # error if user enters anything other than number
            self.ui.take_number.clear()  # cleaning the section where the user entered numbers
        except AttributeError:
            self.msg = QMessageBox.information(self, "Error", "Please create an array...")

    def clearBinary(self):
        self.lower = 0
        self.upper = 0
        self.length_array = 0
        self.unsorted_array = []
        self.sorted_array = []
        self.ui.MplSort_binary.canvas.axes.clear()
        self.ui.MplSort_binary.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort_binary.canvas.draw()
        self.ui.lower_range_binary.clear()
        self.ui.upper_range_binary.clear()
        self.ui.display_arraylen.clear()
        self.ui.disp_unsorted_array.clear()
        self.ui.disp_sorted_array.clear()
        self.ui.take_number.clear()
        self.ui.result_edit.clear()
        self.ui.array_len.setValue(0)

    #matrix page UI
    def voiceMatrix(self):
        r = sr.Recognizer()
        microphoneValue = ""
        with sr.Microphone() as source:
            try:
                self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                self.statusBar().showMessage('Stop talking...')
                print(microphoneValue)
                try:
                    if microphoneValue == 'random Matrix':
                        try:
                            self.random_matrices()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'multiply':
                        try:
                            self.multiplication()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'clear':
                        try:
                            self.clearMatrix()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'close':
                        try:
                            self.close()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'create Matrix one':
                        try:
                            self.matrix1_user()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'create Matrix two':
                        try:
                            self.matrix2_user()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")

                    elif self.ui.determinant_btn_1.isVisible():
                        if microphoneValue == 'determinant Matrix 1':
                            try:
                                self.determinant1()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")

                        elif microphoneValue == 'inverse Matrix one':
                            try:
                                self.inverse1()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'transpose Matrix one':
                            try:
                                self.transpose1()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'rank Matrix one':
                            try:
                                self.rank1()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'multiply Matrix one':
                            try:
                                self.mult_scalar1()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        else:
                            QMessageBox.warning(self, "ERROR", "Try Again...")

                    elif self.ui.determinant_btn_2.isVisible:
                        if microphoneValue == 'determinant Matrix two':
                            try:
                                self.determinant2()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'inverse Matrix two':
                            try:
                                self.inverse2()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'transpose Matrix two':
                            try:
                                self.transpose2()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'rank Matrix two':
                            try:
                                self.rank2()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        elif microphoneValue == 'multiply Matrix two':
                            try:
                                self.mult_scalar2()
                                microphoneValue = ""
                            except:
                                QMessageBox.warning(self, "ERROR", "Try Again...")
                        else:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    else:
                        QMessageBox.warning(self, "ERROR", "Try Again...")

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

    def inputs(self):
        if self.ui.row_m1.text() != '' or self.ui.column_m1.text() != '':
            try:
                # Getting row number of first matrix from line edit
                self.number_of_rows_matrix1 = int(self.ui.row_m1.text())
                # Getting column number of first matrix from line edit
                self.number_of_columns_matrix1 = int(self.ui.column_m1.text())
                self.matrix1 = [(i, j) for i in range(int(self.ui.column_m1.text())) for j in
                                range(int(self.ui.row_m1.text()))]
            except ValueError:
                pass
        if self.ui.row_m2.text() != '' or self.ui.column_m2.text() != '':
            try:
                self.number_of_rows_matrix2 = int(self.ui.row_m2.text())
                # §self.ui.row_m2.setText(str(int(self.ui.column_m1.text()))) #the number of rows of the second
                # matrix appears as the number of columns of the first according to the matrix multiplication rule

                # Getting row number of first matrix from line edit
                self.number_of_columns_matrix2 = int(self.ui.column_m2.text())
                self.matrix2 = [(i, j) for i in range(int(self.ui.column_m2.text())) for j in
                                range(int(self.ui.row_m2.text()))]
            except ValueError:
                pass

    def visible1_false(self):
        self.ui.label_6.setVisible(False)
        self.ui.line.setVisible(False)
        self.ui.determinant_btn_1.setVisible(False)
        self.ui.display_det_1.setVisible(False)
        self.ui.inverse_btn_1.setVisible(False)
        self.ui.transpose_btn_1.setVisible(False)
        self.ui.rank_btn_1.setVisible(False)
        self.ui.multiplyby_btn.setVisible(False)
        self.ui.takenumbermult_1.setVisible(False)
        self.ui.rank_1.setVisible(False)

    def visible1_true(self):
        self.ui.label_6.setVisible(True)
        self.ui.line.setVisible(True)
        self.ui.determinant_btn_1.setVisible(True)
        self.ui.display_det_1.setVisible(True)
        self.ui.inverse_btn_1.setVisible(True)
        self.ui.transpose_btn_1.setVisible(True)
        self.ui.rank_btn_1.setVisible(True)
        self.ui.multiplyby_btn.setVisible(True)
        self.ui.takenumbermult_1.setVisible(True)
        self.ui.rank_1.setVisible(True)

    def visible2_false(self):
        self.ui.label_7.setVisible(False)
        self.ui.line_2.setVisible(False)
        self.ui.determinant_btn_2.setVisible(False)
        self.ui.inverse_btn_2.setVisible(False)
        self.ui.transpose_btn_2.setVisible(False)
        self.ui.rank_btn_2.setVisible(False)
        self.ui.multiplyby_btn_2.setVisible(False)
        self.ui.takenumbermult_2.setVisible(False)
        self.ui.rank_2.setVisible(False)
        self.ui.display_det_2.setVisible(False)

    def visible2_true(self):
        self.ui.label_7.setVisible(True)
        self.ui.line_2.setVisible(True)
        self.ui.determinant_btn_2.setVisible(True)
        self.ui.inverse_btn_2.setVisible(True)
        self.ui.transpose_btn_2.setVisible(True)
        self.ui.rank_btn_2.setVisible(True)
        self.ui.multiplyby_btn_2.setVisible(True)
        self.ui.takenumbermult_2.setVisible(True)
        self.ui.rank_2.setVisible(True)
        self.ui.display_det_2.setVisible(True)

    def random_matrices(self):
        self.visible1_false()
        self.visible2_false()
        if self.ui.row_m1.text() == '' and self.ui.column_m1.text() == '' and self.ui.row_m2.text() == '' and self.ui.column_m2.text() == '':
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
        else:
            try:
                # setting the row number of the first table as the number of rows received
                self.ui.Matrix_1.setRowCount(int(self.ui.row_m1.text()))
                # setting the column number of the first table as the number of columns received
                self.ui.Matrix_1.setColumnCount(int(self.ui.column_m1.text()))
                # Creating random matrices with the help of a function I called in another file
                self.matrices = create_matrix.randommatrix(int(self.ui.row_m1.text()), int(self.ui.column_m1.text()),
                                                           int(self.ui.row_m2.text()), int(self.ui.column_m2.text()))
                # Determining the matrix at index 0 as the first matrix among the matrices in the list returned from
                # the function I wrote
                self.matrix1 = self.matrices[0]

                for i, row_1 in enumerate(
                        self.matrix1):  # Placing the first random matrix created using the enumerate function into the first table
                    for j, val in enumerate(row_1):
                        newItem1 = QtWidgets.QTableWidgetItem(str(val))
                        newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                        self.ui.Matrix_1.setItem(i, j, newItem1)

                # setting the number of rows of the second matrix as the number of columns of the first matrix
                self.ui.Matrix_2.setRowCount(int(self.ui.row_m2.text()))
                # setting the column number of the second table as the number of columns received
                self.ui.Matrix_2.setColumnCount(int(self.ui.column_m2.text()))
                # Determining the matrix at index 1 as the first matrix among the matrices in the list returned from
                # the function I wrote
                self.matrix2 = self.matrices[1]
                for i in range(int(self.ui.column_m1.text())):
                    self.ui.Matrix_1.setColumnWidth(i, 500 / int(self.ui.column_m1.text()))

                for i in range(int(self.ui.row_m1.text())):  # set the row of first matrix height to 50 px
                    self.ui.Matrix_1.setRowHeight(i, 300 / int(self.ui.row_m1.text()))

                for i in range(int(self.ui.column_m2.text())):
                    self.ui.Matrix_2.setColumnWidth(i, 500 / int(self.ui.column_m2.text()))

                for i in range(int(self.ui.row_m2.text())):  # set the row of second matrix height to 50 px
                    self.ui.Matrix_2.setRowHeight(i, 300 / int(self.ui.row_m2.text()))

                for k, row_2 in enumerate(
                        self.matrix2):  # Placing the second random matrix created using the enumerate function into the second table
                    for l, value in enumerate(row_2):
                        newItem2 = QtWidgets.QTableWidgetItem(str(value))
                        newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                        self.ui.Matrix_2.setItem(k, l, newItem2)
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def matrix1_user(self):
        self.ui.Matrix_1.clear()  # cleaning the table of first matrix
        if self.ui.row_m1.text() == '' or self.ui.column_m1.text() == '':
            # if self.ui.row_m1.text()=='' or self.ui.column_m1.text()=='' and self.ui.row_m2.text()=='' or
            # self.ui.column_m2.text()=='':
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
        else:
            try:
                self.visible1_true()
                # setting the row number of the first table as the number of rows received
                self.ui.Matrix_1.setRowCount(int(self.ui.row_m1.text()))
                # setting the column number of the first table as the number of columns received
                self.ui.Matrix_1.setColumnCount(int(self.ui.column_m1.text()))
                for i in range(int(self.ui.column_m1.text())):
                    self.ui.Matrix_1.setColumnWidth(i, 500 / int(self.ui.column_m1.text()))

                for i in range(int(self.ui.row_m1.text())):  # set the row of first matrix height to 50 px
                    self.ui.Matrix_1.setRowHeight(i, 300 / int(self.ui.row_m1.text()))
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def matrix2_user(self):
        self.ui.Matrix_2.clear()  # cleaning the table of second matrix
        if self.ui.row_m2.text() == '' or self.ui.column_m2.text() == '':
            # if self.ui.row_m1.text()=='' or self.ui.column_m1.text()=='' and self.ui.row_m2.text()=='' or
            # self.ui.column_m2.text()=='':
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
        else:
            try:
                self.visible2_true()
                self.ui.Matrix_2.setRowCount(
                    int(self.ui.row_m2.text()))  # setting the number of rows of the second matrix as the number of columns of the first matrix
                self.ui.Matrix_2.setColumnCount(
                    int(self.ui.column_m2.text()))  # setting the column number of the second table as the number of columns received
                for i in range(int(self.ui.column_m2.text())):
                    self.ui.Matrix_2.setColumnWidth(i, 500 / int(self.ui.column_m2.text()))

                for i in range(int(self.ui.row_m2.text())):  # set the row of second matrix height to 50 px
                    self.ui.Matrix_2.setRowHeight(i, 300 / int(self.ui.row_m2.text()))

            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def determinant1(self):
        self.matrix1 = [[(i, j) for i in range(int(self.ui.column_m1.text()))] for j in
                        range(int(self.ui.row_m1.text()))]
        if self.ui.row_m1.text() != self.ui.column_m1.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!"
                                            "\nPlease check your first matrix row count and column count......")
        else:
            try:
                for i in range(len(self.matrix1)):
                    for j in range(len(self.matrix1[0])):
                        self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())

                print(self.matrix1)
                self.matrix1 = np.asarray(self.matrix1)
                self.det = np.linalg.det(self.matrix1)
                self.ui.display_det_1.setText(str(math.ceil(self.det)))
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def determinant2(self):
        self.matrix2 = [[(i, j) for i in range(int(self.ui.column_m2.text()))] for j in
                        range(int(self.ui.row_m2.text()))]
        if self.ui.row_m2.text() != self.ui.column_m2.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!"
                                            "\nPlease check your second matrix row count and column count...")
        else:
            try:
                for i in range(len(self.matrix2)):
                    for j in range(len(self.matrix2[0])):
                        self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
                self.matrix2 = np.asarray(self.matrix2)
                self.det2 = np.linalg.det(self.matrix2)
                print("determinant")
                print(self.det)
                self.ui.display_det_2.setText(str(math.ceil(self.det2)))
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def inverse1(self):
        if self.ui.row_m1.text() != self.ui.column_m1.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
        else:
            try:
                for i in range(len(self.matrix1)):
                    for j in range(len(self.matrix1[0])):
                        self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
                self.matrix1 = np.asarray(self.matrix1)
                self.det = np.linalg.det(self.matrix1)
                if self.det != 0:
                    self.matrix1 = np.asarray(self.matrix1)
                    self.inverse_1 = np.linalg.inv(self.matrix1)
                    for i, row_1 in enumerate(
                            self.inverse_1):  # Placing the first random matrix created using the enumerate function into the first table
                        for j, val in enumerate(row_1):
                            newItem1 = QtWidgets.QTableWidgetItem(str(val))
                            newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.ui.Matrix_1.setItem(i, j, newItem1)

                else:
                    self.msg = QMessageBox.critical(self, "Error",
                                                    "For inverse matrix, determinant must be non-zero...")
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def inverse2(self):
        if self.ui.row_m2.text() != self.ui.column_m2.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
        else:
            try:
                for i in range(len(self.matrix2)):
                    for j in range(len(self.matrix2[0])):
                        self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
                self.matrix2 = np.asarray(self.matrix2)
                self.det = np.linalg.det(self.matrix2)
                if self.det != 0:
                    self.matrix2 = np.asarray(self.matrix2)
                    self.inverse_2 = np.linalg.inv(self.matrix2)
                    for k, row_2 in enumerate(
                            self.inverse_2):  # Placing the second random matrix created using the enumerate function into the second table
                        for l, value in enumerate(row_2):
                            newItem2 = QtWidgets.QTableWidgetItem(str(value))
                            newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.ui.Matrix_2.setItem(k, l, newItem2)

                else:
                    self.msg = QMessageBox.critical(self, "Error",
                                                    "For inverse matrix, determinant must be non-zero...")
            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def transpose1(self):
        try:
            for i in range(len(self.matrix1)):
                for j in range(len(self.matrix1[0])):
                    self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
            self.matrix1 = np.asarray(self.matrix1)
            self.matrix1 = self.matrix1.transpose()
            rows = len(self.matrix1)
            columns = len(self.matrix1[0])
            self.ui.Matrix_1.setRowCount(len(self.matrix1))  # cleaning the row value of table of first matrix
            self.ui.Matrix_1.setColumnCount(len(self.matrix1[0]))  # cleaning the column value of table of first matrix
            for i in range(columns):
                self.ui.Matrix_1.setColumnWidth(i, 500 / columns)
            for i in range(rows):  # set the row of second matrix height to 50 px
                self.ui.Matrix_1.setRowHeight(i, 300 / rows)
            for i, row_1 in enumerate(
                    self.matrix1):  # Placing the first random matrix created using the enumerate function into the first table
                for j, val in enumerate(row_1):
                    newItem1 = QtWidgets.QTableWidgetItem(str(val))
                    newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.Matrix_1.setItem(i, j, newItem1)

        except ValueError:
            self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def transpose2(self):
        try:
            for i in range(len(self.matrix2)):
                for j in range(len(self.matrix2[0])):
                    self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
            self.matrix2 = np.asarray(self.matrix2)
            self.matrix2 = self.matrix2.transpose()
            rows = len(self.matrix2)
            columns = len(self.matrix2[0])
            self.ui.Matrix_2.setRowCount(len(self.matrix2))  # cleaning the row value of table of first matrix
            self.ui.Matrix_2.setColumnCount(len(self.matrix2[0]))  # cleaning the column value of table of first matrix
            for i in range(columns):
                self.ui.Matrix_2.setColumnWidth(i, 500 / columns)

            for i in range(rows):  # set the row of second matrix height to 50 px
                self.ui.Matrix_2.setRowHeight(i, 300 / rows)
            for k, row_2 in enumerate(
                    self.matrix2):  # Placing the second random matrix created using the enumerate function into the second table
                for l, value in enumerate(row_2):
                    newItem2 = QtWidgets.QTableWidgetItem(str(value))
                    newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.Matrix_2.setItem(k, l, newItem2)

        except ValueError:
            self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def rank1(self):
        if self.ui.row_m1.text() != self.ui.column_m1.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!\nPlease check your first "
                                            "matrix row count and column count......")
        else:
            try:
                for i in range(len(self.matrix1)):
                    for j in range(len(self.matrix1[0])):
                        self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
                self.matrix1 = np.asarray(self.matrix1)
                self.det = np.linalg.det(self.matrix1)
                if self.det != 0:
                    self.matrix1 = np.asarray(self.matrix1)
                    self.rank_1 = np.linalg.matrix_rank(self.matrix1)
                    self.ui.rank_1.setText(str(self.rank_1))
                else:
                    self.msg = QMessageBox.critical(self, "Error", "The determinant must be non-zero...")

            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def rank2(self):
        if self.ui.row_m2.text() != self.ui.column_m2.text():
            self.msg = QMessageBox.critical(self, "Error",
                                            "Last 2 dimensions of the array must be square!\nPlease check your first matrix row count and column count......")
        else:
            try:
                for i in range(len(self.matrix2)):
                    for j in range(len(self.matrix2[0])):
                        self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
                self.matrix2 = np.asarray(self.matrix2)
                self.det = np.linalg.det(self.matrix2)
                if self.det != 0:
                    self.matrix2 = np.asarray(self.matrix2)
                    self.rank_2 = np.linalg.matrix_rank(self.matrix2)
                    self.ui.rank_2.setText(str(self.rank_2))
                else:
                    self.msg = QMessageBox.critical(self, "Error", "The determinant must be non-zero...")

            except ValueError:
                self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
            except AttributeError:
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def mult_scalar1(self):
        try:
            if self.ui.takenumbermult_1.text() == '':
                self.msg = QMessageBox.critical(self, "Error", "Please enter a scalar number...")
                self.ui.takenumbermult_1.setStyleSheet("background-color: rgb(255,0,0);\n"
                                                       "border-radius: 10px ;\n"
                                                       "border-width: 3px;\n"
                                                       "border-color: rgb(170,74,48);")
                time.sleep(5)
                self.ui.takenumbermult_1.setStyleSheet("background-color: rgb(255, 212, 169);\n"
                                                       "border-radius: 10px ;\n"
                                                       "border-width: 3px;\n"
                                                       "border-color: rgb(170,74,48);")
            else:
                scalar = int(self.ui.takenumbermult_1.text())
                for i in range(len(self.matrix1)):
                    for j in range(len(self.matrix1[0])):
                        self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
                self.matrix1 = np.asarray(self.matrix1)
                self.new_matrix1 = scalar * self.matrix1
                for k, row_1 in enumerate(
                        self.new_matrix1):  # Placing the second random matrix created using the enumerate function into the second table
                    for l, value in enumerate(row_1):
                        newItem1 = QtWidgets.QTableWidgetItem(str(value))
                        newItem1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                        self.ui.Matrix_1.setItem(k, l, newItem1)

        except ValueError:
            self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def mult_scalar2(self):
        try:
            if self.ui.takenumbermult_1.text() == '':
                self.msg = QMessageBox.critical(self, "Error", "Please enter a scalar number...")
            else:
                scalar = int(self.ui.takenumbermult_2.text())
                for i in range(len(self.matrix2)):
                    for j in range(len(self.matrix2[0])):
                        self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
                self.matrix2 = np.asarray(self.matrix2)
                self.new_matrix2 = scalar * self.matrix2
                for k, row_2 in enumerate(
                        self.new_matrix2):  # Placing the second random matrix created using the enumerate function into the second table
                    for l, value in enumerate(row_2):
                        newItem2 = QtWidgets.QTableWidgetItem(str(value))
                        newItem2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                        self.ui.Matrix_2.setItem(k, l, newItem2)

        except ValueError:
            self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
        except AttributeError:
            self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def multiplication(self):
        if self.ui.column_m1.text() != self.ui.row_m2.text():
            self.msg = QMessageBox.critical(self, "Error", "Dimensions not same...")
        else:
            if self.ui.row_m1.text() == '' and self.ui.column_m1.text() == '' and self.ui.row_m2.text() == '' and self.ui.column_m2.text() == '':
                self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")
            else:
                try:
                    for i in range(len(self.matrix1)):
                        for j in range(len(self.matrix1[0])):
                            self.matrix1[i][j] = float(self.ui.Matrix_1.item(i, j).text())
                    for i in range(len(self.matrix2)):
                        for j in range(len(self.matrix2[0])):
                            self.matrix2[i][j] = float(self.ui.Matrix_2.item(i, j).text())
                    # Calling the matrix multiplication function I wrote and performing the operation
                    self.result_matrix = matrix_mult.multiplication(self.matrix1, self.matrix2)
                    self.ui.resultmatrix.setRowCount(
                        len(self.result_matrix))  # setting the number of rows of the table where the result matrix will appear
                    self.ui.resultmatrix.setColumnCount(len(self.result_matrix[
                                                                0]))  # setting the number of columns of the table where the result matrix will appear

                    for i in range(
                            len(self.result_matrix[0])):  # change the column width value of the table for result matrix
                        self.ui.resultmatrix.setColumnWidth(i, 500 / len(self.result_matrix[0]))
                    for i in range(len(self.result_matrix)):
                        # change the column width value of the table for result matrix
                        self.ui.resultmatrix.setRowHeight(i, 300 / len(self.result_matrix))
                    # Placing returned from multiplication function using the enumerate function into the result table
                    for i, row in enumerate(self.result_matrix):
                        for j, val in enumerate(row):
                            newItem3 = QtWidgets.QTableWidgetItem(str(val))
                            newItem3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                            self.ui.resultmatrix.setItem(i, j, newItem3)

                except ValueError:
                    self.msg = QMessageBox.critical(self, "Error", "Error.Only integer please...")
                except AttributeError:
                    self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields...")

    def clearMatrix(self):
        self.matrix1_current = 0
        self.matrix2_current = 0
        self.visible1_false()
        self.visible2_false()
        self.matrix1 = []
        self.matrix2 = []
        self.result_matrix = []

        # Cleaning the table of matrices.
        self.ui.Matrix_1.clear()
        self.ui.Matrix_2.clear()
        self.ui.resultmatrix.clear()
        # Cleaning the column&row value of table of matrices.
        self.ui.Matrix_1.setRowCount(0)
        self.ui.Matrix_1.setColumnCount(0)
        self.ui.Matrix_2.setRowCount(0)
        self.ui.Matrix_2.setColumnCount(0)
        self.ui.resultmatrix.setRowCount(0)
        self.ui.resultmatrix.setColumnCount(0)
        # Clear all row and columns.
        self.ui.row_m1.clear()
        self.ui.column_m1.clear()
        self.ui.row_m2.clear()
        self.ui.column_m2.clear()

    #Random page UI
    def voiceRandom(self):
        r = sr.Recognizer()
        microphoneValue = ""
        with sr.Microphone() as source:
            try:
                self.statusBar().showMessage('Start talking...')
                audio = r.listen(source)
                microphoneValue = (r.recognize_google(audio))
                self.statusBar().showMessage('Stop talking...')
                try:
                    if microphoneValue == 'set default values':
                        try:
                            self.set_default_array_random()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")


                    elif microphoneValue == 'create array':
                        try:
                            self.create_array_random()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")

                    elif microphoneValue == 'find':
                        try:
                            self.find_number_random()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'clear':
                        try:
                            self.clearRandom()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    elif microphoneValue == 'close':
                        try:
                            self.close()
                            microphoneValue = ""
                        except:
                            QMessageBox.warning(self, "ERROR", "Try Again...")
                    else:
                        QMessageBox.warning(self, "ERROR", "Try Again...")
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

    def set_default_array_random(self):
        self.lowerR = random.randint(-50, 0)
        self.ui.lower_range_2.setText(str(self.lowerR))
        self.upperR = random.randint(50, 300)
        self.ui.upper_range_2.setText(str(self.upperR))
        self.lengthR = random.randint(10, 50)
        self.ui.display_arraylen_2.setText(str(self.lengthR))
        self.ui.array_len_2.setValue(self.lengthR)
        # Calling the create array function from the project operations file
        self.unsorted_array = random_select.createarray(self.lowerR, self.upperR, self.lengthR)
        self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
        self.sorting_array_random()
        self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
        # Display on the interface
        self.ui.disp_unsorted_array_2.setText(str(self.unsorted_array))
        self.ui.MplSort_random.canvas.axes.clear()
        self.ui.MplSort_random.canvas.axes.set_title("Unsorted Array")
        self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2),
                                                      edgecolor="blue")
        self.autolabelRandom(self.rectsR)
        self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort_random.canvas.draw()

    def random_array_random(self):
        self.ui.disp_unsorted_array_2.setReadOnly(True)
        self.ui.array_len_2.setEnabled(True)
        self.ui.create_array_checkbox.setChecked(False)
        self.ui.lower_range_2.setEnabled(True)
        self.ui.upper_range_2.setEnabled(True)
        self.ui.set_default_values_2.setEnabled(True)

    def array_yourself_random(self):
        self.ui.disp_unsorted_array_2.setReadOnly(False)
        self.ui.array_len_2.setEnabled(False)
        self.ui.random_array_checkbox.setChecked(False)
        self.ui.lower_range_2.setEnabled(False)
        self.ui.upper_range_2.setEnabled(False)
        self.ui.set_default_values_2.setEnabled(False)
        self.clear()

    # Function of array size value taken from dial to show next to line edit
    def value_len_random(self):
        self.lengthR = self.ui.array_len.value()
        self.ui.display_arraylen_2.setText(str(self.lengthR))

    # Function to write number values to a bar chart.
    def autolabelRandom(self, rects):
        for rect in self.rectsR:
            height = rect.get_height()
            if height > 0:
                self.ui.MplSort_random.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='bottom')
            else:
                self.ui.MplSort_random.canvas.axes.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                                 '%d' % int(height), ha='center', va='top')

    # %% Creating a random array and display it on the screen
    def create_array_random(self):
        if self.ui.random_array_checkbox.isChecked():  # function written to create an array
            try:
                try:
                    self.lowerR = int(self.ui.lower_range_2.text())
                    self.upperR = int(self.ui.upper_range_2.text())
                    if (self.lowerR != 0 and self.upperR != 0) or self.lengthR != 0:
                        if self.lowerR < self.upperR:
                            if abs(self.upperR - self.lowerR) > self.lengthR:
                                # Calling the create array function from the project operations file
                                self.unsorted_array = random_select.createarray(self.lowerR, self.upperR, self.lengthR)
                                self.unsorted_array = random.sample(self.unsorted_array, len(self.unsorted_array))
                                self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                                self.ui.disp_unsorted_array_2.setText(
                                    str(self.unsorted_array))  # Display on the interface
                                self.ui.MplSort_random.canvas.axes.clear()
                                self.ui.MplSort_random.canvas.axes.set_title("Unsorted Array")
                                self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.t, self.unsorted_array,
                                                                              color='orange', edgecolor="blue")
                                self.autolabelRandom(self.rectsR)
                                self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
                                self.ui.MplSort_random.canvas.draw()
                            else:
                                self.msg = QMessageBox.critical(self, "Error",
                                                                "Array length should be less than the difference between upper range and lower range.!")
                        else:
                            self.msg = QMessageBox.critical(self, "Error",
                                                            "Upper range must be greater than lower range!")
                    else:
                        self.msg = QMessageBox.critical(self, "Error", "Please set the range and array size!")
                except ValueError:
                    self.msg = QMessageBox.critical(self, "Error", "Please fill in the required fields!")
            except AttributeError:
                # If the user presses another button without pressing this button, an error is given
                self.msg = QMessageBox.critical(self, "Error",
                                                "Please make the operations in order!")

        if self.ui.create_array_checkbox.isChecked():
            self.ui.disp_unsorted_array_2.setReadOnly(False)
            try:
                self.unsorted_array = self.ui.disp_unsorted_array_2.toPlainText().split(',')
                for i in range(len(self.unsorted_array)):
                    self.unsorted_array[i] = int(self.unsorted_array[i])
                self.t = np.linspace(1, len(self.unsorted_array), len(self.unsorted_array))
                self.ui.disp_unsorted_array.setText(str(self.unsorted_array))  # Display on the interface
                self.ui.MplSort_random.canvas.axes.clear()
                self.ui.MplSort_random.canvas.axes.set_title("Unsorted Array")
                self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.t, self.unsorted_array, color=(0.4, 0, 0.2),
                                                              edgecolor="blue")
                self.autolabelRandom(self.rectsR)
                self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
                self.ui.MplSort_random.canvas.draw()
            except ValueError:
                # If the user presses another button without pressing this button, an error is given
                self.msg = QMessageBox.critical(self, "Error", "Please enter an array as valid format!")
                self.ui.disp_unsorted_array.clear()
                self.unsorted_array = []

    # %%Sorting a random array and display on the screen
    def sorting_array_random(self):
        if len(self.unsorted_array) != 0:
            temp_array1 = tuple(self.unsorted_array)
            temp_array1 = list(temp_array1)
            # Calling the insertion sort function from the project operations file for sorting
            self.sorted_arrayR = random_select.insertionSort(temp_array1)
            # Display on the interface
            self.ui.disp_sorted_array_2.setText(str(self.sorted_arrayR))
        # self.t = np.lin-space(1, len(self.unsorted_array), len(self.unsorted_array))
        # self.ui.MplSort_random.canvas.axes.clear()
        # self.ui.MplSort_random.canvas.axes.set_title("Sorted Array")
        # self.rects=self.ui.MplSort_random.canvas.axes.bar(self.t, self.sorted_array, color="orange", edge color="black")
        # self.autolabel(self.rects)
        # self.ui.MplSort_random.canvas.draw()
        else:
            pass

    # %%Finding the index of the searched number and display on the screen
    def find_number_random(self):
        try:
            if len(self.sorted_arrayR) != 0:
                self.numberR = int(self.ui.take_number.text())  # Getting the desired number from the user.
                if self.numberR <= len(self.unsorted_array):  # Checking whether the desired number is in the array.
                    # Calling the binary search function from the project operations file for search.
                    self.smallestR = self.randomized_select_random(self.unsorted_array, 0, len(self.sorted_arrayR) - 1,
                                                                   self.numberR)
                    # Display of result.
                    self.ui.result_edit_2.setText(
                        "{}. smallest array is '{}'.".format(str(self.numberR), str(self.smallestR)))

                else:
                    # Give an error if the requested number is not in the array.
                    self.msg3R = QMessageBox.information(self, "Error", "Please enter a sorted array elements...")
                    # Clean the section where the user entered numbers.
                    self.ui.take_number_2.clear()
                    self.ui.result_edit_2.clear()
            else:
                self.msg = QMessageBox.critical(self, "Error", "Please make the operations in order!")
        except ValueError:
            # Error if user enters anything other than number.
            self.msg = QMessageBox.information(self, "Error", "Please enter a valid number...")
            # Clean the section where the user entered numbers.
            self.ui.take_number.clear()
        except AttributeError:
            self.msg = QMessageBox.information(self, "Error", "Please create an array...")

    # %%

    def partitionRandom(self, array, p, r):
        x = array[r]
        i = p - 1
        for j in range(p, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        self.x = np.arange(len(array))
        self.ui.MplSort_random.canvas.axes.clear()
        self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
        self.ui.MplSort_random.canvas.axes.bar(self.x[r], array[r], color="green", edgecolor='black')
        self.ui.MplSort_random.canvas.axes.bar(self.x[i], array[i], color="purple", edgecolor='black')
        self.autolabelRandom(self.rectsR)
        self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort_random.canvas.draw()
        QApplication.processEvents()
        time.sleep(1)
        return i + 1

    def randomized_partition_random(self, array, p, r):
        i = random.randint(p, r)
        self.x = np.arange(len(array))
        self.ui.MplSort_random.canvas.axes.clear()
        self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.x, array, color=(0, 0, 0, 0.1), edgecolor='blue')
        self.autolabelRandom(self.rectsR)
        self.ui.MplSort_random.canvas.draw()
        array[r], array[i] = array[i], array[r]
        return self.partitionRandom(array, p, r)

    def randomized_select_random(self, array, p, q, i):
        if p == q:
            self.ui.MplSort_random.canvas.axes.clear()
            self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
            self.ui.MplSort_random.canvas.axes.bar(self.x[p], array[q], color="blue", edgecolor='blue')
            self.autolabelRandom(self.rectsR)
            self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
            self.ui.MplSort_random.canvas.draw()
            return array[p]
        r = self.randomized_partition_random(array, p, q)
        k = r - p + 1
        if i == k:
            self.ui.MplSort_random.canvas.axes.clear()
            self.rectsR = self.ui.MplSort_random.canvas.axes.bar(self.x, array, color="orange", edgecolor="black")
            self.ui.MplSort_random.canvas.axes.bar(self.x[r], array[r], color="blue", edgecolor='blue')
            self.autolabelRandom(self.rectsR)
            self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
            self.ui.MplSort_random.canvas.draw()
            return array[r]
        elif i < k:
            return self.randomized_select_random(array, p, r - 1, i)
        else:
            return self.randomized_select_random(array, r + 1, q, i - k)

    # %% Clear post-values with clear button
    def clearRandom(self):
        self.lowerR = 0
        self.upperR = 0
        self.lengthR = 0
        self.unsorted_array = []
        self.sorted_arrayR = []
        self.ui.lower_range_2.clear()
        self.ui.upper_range_2.clear()
        self.ui.display_arraylen_2.clear()
        self.ui.disp_unsorted_array_2.clear()
        self.ui.disp_sorted_array_2.clear()
        self.ui.take_number_2.clear()
        self.ui.result_edit_2.clear()
        self.ui.MplSort_random.canvas.axes.clear()
        self.ui.MplSort_random.canvas.axes.patch.set_alpha(0)
        self.ui.MplSort_random.canvas.draw()
        self.ui.array_len_2.setValue(0)


    #Info page Uı
    def uni_logo(self):
        webbrowser.open('https://www.ikcu.edu.tr/')

    def youtube_logo(self):
        webbrowser.open('https://www.youtube.com/@ikcuelectricalandelectroni2451')

    def github_logo(self):
        webbrowser.open('https://github.com/muratkilci')

    def linkedIn_logo(self):
        webbrowser.open('https://www.linkedin.com/in/murat-kilci-4615961b9/')

    def intagram_logo(self):
        webbrowser.open('https://www.instagram.com/murat_kilci/?igshid=YmMyMTA2M2Y%3D')


# %% Initialization
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
