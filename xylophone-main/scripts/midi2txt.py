import time
import serial

from mido import MidiFile
from sys import argv


if __name__ == '__main__':

    m2a = {
        55:'18', 57:'17', 59:'16',
        60:'15', 62:'14', 64:'13',
        65:'12', 67:'11', 69:'10',
        71:'09', 72:'08', 74:'07',
        76:'06', 77:'05', 79:'04',
        81:'03', 83:'02', 84:'01'
    }


    m2a2 = {
        56: '01', 58: '02', 61: '03',
        63: '04', 66: '05', 68: '06',
        70: '07', 73: '08', 75: '09',
        78: '10', 80: '11', 82: '12'
    }


    device = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
    time.sleep(2)
        

    def parse(file):
        mid = MidiFile(file)
        for msg in mid.play():
            if msg.type == 'note_on':
                if msg.note in m2a:
                    mess = str(m2a[msg.note]) + ('0'+str(msg.velocity) if msg.velocity<100 else str(msg.velocity))
                    device.write(bytes(mess, 'utf-8'))

    parse(argv[1])

