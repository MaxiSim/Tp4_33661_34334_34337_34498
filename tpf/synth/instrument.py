
from functions import Modulators
import math 
import numpy as np
import matplotlib.pyplot as plt

class Instrument:
    def __init__(self, name, instrument_file):
        self.name = name
        self.path = f'c:/Users/Usuario/Pensamiento_Computacional/tps/Tp_final/tpf/instruments/{instrument_file}'
        self.n_harmonics = 0
        self.file = self.read_file()
        self.harmonics = self.set_harmonics()
        self.mods = self.set_mods()
        self.functions = self.set_functions()
        
        
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

        #if mods["Attack"][0] in functions:
            #print(Modulators.linear(np.arange(0,10,0.01), mods["Attack"][1][0]))

        return mods
        

    def str(self):
        return str(self.functions) and str(self.mods)


    def set_functions(self):
        functions = {"CONSTANT": Modulators.constant, 
        "LINEAR": Modulators.linear,
        "INVLINEAR":Modulators.invlinear, 
        "SIN":Modulators.sin, 
        "EXP": Modulators.exp,
        "INVEXP": Modulators.invexp, 
        "QUARTCOS": Modulators.quartcos,
        "QUARTSIN": Modulators.quartsin,
        "HALFCOS": Modulators.halfcos,
        "HALFSIN":Modulators.halfsin,
        "LOG": Modulators.log, 
        "INVLOG": Modulators.invlog}
        #(self.set_mods()["Attack"][1][0:])
        
        t = np.arange(0,10,0.01)
        if self.set_mods()["Attack"][0] in functions:
            y = ( np.sin(2*math.pi*440*t)*(functions[self.set_mods()["Attack"][0]](t,self.set_mods()["Attack"][1][0])))
            
        plt.plot(t,y)
        plt.show()
            

        #if self.set_mods()["Sustain"][0] in functions:
            #return functions[self.set_mods()["Sustain"][0]]()

        #if self.set_mods()["Decay"][0] in functions:
           # return (functions[self.set_mods()["Decay"][0]](t,self.set_mods()["Decay"][1][0]))


        







def main():
    piano = Instrument('piano', 'piano.txt') 
    
    print (piano.harmonics)
    print (piano.mods)
    print(piano.functions) 
    
 
    
           

if __name__ == '__main__':
    main()

                    
    