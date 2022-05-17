import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
print('49'.encode('utf-8'))
for p in ports:
    print(p)