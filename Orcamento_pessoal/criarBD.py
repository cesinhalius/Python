# importando o SQLite

import sqlite3 as lite

# criando string de conexão com o banco de dados

con = lite.connect('data.db')

# criando tabela de categoria

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Category(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR NOT NULL);')

# criando tabela de receitas

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Incoming(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, category INTEGER NOT NULL, datetime DATE NOT NULL, price DECIMAL NOT NULL, FOREIGN KEY(category) REFERENCES category(id));')

# criando tabela de gastos

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Outgoing(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, category INTEGER NOT NULL, datetime DATE NOT NULL , price DECIMAL NOT NULL, FOREIGN KEY(category) REFERENCES category(id));')
