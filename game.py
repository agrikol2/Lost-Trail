# # pylint: disable=missing-module-docstring
# # pylint: disable=missing-function-docstring

from tkinter import Frame, Label




def start_game(root):
    
    graphics_frame = Frame(
        root,
        bg="Black",
        width=800,
        height=600,
    )
    main_frame = Frame(graphics_frame, bg="gray")
    text_frame = Frame(graphics_frame, bg="black")
    actions_frame = Frame(graphics_frame, bg="darkgray")
    
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
        open_label.pack(side="top", anchor="n",pady = 200)
        root.bind("<Key>", lambda event: open_label.destroy())
        root.focus_set()

    ng_label()