# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from tkinter import Frame, Button, Label


def create_menu(root):

    menu_frame = Frame(root, bg="Black")
    menu_frame.pack(padx=200, pady=150)

    def hide():
        menu_frame.pack_forget()

    button_ng = Button(
        menu_frame,
        text="New game",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=hide,
    )
    button_ng.pack(pady=10, ipadx=100, ipady=10)

    button_settings = Button(
        menu_frame,
        text="Settings",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=hide,
    )
    button_settings.pack(pady=10, ipadx=100, ipady=10)

    button_credits = Button(
        menu_frame,
        text="credits",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=hide,
    )
    button_credits.pack(pady=10, ipadx=100, ipady=10)

    button_quit = Button(
        menu_frame,
        text="quit",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=root.destroy,
    )
    button_quit.pack(pady=10, ipadx=100, ipady=10)


def label(root):
    version_label = Label(
        root,
        text="Version: 0.0.2",
        font=("Times New Roman", 15),
        bg="black",
        fg="white",
    )
    version_label.pack(expand=True, anchor="sw", padx=10, pady=10)
