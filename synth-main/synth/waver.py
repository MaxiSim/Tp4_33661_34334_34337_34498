from scipy.io.wavfile import write as wavwrite
import numpy as np

def make_wave (array, output_file, samplerate ):
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite(output_file, samplerate, data.astype(np.int16))