from jogo import *
import dicionario
import random
import os
clear = lambda: os.system("cls")
aleatorio = random.choice  # atribui módulo
categorias = [aleatorio(dicionario.desenho()), aleatorio(dicionario.lugar()),
              aleatorio(dicionario.marca()), aleatorio(dicionario.cor()),
              aleatorio(dicionario.time()), aleatorio(dicionario.animal()),
              aleatorio(dicionario.carro())]  # Sorteia uma categoria.
novojogo = 1
bestname = ''
melhorscore = 0
while novojogo == 1:  # Menu Principal
    newgame = 1
    inicio()
    print('\n1 - Novo jogo\n2 - Sair')
    novojogo = int(input('Selecione uma opção: '))

    if novojogo == 1:

        vit = der = 0  # Reseta pontos
        nome = input('Nome do jogador: ')  # Nome do jogador
        while newgame == 1:
            erros = 0  # reseta os erros
            # Grava a primeira Palavra
            clear()
            print('Jogo Pronto, vamos começar\n  ')
            print('1 - Digite 1 para categoria aleatória\n2 - Digite 2 para escolher uma categoria')
            modo = int(input('Selecione uma opção : '))

                # Permite o usuário escolher uma categoria.
            if modo == 2:
                print('1 - Animais\n2 - Cores\n3 - Marcas\n4 - Desenhos\n5 - Carros\n6 - Lugares\n7 - Times de Futebol')
                print('\n')
                categ = int(input('Selecione uma opção:  '))
                # Seleciona uma palavra da categoria animais.
                if categ == 1:
                    word = aleatorio(dicionario.animal())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')
                    # Seleciona uma palavra da categoria cores.
                elif categ == 2:
                    word = aleatorio(dicionario.cor())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')

                    # Seleciona uma palavra da categoria Marcas
                elif categ == 3:
                    word = aleatorio(dicionario.marca())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')

                    # Seleciona uma palavra da categoria desenhos
                elif categ == 4:
                    word = aleatorio(dicionario.desenho())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')

                    # Seleciona uma palavra da categoria Carros
                elif categ == 5:
                    word = aleatorio(dicionario.carro())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')

                    # Seleciona uma palavra da categoria lugar
                elif categ == 6:
                    word = aleatorio(dicionario.lugar())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')

                    # Seleciona uma palavra da categoria time
                elif categ == 7:
                    word = aleatorio(dicionario.time())
                    temp = []
                    for letra in word:
                        if letra == ' ':
                            temp.append(' ')
                        else:
                            temp.append('_')
                clear()
                # Sorteia uma categoria.
            elif modo == 1:
                categ = aleatorio(categorias)
                word = categ
                temp = []
                for letra in word:
                    if letra == ' ':
                        temp.append(' ')
                    else:
                        temp.append('_')
                    clear()
            while True:
                print('\n')
                print('Jogador: {} ☼ Vitórias: {} ☼ Derrotas: {} ☼ Partidas: {}'.format(nome, vit, der, vit + der))
                print()
                jogo(erros, nome, vit, der)  # imprime a forca

                # imprime o desafio de advinhação
                print('\n\nTente Adivinhar: ', end='')

                for let in temp:
                    print(let, end=' ')

                print('\n' * 2)

                # Verifica se jogador perdeu
                if erros == 6:
                    der += 1
                    break


                # Verificar se o jogador ganhou
                ganhouJogo = True
                for let in temp:
                    if let == '_':
                        ganhouJogo = False
                if ganhouJogo:
                    clear()
                    vit += 1
                    print('\033[1;35m\nVOCÊ VENCEU!!!\033[m')
                    break

                # captura a letra do usuario
                print('2 - Desistir')
                letraDig = input('Informe uma letra:').upper()
                if letraDig == '2':
                    der += 1
                    break

                # verifica se acertou alguma letra
                errouLetra = True
                for i, let in enumerate(word):
                    if word[i] == letraDig:
                        temp[i] = word[i]
                        errouLetra = False
                if errouLetra:
                    erros = erros + 1
                clear()
            print('\nJogador: {} | Vitórias: {} | Derrotas: {} | Partidas: {}'.format(nome, vit, der, vit + der))
            print('\nDeseja jogar novamente?')
            print('1 - Continuar jogando  2 - Menu')
            newgame = int(input('\nSelecione uma opção: '))
            clear()