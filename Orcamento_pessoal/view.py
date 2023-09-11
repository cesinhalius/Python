# importando o SQLite

import sqlite3 as lite

# criando string de conexão com o banco de dados

con = lite.connect('data.db')

# Inserindo categoria

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Category (name) VALUES(?)"
        cur.execute(query,i)

# Inserindo Receita

def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Incoming(category,datetime,price) VALUES(?,?,?,?)"
        cur.execute(query,i)

# Inserindo Gasto

def inserir_gasto(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Outgoing(category,datetime,price) VALUES(?,?,?,?)"
        cur.execute(query,i)

# Funçoes para ver os dados--------------------------------------------

# Ver Receita
 
def ver_receita():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Incoming")
        line = cur.fetchall()
        for l in line:
            lista_itens.append(l)
    
    return lista_itens


def ver_gasto():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Outgoing")
        line = cur.fetchall()
        for l in line:
            lista_itens.append(l)
    
    return lista_itens

