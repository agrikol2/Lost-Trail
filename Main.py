from config import setup_window
from UI import label,buttons


def main():
    window = setup_window()
    buttons(window)
    label(window)
    window.mainloop()


if __name__=="__main__":

    main()