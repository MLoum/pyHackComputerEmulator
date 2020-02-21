from __future__ import print_function
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, simpledialog
import tkinter.font as tkFont
import os
import threading
import time

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
        self.register_frame = tk.LabelFrame(self.status_frame, text="Register")


        tk.Label(self.register_frame, text="").grid(row=0, column=0)

        tk.Label(self.register_frame, text="bin").grid(row=0, column=1)
        tk.Label(self.register_frame, text="hex").grid(row=0, column=2)
        tk.Label(self.register_frame, text="dec").grid(row=0, column=3)

        tk.Label(self.register_frame, text="A").grid(row=1, column=0)
        tk.Label(self.register_frame, text="D").grid(row=2, column=0)
        tk.Label(self.register_frame, text="out ALU").grid(row=3, column=0)
        tk.Label(self.register_frame, text="idx ROM").grid(row=4, column=0)

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

        e = ttk.Entry(self.register_frame, textvariable=self.A_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=1, column=1)
        e = ttk.Entry(self.register_frame, textvariable=self.A_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=1, column=2)
        e = ttk.Entry(self.register_frame, textvariable=self.A_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=1, column=3)

        e = ttk.Entry(self.register_frame, textvariable=self.D_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=2, column=1)
        e = ttk.Entry(self.register_frame, textvariable=self.D_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=2, column=2)
        e = ttk.Entry(self.register_frame, textvariable=self.D_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=2, column=3)

        e = ttk.Entry(self.register_frame, textvariable=self.out_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=3, column=1)
        e = ttk.Entry(self.register_frame, textvariable=self.out_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=3, column=2)
        e = ttk.Entry(self.register_frame, textvariable=self.out_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=3, column=3)

        e = ttk.Entry(self.register_frame, textvariable=self.idx_rom_bin_sv, justify=tk.CENTER, width=25)
        e.configure(state='readonly')
        e.grid(row=4, column=1)
        e = ttk.Entry(self.register_frame, textvariable=self.idx_rom_hex_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=4, column=2)
        e = ttk.Entry(self.register_frame, textvariable=self.idx_rom_dec_sv, justify=tk.CENTER, width=10)
        e.configure(state='readonly')
        e.grid(row=4, column=3)



        self.RAM_frame = tk.LabelFrame(self.status_frame, text="RAM")

        # create a treeview with one scrollbars

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        header = ['num', 'binary', 'hex', 'dec']
        self.tree_RAM = ttk.Treeview(columns=header, show="headings", style="mystyle.Treeview")
        vsb = ttk.Scrollbar(orient="vertical",
                            command=self.tree_RAM.yview)

        self.tree_RAM.grid(column=0, row=0, sticky='nsew', in_=self.RAM_frame)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.RAM_frame)
        self.RAM_frame.grid_columnconfigure(0, weight=1)
        self.RAM_frame.grid_rowconfigure(0, weight=1)

        for col in header:
            self.tree_RAM.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.tree_RAM.column(col,
                width=tkFont.Font().measure(col.title()))

        # self.tree_RAM.bind('<<TreeviewSelect>>', self.treeview_instruction_select)

        # Current ROM instruction has a different background
        self.tree_RAM.tag_configure('current_address', background='orange')

        self.RAM_frame.pack(side="left", fill="both", expand=True)
        self.register_frame.pack(side="left", fill="both", expand=True)

        self.ROM_frame = tk.LabelFrame(self.root, text="ROM")
        self.ROM_listing = tk.LabelFrame(self.root, text="ROM Listing")
        self.ROM_modif = tk.LabelFrame(self.root, text="ROM edit")

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

        self.tree_ROM.grid(column=0, row=0, sticky='nsew', in_=self.ROM_listing)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.ROM_listing)
        self.ROM_listing.grid_columnconfigure(0, weight=1)
        self.ROM_listing.grid_rowconfigure(0, weight=1)

        for col in header:
            self.tree_ROM.heading(col, text=col.title())
            # adjust the column's width to the header string
            self.tree_ROM.column(col,
                width=tkFont.Font().measure(col.title()))

        self.tree_ROM.bind('<<TreeviewSelect>>', self.treeview_instruction_select)

        # Current ROM instruction has a different background
        self.tree_ROM.tag_configure('current_instruction', background='orange')

        ttk.Button(self.ROM_modif, text="Insert Instruction", width=12, command=self.insert_instruction).grid(row=0, column=0)
        self.cb_before_after_sv = tk.StringVar()
        self.cb_before_after = ttk.Combobox(self.ROM_modif, width=20, justify=tk.CENTER, textvariable=self.cb_before_after_sv,
                          values='', state='readonly')
        # self.cb_before_after.bind('<<ComboboxSelected>>', self.select_IR)
        self.cb_before_after['values'] = ["before", "after"]
        self.cb_before_after.grid(row=0, column=1)
        self.cb_before_after.set("before")
        self.instruction_num_insert_sv = tk.StringVar()
        self.instruction_num_insert_sv.set("1")

        ttk.Entry(self.ROM_modif, textvariable=self.instruction_num_insert_sv, justify=tk.CENTER, width=10).grid(row=0, column=2)


        self.ROM_listing.pack(side="top", fill="both", expand=True)
        self.ROM_modif.pack(side="top", fill="both", expand=True)


        # Navigation
        ############

        self.navigation_frame = tk.LabelFrame(self.root, text="Navigation")
        self.tick_frame = tk.LabelFrame(self.navigation_frame, text="Tick")
        self.clock_frame = tk.LabelFrame(self.navigation_frame, text="Clock")

        ttk.Button(self.tick_frame, text="Next", width=12, command=self.next_tick).grid(row=0, column=0)
        ttk.Button(self.tick_frame, text="Previous", width=12, command=self.previous_tick).grid(row=0, column=1)

        ttk.Button(self.clock_frame, text="Start", width=12, command=self.start_tick).grid(row=0, column=2)
        ttk.Button(self.clock_frame, text="Stop", width=12, command=self.stop_tick).grid(row=0, column=3)
        self.tick_freq_sv = tk.StringVar()
        self.tick_freq_sv.set("1")
        tk.Label(self.clock_frame, text="tick frequency (Hz)").grid(row=0, column=4)
        #TODO callback when changin freq
        ttk.Entry(self.clock_frame, textvariable=self.tick_freq_sv, justify=tk.CENTER, width=10).grid(row=0, column=5)


        self.goto_frame = tk.LabelFrame(self.navigation_frame, text="Go to")
        tk.Label(self.goto_frame, text="instruction num :").grid(row=0, column=0)
        self.instruction_num_sv = tk.StringVar()
        ttk.Entry(self.goto_frame, textvariable=self.instruction_num_sv, justify=tk.CENTER, width=10).grid(row=0, column=1)
        ttk.Button(self.goto_frame, text="goto", width=12, command=self.goto_instruction).grid(row=0, column=2)
        ttk.Button(self.goto_frame, text="restart", width=12, command=self.restart).grid(row=0, column=3)

        self.tick_frame.pack(side="left", fill="both", expand=True)
        self.clock_frame.pack(side="left", fill="both", expand=True)
        self.goto_frame.pack(side="left", fill="both", expand=True)

        #Vram
        self.image_frame = tk.LabelFrame(self.root, text="Image")
        self.image_WIDTH, self.image_HEIGHT = 16, 16
        self.image_dim_mult = 8

        self.image_canvas = tk.Canvas(self.image_frame, width=self.image_WIDTH*self.image_dim_mult, height=self.image_HEIGHT*self.image_dim_mult, bg="#000000")
        self.image_canvas.pack()
        self.img = PhotoImage(width=self.image_WIDTH*self.image_dim_mult, height=self.image_HEIGHT*self.image_dim_mult)
        self.image_canvas.create_image((self.image_WIDTH*self.image_dim_mult / 2, self.image_HEIGHT*self.image_dim_mult / 2), image=self.img, state="normal")

        # for x in range(4 * WIDTH):
        #     y = int(HEIGHT / 2 + HEIGHT / 4 * sin(x / 80.0))
        #     img.put("#ffffff", (x // 4, y))

        self.set_image_from_VRAM()

        # Pack frames
        self.navigation_frame.pack(side="top", fill="both", expand=True)
        self.ROM_frame.pack(side="top", fill="both", expand=True)
        self.instruction_frame.pack(side="top", fill="both", expand=True)
        self.status_frame.pack(side="top", fill="both", expand=True)
        self.image_frame.pack(side="top", fill="both", expand=True)



        self.menu_system = tk.Menu(self.root)

        # FILE#############
        self.menu_file = tk.Menu(self.menu_system, tearoff=0)
        self.menu_file.add_command(label='New / Clear', underline=1, accelerator="Ctrl+n", command=self.clear)
        self.menu_file.add_command(label='import', underline=4, accelerator="Ctrl+o", command=self.import_)
        self.menu_file.add_command(label='export', underline=1, accelerator="Ctrl+e", command=self.export)
        self.menu_file.add_command(label='quit',  command=self.quit)
        self.menu_system.add_cascade(label="File", menu=self.menu_file)
        self.root.config(menu=self.menu_system)


    def goto_instruction(self):
        num_instruction = int(self.instruction_num_sv.get())
        self.CPU.go_to_instruction_n(num_instruction)
        self.update_all()

    def set_image_from_VRAM(self):
        def _from_rgb(rgb):
            """translates an rgb tuple of int to a tkinter friendly color code
            """
            return "#%02x%02x%02x" % rgb

        for x in range(16):
            for y in range(16):
                pix_val = self.CPU.VRAM.get_pixel(x, y)
                for i in range(self.image_dim_mult):
                    for j in range(self.image_dim_mult):
                        self.img.put(_from_rgb((pix_val, pix_val, pix_val)), (x+i, y+j))


    def start_tick(self):
        self.wait_time_s = (1/float(self.tick_freq_sv.get()))
        self.is_ticking = True
        self.thread_tick = threading.Thread(name='CPU_tick', target=self.ticking)
        self.thread_tick.start()

    def ticking(self):
        while self.is_ticking:
            self.next_tick()
            time.sleep(self.wait_time_s)
            pass

    def restart(self):
        self.instruction_num_sv.set("0")
        self.goto_instruction()



    def stop_tick(self):
        self.is_ticking = False
        if self.thread_tick.is_alive():
            self.thread_tick.join(timeout=0.5)
        self.isMonitor = False


    def insert_instruction(self):
        pos = int(self.instruction_num_insert_sv.get())
        mode = self.cb_before_after_sv.get()
        d = insertInstructionDialog(self.root, title="Insert instruction")
        if d.result is not None:
            instruction, type_ = d.result
            self.CPU.ROM.insert_instruction(instruction, type_, mode, pos)
            self.update_ROM(self.CPU.ROM)
            self.update_all()


    def load_ROM(self):
        # Ask for file path
        # self.CPU.ROM.load_machine_code("")
        self.update_ROM(self.CPU.ROM)

    def quit(self):
        result = messagebox.askquestion("Quit ?", "Are You Sure ?", icon='warning')
        if result == 'yes':
            self.on_quit()

    def update_RAM(self, RAM):
        i = 0
        RAM_mem_list = RAM.get_mem()
        self.tree_RAM.delete(*self.tree_RAM.get_children())
        for mem in RAM_mem_list:
            item = [str(i), self.CPU.format_binary_instruction(mem), self.CPU.format_hex_instruction(mem), mem]
            self.tree_RAM.insert('', 'end', values=item)

            #TODO
            # adjust column's width if necessary to fit each value
            # for ix, val in enumerate(item):
            #     col_w = tkFont.Font().measure(val)
            #     if self.tree_ROM.column(item[ix], width=None) < col_w:
            #         self.tree_ROM.column(item[ix], width=col_w)
            i += 1


    def import_(self):
        filePath = filedialog.askopenfilename(title="Open hack computer ROM file")
        if filePath == None or filePath == '':
            return None
        else:
            extension = os.path.splitext(filePath)[1]
            if extension not in (".txt", ".csv", ".bin"):
                messagebox.showwarning("Open file",
                                       "The file has not the correct .txt, .csv, .bin, extension. Aborting")
                return None
            else:
                if extension == ".txt":
                    self.clear()
                    self.CPU.ROM.load_machine_code(filePath, "logisim")
                self.update_ROM(self.CPU.ROM)
                self.update_ROM_list()


                return filePath

    def export(self):
        pass

    def clear(self):
        pass

    def update_ROM(self, ROM):
        i = 0
        self.tree_ROM.delete(*self.tree_ROM.get_children())
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
        self.instruction_num_sv.set(str(instruction_num))
        instruction_binary = selected_item["values"][1]
        instruction_hex = selected_item["values"][2]
        self.update_instruction(instruction_binary, origin="ROM_list_GUI")


    def next_tick(self):
        self.CPU.tick()
        self.num_current_instruction = self.CPU.ROM.idx
        if self.CPU.instruction_type == "V":
            self.set_image_from_VRAM()
        self.update_state()
        self.update_ROM_list()
        self.update_RAM(self.CPU.RAM)
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
            instruction = self.CPU.ROM.idx
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
            if instruction_num == self.CPU.ROM.idx:
                self.tree_ROM.item(child, tags="current_instruction")
            else:
                self.tree_ROM.item(child, tags="")
        #TODO changer le tag de l'item correspondant à l'instruction courante.

        # self.tree_ROM.item(iid, tags="")

    def update_all(self):
        self.update_ROM_list()
        self.update_RAM(self.CPU.RAM)
        self.update_state()
        self.update_instruction()

    def on_quit(self):
        # paramFile = open('param.ini', 'w')
        # paramFile.write(self.saveDir)
        self.root.destroy()
        self.root.quit()


class insertInstructionDialog(simpledialog.Dialog):

    def body(self, master):

        ttk.Label(master, text="Instruction").grid(row=0)
        self.e1 = ttk.Entry(master)
        self.e1.grid(row=0, column=1)
        self.cb_sv = tk.StringVar()
        self.cb_type = ttk.Combobox(master, width=20, justify=tk.CENTER, textvariable=self.cb_sv,
                          values=["hex", "binary", "dec"], state='readonly')
        # self.cb_before_after.bind('<<ComboboxSelected>>', self.select_IR)
        self.cb_type.grid(row=0, column=2)
        self.cb_type.set("hex")


        self.result = None
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.cb_sv.get()
        self.result = first, second