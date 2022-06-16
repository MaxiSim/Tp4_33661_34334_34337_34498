

class Instrument:
    def __init__(self, name, instrument_file):
        self.name = name
        self.path = f'/Users/Maxi 1/pensamiento_computacional/TPS/Tp_final/tpf/instruments/{instrument_file}'
        self.n_harmonics = 0
        self.file = self.read_file()
        self.harmonics = self.set_harmonics()
        self.mods = self.set_mods()
        
        
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

def main():
    piano = Instrument('piano', 'piano.txt') 
    
    print (piano.harmonics)
    print (piano.mods)  
           

if __name__ == '__main__':
    main()

                    
    