import numpy as np
from RAM import RAM
import time


class CPU:
    def __init__(self, ROM, RAM, VRAM, is_print_state=False, log_path="log.txt"):
        self.ROM = ROM
        self.RAM = RAM
        self.VRAM = VRAM
        self.A_reg = np.zeros(1, dtype='uint16')
        self.D_reg = np.zeros(1, dtype='uint16')
        self.out_ALU = np.zeros(1, dtype='uint16')
        self.is_print_state = is_print_state
        self.log_path = log_path
        self.wait_time_ms = 0
        self.refresh_rate = 1000

        self.instruction_str = ""
        self.instruction_type = ""
        self.alu_instruction = ""
        self.dest_instruction = ""
        self.jump_instruction = ""
        self.assembler_string = ""


    def tick(self):
        # fetch instruction from the ROM
        self.current_instruction = instruction = self.ROM.mem[self.ROM.idx]

        self.instruction_str = str(instruction)
        # A or C instruction ?
        is_c_instruction = np.bitwise_and(instruction, 0xE000)
        is_V_instruction = np.bitwise_and(instruction, 0x8000)

        if is_c_instruction:
            self.instruction_type = "C"

            # 1) ALU
            a = np.bitwise_and(instruction, 0x1000)
            alu_instruction = np.bitwise_and(instruction, 0x0FC0)
            alu_instruction = np.right_shift(alu_instruction, 6)
            result_ALU = 0  # default value
            if a == 0:
                if alu_instruction == 42:        #101010 -> 0
                    self.alu_instruction = "0"
                    result_ALU = 0
                elif alu_instruction == 63:      #111111 -> 1
                    self.alu_instruction = "1"
                    result_ALU = 1
                elif alu_instruction == 58:      #111010 -> -1
                    self.alu_instruction = "-1"
                    result_ALU = -1
                elif alu_instruction == 12:      #001100 -> D
                    self.alu_instruction = "D"
                    result_ALU = self.D_reg[0]
                elif alu_instruction == 48:      #110000 -> A
                    self.alu_instruction = "A"
                    result_ALU = self.A_reg[0]
                elif alu_instruction == 13:      #001101 -> !D
                    self.alu_instruction = "!D"
                    result_ALU = np.invert(self.D_reg[0])
                elif alu_instruction == 49:      #110001 -> !A
                    self.alu_instruction = "!A"
                    result_ALU = np.invert(self.A_reg[0])
                elif alu_instruction == 15:      #001111 -> -D
                    self.alu_instruction = "-D"
                    result_ALU = - self.D_reg[0]
                elif alu_instruction == 51:      #110011 -> -A
                    self.alu_instruction = "-A"
                    result_ALU = - self.A_reg[0]
                elif alu_instruction == 31:      #011111 -> D + 1
                    self.alu_instruction = "D+1"
                    result_ALU = self.D_reg[0] + 1
                elif alu_instruction == 55:      #110111 -> A + 1
                    self.alu_instruction = "A+1"
                    result_ALU = self.A_reg[0] + 1
                elif alu_instruction == 14:  # 001110 -> D - 1
                    self.alu_instruction = "D-1"
                    result_ALU = self.D_reg[0] - 1
                elif alu_instruction == 50:      #110010 -> A-1
                    self.alu_instruction = "A-1"
                    result_ALU = self.A_reg[0] - 1
                elif alu_instruction == 2:      #000010 -> D+A
                    self.alu_instruction = "D+A"
                    result_ALU = self.A_reg[0] + self.D_reg[0]
                elif alu_instruction == 19:      #010011 -> D-A
                    self.alu_instruction = "D-A"
                    result_ALU = self.D_reg[0] - self.A_reg[0]
                elif alu_instruction == 7:      #000111 -> A-D
                    self.alu_instruction = "A-D"
                    result_ALU = self.A_reg[0] - self.D_reg[0]
                elif alu_instruction == 0:      #000000 -> D&A
                    self.alu_instruction = "D&A"
                    result_ALU = self.D_reg[0] & self.A_reg[0]
                elif alu_instruction == 21:      #010101 -> D|A
                    self.alu_instruction = "D|A"
                    result_ALU = self.D_reg[0] | self.A_reg[0]
            else:   # a = 0
                if alu_instruction == 42:        #101010 -> 0
                    self.alu_instruction = "0"
                    result_ALU = 0
                elif alu_instruction == 63:      #111111 -> 1
                    self.alu_instruction = "1"
                    result_ALU = 1
                elif alu_instruction == 58:      #111010 -> -1
                    self.alu_instruction = "-1"
                    result_ALU = -1
                elif alu_instruction == 12:      #001100 -> D
                    self.alu_instruction = "D"
                    result_ALU = self.D_reg[0]
                elif alu_instruction == 48:      #110000 -> A
                    self.alu_instruction = "M"
                    result_ALU = self.RAM.mem[self.A_reg[0]]
                elif alu_instruction == 13:      #001101 -> !D
                    self.alu_instruction = "!D"
                    result_ALU = np.invert(self.D_reg[0])
                elif alu_instruction == 49:      #110001 -> !A
                    self.alu_instruction = "!M"
                    result_ALU = np.invert(self.RAM.mem[self.A_reg[0]])
                elif alu_instruction == 15:      #001111 -> -D
                    self.alu_instruction = "-D"
                    result_ALU = - self.D_reg[0]
                elif alu_instruction == 51:      #110011 -> -A
                    self.alu_instruction = "-M"
                    result_ALU = - self.RAM.mem[self.A_reg[0]]
                elif alu_instruction == 31:      #011111 -> D + 1
                    self.alu_instruction = "D+1"
                    result_ALU = self.D_reg[0] + 1
                elif alu_instruction == 55:      #110111 -> A + 1
                    self.alu_instruction = "M+1"
                    result_ALU = self.RAM.mem[self.A_reg[0]] + 1
                elif alu_instruction == 14:  # 001110 -> D - 1
                    self.alu_instruction = "D-1"
                    result_ALU = self.D_reg[0] - 1
                elif alu_instruction == 50:      #110010 -> A-1
                    self.alu_instruction = "M-1"
                    result_ALU = self.RAM.mem[self.A_reg[0]] - 1
                elif alu_instruction == 2:      #000010 -> D+A
                    self.alu_instruction = "D+M"
                    result_ALU = self.RAM.mem[self.A_reg[0]] + self.D_reg[0]
                elif alu_instruction == 19:      #010011 -> D-A
                    self.alu_instruction = "D-M"
                    result_ALU = self.D_reg[0] - self.RAM.mem[self.A_reg[0]]
                elif alu_instruction == 7:      #000111 -> A-D
                    self.alu_instruction = "M-D"
                    result_ALU = self.RAM.mem[self.A_reg[0]] - self.D_reg[0]
                elif alu_instruction == 0:      #000000 -> D&A
                    self.alu_instruction = "D&M"
                    result_ALU = self.D_reg[0] & self.RAM.mem[self.A_reg[0]]
                elif alu_instruction == 21:      #010101 -> D|A
                    self.alu_instruction = "D|M"
                    result_ALU = self.D_reg[0] | self.RAM.mem[self.A_reg[0]]

            self.out_ALU[0] = result_ALU
            # 2) Destination
            dest = np.bitwise_and(instruction, 0x0038)
            dest = np.right_shift(dest, 3)

            if dest == 0:
                pass
            elif dest == 1:  # 001 M
                self.dest_instruction = "M"
                self.RAM.mem[self.A_reg[0]] = result_ALU
            elif dest == 2:  #010 D
                self.dest_instruction = "D"
                self.D_reg[0] = result_ALU
            elif dest == 3:  #011 MD
                self.dest_instruction = "MD"
                self.RAM.mem[self.A_reg[0]] = self.D_reg[0] = result_ALU
            elif dest == 4:  #100 A
                self.dest_instruction = "A"
                self.A_reg[0] = result_ALU
            elif dest == 5:  #101 AM
                self.dest_instruction = "AM"
                self.A_reg[0] = self.RAM.mem[self.A_reg[0]] = result_ALU
            elif dest == 6:  #110 AD
                self.dest_instruction = "AD"
                self.A_reg[0] = self.D_reg[0] = result_ALU
            elif dest == 7:  #111 AMD
                self.dest_instruction = "AMD"
                self.A_reg[0] = self.RAM.mem[self.A_reg[0]] = self.D_reg[0] = result_ALU

            # 3) jump
            jump = np.bitwise_and(instruction, 0x0007)
            is_jump = False
            if jump == 0:  # null
                self.jump_instruction = "null"
                is_jump = False
            elif jump == 1:  # JGT
                self.jump_instruction = "JGT"
                if result_ALU > 0:
                    is_jump = True
            elif jump == 2:  # JEQ
                self.jump_instruction = "JEQ"
                if result_ALU == 0:
                    is_jump = True
            elif jump == 3:  # JGE
                self.jump_instruction = "JGE"
                if result_ALU >= 0:
                    is_jump = True
            elif jump == 4:  # JLT
                self.jump_instruction = "JLT"
                if result_ALU < 0:
                    is_jump = True
            elif jump == 5:  # JNE
                self.jump_instruction = "JNE"
                if result_ALU != 0:
                    is_jump = True
            elif jump == 6:  # JLE
                self.jump_instruction = "JLE"
                if result_ALU <= 0:
                    is_jump = True
            elif jump == 7:  # JMP
                self.jump_instruction = "JMP"
                is_jump = True

            if is_jump:
                self.ROM.idx = self.A_reg[0]
            else:
                self.ROM.idx += 1
        elif is_V_instruction:
            self.instruction_type = "V"
            address = np.bitwise_and(instruction, 0x000F)
            self.set_VRAM(address)
        else:
            self.instruction_type = "A"
            # A instruction, write in A register
            self.A_reg[0] = instruction
            # no jump to consider
            self.ROM.idx += 1
            self.assembler_string = hex(instruction)[2:] + " -> A"


        if self.ROM.idx % self.refresh_rate == 0:
            # PPU display image
            pass

        # time.sleep(self.wait_time_ms)

        #TODO log

        if self.is_print_state:
            self.print_state()

    def go_to_instruction_n(self, n):
        """
        We recompute all the instruction to the nb n
        :param n:
        :return:
        """
        self.ROM.idx = 0
        self.RAM.clear()
        self.A_reg[0] = 0
        self.D_reg[0] = 0
        self.out_ALU[0] = 0
        #TODO test infinite loop et faire cela dans un thread séparé que l'on peut tuer.
        while self.ROM.idx != n:
            self.tick()



    def get_instruction_type(self, instruction):
        if np.bitwise_and(instruction, 0xE000) :
            return 'C'
        elif np.bitwise_and(instruction, 0x8000) :
            return 'V'
        else:
            return 'A'

    def get_ALU_operation_type(self, instruction):
        if self.get_instruction_type(instruction) == "A":
            return "NA"
        a = np.bitwise_and(instruction, 0x1000)
        alu_instruction = np.bitwise_and(instruction, 0x0FC0)
        alu_instruction = np.right_shift(alu_instruction, 6)

        if a:
            if alu_instruction == 42:  # 101010 -> 0
                return "0"
            elif alu_instruction == 63:  # 111111 -> 1
                return "1"
            elif alu_instruction == 58:  # 111010 -> -1
                return "-1"
            elif alu_instruction == 12:  # 001100 -> D
                return "D"
            elif alu_instruction == 48:  # 110000 -> A
                return "A"
            elif alu_instruction == 13:  # 001101 -> !D
                return "!D"
            elif alu_instruction == 49:  # 110001 -> !A
                return "!A"
            elif alu_instruction == 15:  # 001111 -> -D
                return "-D"
            elif alu_instruction == 51:  # 110011 -> -A
                return "-A"
            elif alu_instruction == 31:  # 011111 -> D + 1
                return "D+1"
            elif alu_instruction == 55:  # 110111 -> A + 1
                return "A+1"
            elif alu_instruction == 14:  # 001110 -> D - 1
                return "D-1"
            elif alu_instruction == 50:  # 110010 -> A-1
                return "A-1"
            elif alu_instruction == 2:  # 000010 -> D+A
                return "D+A"
            elif alu_instruction == 19:  # 010011 -> D-A
                return "D-A"
            elif alu_instruction == 7:  # 000111 -> A-D
                return "A-D"
            elif alu_instruction == 0:  # 000000 -> D&A
                return "D&A"
            elif alu_instruction == 21:  # 010101 -> D|A
                return "D|A"

        else:  # a = 0
            if alu_instruction == 42:  # 101010 -> 0
                return "0"
            elif alu_instruction == 63:  # 111111 -> 1
                return "1"
            elif alu_instruction == 58:  # 111010 -> -1
                return "-1"
            elif alu_instruction == 12:  # 001100 -> D
                return  "D"
            elif alu_instruction == 48:  # 110000 -> A
                return "M"
            elif alu_instruction == 13:  # 001101 -> !D
                return "!D"
            elif alu_instruction == 49:  # 110001 -> !A
                return "!M"
            elif alu_instruction == 15:  # 001111 -> -D
                return "-D"
            elif alu_instruction == 51:  # 110011 -> -A
                return "-M"
            elif alu_instruction == 31:  # 011111 -> D + 1
                return "D+1"
            elif alu_instruction == 55:  # 110111 -> A + 1
                return "M+1"
            elif alu_instruction == 14:  # 001110 -> D - 1
                return "D-1"
            elif alu_instruction == 50:  # 110010 -> A-1
                return "M-1"
            elif alu_instruction == 2:  # 000010 -> D+A
                return "D+M"
            elif alu_instruction == 19:  # 010011 -> D-A
                return "D-M"
            elif alu_instruction == 7:  # 000111 -> A-D
                return "M-D"
            elif alu_instruction == 0:  # 000000 -> D&A
                return "D&M"
            elif alu_instruction == 21:  # 010101 -> D|A
                return "D|M"

    def get_dest_type(self, instruction):
        if self.get_instruction_type(instruction) == "A":
            return "NA"
        dest = np.bitwise_and(instruction, 0x0038)
        dest = np.right_shift(dest, 3)

        if dest == 0:
            return "None"
        elif dest == 1:  # M
            return "M"
        elif dest == 2:  # D
            return "D"
        elif dest == 3:  # MD
            return "MD"
        elif dest == 4:  # A
            return "A"
        elif dest == 5:  # AM
            return "AM"
        elif dest == 6:  # AD
            return "AD"
        elif dest == 7:  # AMD
            return "AMD"

    def get_jump_type(self, instruction):
        if self.get_instruction_type(instruction) == "A":
            return "NA"
        jump = np.bitwise_and(instruction, 0x0007)
        if jump == 0:  # null
            return "null"
        elif jump == 1:  # JGT
            return "JGT"
        elif jump == 2:  # JEQ
            return "JEQ"
        elif jump == 3:  # JGE
            return "JGE"
        elif jump == 4:  # JLT
            return "JLT"
        elif jump == 5:  # JNE
            return "JNE"
        elif jump == 6:  # JLE
            return "JLE"
        elif jump == 7:  # JMP
            return "JMP"

    def format_binary_instruction(self, instruction):
        raw_bin = bin(instruction)[2:]
        nb_bits = len(raw_bin)
        nb_bits_to_add = 16 - nb_bits
        padding = "0"*nb_bits_to_add
        raw_bin = padding + raw_bin
        bin_ = raw_bin[0:4] + " " + raw_bin[4:8] + " " + raw_bin[8:12] + " " + raw_bin[12:16]
        return bin_

    def format_hex_instruction(self, instruction):
        raw_hex = hex(instruction)[2:]
        nb_bits = len(raw_hex)
        nb_bits_to_add = 4 - nb_bits
        padding = "0"*nb_bits_to_add
        hex_ = padding + raw_hex
        return hex_

    def set_VRAM(self, address):

        # find 1 bit in register D
        bits = []
        for i, c in enumerate(bin(self.D_reg[0])[:1:-1], 1):
            if c == '1':
                bits.append(i)

        for bit in bits:
            self.VRAM.set_pixel(address, bit, 65536)


    def get_assembler_string(self, instruction):
        if self.get_instruction_type(instruction) == "A":
            self.assembler_string = self.format_hex_instruction(instruction) + " -> A"
        else:
            hex_instruction = hex(instruction)[2:]
            if hex_instruction == "fc10":
                self.assembler_string = "M[A] -> D"
            elif hex_instruction == "f090":
                self.assembler_string = "M[A] + D -> D"
            elif hex_instruction == "e308":
                self.assembler_string = "D -> M[A]"

            elif hex_instruction == "ec10":
                self.assembler_string = "A -> D"
            elif hex_instruction == "e302":
                self.assembler_string = "D?0"
            elif hex_instruction == "f088":
                self.assembler_string = "M[A] + D -> M[A]"
            elif hex_instruction == "fc88":
                self.assembler_string = "M[A] - 1 -> M[A]"
            elif hex_instruction == "e007":
                self.assembler_string = "JUMP"
            elif hex_instruction == "f007":
                self.assembler_string = "JUMP"
            else:
                self.assembler_string = ""

            #TODO dictionnary of useful instruction
            pass

        return self.assembler_string

    def print_state(self):
        print("instruction nb : %d\nA : \nD : \n out_ALU : \n idx_ROM : \n)")

    def save_state(self):
        #TODO with shelves ?
        pass

    def load_state(self):
        #TODO with shelves ?
        pass