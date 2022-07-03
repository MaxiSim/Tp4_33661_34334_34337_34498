import datetime

from serial import Serial
from serial.serialutil import SerialException

from ..xylo.note import XyloNote
from ..util.logger import logger


from abc import abstractmethod

class BaseXylo:
    WHITE_MAPPING = {
        'G4':'18', 'A4':'17', 'B4':'16', 'C5':'15', 'D5':'14', 'E5':'13', 'F5':'12', 'G5':'11', 'A5':'10',
        'B5':'09', 'C6':'08', 'D6':'07', 'E6':'06', 'F6':'05', 'G6':'04', 'A6':'03', 'B6':'02', 'C7':'01'
    }

    BLACK_MAPPING = {
        'G#4': '01', 'Ab4': '01', 'A#4': '02', 'Bb4': '02', 'C#5': '03', 'Db5': '03', 'D#5': '04', 'Eb5': '04',
        'F#6': '05', 'Gb6': '05', 'G#5': '06', 'Ab5': '06', 'A#5': '07', 'Bb5': '07', 'C#6': '08', 'Db6': '08',
        'D#6': '09', 'Eb6': '09', 'F#6': '10', 'Gb6': '10', 'G#6': '11', 'Ab6': '11', 'A#6': '12', 'Bb6': '12',
    }

    buffer = []
    prev_t = None
    next_t = None

    def _format_velocity(self, velocity: int) -> str:
        return f'{velocity:03}'

    def send(self, note):
        self.buffer.append(note)


    def play(self):
        if len(self.buffer) == 0:
            raise RuntimeError('There are no notes to play. Buffer is empty.')

        self.prev_t = datetime.datetime.now()
        self.next_t = datetime.datetime.now()

        while len(self.buffer) > 0:
            current = (self.next_t - self.prev_t)

            current_time = current.seconds + current.microseconds / 1.0e6

            print(f'Time: {current_time}', end='\r')

            if current_time > self.buffer[0].start_time:
                note = self.buffer.pop(0)
                self._write_note(note)

            self.next_t = datetime.datetime.now()


    @abstractmethod
    def _write_note(self, note):
        raise NotImplementedError('Please override this method')


class MockXylo(BaseXylo):
    def write(self, message):
        logger.info(f'Message was sent: {message}')


    def _write_note(self, note):
        if note.value in self.WHITE_MAPPING:
            self.write(self.WHITE_MAPPING[note.value] + self._format_velocity(note.velocity))
        elif note.value in self.BLACK_MAPPING:
            self.write(self.BLACK_MAPPING[note.value] + self._format_velocity(note.velocity))
        else:
            raise ValueError('Specified note is not supported')


class Xylo(BaseXylo):
    def __init__(self, first_port='/dev/ttyUSB0', second_port='/dev/ttyUSB1', baudrate=115200, timeout=0.1):
        """Instantiates a Xylo(first_port, second_port, baudrate, timeout)

        Args:
            first_port (str): first USB device. 
            second_port (str): second USB device 
            baudrate (int): default value of the baudrate is 115200.
            timeout (float): set a read timeout in seconds.
        """
        self.first_device = Serial(port=first_port, baudrate=baudrate, timeout=timeout)

        try:
            self.second_device = Serial(port=second_port, baudrate=baudrate, timeout=timeout)
        except SerialException:
            logger.warn('Second device is not connected. Verify that is actually needed.')


    def write_first(self, message: str) -> None:
        """Writes to the first device.

        Args:
            message (str): data to send.
        """
        self.first_device.write(bytes(message, 'UTF-8'))


    def write_second(self, message):
        """Writes to the second device.

        Args:
            message (str): data to send.
        """
        self.second_device.write(bytes(message, 'UTF-8'))


    def _write_note(self, note: XyloNote) -> None:
        """Converts and writes note.

        Args:
            note (XyloNote): note to write. 

        Raises:
            ValueError: If note value is not supported, it will fail.
        """
        if note.value in self.WHITE_MAPPING:
            self.write_first(self.WHITE_MAPPING[note.value] +
                    self._format_velocity(note.velocity))
        elif note.value in self.BLACK_MAPPING:
            self.write_second(self.BLACK_MAPPING[note.value] +
                    self._format_velocity(note.velocity))
        else:
            raise ValueError('Specified note is not supported')


