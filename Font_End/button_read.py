import customtkinter
from customtkinter import CTkButton

def read_button(master, command):
    button_read = CTkButton(
        master=master,
        text="Listar",
        width=80,
        font=("Arial", 16, "bold"),
        command=command,
    )
    button_read.place(relx=0.4, rely=0.7, anchor=customtkinter.CENTER)

    return button_read