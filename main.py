import time
import random
import sqlite3
from frase import listaFacil
from frase import listaMedio
from datetime import datetime
from banco import cursor,conn,verifNivel

menor=100
nivel =1
dataAtual = datetime.now().strftime('%Y-%m-%d')
niveVerificado =verifNivel()



def type(nivel):
    global menor,niveVerificado
    lista = []
    verifica = False
    
    if nivel==1:
        lista=listaFacil
    else:
        lista=listaMedio

    numAle =random.randint(0, len(lista) - 1)
    
    print(lista[numAle])
    time.sleep(0.5)
    print()
    tempoIni =time.time()
    frase = input(f"\n")

    tempoFim =time.time()
    if frase == lista[numAle]:
        print()
        print("acertou!")
        verifica =True

    else:
        print()
        print("errou!")

    tempoFinal =tempoFim-tempoIni


    if tempoFinal<menor and verifica == True and niveVerificado[0] == nivel :
       menor=tempoFinal

       cursor.execute('''
                      INSERT INTO Tempo(recorde,data,nivel)
                      VALUES(?,?,?) '''
                      ,(menor,dataAtual,nivel))
       conn.commit()
       
       

    print(f"Levou {tempoFinal:.2f}")
    time.sleep(1.5)
    print()
    print(f"Seu record é {menor:.2f}")



def pontua(nivel):
   if nivel ==1:
       temp=1
   else:
       temp=1.5

   print()
   print(f"Pontuação < {1*temp}s = Impossível")
   print(f"Pontuação < {2*temp}s = Lenda")
   print(f"Pontuação < {3*temp}s = Ótimo")
   print(f"Pontuação < {4*temp}s = Bom")
   print(f"Pontuação < {5*temp}s = Da pra melhorar")

def nivel():
    while True:
        global nivel,menor

        print("")
        print("_"*15)
        print("     Menu\n")
        print("1-Fácil")
        print("2-Médio")
        print("3-Voltar")
        print("_"*15)
        print("")

        escolha = int(input("Digite uma opcao:"))

        if escolha == 1:
            nivel = 1
            menuJogo(nivel)
        elif escolha == 2:
             
            if niveVerificado[0]<2 and menor<=5.00:
                nivel = 2
                menuJogo(nivel)
            else:
                print("\nÉ necessário ter um desempenho menor que 3s para avançar de nível!")
                time.sleep(1.0)
        elif escolha == 3:
            break
        else:
            print("Digite uma opcao valida!")
            time.sleep(0.5)
   
def menu():
   while True:
    print("")
    print("_"*15)
    print("      Menu\n")
    print("1-Jogar")
    print("2-Sair")
    print("_"*15)
    print("")
    
    escolha = int(input("Escolha uma opcao:"))

    if escolha == 1:
       nivel()
    
    elif escolha == 2:
       break

    else:
       print("Digite uma opcao valida!")
       time.sleep(0.5)

def menuJogo(nivel):

    while True:
        print("")
        print("_"*15)
        print("     Menu\n")
        print("1-Iniciar")
        print("2-Pontuação")
        print("3-Voltar")
        print("_"*15)
        print("")

        escolha = int(input("Digite uma opcao:"))

        if escolha == 1:
            type(nivel)
        elif escolha == 2:
            pontua(nivel)
        elif escolha == 3:
            break
        else:
            print("Digite uma opcao valida!")
            time.sleep(0.5)

menu()

#Pyinstaller não reconhecido python -m PyInstaller main.py

# executável pyinstaller --onefile  main.py