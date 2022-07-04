
import numpy as np
import math
import matplotlib.pyplot as plt
import functions 
from scipy.io.wavfile import write as wavwrite
from functions import Modulator
from notes import notes_mapping

class Instrument:
    def __init__(self, name, instrument_file):
        self.name = name
        self.path = "c:/Users/Usuario/Pensamiento_Computacional/tps/Tp_final/tpf/instruments/ejemplo.txt"
        self.n_harmonics = 0
        self.file = self.read_file()
        self.harmonics = self.set_harmonics()
        self.mods = self.set_mods()
        self.decay_time = self.set_decay()
        
        self.array = self.synthetise()
        self.functions = self.set_functions(self.array)
        
        
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
        functions = ["CONSTANT", "LINEAR", "INVLINEAR", "SIN", "EXP", "INVEXP", "QUARTCOS", "QUARTSIN", "HALFCOS", "HALFSIN", "LOG", "INVLOG"] 
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
        # sine = self.harmonics[0][1] * (np.sin(2*math.pi*freq*self.harmonics[0][0]*note_wave))
        for harmonic in range(len(self.harmonics)):
            sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
            array += sine 
        # plt.plot(note_wave, array)
        # plt.show()
        # self.modulate(array, duration)
        
        self.make_wave(freq, duration, array)  
        return array

    def modulate (self, array, duration):
        pass
        # for t in range(duration*48000):
        #     if t 
        

    def make_wave (self, freq, duration, array):
        samplerate = 48000
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite('sample1.wav', samplerate, data.astype(np.int16))

    def str(self):
        return str(self.functions) and  str(self.mods)
        

    def set_functions(self, array):
        functions = {"CONSTANT": Modulator.constant, 
        "LINEAR": Modulator.linear,
        "INVLINEAR":Modulator.invlinear, 
        "SIN":Modulator.sin, 
        "EXP": Modulator.exp,
        "INVEXP": Modulator.invexp, 
        "QUARTCOS": Modulator.quartcos,
        "QUARTSIN": Modulator.quartsin,
        "HALFCOS": Modulator.halfcos,
        "HALFSIN":Modulator.halfsin,
        "LOG": Modulator.log, 
        "INVLOG": Modulator.invlog,
        "TRI":Modulator.tri}
        
        
        if self.set_mods()["Attack"][0] in functions:
            attack_array = array[0:int(self.set_mods()["Attack"][1][0]+1)]
            if len(self.mods()["Attack"][1]) > 1:
                y =  self.array*(functions[self.set_mods()["Attack"][0]](attack_array,self.set_mods()["Attack"][1][0],self.set_mods()["Attack"][1][1],self.set_mods()["Attack"][1][2]))
            else:
                y =  self.array*(functions[self.set_mods()["Attack"][0]](attack_array,self.set_mods()["Attack"][1][0]))

        if self.set_mods()["Sustain"][0] in functions:
            sustain_array = array[int(self.set_mods()["Attack"][1][0]):self.set_mods()["Decay"][1]]
            if len (self.mods()["Sustain"])== 3:
                x =  self.array*(functions[self.set_mods()["Sustain"][0]](sustain_array,self.set_mods()["Sustain"][1][0],self.set_mods()["Sustain"][1][1],self.set_mods()["Sustain"][1][2]))
            elif len(self.mods()["Sustain"])==2:
                x =  self.array*(functions[self.set_mods()["Sustain"][0]](sustain_array,self.set_mods()["Sustain"][1][0],self.set_mods()["Sustain"][1][1]))
            elif len(self.mods()["Sustain"])==1:
                x =  self.array*(functions[self.set_mods()["Sustain"][0]](sustain_array,self.set_mods()["Sustain"][1][0]))
            else:
                x =  self.array*(functions[self.set_mods()["Sustain"][0]](sustain_array))

        if self.set_mods()["Decay"][0] in functions:
            decay_array = array[self.set_mods()["Decay"][1]:]
            w = self.aray*(functions[self.set_mods()["Decay"][0]](decay_array,self.set_mods()["Decay"][1]))

        z = np.concatenate((y, x))
        a = np.concatenate((z, w))

        plt.plot(self.array,a)
        plt.show()

        

def main():

    piano = Instrument( "piano", "ejemplo.txt")
    print(piano.functions) 

#     print (piano.mods)  
#     print (piano.harmonics)
#     print (piano.mods)
   
    
 
   
#     piano.synthetise()

if __name__ == '__main__':
     main()

                    
    