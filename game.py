# # pylint: disable=missing-module-docstring
# # pylint: disable=missing-function-docstring

from tkinter import Frame, Label


def start_game(root):
    graphics_frame = Frame(
        root,
        bg="Black",
        width=1920,
        height=1080,
    )
    

    def load_location(location_name):
        file_path = f"pictures/{location_name}.txt"
        with open(file_path, "r", encoding="utf-8") as file:
            picture = file.read()
        return picture

    def main_frame():
        frame = Frame(
            graphics_frame,
            bg="black",
            width=1500,
            height=800,
            highlightbackground="white",
            highlightthickness=2,
        )
        frame.grid_propagate(False)
        frame.grid(row=0, column=0)
        picture = load_location("tested_loc")
        localtion_label = Label(
            frame, text=picture, font=("Courier New", 16), bg="black", fg="white"
        )
        localtion_label.pack()

        return frame

    def text_frame():
        text_frame = Frame(
            graphics_frame,
            bg="black",
            width=1500,
            height=280,
            highlightbackground="white",
            highlightthickness=2,
        )
        text_frame.grid_propagate(False)
        text_frame.grid(row=1, column=0)
        return text_frame

    def actions_frame():
        actions_frame = Frame(
            graphics_frame,
            bg="black",
            width=420,
            height=1080,
            highlightbackground="white",
            highlightthickness=2,
        )
        actions_frame.grid_propagate(False)
        actions_frame.grid(row=0, column=1, rowspan=2)
        return actions_frame

    def show_frames():
        main_frame()
        text_frame()
        actions_frame()

    graphics_frame.pack(expand=True, fill="both")
    graphics_frame.pack_propagate(False)

    def ng_label():
        open_label = Label(
            graphics_frame,
            text="""
            Это тестовый текст экрана перед игрой. 
            Игра пишется на питоне, одним человеком.
            Начальная часть игры будет представлена для лабораторной работы по предмету:
            Разработка кода информационных систем. Остальная часть будет сделана после. 
            Всем спасибо. Для продолжения нажмите любую кнопку.

            """,
            font=("Times New Roman", 25),
            bg="black",
            fg="white",
        )
        open_label.place(relwidth=1, relheight=1)

        def continue_game(event):
            open_label.destroy()
            root.unpind("<Key>")

        root.bind("<Key>", continue_game)
        root.focus_set()

    show_frames()
    ng_label()
