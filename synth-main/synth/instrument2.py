
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
        self.path = instrument_file
        self.n_harmonics = 0
        self.file = self.read_file()
        self.harmonics = self.set_harmonics()
        self.mods = self.set_mods()
        self.decay_time = self.set_decay()
        # self.functions = self.set_functions()
        
        
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
        
        return decay_time
    
    def synthetise(self, note, length):
        freq = 880.000
        duration = length + self.decay_time
        note_wave = np.arange(0,int(duration*48000//1))
        sine_array = 0
        # sine = self.harmonics[0][1] * (np.sin(2*math.pi*freq*self.harmonics[0][0]*note_wave))
        for harmonic in range(len(self.harmonics)):
            sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
            array += sine_array 
        # plt.plot(note_wave, array)
        # plt.show()
        # self.modulate(array, duration)
        modulator_array = self.modulate(note_wave)
        final_note_wave = 1 * modulator_array * sine_array
        return final_note_wave
        self.make_wave(freq, duration, array)
        
    
    def modulate (self, length_array):
        attack_time = self.mods['Attack'][1][0]
        decay_time = self.mods['Decay'][1]
        if attack_time*48000//1>(len(length_array)-(int(decay_time*48000//1))):
            attack_array = length_array[:(len(length_array)-(int(decay_time*48000//1)))]
        else:
            attack_array = length_array[:int(attack_time*48000//1)+1]
            sustain_array = length_array[int(attack_time*48000//1)+1:len(length_array)-int(decay_time*48000//1+1)]
        decay_array = length_array[len(length_array)-int(decay_time*48000//1+1):]
        

    # aca falta la multiplicacion de cada array con su funcion de modulacion
        if sustain_array:
            concat1 = np.concatenate((attack_array, sustain_array), axis=None)
        else:
            concat1 = attack_array
        concat2 = np.concatenate((concat1, decay_array), axis=None)
        return concat2

    def make_wave (self, freq, duration, array):
        samplerate = 48000
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite('sample1.wav', samplerate, data.astype(np.int16))
        

    def set_functions(self, array, duration):
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
        "INVLOG": Modulator.invlog}
        
        t = np.arange(0,10,0.01)
        if self.set_mods()["Attack"][0] in functions:
            y = ( np.sin(2*math.pi*440*t)*(functions[self.set_mods()["Attack"][0]](t,self.set_mods()["Attack"][1][0])))
            
        plt.plot(t,y)
        plt.show()

    
        attack_time = self.mods['Attack'][1][0]
        decay_time = self.mods['Decay'][1]
        sustain_time = duration-decay_time
        attack_array = array[int(attack_time*48000//1)+1:int(sustain_time*48000//1+1)]
        decay_array = array[int(sustain_time*48000//1+1):]

        

instrumento = Instrument('Piano', '/Users/brunocr/Documents/PC_Proyecto_Final/Tp_final/tpf/instruments/piano.txt')
print(instrumento.mods)
# Mods es diccionario que contiene tuplas con [0] nombre de la funcion en mayus, [1] una lista con los args de la funcion

    
