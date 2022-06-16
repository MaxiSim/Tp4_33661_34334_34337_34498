from instrument import Instrument

class synth():
    def __init__ (self, freq, sheet, instrument):
        self.freq = freq
        self.sheet = sheet
        self.instrument = instrument
        
    def synthetise(self, sheet, instrument):
        with open(sheet, 'r') as file:
            for note in file:
                line = note.split(' ')
                for harmonic in range(1, instrument.harmonics):
                    print()
        