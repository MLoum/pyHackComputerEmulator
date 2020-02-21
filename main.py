from GUI import HackComputerGUI
from CPU import CPU
from ROM import ROM
from RAM import RAM
from VRAM import VRAM


if __name__ == "__main__":

    #def __init__(self, ROM, RAM, is_print_state=False, log_path="log.txt"):
    cpu = CPU(ROM(), RAM(), VRAM(), is_print_state=False)
    hack_computer_GUI = HackComputerGUI(cpu)
    hack_computer_GUI.run()