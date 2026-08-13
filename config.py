# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from pathlib import Path
from tkinter import Tk, PhotoImage


def setup_window():
    root = Tk()
    root.title("Lost Trail")

    root.geometry("800x600")

    root.minsize(800, 600)



    project_path = Path(__file__).resolve().parent
    icon_path = project_path / "pictures" / "@.png"
    icon = PhotoImage(file=icon_path)
    root.iconphoto(True, icon)


    root["bg"] = "black"

    return root
