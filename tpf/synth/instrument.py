
from msilib.schema import Error
import numpy as np
import math
import matplotlib.pyplot as plt
import functions 
from scipy.io.wavfile import write as wavwrite
from notes import notes_mapping

class Instrument:
    def __init__(self, name, instrument_file, output_file):
        self.name = name
        self.path = instrument_file
        self.output_file = output_file
        self.n_harmonics = 0
        self.mapping = notes_mapping
        self.harmonics = []
        self.attack = None
        self.sustain = None 
        self.decay = None
        self.decay_time = 0
        
        
        
    def read_file(self):
        with open(self.path, 'r') as file:
            # set number of harmonics
            n_harmonics = file.readline().rstrip()
            if n_harmonics.isdigit():
                n_harmonics = int(n_harmonics)
                self.n_harmonics = int(n_harmonics)
            else:
                raise Exception ("Error: number of harmonics is not defined")
                
            # set harmonics
            for n in range (n_harmonics):
                a = file.readline().rstrip().split(' ')
                print (a)
                if len(a) == 2 and a[0].isdigit() and functions.isfloat(a[1]): 
                    self.harmonics.append((int(a[0]), float(a[1])))
                else:
                    print("File harmonics error")
            
            # set moodulators
            # attack     
            attack = file.readline().rstrip().split(' ')
            if attack[0] in functions.attack and len(attack) >= 2 and all(functions.isfloat(x) for x in attack[1:]):
                a = functions.attack[attack[0]]
                param = ([float(i) for i in attack[1:]])
                self.attack = (a, param)
            else:
                print("Error: attack function not defined or has wrong parameters")
            # sustain
            sustain = file.readline().rstrip()
            if ' ' in sustain:
                sustain = sustain.split(' ')
                if sustain[0] in functions.sustain and len(sustain) <= 2 and all(functions.isfloat(x) for x in sustain[1:]):
                    a = functions.sustain[sustain[0]]
                    param = ([float(i) for i in sustain[1:]])
                    self.sustain = (a, param)
            elif ' ' not in sustain and sustain in functions.sustain:
                a = functions.sustain[sustain]
                param = 1
                self.sustain = (a, param)
            else:
                print ("Error: sustain function not defined or has wrong parameters")
            # decay
            decay = file.readline().rstrip().split(' ')
            if decay [0] in functions.decay and len(decay) == 2 and functions.isfloat(decay[1]):
                a = functions.decay[decay[0]]
                param = float(decay[1])
                self.decay = (a, param)
                self.decay_time = param
            else:
                print("Error: decay function not defined or has wrong parameters")
        
    def synthetise(self, note, length):
        freq = self.mapping[note]
        duration = length + self.decay_time
        note_wave = np.arange(0,duration, 1/48000)
        array = 0
        # sine = self.harmonics[0][1] * (np.sin(2*math.pi*freq*self.harmonics[0][0]*note_wave))
        for harmonic in range(len(self.harmonics)):
            sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
            array += sine 
        # plt.plot(note_wave, array)
        # plt.show()
        # self.modulate(array, duration)
        self.make_wave(array)  
        return array
    
    def modulate (self, array):
        pass
        # for t in range(duration*48000):
        #     if t 
        

    def make_wave (self, array):
        samplerate = 48000
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite(self.output_file, samplerate, data.astype(np.int16))
        
                    
    