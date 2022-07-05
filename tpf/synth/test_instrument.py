import numpy as np
from instrument import Instrument
import functions

def test_read_file():
    piano = Instrument('piano', 'tpf/instruments/pianotest.txt')

def test_attack():
    piano = Instrument('piano', 'tpf/instruments/pianotest.txt')
    function, parameters = piano.get_attck()
    assert function == functions.attack['LINEAR'] and len(parameters) >= 1
    
def test_sustain():
    piano = Instrument('piano', 'tpf/instruments/pianotest.txt')
    function, parameters = piano.get_sustain()
    assert function == functions.sustain['CONSTANT'] and len(parameters) == 1
    
def test_decay():
    piano = Instrument('piano', 'tpf/instruments/pianotest.txt')
    function, parameters = piano.get_decay()
    assert function == functions.decay['INVEXP'] and len(parameters) == 1
    
def test_synth_mods():
    piano = Instrument('piano', 'tpf/instruments/pianotest.txt')
    value = piano.synthetise('A4', 1.5)
    assert type(value) == np.ndarray and len(value) == ((1.5*48000)+(piano.get_decay_time()*48000))
    # el value checkea bien, pero la len da 74879 == 74880 osea que el array pifia en algun lado 