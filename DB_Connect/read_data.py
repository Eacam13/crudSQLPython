from DB_Connect.db_sql import DB_Connect

def listar_db():
    criar_conexao_db = DB_Connect()
    try:
        sql_select = "SELECT * FROM funcionarios"
        criar_conexao_db.cursor.execute(sql_select)
        criar_conexao_db.conecta_db.commit()
        database = criar_conexao_db.cursor.fetchall()
        return database

    except Exception as error:
        print(error)
