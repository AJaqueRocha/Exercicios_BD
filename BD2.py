import sqlite3

conexao = sqlite3.connect('Segundo_projeto') #nome do arquivo que criei no DBeaver
cursor = conexao.cursor()

#5. Criar uma Tabela e Inserir Dados: Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

# cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES(1, 'João', 25, 1000.50), (2, 'Maria', 30, 500.75)")

# cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES(3, 'Ana', 35, 2000.25), (4, 'Pedro', 28, 1500.50), (5, 'Mariana', 32, 3000.75), (6, 'Carlos', 40, 2500.80), (7, 'Julia', 27, 1800.90), (8, 'Lucas', 29, 1200.60), (9, 'Isabela', 33, 3500.70), (10, 'Rafael', 31, 2200.40)")

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
# for clientes in dados:
#     print(clientes)

# b) Calcule o saldo médio dos clientes.
# dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
# for clientes in dados:
#     print(clientes)
    
# c) Encontre o cliente com o saldo máximo.
# dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1;')
# for clientes in dados:
#     print(clientes)

# d) Conte quantos clientes têm saldo acima de 1000.
# dados = cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo > 1000;')
# for clientes in dados:
#     print(clientes)

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
# dados = cursor.execute('SELECT * FROM clientes')
# cursor.execute('UPDATE clientes SET saldo = 900.00 WHERE id = 5;')

# b) Remova um cliente pelo seu ID.
# dados = cursor.execute('SELECT * FROM clientes')
# cursor.execute('DELETE FROM clientes WHERE id=3')


# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.
# cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# cursor.execute("INSERT INTO compras (id, cliente_id, produto, valor) VALUES(1, 2, 'Arroz', 5.99), (2, 4, 'Feijão', 3.50), (3, 3, 'Macarrão', 2.75), (4, 1, 'Leite', 4.25), (5, 6, 'Ovos', 6.00), (6, 10, 'Café', 8.99), (7, 9, 'Açúcar', 3.75), (8, 5, 'Óleo', 9.50), (9, 8, 'Sal', 2.25), (10, 7, 'Farinha', 4.99);")

# dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
# for clientes in dados:
#     print(clientes)

conexao.commit()
conexao.close