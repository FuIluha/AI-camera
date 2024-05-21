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
    def __init__(self, port: str):
        self.port = serial.Serial(port = port, baudrate = 9600, timeout = 0.1)
    
    def upload_data(self, x, y):
        """
        loads x y coordinates into serialport
        """
        self.port.write(str.encode(f'{{\"x\":{x},\"y\":{y}}}\n'))

    def move_x(self, step: bool):
        """
        step == True: x + 1, step == False: x - 1
        """
        if step:
            self.x += 1
        else:
            self.x -= 1
        self.port.write(str.encode(f'{{\"x\":{self.x},\"y\":{self.y}}}\n'))
    
    def move_y(self, step: bool):
        """
        step == True: x + 1, step == False: x - 1
        """
        if step:
            self.y += 1
        else:
            self.y -= 1
        self.port.write(str.encode(f'{{\"x\":{self.x},\"y\":{self.y}}}\n'))
