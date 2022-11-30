
from pymem import *
from pymem.process import *
import keyboard

shortcut = "F1" #Press F1 to write new value
pm = Pymem("smt3hd.exe") #smt3hd.exe is the name of the process for the game

module = module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll



offsets = [0x50, 0x98, 0x1C8, 0x18, 0xB8, 0x28, 0x48]


def getPtrAddr(base, offsets):
    addr = pm.read_longlong(base)
    for offset in offsets:
        if offset != offsets[-1]: #adds offset to base address if it's not the last offset
            addr = pm.read_longlong(addr + offset)
    addr = addr + offsets[-1] #adds last offset
    return addr

while True:
    if keyboard.is_pressed(shortcut): #Press F1 to write new value in this case 9999999
      pm.write_int(getPtrAddr(module + 0x02E99D40, offsets), 9999999)