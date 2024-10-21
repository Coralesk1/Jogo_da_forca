import os
import sys
from random import choice 

def limpar_tela():
    os.system('cls')

def exibir_forca(tentativas):
    estados = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========''', '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========''', '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========''', '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========''', '''
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========''', '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========''', '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========='''
    ]
    print(estados[6 - tentativas])

def startgame():
    lista_de_palavras = ['cachorro', 'computador', 'maracujá', 'torradeira', 'biblioteca']
    palavra_secreta = choice(lista_de_palavras)
    letras_acertadas = ''
    numero_tentativas = 0
    tentativas = 6

    while tentativas > 0:
        limpar_tela()  # Limpa a tela antes de mostrar o estado atual
        exibir_forca(tentativas)  # Exibe o estado da forca
        print(f'Tentativas restantes: {tentativas}')  # Exibe as tentativas restantes
       
        # Exibe o progresso da palavra
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '_'
        
        if palavra_secreta == 'cachorro':
            print("DICA: Animal")
        elif palavra_secreta == 'computador':
            print("DICA: Dispositivo eletrônico")
        elif palavra_secreta == 'maracujá':
            print("DICA: Fruta")
        elif palavra_secreta == 'torradeira':
            print("DICA:  Eletrodoméstico")
        elif palavra_secreta == 'biblioteca':
            print("DICA:  Livros")
        print('Palavra formada:', palavra_formada)
        
        # Verifica se o jogador já ganhou antes de solicitar uma letra
        if palavra_formada == palavra_secreta:
            print('VOCÊ GANHOU!! PARABÉNS!')
            print('A palavra era', palavra_secreta)
            print('Tentativas:', numero_tentativas)
            sair = input("Deseja sair do jogo? [S/N]: ").lower()
            while len(sair) > 1 or not sair.isalpha():  # Verificação da entrada
                sair = input("Entrada inválida. Deseja sair do jogo? [S/N]: ").lower()
            if sair == 's':
                sys.exit(0)
            else:
                return startgame()  # Reinicia o jogo

        # Solicita a letra do usuário
       
        letra_digitada = input('Digite uma letra: ').lower()
        numero_tentativas += 1

        # Verifica se o jogador digitou mais de uma letra
        if len(letra_digitada) > 1 or letra_digitada.isnumeric():
            print('Digite apenas uma letra.')
            input("Pressione Enter para continuar...")
            continue

        # Verifica se a letra está na palavra secreta
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        else:
            tentativas -= 1  # Reduz as tentativas se errar
        
        # Verifica se as tentativas acabaram
        if tentativas == 0:
            limpar_tela()
            exibir_forca(tentativas)
            print("Acabaram as chances!!! A palavra era:", palavra_secreta)
            try:
                sair = input("Deseja sair do jogo? [S/N]: ").lower()
                while len(sair) > 1 or not sair.isalpha():  # Verificação da entrada
                    sair = input("Entrada inválida. Deseja sair do jogo? [S/N]: ").lower()
                while sair not in ['s', 'n']:
                    sair = input("Digite apenas S ou N: ").lower()
            except:
                print('Digite apenas uma letra.')
                input("Pressione Enter para continuar...")
            if sair == 's':
                sys.exit(0)
            elif sair == 'n':
                return startgame()  # Reinicia o jogo
# Inicia o jogo
startgame()
