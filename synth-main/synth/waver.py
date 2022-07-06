from scipy.io.wavfile import write as wavwrite
import numpy as np

def make_wave (array, output_file, samplerate ):
        """
        The make_wave function writes a wave file with a song in it.

        :param array:ArrayType: The array that is used to create the wave file.
        :param output_file:str: The name and path of the output file.
        :param samplerate:int: The samplerate of the output file.
        :return: None
        """
        amplitude = np.iinfo(np.int16).max
        data = amplitude * array
        wavwrite(output_file, samplerate, data.astype(np.int16))