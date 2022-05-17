import os
import serial
import time
import traceback
import logger
import serial.tools.list_ports
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from form import Ui_MainWindow
import numpy as np
import os
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)


Log = logger.getLogger(__name__)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(1,1,1)
        self.figure.set_figheight(5)
        self.figure.set_figwidth(1)
        self.ax.set_xlim(190, 1100)
        self.ax.set_ylim(0, 100)
        self.ax.xaxis.set_major_locator(MultipleLocator(45))
        self.ax.yaxis.set_major_locator(MultipleLocator(10))
        self.ax.xaxis.set_minor_locator(AutoMinorLocator(3))
        self.ax.yaxis.set_minor_locator(AutoMinorLocator(4))
        self.ax.grid(which='both')
        self.ax.grid(which='minor', alpha=0.2)
        self.ax.grid(which='major', alpha=0.5)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout(self.ui.frame_2)
        self.layout().setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toolbar,0)
        layout.addWidget(self.canvas, 0)
        self.test_port() #вывод всех портов
        self.ui.pushButton_2.clicked.connect(self.test_port)  #обновление портов
        self.ui.pushButton.clicked.connect(self.connect)    #запуск
        self.ui.pushButton2.clicked.connect(self.calibration)   # калибровка
        self.ui.pushButton3.clicked.connect(self.start_with_calibration)  # запуск калибровочный


    def test_port(self):
        try:
            list_port = []
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                list_port.append(list(p)[0])
            Log.info("Получен список всех портов")
            self.ui.comboBox.addItems(list_port)
            return list_port
        except Exception as exe:
            print(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при обновлении портов!", QMessageBox.Ok)

    def connect(self):
        self.ui.progressBar.setValue(20)
        data = self.connect_port(self.ui.comboBox.currentText())
        self.ui.progressBar.setValue(30)
        self.ui.progressBar.setValue(50)
        self.plot(data, 1, 0)
        print(data)
        # self.ui.pushButton2.clicked.connect(self.plot_test)
        return data


    def connect_port(self, port):
        try:
            com = serial.Serial(port, 115200)
            Log.info("Успешно подключен!")
            Log.info(com)
            com.write(b'\x31')
            Log.info("Послан сигнал")
            Log.info("Считывание данных")
            while True:
                wait_buf = com.inWaiting()
                if wait_buf != 0:
                    data = list(com.read(wait_buf))
                    print(data)
                    break
            Log.info("Данные получены")
            com.close()
            return data
        except Exception as exe:
            print(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при подключении!", QMessageBox.Ok)

    def calibration(self):
        self.ui.progressBar.setValue(20)
        data = self.connect_port(self.ui.comboBox.currentText())
        self.ui.progressBar.setValue(40)
        os.system(r' >text.txt')
        calibr_data = []
        for i in data:
            calibr_data.append(100 - i)     # калибровочные данные
        print(f'Калибр записал:{calibr_data}')
        with open("text.txt", "w") as f:
            f.write(str(calibr_data))

        self.ui.progressBar.setValue(50)
        self.plot(calibr_data, 1, 0)

    def start_with_calibration(self):
        self.ui.progressBar.setValue(20)
        data = self.connect_port(self.ui.comboBox.currentText())
        self.ui.progressBar.setValue(40)

        with open("text.txt", "r") as f:            #чтение с файла
             calibr_start_data = f.readline()
        calibr_start_data = eval(calibr_start_data)
        print(calibr_start_data)
        calibr_start_data = list(map(sum, zip(data, calibr_start_data)))
        print(f"Калибр сложеный:{calibr_start_data}")

        self.ui.progressBar.setValue(50)
        self.plot(data, 3, calibr_start_data)
        return data

    def plot(self,data, mode, data2):
        try:
            self.ui.progressBar.setValue(70)
            if len(self.ax.lines) != 0:
                for i in range(len(self.ax.lines)):
                    del self.ax.lines[0]
            self.ui.progressBar.setValue(80)
            x = np.linspace(190, 1100, len(data))
            self.ui.progressBar.setValue(90)
            self.ax.plot(x, data, color='yellow')
            if mode == 3:
                self.ax.plot(x, data2, color='red')
            self.ui.progressBar.setValue(100)
            self.canvas.draw()
        except Exception as exe:
            print(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при построении графика.\n Возможно нужный график уже построен!", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())