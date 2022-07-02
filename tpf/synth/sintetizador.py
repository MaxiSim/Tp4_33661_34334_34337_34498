

from instrument import Instrument

class Song():
    def __init__ (self, freq, sheet, instrument):
        self.freq = freq
        self.sheet = sheet
        self.instrument = instrument
        self.file = self.read_file()
        self.path = f'c:/Users/Usuario/Pensamiento_Computacional/tps/Tp_final/tpf/scores/synthwars.txt'
        
    def synthetise(self, sheet, instrument):
        with open(sheet, 'r') as file:
            for note in file:
                line = note.split(' ')
                for harmonic in range(1, instrument.harmonics):
                    print()
    

    def read_file(self, sheet):
            list = []
            with open(sheet, 'r') as sheet:
                for line in sheet:
                    list.append(line.rstrip())
            return list

        
    def notes(sheet,list):
        notes1 = []
        for note in range(1, len(sheet)):
            temp = list[note].split(' ')
            notes1.append(((temp[0]),(temp[1]), (temp[2])))  
        return notes1

path = f"c:/Users/Usuario/Pensamiento_Computacional/tps/Tp_final/tpf/scores/synthwars.txt"
def main():
    print(notes(path, read_file(path)))

if __name__ == '__main__':
    main()

