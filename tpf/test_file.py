from synth import functions
import numpy as np
from synth import instrument

class Test_Mods:
    def test_constant():
        if functions.Modulator.constant(0) != 1:
            assert False
    def test_linear():
        if functions.Modulator.linear(0, 1) != 0:
            assert False
    def test_invlinear():
        if functions.Modulator.invlinear(0, 1) != 1:
            assert False
    def test_sin():
        if functions.Modulator.sin(1, 0, 1) != 1:
            assert False
    def test_exp():
        if functions.Modulator.exp(4, 1) != np.exp(15):
            assert False
    def test_invexp():
        if functions.Modulator.invexp(0, 1) != 1:
            assert False
    def test_quartcos():
        if functions.Modulator.quartcos(0, 1) != 1:
            assert False
    def test_quartsin():
        if functions.Modulator.quartsin(1, 2) != (np.sin(np.pi / 2 * 2)):
            assert False
    def test_halfcos():
        if functions.Modulator.halfcos(0, 1) != 1:
            assert False
    def test_halfsin():
        if functions.Modulator.halfsin(1, 2) != 1:
            assert False
    def test_log():
        if functions.Modulator.log(1, 1) != np.log(10,10):
            assert False
    def test_invlog1():
        if functions.Modulator.invlog(3, 2) != 0:
            assert False
    def test_invlog2():
        if functions.Modulator.invlog(2, 3) != np.log(4,10):
            assert False
    def test_tri1():
        if functions.Modulator.tri(2, 1, 3, 1.5) != (2/3):
            assert False 
    def test_tri2():
        if functions.Modulator.tri(2, 4, 3, 1) != 2.5:
            assert False
        
class Test_sheets:
    def test_sheet():