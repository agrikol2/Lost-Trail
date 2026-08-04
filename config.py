# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


from tkinter import Tk,PhotoImage


def setup_window():
    root = Tk()
    root.title("Lost Trail")

    root.geometry("900x650")

    root.minsize(400, 250)

    icon = PhotoImage(
        file="/home/tima/Рабочий стол/Программирование/Python/My game/pictures/@.png"
    )
    root.iconphoto(True, icon)

    root["bg"] = "black"

    return root
