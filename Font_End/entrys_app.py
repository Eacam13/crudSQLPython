import customtkinter
from customtkinter import CTkEntry

def create_entries(master):
    entries = [
        CTkEntry(master=master, width=300)
        for _ in range(4)
    ]

    for i, entry in enumerate(entries):
        entry.place(relx=0.55, rely=0.2 + 0.1 * i, anchor=customtkinter.CENTER)

    return entries
