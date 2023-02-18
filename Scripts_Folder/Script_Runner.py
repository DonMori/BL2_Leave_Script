import keyboard
import subprocess
import sys

def run_script():
# Put the directory of a folder containing both the scripts here V
    subprocess.run([sys.executable, "C:\\Users\\licho\\Desktop\\Programação\\BL2\\Script.py"])
def leave():
    keyboard.unhook_all()
    print("Script stopped.")
    quit()

keyboard.add_hotkey('F5', run_script)
keyboard.add_hotkey('F6', leave)
keyboard.wait()
