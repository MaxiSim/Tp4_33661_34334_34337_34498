import numpy as np
import math
import functions 
from notes import notes_mapping
import matplotlib.pyplot as plt


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
        """
        The read_file function reads the instrument setup file, validates it, and sets up the instrument object.
    
        :param self: The instrument object.
        :return: None
        """
        with open(self.path, 'rt') as file:
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
        """
        The synthetise function creates the array with each note.
        It also calls the function to modulate the note.
        
        :param self: The instrument object.
        :param note: The note to be created.
        :param length: The length of the note.
        return: The array with the modulated note.
        """
        freq = self.mapping[note]
        duration = length + self.decay_time
        note_wave = np.arange(1/48000,duration, 1/48000)
        sine_array = 0
        for harmonic in range(len(self.harmonics)):
            sine = self.harmonics[harmonic][1] * (np.sin(2*math.pi*freq*self.harmonics[harmonic][0]*note_wave))
            sine_array += sine 
        modulator_array = self.modulate(note_wave)
        final_note_wave = 0.007 * modulator_array * sine_array
        return final_note_wave

    
    def modulate (self, length_array):
        """
        The modulate function modulates the note.
    
        :param self: The instrument object.
        :param length_array: The array with the timeframe for the note.
        return: The array with the modulated timeframe of the note.
        """
        attack_time = self.attack_param[0]
        decay_time = self.decay_time
        if (attack_time*48000)>(len(length_array)-(int(decay_time*48000))):
            complete = False
            attack_array = length_array[:(len(length_array)-(int(decay_time*48000)))]
        else:
            complete = True
            attack_array = length_array[:int(attack_time*48000)]
            sustain_array = length_array[int(attack_time*48000):int(len(length_array)-int(decay_time*48000))]

        decay_array = np.arange(1/48000, decay_time+1/48000, 1/48000)
        attack_array = self.attack_func(attack_array, *self.attack_param)
        decay_array = self.decay_func(decay_array, *self.decay_param)

        if complete:
            sustain_array = self.sustain_func(sustain_array, *self.sustain_param)
            concat1 = np.concatenate((attack_array, sustain_array), axis=None)
            
        else:
            concat1 = attack_array
        concat2 = np.concatenate((concat1, decay_array), axis=None)

        return concat2

    
    def set_attck(self, func_name, param):
        """
        The set_attck function sets the attack function and its parameters.
        
        :param self: The instrument object.
        :param func_name: The attack function.
        :param param: The parameters of the attack function.
        return: None
        """
        self.attack_func = func_name
        self.attack_param = param 
            
    def set_sustain(self, func_name, param):
        """
        The set_sustain function sets the sustain function and its parameters.
        
        :param self: The instrument object.
        :param func_name: The sustain function.
        :param param: The parameters of the sustain function.
        return: None
        """
        self.sustain_func = func_name
        self.sustain_param = param
    
    def set_decay(self, func_name, param):
        """
        The set_decay function sets the decay function and its parameters.
        
        :param self: The instrument object.
        :param func_name: The decay function.
        :param param: The parameters of the decay function.
        return: None
        """
        self.decay_func = func_name
        self.decay_param.append(param)
    
    def get_decay_time(self):
        """
        The get_decay_time function returns the decay time of the instrument.
        
        :param self: The instrument object.
        return: The decay time of the instrument.
        """
        return self.decay_time  
      
    def get_attck(self):
        """
        The get_attck function returns the attack function and its parameters.
        
        :param self: The instrument object.
        return: The attack function and its parameters.
        """
        return self.attack_func, self.attack_param
    
    def get_sustain(self):
        """
        The get_sustain function returns the sustain function and its parameters.
        
        :param self: The instrument object.
        return: The sustain function and its parameters.
        """
        return self.sustain_func, self.sustain_param
    
    def get_decay(self):
        """
        The get_decay function returns the decay function and its parameters.
        
        :param self: The instrument object.
        return: The decay function and its parameters.
        """
        return self.decay_func, self.decay_param
    
    def __str__ (self):
        return f'{self.name}'
    def __repr__(self) -> str:
        return f'{self.name}'
        
                    
    