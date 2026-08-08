# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from tkinter import Frame, Button, Label
from tkinter.ttk import Combobox

def create_menu(root):

    menu_frame = Frame(root, bg="Black")
    menu_frame.pack(padx=200, pady=150)

    def start_new_game():

        menu_frame.pack_forget()
        new_game_frame = Frame(root, bg="Black")
        new_game_frame.pack(padx=200, pady=150)

    button_ng = Button(
        menu_frame,
        text="New game",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=start_new_game,
    )
    button_ng.pack(pady=10, ipadx=100, ipady=10)

    def open_settings():

        menu_frame.pack_forget()
        settings_frame = Frame(root, bg="Black")
        settings_frame.pack(padx=200, pady=150)


        def back():
            settings_frame.destroy()
            menu_frame.pack(padx=200, pady=150)
            #List of permits in progress
        resolutions = ["800x600","1920x1080"]
        resolutions_box = Combobox(settings_frame,values=resolutions,state="readonly")
        resolutions_box.set("800x600")  
        resolutions_box.pack(pady=10, ipadx=50, ipady=5)


        button_back = Button(
            settings_frame,
            text="back",
            width=5,
            bg="black",
            fg="white",
            relief="flat",
            command=back,
        )
        button_back.pack(pady=10, ipadx=100, ipady=10)

    button_settings = Button(
        menu_frame,
        text="Settings",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=open_settings,
    )
    button_settings.pack(pady=10, ipadx=100, ipady=10)

    def open_credits():
        label_credits = Label(
            root,
            text="Autors: Saint_Wolf",
            font=("Times New Roman", 15),
            bg="Black",
            fg="White",
        )
        label_credits.pack(side="top", anchor="n", padx=10, pady=100)

        menu_frame.pack_forget()
        credits_frame = Frame(root, bg="Black")
        credits_frame.pack(padx=200, pady=150)

        def back():
            credits_frame.destroy()
            label_credits.destroy()
            menu_frame.pack(padx=200, pady=150)

        button_back = Button(
            credits_frame,
            text="back",
            width=5,
            bg="black",
            fg="white",
            relief="flat",
            command=back,
        )
        button_back.pack(pady=10, ipadx=100, ipady=55)

    button_credits = Button(
        menu_frame,
        text="Credits",
        width=5,
        bg="black",
        fg="white",
        relief="flat",
        command=open_credits,
    )
    button_credits.pack(pady=10, ipadx=100, ipady=10)

    button_quit = Button(
        menu_frame,
        text="Quit",
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
        text="Version: 0.0.4",
        font=("Times New Roman", 15),
        bg="black",
        fg="white",
    )
    version_label.pack(side="bottom", anchor="sw", padx=10, pady=10)
