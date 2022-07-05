import functions
import numpy as np


def test_constant():
    if functions.constant(0, 1) != np.ones_like(0) * 1:
        assert False
def test_linear():
    if functions.linear(0, 1) != 0:
        assert False
def test_invlinear1():
    if functions.invlinear(1, 2) != 0.5:
        assert False
def test_invlinear2():
    if functions.invlinear(3, 2) != 0:
        assert False
def test_sin():
    if functions.sin(1, 0, 1) != 1:
        assert False
def test_exp():
    if functions.exp(4, 1) != np.exp(15):
        assert False
def test_invexp():
    if functions.invexp(0, 1) != 1:
        assert False
def test_quartcos():
    if functions.quartcos(0, 1) != 1:
        assert False
def test_quartsin():
    if functions.quartsin(1, 2) != (np.sin(np.pi / 2 * 2)):
        assert False
def test_halfcos():
    if functions.halfcos(0, 1) != 1:
        assert False
def test_halfsin():
    if functions.halfsin(1, 2) != 1:
        assert False
def test_log():
    if functions.log(1, 1) != 1:
        assert False
def test_invlog1():
    if functions.invlog(2, 2) != 0:
        assert False
def test_invlog2():
    if functions.invlog(2, 3) != np.log10(4):
        assert False
def test_tri1():
    if functions.tri(2, 1, 3, 1.5) != (2/3):
        assert False 
def test_tri2():
    if functions.tri(4, 2, 3, 1) != (5/2):
        assert False
        
