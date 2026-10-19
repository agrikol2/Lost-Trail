# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from config import setup_window
from ui import label, create_menu


def main():
    window = setup_window()
    create_menu(window)
    label(window)
    window.mainloop()


if __name__ == "__main__":

    main()
