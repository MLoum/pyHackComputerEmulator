import numpy as np



class RAM:
    MEM_SIZE = 65535

    def __init__(self):
        self.mem = np.zeros(RAM.MEM_SIZE, dtype='uint16')
        self.idx_last_mem = None
        self.find_idx_last_instruction()

    def find_idx_last_instruction(self):
        # Find the last non zero instruction
        list_nonzero = np.nonzero(self.mem)
        if len(list_nonzero[0]) == 0:
            self.idx_last_mem = 0
        else:
            self.idx_last_mem = list_nonzero[0][-1]

    def get_mem(self):
        self.find_idx_last_instruction()
        return self.mem[0:self.idx_last_mem+1]

    def clear(self):
        self.mem = np.zeros(RAM.MEM_SIZE, dtype='uint16')
        self.idx_last_mem = None
        self.find_idx_last_instruction()
