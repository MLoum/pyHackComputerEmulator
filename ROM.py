import numpy as np



class ROM:
    MEM_SIZE = 65535

    def __init__(self):
        self.mem = np.zeros(ROM.MEM_SIZE, dtype='uint16')
        self.idx = 0

    def load_machine_code(self, file_path, type_="binary"):
        pass

    def compile_hack_assembler(self, file_path):
        pass