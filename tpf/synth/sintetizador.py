

from instrument import Instrument
import numpy as np

class song():

    def __init__ (self, freq, sheet, instrument):
        self.freq = freq
        self.sheet = sheet
        self.instrument = instrument
        self.file = self.read_file()
        self.path = f'c:/Users/Usuario/Pensamiento_Computacional/tps/Tp_final/tpf/scores/synthwars.txt'
        
