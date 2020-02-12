from __future__ import print_function
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog
import tkinter.font as tkFont



class HackComputerGUI():
    def __init__(self, CPU):
        self.CPU = CPU
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.padx = 10
        self.num_current_instruction = 0
        self.create_gui()
        self.load_ROM()
        self.update_ROM_list()


    def run(self):
        self.root.title("Hack computer emulator")
        self.root.deiconify()
        self.root.deiconify()
        self.root.mainloop()

    def create_gui(self):
        pass
        # wait time
        self.instruction_frame = tk.LabelFrame(self.root, text="Instruction")


        # tk.Label(self.instruction_frame, text="Instruction : ").grid(row=0, column=0)
        self.instruction_byte_1_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_1_sv, justify=tk.CENTER, width=24)
        e.grid(row=0, column=0)
        e.configure(state='readonly')

        self.instruction_byte_2_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_2_sv, justify=tk.CENTER, width=24)
        e.grid(row=0, column=1)
        e.configure(state='readonly')

        self.instruction_byte_3_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_3_sv, justify=tk.CENTER, width=24)
        e.grid(row=0, column=2)
        e.configure(state='readonly')

        self.instruction_byte_4_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_4_sv, justify=tk.CENTER, width=24)
        e.grid(row=0, column=3)
        e.configure(state='readonly')

        self.instruction_byte_1_hex_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_1_hex_sv, justify=tk.CENTER, width=24)
        e.grid(row=1, column=0)
        e.configure(state='readonly')

        self.instruction_byte_2_hex_sv = tk.StringVar()
        e =ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_2_hex_sv, justify=tk.CENTER, width=24)
        e.grid(row=1, column=1)
        e.configure(state='readonly')

        self.instruction_byte_3_hex_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_3_hex_sv, justify=tk.CENTER, width=24)
        e.grid(row=1, column=2)
        e.configure(state='readonly')

        self.instruction_byte_4_hex_sv = tk.StringVar()
        e = ttk.Entry(self.instruction_frame, textvariable=self.instruction_byte_4_hex_sv, justify=tk.CENTER, width=24)
        e.grid(row=1, column=3)
        e.configure(state='readonly')

        tk.Label(self.instruction_frame, text="Type : ").grid(row=3, column=0)
        self.instruction_type_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_type_sv, justify=tk.CENTER, width=24).grid(row=4, column=0)
        tk.Label(self.instruction_frame, text="ALU : ").grid(row=3, column=1)
        self.instruction_alu_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_alu_sv, justify=tk.CENTER, width=24).grid(row=4, column=1)
        tk.Label(self.instruction_frame, text="Dest : ").grid(row=3, column=2)
        self.instruction_dest_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_dest_sv, justify=tk.CENTER, width=24).grid(row=4, column=2)
        tk.Label(self.instruction_frame, text="Jump : ").grid(row=3, column=3)
        self.instruction_jump_sv = tk.StringVar()
        ttk.Entry(self.instruction_frame, textvariable=self.instruction_jump_sv, justify=tk.CENTER, width=24).grid(row=4
                                                                                                                  , column=3)

        self.status_frame = tk.LabelFrame(self.root, text="Current State")


        tk.Label(self.status_frame, text="").grid(row=0, column=0)

        tk.Label(self.status_frame, text="bin").grid(row=0, column=1)
        tk.Label(self.status_frame, text="hex").grid(row=0, column=2)
        tk.Label(self.status_frame, text="dec").grid(row=0, column=3)

        tk.Label(self.status_frame, text="A").grid(row=1, column=0)
        tk.Label(self.status_frame, text="D").grid(row=2, column=0)
        tk.Label(self.status_frame, text="out ALU").grid(row=3, column=0)
        tk.Label(self.status_frame, text="idx ROM").grid(row=4, column=0)

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

        e = ttk.Entry(self.status_frame, textvariable=self.A_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=1, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.A_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=1, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.A_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=1, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.D_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=2, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.D_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=2, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.D_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=2, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.out_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=3, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.out_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=3, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.out_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=3, column=3)

        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=4, column=1)
        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=4, column=2)
        e = ttk.Entry(self.status_frame, textvariable=self.idx_rom_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=4, column=3)


        self.ROM_frame = tk.LabelFrame(self.root, text="ROM")



        # create a treeview with one scrollbars

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        header = ['num', 'binary', 'hex', 'assembler']
        self.tree_ROM = ttk.Treeview(columns=header, show="headings", style="mystyle.Treeview")
        vsb = ttk.Scrollbar(orient="vertical",
                            command=self.tree_ROM.yview)

        self.tree_ROM.grid(column=0, row=0, sticky='nsew', in_=self.ROM_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.ROM_frame)
        self.ROM_frame.grid_columnconfigure(0, weight=1)
        self.ROM_frame.grid_rowconfigure(0, weight=1)

        for col in header:
            self.tree_ROM.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.tree_ROM.column(col,
                width=tkFont.Font().measure(col.title()))

        self.tree_ROM.bind('<<TreeviewSelect>>', self.treeview_instruction_select)

        # Current ROM instruction has a different background
        self.tree_ROM.tag_configure('current_instruction', background='orange')

        self.tick_frame = tk.LabelFrame(self.root, text="Tick")

        ttk.Button(self.tick_frame, text="Next", width=12, command=self.next_tick).grid(row=0, column=0)
        ttk.Button(self.tick_frame, text="Previous", width=12, command=self.previous_tick()).grid(row=0, column=1)

        # Pack frames
        self.tick_frame.pack(side="top", fill="both", expand=True)
        self.ROM_frame.pack(side="top", fill="both", expand=True)
        self.instruction_frame.pack(side="top", fill="both", expand=True)
        self.status_frame.pack(side="top", fill="both", expand=True)

        # self.list_ROM.bind('<<ListboxSelect>>', self.onselect_ROM_list)

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

    def load_ROM(self):
        # Ask for file path
        # self.CPU.ROM.load_machine_code("")
        self.fill_ROM_list(self.CPU.ROM)



    def fill_ROM_list(self, ROM):
        i = 0
        ROM_instructions_list = ROM.get_instructions()
        for instruction in ROM_instructions_list:
            item = [str(i), self.CPU.format_binary_instruction(instruction), self.CPU.format_hex_instruction(instruction), self.CPU.get_assembler_string(instruction)]
            self.tree_ROM.insert('', 'end', values=item)

            #TODO
            # adjust column's width if necessary to fit each value
            # for ix, val in enumerate(item):
            #     col_w = tkFont.Font().measure(val)
            #     if self.tree_ROM.column(item[ix], width=None) < col_w:
            #         self.tree_ROM.column(item[ix], width=col_w)
            i += 1

    def treeview_instruction_select(self, event):
        id_selected_item = self.tree_ROM.focus()
        selected_item = self.tree_ROM.item(id_selected_item)
        instruction_num = selected_item["values"][0]
        instruction_binary = selected_item["values"][1]
        instruction_hex = selected_item["values"][2]
        self.update_instruction(instruction_binary, origin="ROM_list_GUI")




    def next_tick(self):
        self.CPU.tick()
        self.num_current_instruction = self.CPU.ROM.idx
        self.update_state()
        self.update_ROM_list()
        self.update_instruction()


    def previous_tick(self):
        """
        Start from zero
        :return:
        """
        #FIXME
        if self.CPU.ROM.idx != 0:
            self.CPU.go_to_instruction_n(self.CPU.ROM.idx - 1)

    def update_state(self):
        self.A_bin_sv.set(self.CPU.format_binary_instruction(self.CPU.A_reg[0]))
        self.A_hex_sv.set(self.CPU.format_hex_instruction(self.CPU.A_reg[0]))
        self.A_dec_sv.set(str(self.CPU.A_reg[0]))
        self.D_dec_sv.set(str(self.CPU.D_reg[0]))
        self.D_bin_sv.set(self.CPU.format_binary_instruction(self.CPU.D_reg[0]))
        self.D_hex_sv.set(self.CPU.format_hex_instruction(self.CPU.D_reg[0]))
        self.out_dec_sv.set(str(self.CPU.out_ALU[0]))
        self.out_bin_sv.set(self.CPU.format_binary_instruction(self.CPU.out_ALU[0]))
        self.out_hex_sv.set(self.CPU.format_hex_instruction(self.CPU.out_ALU[0]))
        self.idx_rom_bin_sv.set(self.CPU.format_binary_instruction(self.CPU.ROM.idx))
        self.idx_rom_hex_sv.set(self.CPU.format_hex_instruction(self.CPU.ROM.idx))
        self.idx_rom_dec_sv.set(str(self.CPU.ROM.idx))

    def update_instruction(self, instruction="from CPU", origin="from_CPU"):
        if origin == "from_CPU":
            instruction = self.CPU.current_instruction
            instruction_bin = self.CPU.format_binary_instruction(instruction)
            instruction_hex = self.CPU.format_hex_instruction(instruction)
        elif origin == "ROM_list_GUI":
            instruction_wo_space = instruction.replace(" ", "")
            instruction_int = int(instruction_wo_space, 2)
            instruction_bin = instruction
            instruction_hex = self.CPU.format_hex_instruction(instruction_int)


        self.instruction_byte_1_sv.set(instruction_bin[0:4])
        self.instruction_byte_2_sv.set(instruction_bin[5:9])
        self.instruction_byte_3_sv.set(instruction_bin[10:14])
        self.instruction_byte_4_sv.set(instruction_bin[15:19])

        self.instruction_byte_1_hex_sv.set(instruction_hex[0])
        self.instruction_byte_2_hex_sv.set(instruction_hex[1])
        self.instruction_byte_3_hex_sv.set(instruction_hex[2])
        self.instruction_byte_4_hex_sv.set(instruction_hex[3])
        if origin == "from_CPU":
            self.instruction_type_sv.set(self.CPU.instruction_type)
            self.instruction_alu_sv.set(self.CPU.alu_instruction)
            self.instruction_dest_sv.set(self.CPU.dest_instruction)
            self.instruction_jump_sv.set(self.CPU.jump_instruction)
        elif origin == "ROM_list_GUI":
            self.instruction_type_sv.set(self.CPU.get_instruction_type(instruction_int))
            self.instruction_alu_sv.set(self.CPU.get_ALU_operation_type(instruction_int))
            self.instruction_dest_sv.set(self.CPU.get_dest_type(instruction_int))
            self.instruction_jump_sv.set(self.CPU.get_jump_type(instruction_int))


    def update_ROM_list(self):
        # Change background of current instruction
        children = self.tree_ROM.get_children("")
        for child in children:
            selected_item = self.tree_ROM.item(child)
            instruction_num = selected_item["values"][0]
            if instruction_num == self.num_current_instruction:
                self.tree_ROM.item(child, tags="current_instruction")
            else:
                self.tree_ROM.item(child, tags="")
        #TODO changer le tag de l'item correspondant à l'instruction courante.

        # self.tree_ROM.item(iid, tags="")

    def on_quit(self):
        # paramFile = open('param.ini', 'w')
        # paramFile.write(self.saveDir)
        self.root.destroy()
        self.root.quit()
