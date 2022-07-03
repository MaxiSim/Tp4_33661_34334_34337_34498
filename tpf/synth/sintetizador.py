from instrument import Instrument
import numpy as np

class Song():
    def __init__ (self, tracks):
        self.freq = freq
        self.sheet = sheet
        self.instrument = instrument

class Track():
    def __init__(self, sheet_file_path, instrument) -> None:
        self.sheet_path = sheet_file_path
        self.instrument = instrument
        self.sheet = self.read_sheet_file()
        self.duration = self.set_track_duration()
        self.track_array = self.create_track_array()
        
    def read_sheet_file (self):
        sheet_list = []
        with open (self.sheet_path, 'rt') as sheet:
            for line in sheet:
                temp = line.rstrip().split(' ')
                temp[0] = float(temp[0])
                temp[2] = float(temp[2])
                sheet_list.append(temp)
        return sheet_list
    
    def set_track_duration (self):
        duration = 0
        for note in self.sheet:
            if note[0]+note[2] > duration:
                duration = note[0]+note[2]
        return duration + self.instrument.decay_time

    def create_track_array (self):
        track_array = np.zeros(int(self.duration*48000//1))
        for note in self.sheet:
            note_array = self.instrument.synthetise(note[1], (note[2]*48000//1)/48000)
            pre_note_array = np.zeros(int(note[0]*48000//1))
            post_note_len= ((self.duration-(note[0]+note[2]))*48000//1)/48000
            post_note_array = np.zeros(int(post_note_len*48000))
            a = np.concatenate((pre_note_array, note_array), axis=None)
            b = np.concatenate((a, post_note_array), axis=None)
            track_array+=b
        return track_array


