from __future__ import print_function
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog



class HackComputerGUI():
    def __init__(self, CPU):
        self.CPU = CPU
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.padx = 10
        self.create_gui()

    def create_gui(self):
        pass
        # wait time
        self.instruction_frame = tk.LabelFrame(self.root, text="Instruction")
        self.instruction_frame.pack(side="top", fill="both", expand=True)

        tk.Label(self.instruction_frame, "Instruction : ").grid(row=0, column=0)
        self.instruction_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_sv, justify=tk.CENTER, width=24).grid(row=0, column=1)
        tk.Label(self.instruction_frame, "Type : ").grid(row=0, column=2)
        self.instruction_type_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_type_sv, justify=tk.CENTER, width=24).grid(row=0, column=3)
        tk.Label(self.instruction_frame, "ALU : ").grid(row=0, column=4)
        self.instruction_alu_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_alu_sv, justify=tk.CENTER, width=24).grid(row=0, column=5)
        tk.Label(self.instruction_frame, "Dest : ").grid(row=0, column=6)
        self.instruction_dest_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_alu_sv, justify=tk.CENTER, width=24).grid(row=0, column=7)
        tk.Label(self.instruction_frame, "Jump : ").grid(row=0, column=8)
        self.instruction_jump_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_alu_sv, justify=tk.CENTER, width=24).grid(row=0, column=9)

        self.status_frame = tk.LabelFrame(self.root, text="Status")
        self.status_frame.pack(side="top", fill="both", expand=True)

        tk.Label(self.status_frame, "").grid(row=0, column=0)

        tk.Label(self.status_frame, "bin").grid(row=0, column=1)
        tk.Label(self.status_frame, "hex").grid(row=0, column=2)
        tk.Label(self.status_frame, "dec").grid(row=0, column=3)

        tk.Label(self.status_frame, "A").grid(row=1, column=0)
        tk.Label(self.status_frame, "D").grid(row=1, column=0)
        tk.Label(self.status_frame, "out ALU").grid(row=1, column=0)
        tk.Label(self.status_frame, "idx ROM").grid(row=1, column=0)

        self.A_bin_sv = tk.StringVar()
        self.A_hex_sv = tk.StringVar()
        self.A_dec_sv = tk.StringVar()
        self.D_dec_sv = tk.StringVar()
        self.D_bin_sv = tk.StringVar()
        self.D_hex_sv = tk.StringVar()
        self.out_dec_sv = tk.StringVar()
        self.out_bin_sv = tk.StringVar()
        self.out_hex_sv = tk.StringVar()
        self.idx_rom_bin_sv = tk.StringVar()
        self.idx_rom_hex_sv = tk.StringVar()
        self.idx_rom_dec_sv = tk.StringVar()

        e = ttk.Entry(self.status_frame, textvariable=self.A_bin_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=1, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.A_hex_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=1, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.A_dec_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=1, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.D_bin_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=2, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.D_hex_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=2, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.D_dec_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=2, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.out_bin_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=3, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.out_hex_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=3, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.out_dec_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=3, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_bin_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=4, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_hex_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=4, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_dec_sv, justify=tk.CENTER, width=7)
        e.configure(state='readonly')
        e.grid(row=4, column=3)


        # diplay num instruction

        # idx ROM

        # instructions en langage machine et les suivantes

        # load data.

        # PPU avec un canvas

        # input

        # log instruction

        # current state (table ? ac binaire dec et hexa)

        # start stop

        # go back (save state ?)


    def update_state(self):
        self.A_bin_sv.set(bin(self.CPU.A_reg[0]))
        self.A_hex_sv.set(hex(self.CPU.A_reg[0]))
        self.A_dec_sv.set(str(self.CPU.A_reg[0]))
        self.D_dec_sv.set(str(self.CPU.D_reg[0]))
        self.D_bin_sv.set(bin(self.CPU.D_reg[0]))
        self.D_hex_sv.set(hex(self.CPU.D_reg[0]))
        self.out_dec_sv.set(str(self.CPU.out_ALU[0]))
        self.out_bin_sv.set(bin(self.CPU.out_ALU[0]))
        self.out_hex_sv.set(hex(self.CPU.out_ALU[0]))
        self.idx_rom_bin_sv.set(bin(self.CPU.ROM.idx))
        self.idx_rom_hex_sv.set(hex(self.CPU.ROM.idx))
        self.idx_rom_dec_sv.set(str(self.CPU.ROM.idx))

    def update_instruction(self):
        self.instruction_sv.set(self.CPU.instruction_str)
        self.instruction_type_sv.set(self.CPU.instruction_type)
        self.instruction_alu_sv.set(self.CPU.alu_instruction)
        self.instruction_dest_sv.set(self.CPU.dest_instruction)
        self.instruction_jump_sv.set(self.CPU.jump_instruction)



    def on_quit(self):
        # paramFile = open('param.ini', 'w')
        # paramFile.write(self.saveDir)
        self.root.destroy()
        self.root.quit()
