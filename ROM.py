import numpy as np



class ROM:
    MEM_SIZE = 65535

    def __init__(self):
        self.mem = np.zeros(ROM.MEM_SIZE, dtype='uint16')
        self.idx = 0
        self.mem[0] = 42
        self.mem[1] = 208
        self.mem[2] = 507
        self.mem[3] = 16507
        #FIXME
        self.idx_last_instruction = None
        self.find_idx_last_instruction()

    def load_machine_code(self, file_path, type_="text_binary"):
        if type_ == "binary":
            raw = np.loadtxt(file_path)
            self.mem = np.transpose(raw)
        elif type_ == "text_binary":
            file = open(file_path)
            idx = 0
            for line in file:
                self.mem[idx] = int(line, 2)
                idx += 1
        elif type_ == "logisim":
            file = open(file_path)
            idx = 0
            for line in file:
                if idx==0:
                    if line != "v2.0 raw":
                        print("This is not a valid logisim image file since it does not start with v2.0 raw")
                        break
                    idx+= 1
                else:
                    self.mem[idx] = int(line, 16)
                    idx += 1

        self.find_idx_last_instruction()

    def export_machine_code(self, file_path, type_="logisim"):
        if type_ == "logisim":
            """
            The file format used for image files is intentionally simple; this permits you to write a program, such as an assembler, that generates memory images that can then be loaded into memory. As an example of this file format, if we had a 256-byte memory whose first five bytes were 2, 3, 0, 20, and -1, and all subsequent values were 0, then the image would be the following text file.
            v2.0 raw
            02
            03
            00
            14
            ff
            The first line identifies the file format used (currently, there is only one file format recognized). Subsequent values list the values in hexadecimal, starting from address 0; you can place several such values on the same line. Logisim will assume that any values unlisted in the file are zero.
            
            The image file can use run-length encoding; for example, rather than list the value 00 sixteen times in a row, the file can include 16*00. Notice than the number of repetitions is written in base 10. Files produced by Logisim will use run-length encoding for runs of at least four values.
            """
            file = open(file_path, "w")
            file.write("v2.0 raw\n")
            for i in range(self.idx_last_instruction):
                file.write(hex(self.mem[0])[2:] + "\n")

    def find_idx_last_instruction(self):
        # Find the last non zero instruction
        list_nonzero = np.nonzero(self.mem)
        # test = list_nonzero[0][-1]
        self.idx_last_instruction = list_nonzero[0][-1]
        # self.idx_last_instruction = np.nonzero(self.mem)[-1]

    def get_instructions(self):
        return self.mem[0:self.idx_last_instruction]

    def compile_hack_assembler(self, file_path):
        pass