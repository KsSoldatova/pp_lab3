import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from task1 import create_csv_annotation
from task2 import create_copy_dataset
from task3 import create_randomname_file
from task5 import IteratorTask1


class Ui_MainWindow(object):

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """This function was created automatically by qtdesigner.
        Fields are being initialized here"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #E6E6FA")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 550, 470))
        self.frame.setStyleSheet("background-color: #FFE9A3;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 0, 350, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(95)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 251, 170))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            r"C:\Users\kssol\PycharmProjects\pythonProject5\dataset"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.PathToDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDataset.setGeometry(QtCore.QRect(60, 280, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDataset.setFont(font)
        self.PathToDataset.setStyleSheet("background-color: #FFE9A3;\n"
                                         "border: 2px solid ##E6E6FA;\n"
                                         "border-radius: 10px;\n"
                                         "color: black;")
        self.PathToDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDataset.setObjectName("PathToDataset")
        self.NextTulip = QtWidgets.QPushButton(self.centralwidget)
        self.NextTulip.setGeometry(QtCore.QRect(30, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.NextTulip.setFont(font)
        self.NextTulip.setStyleSheet("QPushButton{\n"
                                    "color:black;\n"
                                    "background-color: #E6E6FA;\n"
                                    "border-radius: 10;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color:#FFE9A3;\n"
                                    "}\n"
                                    "")
        self.NextTulip.setObjectName("NextTulip")
        self.NextRose = QtWidgets.QPushButton(self.centralwidget)
        self.NextRose.setGeometry(QtCore.QRect(280, 360, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.NextRose.setFont(font)
        self.NextRose.setStyleSheet("QPushButton{\n"
                                     "color:black;\n"
                                     "background-color: #E6E6FA;\n"
                                     "border-radius: 10;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color:#FFE9A3;\n"
                                     "}\n"
                                     "")
        self.NextRose.setObjectName("NextRose")
        self.CreateAnnotation = QtWidgets.QPushButton(self.centralwidget)
        self.CreateAnnotation.setGeometry(QtCore.QRect(110, 420, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.CreateAnnotation.setFont(font)
        self.CreateAnnotation.setStyleSheet("QPushButton{\n"
                                            "color:black;\n"
                                            "background-color: #E6E6FA;\n"
                                            "border-radius: 10;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color:#FFE9A3;\n"
                                            "}\n"
                                            "")
        self.CreateAnnotation.setObjectName("CreateAnnotation")
        self.PathToDirOfDataset = QtWidgets.QLineEdit(self.centralwidget)
        self.PathToDirOfDataset.setGeometry(QtCore.QRect(60, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PathToDirOfDataset.setFont(font)
        self.PathToDirOfDataset.setStyleSheet("background-color: #FFE9A3;\n"
                                              "border: 2px solid #CCCCFF;\n"
                                              "border-radius: 10px;\n"
                                              "color: black;")
        self.PathToDirOfDataset.setAlignment(QtCore.Qt.AlignCenter)
        self.PathToDirOfDataset.setObjectName("PathToDirOfDataset")
        self.Task1 = QtWidgets.QPushButton(self.centralwidget)
        self.Task1.setGeometry(QtCore.QRect(30, 560, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.Task1.setFont(font)
        self.Task1.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #FFE9A3;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task1.setObjectName("Task1")
        self.Task2 = QtWidgets.QPushButton(self.centralwidget)
        self.Task2.setGeometry(QtCore.QRect(180, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.Task2.setFont(font)
        self.Task2.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #FFE9A3;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task2.setObjectName("Task2")
        self.Task3 = QtWidgets.QPushButton(self.centralwidget)
        self.Task3.setGeometry(QtCore.QRect(330, 560, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.Task3.setFont(font)
        self.Task3.setStyleSheet("QPushButton{\n"
                                 "color:black;\n"
                                 "background-color: #FFE9A3;\n"
                                 "border-radius: 10;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color:#CCFFCC;\n"
                                 "}\n"
                                 "")
        self.Task3.setObjectName("Task3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__iterator_tulip = IteratorTask1()
        self.__iterator_rose = IteratorTask1()
        self.add_functions()






