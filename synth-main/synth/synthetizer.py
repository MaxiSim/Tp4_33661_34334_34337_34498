from instrument import Instrument
import numpy as np
import functions
from notes import notes_mapping

# class Song():
#     def __init__ (self, sheet=1, tracks=1):
#         self.freq = freq
#         self.sheet = sheet
#         self.instruments = instrument

class Track():
    def __init__(self, sheet_file_path, instrument_name, instrument_file):
        self.sheet_path = sheet_file_path
        self.instrument_file = instrument_file
        self.instrument_name = instrument_name
        self.instrument = self.set_instrument()
        self.sheet = self.read_sheet_file()
        self.duration = self.set_track_duration()
        self.track_array = self.create_track_array()
        
    def get_array (self):
        return self.track_array
    
    
    def set_instrument (self):
        return Instrument(self.instrument_name, self.instrument_file)
    
        
    def read_sheet_file (self):
        sheet_list = []
        with open (self.sheet_path, 'rt') as sheet:
            for line in sheet:
                temp = line.rstrip().split(' ')
                if len(temp) == 3 and functions.isfloat(temp[0]) and functions.isfloat(temp[2]) and temp[1] in notes_mapping:
                    temp[0] = float(temp[0])
                    temp[2] = float(temp[2])
                    sheet_list.append(temp)
                else:
                    raise Exception ("Error: sheet file has wrong format")
        return sheet_list
    
    
    def set_track_duration (self):
        duration = 0
        for note in self.sheet:
            if note[0]+note[2] > duration:
                duration = note[0]+note[2]
        decay_time = self.instrument.get_decay_time()
        track_duration = duration + decay_time
        return track_duration


    def create_track_array (self):
        track_array = np.zeros(int(self.duration*48000))
        n = 0
        for note in self.sheet:
            if note[2] == 0:
                continue
            note_array = self.instrument.synthetise(note[1], (note[2]))
            pre_note_array = np.zeros(int(note[0]*48000))
            post_note_len = (self.duration-(note[0]+note[2]+self.instrument.get_decay_time()))
            post_note_array = np.zeros(len(track_array)-(len(note_array)+len(pre_note_array)))
            a = np.concatenate((pre_note_array, note_array), axis=None)
            b = np.concatenate((a, post_note_array), axis=None)
            track_array += b
            n += 1
            print((n/len(self.sheet))*100, '%')
        return track_array