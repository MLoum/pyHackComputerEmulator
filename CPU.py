import numpy as np
import time


class CPU:
    def __init__(self, ROM, RAM, is_print_state=False, log_path="log.txt"):
        self.ROM = ROM
        self.RAM = RAM
        self.A_reg = np.zeros(1, dtype='uint16')
        self.D_reg = np.zeros(1, dtype='uint16')
        self.out_ALU = np.zeros(1, dtype='uint16')
        self.is_print_state = is_print_state
        self.log_path = log_path
        self.num_instruction = 0
        self.wait_time_ms = 0
        self.refresh_rate = 1000

        self.instruction_str = ""
        self.instruction_type = ""
        self.alu_instruction = ""
        self.dest_instruction = ""
        self.jump_instruction = ""


    def tick(self):
        # fetch instruction from the ROM
        instruction = self.ROM.mem[self.ROM.idx]
        self.instruction_str = str(instruction)
        # A or C instruction ?
        is_c_instruction = np.bitwise_and(instruction, 0x8000)

        if is_c_instruction:
            self.instruction_type = "C"

            # 1) ALU
            a = np.bitwise_and(instruction, 0x1000)
            alu_instruction  = np.bitwise_and(instruction, 0x0FC0)
            alu_instruction = np.right_shift(alu_instruction, 6)
            result_ALU = 0  # default value
            if a:
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
            else:   # a = 0
                pass

            #TODO others instruction

            # 2) Destination
            dest = np.bitwise_and(instruction, 0x0038)
            dest = np.right_shift(alu_instruction, 3)

            if dest == 0:
                pass
            elif dest == 1:  # M
                self.dest_instruction = "M"
                self.RAM.mem[self.A_reg[0]] = result_ALU
            elif dest == 2:  # D
                self.dest_instruction = "D"
                self.D_reg[0] = result_ALU
            elif dest == 3:  # MD
                self.dest_instruction = "MD"
                self.RAM.mem[self.A_reg[0]] = self.D_reg[0] = result_ALU
            elif dest == 4:  # A
                self.dest_instruction = "A"
                self.A_reg[0] = result_ALU
            elif dest == 5:  # AM
                self.dest_instruction = "AM"
                self.A_reg[0] = self.RAM.mem[self.A_reg[0]] = result_ALU
            elif dest == 6:  # AD
                self.dest_instruction = "AD"
                self.A_reg[0] = self.D_reg[0] = result_ALU
            elif dest == 7:  # AMD
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

        else:
            self.CPU.instruction_type = "A"
            # A instruction, write in A register
            self.A_reg[0] = instruction
            # no jump to consider
            self.ROM.idx += 1


        if self.num_instruction % self.refresh_rate == 0:
            # PPU display image
            pass

        time.sleep(self.wait_time_ms)

        if self.is_print_state:
            self.print_state()

    def print_state(self):
        print("instruction nb : %d\nA : \nD : \n out_ALU : \n idx_ROM : \n)")

    def save_state(self):
        pass

    def load_state(self):
        pass