from notes import notes
import functions
from xylophone.xylo import XyloNote

class Xylophone:
    def __init__(self, notefile):
        self.notefile = notefile
        self.note_list = self.read_note()
        self.notes = self.set_notes()
        
    def read_note(self):
        """
        Reads the note from the note file and saves a list of the notes and their starting time.
        
        returns: list of notes and their starting time
        """
        notes_list = []
        with open (self.notefile, 'rt') as file:
            for line in file:
                temp = line.rstrip().split(' ')
                if len(temp) == 3 and functions.isfloat(temp[0]) and functions.isfloat(temp[2]) and temp[1] in notes:
                    note = (temp[1], float(temp[0]))
                    notes_list.append(note)
                elif temp[1] not in notes:
                    pass
                else:
                    raise Exception ("Error: sheet file has wrong format")
        return notes_list
    
    def set_notes(self):
        """
        Sets the notes in a format that is compatible with the xylophone.
        
        returns: list of xylophone notes
        """
        notes = []
        for note in self.note_list:
            notes.append(XyloNote(note[0], note[1], 90))
        return notes
    
    def get_notes(self):
        """
        Returns the notes.
        """
        return self.notes