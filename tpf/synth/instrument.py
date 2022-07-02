import numpy as np
import math
import matplotlib.pyplot as plt
import functions 
from scipy.io.wavfile import write as wavwrite
from notes import notes_mapping

class Instrument:
    def __init__(self, name, instrument_file):
        self.name = name
        self.path = instrument_file
        self.n_harmonics = 0
        self.file = self.read_file()
        self.harmonics = self.set_harmonics()
        self.mods = self.set_mods()
        self.decay_time = self.set_decay()
        self.functions = {}
        self.mapping = notes_mapping
        
        
    def read_file(self):
        list = []
        with open(self.path, 'r') as file:
            for line in file:
                list.append(line.rstrip())
        return list
        
    def set_harmonics(self):
        harmonics = []
        self.n_harmonics = int(self.file[0])
        for harmonic in range(1, self.n_harmonics+1):
            temp = self.file[harmonic].split(' ')
            harmonics.append((int(temp[0]),float(temp[1])))  
        return harmonics        
    
    def set_mods(self):
        mods = {}
        attack = self.file[self.n_harmonics+1].split(' ')
        mods["Attack"] = (attack[0], [float(i) for i in attack[1:]])
        
        sustain = self.file[self.n_harmonics+2]
        if " " in sustain:
            sustain = sustain.split(' ')
            mods["Sustain"] = (sustain[0], [float(i) for i in sustain[1:]])
        else: 
            mods["Sustain"] = (sustain, 1)
        
        decay = self.file[self.n_harmonics+3].split(' ')
        mods["Decay"] = (decay[0], float(decay[1]))
        return mods
    
    def set_decay (self):
        decay_time = self.mods['Decay'][1]
        return decay_time
    
    def synthetise(self, note, length):
        freq = 880.000
        duration = length + self.decay_time
        note_wave = np.arange(0,duration, 1/48000)
        array = 0
        sine = self.harmonics[0][1] * (np.sin(2*math.pi*freq*self.harmonics[0][0]*note_wave))
        # for harmonic in range(len(self.harmonics)):
        #     sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
        array += sine 
        # plt.plot(note_wave, array)
        # plt.show()
        # self.modulate(array, duration)
        self.make_wave(freq, duration, array)  
    
    def modulate (self, array, duration):
        pass
        # for t in range(duration*48000):
        #     if t 
        
    def make_wave (self, freq, duration, array):
        samplerate = 48000
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite('sample1.wav', samplerate, data.astype(np.int16))
        

# def main():
#     piano = Instrument('ejemplo2', 'ejemplo2.txt') 
    
#     print (piano.harmonics)
    
#     print (piano.mods)  
           
#     piano.synthetise()

# if __name__ == '__main__':
#     main()

                    
    