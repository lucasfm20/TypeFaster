import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Tempo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recorde FLOAT NOT NULL,
    nivel INT NOT NULL,
    data STRING NOT NULL
)
''')


cursor.execute('SELECT COUNT(*) from Tempo')
tempos = cursor.fetchone()
if (tempos[0]==0): 
    
     cursor.execute('''
                           INSERT INTO Tempo(recorde,data,nivel)
                           VALUES(20.00,1800-01-01,1) '''
                           ,)
     conn.commit()

def consultaTab():
    cursor.execute('SELECT * from Tempo')
    tempos = cursor.fetchall()

    for tempo in tempos:
        print(tempo)

def deleteTab():
    cursor.execute('DROP TABLE IF EXISTS Tempo')
    print("Tabela deletada")


def verifNivel():
    cursor.execute('SELECT nivel,recorde from Tempo')
    tempos = cursor.fetchall()
    if (tempos): 
        for tempo in tempos:
            
            return tempo

#verifNivel()

#consultaTab()
#deleteTab()
    




