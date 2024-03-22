import customtkinter
from customtkinter import CTkLabel

def create_labels(master):
    label_title = CTkLabel(master=master, text="Cadastro de funcionários",
                           fg_color="transparent", font=("Arial", 18, "bold"))
    label_title.place(relx=0.55, rely=0.1, anchor=customtkinter.CENTER)

    labels = [
        CTkLabel(master=master, text=label_text, fg_color="transparent", font=("Arial", 12, "bold"))
        for label_text in ["Nome", "Email", "Idade", "Cargo"]
    ]

    for i, label in enumerate(labels):
        label.place(relx=0.2, rely=0.2 + 0.1 * i, anchor=customtkinter.CENTER)

    return labels, label_title
