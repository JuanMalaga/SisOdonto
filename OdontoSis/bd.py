import sqlite3

conexion=sqlite3.connect('approved.db')
c=conexion.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT)")
	conexion.commit()

def insertar():
    sql="""
    INSERT INTO usuarios VALUES ('Favio', 'Cuya', 'FCUYA', 'Favio123');
    INSERT INTO usuarios VALUES ('Juan', 'Malaga', 'JMALAGA', 'Juan123');
    INSERT INTO usuarios VALUES ('Romel', 'Watanabe', 'RWATANABE', 'Romel123');
    """
    c.executescript(sql)
    conexion.commit()
   

create_table()
insertar()
c.close()
conexion.close()