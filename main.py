import customtkinter
import pandas as pd
from CTkTable import *
from io import StringIO
from Font_End.labels_app import create_labels
from Font_End.entrys_app import create_entries
from Font_End.button_app import create_button
from Font_End.button_read import read_button
from DB_Connect.create_data import cadastro_db
from DB_Connect.read_data import listar_db
from DB_Connect.upadate_data import update_db
from DB_Connect.delete_data import delete_db
from Font_End.label_listdb import labels_read
from Font_End.button_update import update_button
from Font_End.button_delete import delete_button


def register_db(entries):

    data = [entry.get() for entry in entries]
    nome, email, idade, cargo = data
    if nome == '' and email == '' and idade == '' and cargo == '':
        return print('Preencha todos os dados!!')
    else:
        cadastro_db(nome, email, idade, cargo)

    for entry in entries:
        entry.delete(0, customtkinter.END)

def read_db(label):
    newapp = customtkinter.CTk()
    newapp.geometry("600x200")
    data_lista = listar_db()
    data_lista = list(data_lista)

    columns =[("ID", "Nome", "Email", "Idade", "Cargo")]

    for index, item in enumerate(data_lista):
        columns.append(item)

    table = CTkTable(newapp, row=len(columns), width=300, height= 20, header_color="green", column=5, values=columns)
    table.pack(expand=True, padx=10, pady=10)

    newapp.mainloop()


if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")
    app = customtkinter.CTk()
    app.geometry("500x400")
    app.resizable(False, False)



    labels = create_labels(app)
    entries = create_entries(app)
    #label_readDb = labels_read(app)

    create_button(app, command=lambda: register_db(entries))
    read_button(app, command=lambda: read_db(labels))
    update_button(app, command=lambda: update_db())
    delete_button(app, command=lambda: delete_db())



    app.mainloop()
