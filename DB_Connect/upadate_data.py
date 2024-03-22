from DB_Connect.db_sql import DB_Connect

def update_db():
    criar_conexao_db = DB_Connect()
    opcao = int(input('Deseja atualizar qual id? '))
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = int(input('Digite sua idade: '))
    cargo = input('Digite seu cargo: ')
    try:
        sql_update = "UPDATE funcionarios SET nome=%s, email=%s, idade=%s, cargo=%s WHERE id = %s"
        criar_conexao_db.cursor.execute(sql_update, (nome, email, idade, cargo, opcao))
        criar_conexao_db.conecta_db.commit()
        print('Atualizado com sucesso!')

    except Exception as error:
        print(error)
