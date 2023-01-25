# Importando SQL Lite

import sqlite3 as lite

# Criando conexão / caso não existir será criando novo banco de dados

con = lite.connect('livraria.db')

# Verificando o que tem dentro da tabela o resultado é uma lista vazia

cur = con.cursor()
cur.execute("SELECT * FROM Categoria")

print(cur.fetchall())

# Inserindo dados na tabela Categoria

with con:
    cur = con.cursor()
    cur.execute("INSERT INTO Categoria (nome) VALUES('Romance')")
    cur.execute("INSERT INTO Categoria (nome) VALUES('Terror')")
    cur.execute("INSERT INTO Categoria (nome) VALUES('Aventura')")
    cur.execute("INSERT INTO Categoria (nome) VALUES('Comedia')")

# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados inseridos

cur = con.cursor()
cur.execute("SELECT * FROM Categoria")

print(cur.fetchall())

# Inserindo dados na tabela Menbro

# Observe que de um novo jeito aconselhável para programar

# Mais fácil para usar com vários dados usando FOR

valores = ['Pri', 'F', '13545866', 'Sao Paulo-SP']

with con:
    cur = con.cursor()
    query = ("INSERT INTO Membro (nome, genero, tel, endereco) \
        VALUES(?,?,?,?)")
    cur.execute(query, valores)


# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados inseridos

cur = con.cursor()
cur.execute("SELECT * FROM Membro")

print(cur.fetchall())

# Inserindo dados na tabela Livro

valores = ['Racismo Estrutural', 'Silvo Almeida',
           'Pretos', 2, 10, '20/01/2023']

with con:
    cur = con.cursor()
    query = ("INSERT INTO Livro ('titulo', 'autor', 'editora', 'categoria', \
        'copias', 'adicionado_em') VALUES(?, ?, ?, ?, ?, ?)")
    cur.execute(query, valores)


# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados inseridos

cur = con.cursor()
cur.execute("SELECT * FROM Livro")

print(cur.fetchall())

# Inserindo dados na tabela Livros Alugados

valores = [2, 2, '21.01.2023', '0']

with con:
    cur = con.cursor()
    query = ("INSERT INTO Livros_Alugados ( 'id_livro', 'id_membro', \
        'alugado_em', 'data_de_retorno' ) VALUES(?, ?, ?, ?)")
    cur.execute(query, valores)


# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados inseridos

cur = con.cursor()
cur.execute("SELECT * FROM Livros_Alugados")

print(cur.fetchall())

# Atualizando os dados na tabela Livro

valores = ['20/01/2020', 2]

with con:
    cur = con.cursor()
    query = ("UPDATE Livro SET adicionado_em = ? WHERE id = ?")
    cur.execute(query, valores)


# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados alterado

cur = con.cursor()
cur.execute("SELECT * FROM Livro")

print(cur.fetchall())

# Apagar dados na tabela Categoria

valores = [4]

with con:
    cur = con.cursor()
    query = ("DELETE FROM Categoria WHERE id = ?")
    cur.execute(query, valores)


# Obs. com o with não precisa fechar o banco de dados Ex. con.close()

# Verificando os dados alterado

cur = con.cursor()
cur.execute("SELECT * FROM Categoria")

print(cur.fetchall())
