from DB_Connect.db_sql import DB_Connect

def cadastro_db(nome, email, idade, cargo):
    criar_conexao_db = DB_Connect()

    try:
        sql_insert = "INSERT INTO funcionarios (nome, email, idade, cargo) VALUES (%s, %s, %s, %s)"
        criar_conexao_db.cursor.execute(sql_insert, (nome, email, idade, cargo))
        criar_conexao_db.conecta_db.commit()

        print('Nome cadastrado no banco!')

    except Exception as error:
        print(error)

