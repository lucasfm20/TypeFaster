import time
import random
from frase import listaFacil




def type():
    numAle =random.randint(0,len(listaFacil) - 1)
    
    print(listaFacil[numAle])
    time.sleep(0.5)
    print()
    tempoIni =time.time()
    frase = input(f"\n")

    tempoFim =time.time()
    if frase == listaFacil[numAle]:
        print()
        print("acertou")

    else:
        print()
        print("errou")

    tempoFinal =tempoFim-tempoIni

    print(f"Levou {tempoFinal}")
    time.sleep(1.5)

def pontua():
   print()
   print("Pontuação < 1s = Impossível")
   print("Pontuação < 2s = Lenda")
   print("Pontuação < 3s = Ótimo")
   print("Pontuação < 4s = Bom")
   print("Pontuação < 5s = Da pra melhorar")

def menu():
   while True:
    print("")
    print("*"*15)
    print("Menu")
    print("1-Iniciar")
    print("2-Pontuação")
    print("3-Sair")
    print("*"*15)
    print("")

    escolha = int(input("Digite uma opcao:"))

    if escolha == 1:
        type()
    elif escolha == 2:
        pontua()
    elif escolha == 3:
        break
    else:
       print("Informe um número correto")


menu()
