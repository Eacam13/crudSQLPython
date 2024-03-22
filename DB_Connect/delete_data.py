from DB_Connect.db_sql import DB_Connect

def delete_db():
    criar_conexao_db = DB_Connect()
    opcao = int(input('Deseja deletar qual ID: '))
    try:
        sql_select = "DELETE FROM funcionarios WHERE id = %s"
        criar_conexao_db.cursor.execute(sql_select, opcao)
        criar_conexao_db.conecta_db.commit()
        print(f'ID = {opcao}, Deletado com sucesso')

    except Exception as error:
        print(error)
