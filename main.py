import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from ui.ui_mainwindow import Ui_MainWindow

def section_to_points():
    if (ui.spinBox_2.value() + ui.spinBox_3.value()) > 65535:
        ui.spinBox_2.setValue(ui.spinBox_2.value() + ui.spinBox_3.value() - 65536)
    else:
        ui.spinBox_2.setValue(ui.spinBox_2.value() + ui.spinBox_3.value())
    if (ui.spinBox.value() + ui.spinBox_3.value()) > 65535:
        ui.spinBox.setValue(ui.spinBox.value() + ui.spinBox_3.value() - 65536)
    else:
        ui.spinBox.setValue(ui.spinBox.value() + ui.spinBox_3.value())


def points_to_count():
    ui.label.setText(ui.label.text()[:-5] + f"{ui.spinBox.value()}".zfill(5))
    ui.label_4.setText(ui.label_4.text()[:-5] + f"{ui.spinBox_2.value()}".zfill(5))

def set_correction():
    in_count = int(ui.label.text()[-5:])
    out_count = int(ui.label_4.text()[-5:])
    if (in_count - out_count) >= 0:
        ui.label_5.setText(ui.label_5.text()[:-5] + f"{in_count - out_count}".zfill(5))
    else:
        ui.label_5.setText(ui.label_5.text()[:-5] + f"{65536 + in_count - out_count}".zfill(5))
    ui.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 0);")

def get_section_status():
    in_count = int(ui.label.text()[-5:])
    out_count = int(ui.label_4.text()[-5:])
    corr = int(ui.label_5.text()[-5:])
    if in_count >= out_count:
        if (in_count - out_count - corr) == 0:
            ui.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            ui.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")
    else:
        if (65536 - out_count + in_count - corr) == 0:
            ui.pushButton_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            ui.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")

app = QtWidgets.QApplication(sys.argv)
CounterAxle = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(CounterAxle)
CounterAxle.setWindowFlags(QtCore.Qt.WindowType.CustomizeWindowHint | QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
CounterAxle.show()

ui.pushButton.clicked.connect(section_to_points)
ui.pushButton_2.clicked.connect(points_to_count)
ui.pushButton_4.clicked.connect(set_correction)
ui.pushButton_3.clicked.connect(get_section_status)
ui.label.setText(f'{ui.label.text()[:-5]}\t{ui.label.text()[-5:]}')
ui.label_4.setText(f'{ui.label_4.text()[:-5]}\t{ui.label_4.text()[-5:]}')
ui.label_5.setText(f'{ui.label_5.text()[:-5]}\t{ui.label_5.text()[-5:]}')

sys.exit(app.exec())