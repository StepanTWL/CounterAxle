# Form implementation generated from reading ui file 'E:\MyProject\Python\CounterAxle\ui\ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 230)
        MainWindow.setMinimumSize(QtCore.QSize(370, 230))
        MainWindow.setMaximumSize(QtCore.QSize(370, 230))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 350, 80))
        self.groupBox.setMinimumSize(QtCore.QSize(350, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(350, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 20))
        self.pushButton.setMinimumSize(QtCore.QSize(75, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 50, 75, 20))
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 30, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(30, 50, 80, 20))
        self.spinBox.setMinimumSize(QtCore.QSize(80, 20))
        self.spinBox.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(65535)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 50, 80, 20))
        self.spinBox_2.setMinimumSize(QtCore.QSize(80, 20))
        self.spinBox_2.setMaximumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(65535)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_3.setGeometry(QtCore.QRect(90, 20, 90, 20))
        self.spinBox_3.setMinimumSize(QtCore.QSize(90, 20))
        self.spinBox_3.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMaximum(65535)
        self.spinBox_3.setObjectName("spinBox_3")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 350, 80))
        self.groupBox_2.setMinimumSize(QtCore.QSize(350, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(350, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 15, 180, 20))
        self.label.setMinimumSize(QtCore.QSize(180, 20))
        self.label.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 35, 180, 20))
        self.label_4.setMinimumSize(QtCore.QSize(180, 20))
        self.label_4.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 55, 180, 20))
        self.label_5.setMinimumSize(QtCore.QSize(180, 20))
        self.label_5.setMaximumSize(QtCore.QSize(180, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 15, 75, 20))
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 20))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 350, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(350, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(350, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Counter Axle"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Axle"))
        self.pushButton.setText(_translate("MainWindow", "Section"))
        self.pushButton_2.setText(_translate("MainWindow", "Point"))
        self.label_2.setText(_translate("MainWindow", "In"))
        self.label_3.setText(_translate("MainWindow", "Out"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Get Axle"))
        self.label.setText(_translate("MainWindow", "In point count00000"))
        self.label_4.setText(_translate("MainWindow", "Out point count00000"))
        self.label_5.setText(_translate("MainWindow", "Correction00000"))
        self.pushButton_4.setText(_translate("MainWindow", "Adjust"))
        self.pushButton_3.setText(_translate("MainWindow", "Status Section"))
