import sqlite3

conexao = sqlite3.connect('Primeiro_projeto') #nome do arquivo que criei no DBeaver
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto)
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')


# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
# cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (1, 'João', 20, 'Engenharia'), (2, 'Maria', 22, 'Medicina'), (3, 'Pedro', 19, 'Administração'), (4, 'Ana', 21, 'Psicologia'), (5, 'Carlos', 23, 'Direito')")


# 3. a) Selecionar todos os registros da tabela "alunos"
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)


# 3. b) Selecionar o nome e a idade dos alunos com mais de 20 anos
# dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20')
# for alunos in dados:
#     print(alunos)


#3. c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
# dados = cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
# for alunos in dados:
#     print(alunos)


# 3. d) Contar o número total de alunos na tabela
# dados = cursor.execute('SELECT COUNT(*) FROM alunos')
# for alunos in dados:
#     print(alunos)

# 4. a) Atualize a idade de um aluno específico na tabela
# dados = cursor.execute('SELECT * FROM alunos')
# cursor.execute('UPDATE alunos SET idade=30 WHERE nome="Ana"')

# Verificação
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

# 4. b) Remova um aluno pelo seu ID.
# dados = cursor.execute('SELECT * FROM alunos')
# cursor.execute('DELETE FROM alunos WHERE id=1')

# Verificação
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

conexao.commit()
conexao.close
