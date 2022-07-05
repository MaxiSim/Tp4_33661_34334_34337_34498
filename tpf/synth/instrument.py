
import numpy as np
import math
import matplotlib.pyplot as plt
from sqlalchemy import func
import functions 
from notes import notes_mapping

class Instrument:
    def __init__(self, name, instrument_file):
        self.name = name
        self.path = instrument_file
        self.n_harmonics = 0
        self.mapping = notes_mapping 
        self.harmonics = []
        self.attack_func = None
        self.attack_param = []
        self.sustain_func = None
        self.sustain_param = []
        self.decay_func = None
        self.decay_param = []
        self.decay_time = 0
        self.file = self.read_file()
        
        
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
                if len(a) == 2 and a[0].isdigit() and functions.isfloat(a[1]): 
                    self.harmonics.append((int(a[0]), float(a[1])))
                else:
                    raise Exception ("File harmonics error")
            
            # set moodulators
            # attack     
            attack = file.readline().rstrip().split(' ')
            if attack[0] in functions.attack and len(attack) >= 2 and all(functions.isfloat(x) for x in attack[1:]):
                a = functions.attack[attack[0]]
                param = [float(i) for i in attack[1:]]
                self.set_attck(a, param)
            else:
                raise Exception ("Error: attack function not defined or has wrong parameters")
            
            # sustain
            sustain = file.readline().rstrip()
            if ' ' in sustain:
                sustain = sustain.split(' ')
                if sustain[0] in functions.sustain and len(sustain) >= 2 and all(functions.isfloat(x) for x in sustain[1:]):
                    c = functions.sustain[sustain[0]]
                    param = ([float(i) for i in sustain[1:]])
                    self.set_sustain(c, param)
                else:
                    raise Exception ("Error: sustain1 function not defined or has wrong parameters")
            elif ' ' not in sustain and sustain in functions.sustain:
                c = functions.sustain[sustain]
                param = [1]
                self.set_sustain(c, param)
            else:
                raise Exception ("Error: sustain2 function not defined or has wrong parameters")
           
            # decay
            decay = file.readline().rstrip().split(' ')
            if decay[0] in functions.decay and len(decay) == 2 and functions.isfloat(decay[1]):
                d = functions.decay[decay[0]]
                param = float(decay[1])
                self.set_decay(d, param)
                self.decay_time = param
            else:
                raise Exception ("Error: decay function not defined or has wrong parameters")
            
        
        
    def synthetise(self, note, length):
        freq = self.mapping[note]
        duration = length + self.decay_time
        note_wave = np.arange(1/48000,duration, 1/48000)
        sine_array = 0
        for harmonic in range(len(self.harmonics)):
            sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
            sine_array += sine 
        modulator_array = self.modulate(note_wave, length)
        plt.plot(modulator_array)
        plt.show()
        final_note_wave = 0.007 * modulator_array * sine_array
        # plt.plot(final_note_wave)
        # plt.show()
        # print('Note wave',len(note_wave))
        return final_note_wave
        # return 0.007 * sine_array

    
    def modulate (self, length_array, length):
        attack_time = self.attack_param[0]
        decay_time = self.decay_time
        sustain_time = length-self.attack_param[0]
        # if (attack_time*48000)>(len(length_array)-(int(decay_time*48000))):
        if sustain_time <=0:
            complete = False
            attack_array = length_array[:(len(length_array)-(int(decay_time*48000)))]
        else:
            complete = True
            attack_array = length_array[:int(attack_time*48000)]
            sustain_array = length_array[int(attack_time*48000):int(len(length_array)-int(decay_time*48000))]
        # decay_array = length_array[len(length_array)-int(decay_time*48000):]
        decay_array = np.arange(1/48000, decay_time+1/48000, 1/48000)
        attack_array = self.attack_func(attack_array, *self.attack_param)
        # decay_array = () * self.decay_func(decay_array, *self.decay_param)

        if complete:
            # *self.sustain_param
            sustain_array = self.sustain_func(sustain_array, *self.sustain_param)
            decay_array = (sustain_array[-1]) * self.decay_func(decay_array, *self.decay_param)
            concat1 = np.concatenate((attack_array, sustain_array), axis=None)
            plt.plot(attack_array)
            plt.show()
            # plt.plot(concat1)
            # plt.show()
            
        else:
            concat1 = attack_array
            decay_array = (attack_array[-1]) * self.decay_func(decay_array, *self.decay_param)
        concat2 = np.concatenate((concat1, decay_array), axis=None)
        # plt.plot(concat2)
        # plt.show()
        # plt.plot(attack_array)
        # plt.show()
        # plt.plot(decay_array)
        # plt.show()
        return concat2

    
    
    def set_attck(self, func_name, param):
        self.attack_func = func_name
        self.attack_param = param 
            
    def set_sustain(self, func_name, param):
        self.sustain_func = func_name
        self.sustain_param = param
    
    def set_decay(self, func_name, param):
        self.decay_func = func_name
        self.decay_param.append(param)
    
    def get_decay_time(self):
        return self.decay_time  
      
    def get_attck(self):
        return self.attack_func, self.attack_param
    
    def get_sustain(self):
        return self.sustain_func, self.sustain_param
    
    def get_decay(self):
        return self.decay_func, self.decay_param
    
    def __str__ (self):
        return self.name
        
                    
    