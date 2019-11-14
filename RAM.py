import numpy as np



class RAM:
    MEM_SIZE = 65535

    def __init__(self):
        self.mem = np.zeros(RAM.MEM_SIZE, dtype='uint16')