import numpy as np



class VRAM:
    MEM_SIZE = 16

    def __init__(self):
        self.mem = np.zeros((VRAM.MEM_SIZE, VRAM.MEM_SIZE), dtype='uint16')

    def set_pixel(self, x, y, value):
        self.mem[x,y] = value

    def get_pixel(self, x ,y):
        return self.mem[x,y]
