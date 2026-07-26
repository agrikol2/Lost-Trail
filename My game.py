from tkinter import *


counter = 0


def main_config():




    root = Tk()
    root.title("Lost Trail")

    root.geometry("900x650")


    root.minsize(400,250)

    icon = PhotoImage(file ="/home/tima/Рабочий стол/Программирование/Python/My game/pictures/@.png")
    root.iconphoto(True, icon)


    def buttons():

        button_frame = Frame(root, bg="Black")
        button_frame.pack(padx=200,pady=150)  


        
        button_NG = Button(button_frame, text="New game", width=5, bg="black", fg="white",relief="flat")
        button_NG.pack(pady=10, ipadx=100, ipady=10)

        button_settings = Button(button_frame, text="Settings", width=5, bg="black", fg="white",relief="flat")
        button_settings.pack(pady=10, ipadx=100, ipady=10)

        button_credits = Button(button_frame, text="credits", width=5, bg="black", fg="white",relief="flat")
        button_credits.pack(pady=10, ipadx=100, ipady=10)

        button_quit = Button(button_frame,text="quit", width=5, bg="black", fg="white",relief="flat",command=root.destroy)
        button_quit.pack(pady=10, ipadx=100, ipady=10)





    buttons()


    
    root["bg"] = "black"


    label = Label(text=f"Version: 0.0.2",font=("Times New Roman",15),bg="black",fg="white")


    label.pack(expand=True,anchor="sw",padx=10, pady=10)





    root.mainloop()

main_config()