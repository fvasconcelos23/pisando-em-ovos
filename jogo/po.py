
import os

dicio = {'Andarilho': 0, 'Armador': 0, 'n1': 0,
         'n2': 0, 'Parmador': 0, 'Pandarilho': 0}
terreno = []
# definir o terreno limpo
# definir a matriz 7x7


def limpar_terreno():
    global terreno
    terreno = []


def criar_terreno():
    for i in range(8):
        if (i == 0):
            terreno.append([0, 1, 2, 3, 4, 5, 6, 7])
        else:
            terreno.append([i] + ['A'] * 7)

# parte de plantar a armadilha


def armar_terreno():

    if dicio['Armador'] == 0:
        print("Precisa definir armador corretamente")

        return

    # print(terreno)
    for i in range(1, 8):
        for linha in terreno:
            print(*linha)
        for l in range(3):
            print("Você pode esconder até 3 ovos podres por linha do terreno")
            n1 = int(input("insira a coluna que você vai armar a armadilha: "))
            terreno[i][n1] = 'O'

    # for linha in terreno:
    # print(*linha)


def subida():
    simbolo = '='
    print()
    for i in range(100):
        print(i, simbolo * i)


def caminhada():

    if dicio['Andarilho'] == 0:
        print("Escolha o Andarilho")

        return
    for i in range(1, 8):
        print("São válidos os espaços: [1, 2, 3, 4, 5, 6, 7]")
        print("Escolha sabiamente um dos espaços válidos")
        n1 = int(input())
        if terreno[i][n1] == 'O':
            print("“Eca! Você pisou em um ovo podre e perdeu")
            dicio['Parmador'] += 1
            definir_menu()
            break
        else:
            pass
        if i == 7:
            print(
                "“Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!!")
            dicio['Pandarilho'] += 1
            definir_menu()
            break


def definir_menu():
    print('''[1] Definir Armador  \n[2] Plantar Armadilhas \n[3] Iniciar o Placar \n[4] Mostrar o Placar \n[0] Finalizar o Jogo \n ''')

# mostrar quem é o armador


def definir_armador():
    print("Selecione um jogador: ")
    opção = int(input())
    if opção > 0 or opção <= 2:
        if opção == 1:
            dicio['Armador'] = 1
            dicio['Andarilho'] = 2
        elif opção == 2:
            dicio['Armador'] = 2
            dicio['Andarilho'] = 1
    print("O armador é: ", dicio['Armador'])
    print("O andarilho é: ", dicio['Andarilho'])


def mostrar_placar():
    if dicio['Armador'] == 1:
        print("Pontuação do Jogador ",
              dicio['Armador'], " : ", dicio['Parmador'])
        print("Pontuação do Jogador ",
              dicio['Andarilho'], " : ", dicio['Pandarilho'])
    else:
        print("Pontuação do Jogador ",
              dicio['Andarilho'], " : ", dicio['Pandarilho'])
        print("Pontuação do Jogador ",
              dicio['Armador'], " : ", dicio['Parmador'])


while True:

    definir_menu()
    opção = int(input())
    if opção > 4 or opção < 0:
        print("Selecione um numero inteiro de 0 a 4")
    else:
        if opção == 0:
            break
        elif opção == 1:
            definir_armador()
        elif opção == 2:
            limpar_terreno()
            criar_terreno()
            armar_terreno()
            escolha = input("Você gostaria de redefinir o  terreno ?")
            if escolha == "sim":
                limpar_terreno()
            elif escolha == "não":
                pass
        elif opção == 3:
            subida()
            caminhada()
        elif opção == 4:
            mostrar_placar()
