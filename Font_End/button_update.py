import customtkinter
from customtkinter import CTkButton

def update_button(master, command):
    button_update = CTkButton(
        master=master,
        text="Atualizar",
        width=80,
        font=("Arial", 16, "bold"),
        command=command,
    )
    button_update.place(relx=0.6, rely=0.7, anchor=customtkinter.CENTER)

    return button_update