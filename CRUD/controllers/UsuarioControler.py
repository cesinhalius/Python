import services.database as db


def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO  usuario (Nome, Idade, Profissao) 
    VALUES (?,?,?)""", 
    usuario.nome, usuario.idade, usuario.profissao).rowcount
    db.cnxn.commit()
