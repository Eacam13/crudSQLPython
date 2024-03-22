import customtkinter
from customtkinter import CTkLabel

def labels_read(master):
    label_readDb = CTkLabel(
        master=master,
        text="",
        font=("Arial", 16, "bold"),
        width=350,
        height=170,
        bg_color="#A9A9A9"
    )
    label_readDb.place(relx=0.1, rely=0.7)

    return label_readDb