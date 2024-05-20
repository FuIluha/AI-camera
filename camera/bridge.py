"""
A class that implements communication between the arduino and the computer via serialport
"""
import sys
import serial

sys.path.append('../pyserial')

class Bridge:
    """
    A class that implements communication between the arduino and the computer via serialport
    """
    def __init__(self):
        self.port = serial.Serial(port = '/dev/cu.usbserial-110', baudrate = 9600, timeout = 0.1)

    def upload_data(self, x, y):
        """
        loads x y coordinates into serialport
        """
        self.port.write(str.encode(f'{{\"x\":{x},\"y\":{y}}}\n'))
