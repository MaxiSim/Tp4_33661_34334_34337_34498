from instrument import Instrument
import functions
from synthetizer import Track

# test if the music sheet has the correct format
def test_music_sheet():
    track1 = Track('tpf/scores/synthwars.txt', 'piano', 'tpf/instruments/piano.txt')

# test if the instrument is created correctly
def test_read_file():
    piano = Instrument('piano', 'tpf/instruments/piano.txt')

def test_attack():
    piano = Instrument('piano', 'tpf/instruments/piano.txt')
    function, parameters = piano.get_attck()
    assert function == functions.attack['LINEAR'] and len(parameters) >= 1
    
def test_sustain():
    piano = Instrument('piano', 'tpf/instruments/piano.txt')
    function, parameters = piano.get_sustain()
    assert function == functions.sustain['CONSTANT'] and len(parameters) >= 1
    
def test_decay():
    piano = Instrument('piano', 'tpf/instruments/piano.txt')
    function, parameters = piano.get_decay()
    assert function == functions.decay['INVLINEAR'] and len(parameters) == 1
    
