from config import setup_window
from UI import label,create_menu


def main():
    window = setup_window()
    create_menu(window)
    label(window)
    window.mainloop()

if __name__=="__main__":

    main()  