import customtkinter
from customtkinter import CTkButton

def create_button(master, command):
    button = CTkButton(
        master=master,
        text="Cadastrar",
        font=("Arial", 16, "bold"),
        width=80,
        command=command,
    )
    button.place(relx=0.2, rely=0.7, anchor=customtkinter.CENTER)

    return button
