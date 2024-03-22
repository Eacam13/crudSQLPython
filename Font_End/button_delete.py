import customtkinter
from customtkinter import CTkButton

def delete_button(master, command):
    button_delete = CTkButton(
        master=master,
        text="Deletar",
        width=80,
        font=("Arial", 16, "bold"),
        command=command,
    )
    button_delete.place(relx=0.8, rely=0.7, anchor=customtkinter.CENTER)

    return button_delete