import asyncio
import subprocess
import time
from tkinter import *
import pyautogui


def helpful(tt, ds):
    root = Tk()
    x = -2
    y = -2
    if ds == 1:
        abc = PhotoImage(file='data\\img\\figures1.png')
        Label(root, image=abc).pack()
    elif ds == 2:
        abc = PhotoImage(file='data\\img\\mas.png')
        Label(root, image=abc).pack()
    elif ds == 3:
        abc = PhotoImage(file='data\\img\\blur.png')
        Label(root, image=abc).pack()

    root.overrideredirect(True)
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.geometry(f'+{x}+{y}')
    root.update()
    time.sleep(tt)
    root.destroy()
    root.mainloop()


def restart():
    subprocess.run(["data\\bats\\rs.bat"])


def call_bsod():
    subprocess.run(["data\\bats\\BSoD.bat"])


def undo_restart():
    subprocess.run(["data\\bats\\usr.bat"])


def close_ap():
    pyautogui.hotkey('alt', 'f4')


def run_installer():
    subprocess.run(["..\\upd\\upd.exe"])
