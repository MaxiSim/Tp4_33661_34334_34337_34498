import serial
import time


if __name__ == '__main__':    
    device = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
    
    def write(message):
        device.write(bytes(message, 'utf-8'))
    
    time.sleep(2)

    delays = 0.5

    write('18050')
    write('01050')

