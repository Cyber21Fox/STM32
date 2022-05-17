import serial
import time
import traceback
import logger
import matplotlib.pyplot as plt
import serial.tools.list_ports
import matplotlib
import seaborn as sns
import numpy as np

Log = logger.getLogger(__name__)

global com

def connect_port(port):
    com = serial.Serial(port, 115200)
    Log.info("Успешно подключен!")
    Log.info(com)
    time.sleep(1)
    data = read_data(com)
    return data

def read_data(com):
    com.write(b'\x31')
    time.sleep(1)
    Log.info("Послан сигнал")
    Log.info("Считывание данных")
    while True:
        wait_buf = com.inWaiting()
        if wait_buf != 0:
            data = list(com.read(wait_buf))
            print(data)
            break
        time.sleep(1)
    Log.info("Данные получены")
    com.close()
    return data

#def create_graph(data):
 #   plt.figure(figsize=(12, 7))
  #  x = np.linspace(190, 1100, len(data))
   # plt.xlabel('nm', fontsize=10, color='blue')
    #plt.plot(x, data, color='red')
    #plt.yticks(range(0, 110, 10))
    #plt.xticks(range(190, 1100, 40))
    #plt.axis([190, 1100, 0, 100])
    #matplotlib.rc('xtick', labelsize=10)
    #plt.grid()
    #plt.show()

def test_port():
    list_port=[]
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        list_port.append(list(p)[0])
    Log.info("Получен список всех портов")
    return list_port

# if __name__ == "__main__":
#     print("#" * 20 + "STM32" + "#" * 20)
#     print(test_port())
#     port = 'COM7'


