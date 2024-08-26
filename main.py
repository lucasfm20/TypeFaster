import time
import random
import sqlite3
from frase import listaFacil, listaMedio,listaDificil
from datetime import datetime
from banco import cursor, conn, verifNivel


menor= None
menor2 = None
menor3 = None
nivel = 1
dataAtual = datetime.now().strftime('%Y-%m-%d T%H:%M:%S')


def type(nivel):
    global menor, menor2,menor3
    lista = []
    verifica = False
    
    # Carrega a lista de frases de acordo com o nível
    if nivel == 1:
        lista = listaFacil
        menor = verifNivel(1) or 40  
    elif nivel == 2:
        lista = listaMedio
        menor2 = verifNivel(2) or 40 
    else:
        lista = listaDificil
        menor3 = verifNivel(3) or 40

    numAle = random.randint(0, len(lista) - 1)
    
    print(lista[numAle])
    time.sleep(0.5)
    print()
    tempoIni = time.time()
    frase = input("\n")

    tempoFim = time.time()
    if frase == lista[numAle]:
        print("\nAcertou!")
        verifica = True
    else:
        print("\nErrou!")

    tempoFinal = tempoFim - tempoIni

    
    if nivel == 1 and verifica and tempoFinal < menor:
        menor = tempoFinal
        cursor.execute('''
            INSERT INTO Tempo (recorde, data, nivel)
            VALUES (?, ?, ?) 
        ''', (menor, dataAtual, nivel))
        conn.commit()

    
    elif nivel == 2 and verifica and tempoFinal < menor2:
        menor2 = tempoFinal
        cursor.execute('''
            INSERT INTO Tempo (recorde, data, nivel)
            VALUES (?, ?, ?) 
        ''', (menor2, dataAtual, nivel))
        conn.commit()

    elif nivel == 3 and verifica and tempoFinal < menor3:
        menor3 = tempoFinal
        cursor.execute('''
            INSERT INTO Tempo (recorde, data, nivel)
            VALUES (?, ?, ?) 
        ''', (menor3, dataAtual, nivel))
        conn.commit()

    print(f"Levou {tempoFinal:.2f} segundos.")
    time.sleep(1.5)
    print()

    
    if nivel == 1:
        print(f"Seu recorde é {min(menor, verifNivel(1) or 40):.2f} segundos")
    elif nivel == 2:
        print(f"Seu recorde é {min(menor2, verifNivel(2) or 40):.2f} segundos")
    elif nivel == 3:
        print(f"Seu recorde é {min(menor3, verifNivel(3) or 40):.2f} segundos")

def pontua(nivel):
    temp = 1 
    if nivel == 2 :
        temp = 1.5
    elif nivel == 3:
        temp = 2.0
    print()
    print(f"Pontuação < {1*temp:.2f}s = Impossível")
    print(f"Pontuação < {2*temp:.2f}s = Lenda")
    print(f"Pontuação < {3*temp:.2f}s = Ótimo")
    print(f"Pontuação < {4*temp:.2f}s = Bom")
    print(f"Pontuação < {5*temp:.2f}s = Dá pra melhorar")


def niveis():
    global nivel, menor, menor2,menor3

    while True:
        print("\n" + "_"*15)
        print("     Menu\n")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Voltar")
        print("_"*15)
        print()

        escolha = int(input("Digite uma opção:"))

        if escolha == 1:
            nivel = 1
            menuJogo(nivel)

        elif escolha == 2:
            if (verifNivel(1) and verifNivel(1) <= 3.00) or (nivel == 1 and menor <= 3.00):
                nivel = 2
                menuJogo(nivel)
            else:
                print("\nÉ necessário ter um desempenho menor que 3s no nível 1 para avançar de nível!")
                time.sleep(1.0)

        elif escolha == 3:
            if (verifNivel(2) and verifNivel(2) <= 6.00) or (nivel == 2 and menor <= 6.00):
                nivel = 3
                menuJogo(nivel)
            else:
                print("\nÉ necessário ter um desempenho menor que 6s no nível 2 para avançar de nível!")
                time.sleep(1.0)

        elif escolha == 4:
            break

        else:
            print("Digite uma opção válida!")
            time.sleep(0.5)


def menu():
    while True:
        print("\n" + "_"*15)
        print("      Menu\n")
        print("1 - Jogar")
        print("2 - Sair")
        print("_"*15)
        print()

        escolha = int(input("Escolha uma opção:"))

        if escolha == 1:
            niveis()

        elif escolha == 2:
            break

        else:
            print("Digite uma opção válida!")
            time.sleep(0.5)


def menuJogo(nivel):
    while True:
        print("\n" + "_"*15)
        print("     Menu\n")
        print("1 - Iniciar")
        print("2 - Pontuação")
        print("3 - Voltar")
        print("_"*15)
        print()

        escolha = int(input("Digite uma opção:"))

        if escolha == 1:
            type(nivel)

        elif escolha == 2:
            pontua(nivel)

        elif escolha == 3:
            break

        else:
            print("Digite uma opção válida!")
            time.sleep(0.5)


menu()


#Pyinstaller não reconhecido python -m PyInstaller main.py

# executável pyinstaller --onefile  main.py