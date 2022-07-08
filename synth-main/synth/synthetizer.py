from instrument import Instrument
import numpy as np
import functions
from notes import notes_mapping


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
        """
        The get_array function returns the track array.
        
        :param self: The track object.
        return: The track array.
        """
        return self.track_array
    
    
    def set_instrument (self):
        """
        The set_instrument function sets the instrument object.
        
        :param self: The track object.
        return: The instrument object.
        """
        return Instrument(self.instrument_name, self.instrument_file)
    
        
    def read_sheet_file (self):
        """
        The read_sheet_file function reads the sheet file, validates it, and processes the music sheet.
        
        :param self: The track object.
        return: The procesed music sheet.
        """
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
        """
        The set_track_duration function sets the track duration.
        
        :param self: The track object.
        return: The track duration.
        """
        duration = 0
        for note in self.sheet:
            if note[0]+note[2] > duration:
                duration = note[0]+note[2]
        decay_time = self.instrument.get_decay_time()
        track_duration = duration + decay_time
        return track_duration


    def create_track_array (self):
        """
        The create_track_array function creates the track array.
        
        :param self: The track object.
        return: The track array.
        """
        track_array = np.zeros(int(self.duration*48000))
        n = 0
        for note in self.sheet:
            if note[2] == 0:
                continue
            note_array = self.instrument.synthetise(note[1], (note[2]))
            pre_note_array = np.zeros(int(note[0]*48000))
            post_note_array = np.zeros(len(track_array)-(len(note_array)+len(pre_note_array)))
            a = np.concatenate((pre_note_array, note_array), axis=None)
            b = np.concatenate((a, post_note_array), axis=None)
            track_array += b
            # PROGRESS BAR // aesthetic purposes
            n += 1
            percentage = round((n/len(self.sheet))*100, 2)
            progress = '▓'*(int(percentage//10))
            remaining = '_'*(10-int(percentage//10))
            bar = f'[{progress}{remaining}]'
            print(bar, percentage, '%')
        print(f'[▓▓▓▓▓▓▓▓▓▓] 100.00 % PROCESSING COMPLETE')
        return track_array
