# EP - Design de Software
# Equipe: Lorran Caetano Machado Lopes & Deus
# Data: 16/10/2020
import random
#definindo o baralho
baralho52 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#Fichas inicias
fichas = [100]
#inicializar banco, jogador e aposta, soma do jogador, soma do banco
banco = 0
jogador = 0
somajog = 0
somaban = 0
#criação da lista de jogador, de apostas e valor apostado
quantosjogadores = ["jogador 1"]
apostas = []
apostado = []

#alterando a inicialização para ver quantos vão jogar
n = int(input("Entre com o numero de jogadore: 1 ou (insira o valor): "))
if n>1:
    i = 2
    while i<=n:
        quantosjogadores.append("jogador {0}".format(i))
        fichas.append(100)
        i += 1
#tentar implementar um loop para jogar até as fichas acabarem:
valido_para_jogar = True
while valido_para_jogar:
     
    #alterando as apostas
    print("Você(s) possui(em) {0} fichas para apostar(em), respectivamente." .format(fichas))
    if n>=1:
        i=1
        while i<=n:
            salvaaposta = int(input("Entre com a aposta do jogador {0}: ".format(i)))
            if salvaaposta>fichas[i-1]: #verificando se a aposta é válida
                while salvaaposta>fichas[i-1]:
                    print("Valor incompatível com o saldo. Tente novamente.")
                    salvaaposta = int(input("Entre com a aposta do jogador {0}: ".format(i)))
            apostas.append(salvaaposta)
            i += 1
    #implementando mais barahos
    quantosbara = int(input("Deseja(am) jogar com 1, 6 ou 8 baralhos?"))
    if quantosbara == 1:
        baralho52 = baralho52
    elif quantosbara == 6:
        baralho52 = baralho52*6
    elif quantosbara == 8:
        baralho52 = baralho52*8
    else:
        print("Não entendi, prosseguiremos com 1 baralho.")

    #Alterando a aposta no banco ou jogador, ou empate
    if n>=1:
        i=1
        while i<=n:
            em_quem = input("Jogador {0}, aposta no banco, no jogador, ou empate?".format(i))
            apostado.append(em_quem)
            i += 1


        print("O jogo começou!")
        #Cartas do jogador

        #Carta 1
        a = random.randint(0,51)
        carta1jog = baralho52[a]
        print("A carta 1 do jogador é {0}." .format(carta1jog))
        if baralho52[a] == 'A':
            valor1jog = 1
        elif baralho52[a] == 10:
            valor1jog = 0
        elif baralho52[a] == 'J':
            valor1jog = 0
        elif baralho52[a] == 'Q':
            valor1jog = 0
        elif baralho52[a] == 'K':
            valor1jog = 0
        else:
            valor1jog = baralho52[a]
        print("O seu valor é {0} ." .format(valor1jog))

        #Carta 2 

        b = random.randint(0,51)
        carta2jog = baralho52[b]
        print("A carta 2 do jogador é {0}." .format(carta2jog))
        if baralho52[b] == 'A':
            valor2jog = 1
        elif baralho52[b] == 10:
            valor2jog = 0
        elif baralho52[b] == 'J':
            valor2jog = 0
        elif baralho52[b] == 'Q':
            valor2jog = 0
        elif baralho52[b] == 'K':
            valor2jog = 0
        else:
            valor2jog = baralho52[b]
        print("O seu valor é {0} ." .format(valor2jog))

        #Carta 3
        somajog = valor1jog + valor2jog
        #criar uma variavel para saber se o jog recebeu uma terceira carta
        recebeu = False
        if somajog <= 5:
            recebeu = True
            c = random.randint(0,51)
            carta3jog = baralho52[c]
            print("A carta 3 do jogador é {0}." .format(carta3jog))
            if baralho52[3] == 'A':
                valor3jog = 1
            elif baralho52[c] == 10:
                valor3jog = 0
            elif baralho52[c] == 'J':
                valor3jog = 0
            elif baralho52[c] == 'Q':
                valor3jog = 0
            elif baralho52[c] == 'K':
                valor3jog = 0
            else:
                valor3jog = baralho52[c]
            print("O seu valor é {0} ." .format(valor3jog))
            somajog = valor1jog + valor2jog + valor3jog
            if somajog >= 20:
                somajog -= 20
            elif somajog >= 10:
                somajog -= 10
        elif somajog >= 20:
            somajog -= 20
        elif somajog >= 10:
            somajog -= 10
        #Cartas do banco

        #Carta 1
        d = random.randint(0,51)
        carta1b = baralho52[d]
        print("A carta 1 do banco é {0}." .format(carta1b))
        if baralho52[d] == 'A':
            valor1b = 1
        elif baralho52[d] == 10:
            valor1b = 0
        elif baralho52[d] == 'J':
            valor1b = 0
        elif baralho52[d] == 'Q':
            valor1b = 0
        elif baralho52[d] == 'K':
            valor1b = 0
        else:
            valor1b = baralho52[d]
        print("O seu valor é {0} ." .format(valor1b))

        #Carta 2 

        e = random.randint(0,51)
        carta2b = baralho52[e]
        print("A carta 2 do banco é {0}." .format(carta2b))
        if baralho52[e] == 'A':
            valor2b = 1
        elif baralho52[e] == 10:
            valor2b = 0
        elif baralho52[e] == 'J':
            valor2b = 0
        elif baralho52[e] == 'Q':
            valor2b = 0
        elif baralho52[e] == 'K':
            valor2b = 0
        else:
            valor2b = baralho52[e]
        print("O seu valor é {0} ." .format(valor2b))

        #Carta 3
        somaban = valor1b + valor2b
        if somaban <= 5 and recebeu == False:
            f = random.randint(0,51)
            carta3b = baralho52[f]
            print("A carta 3 do banco é {0}." .format(carta3b))
            if baralho52[f] == 'A':
                valor3b = 1
            elif baralho52[f] == 10:
                valor3b = 0
            elif baralho52[f] == 'J':
                valor3b = 0
            elif baralho52[f] == 'Q':
                valor3b = 0
            elif baralho52[f] == 'K':
                valor3b = 0
            else:
                valor3b = baralho52[f]
            print("O seu valor é {0} ." .format(valor3b))
            somaban = valor1b + valor2b + valor3b
            if somaban >= 20:
                somaban -= 20
            elif somaban >= 10:
                somaban -= 10
        elif  recebeu == True and somaban <= 5:
            if somaban == 0 or somaban == 1 or somaban == 2:
                if valor3jog == 0 or valor3jog == 1 or valor3jog == 2 or valor3jog == 3 or valor3jog == 4 or valor3jog == 5 or valor3jog == 6 or valor3jog == 7 or valor3jog == 8 or valor3jog == 9:
                    #REGRAS PADRÃO DE VALOR DE CARTA
                    f = random.randint(0,51)
                    carta3b = baralho52[f]
                    print("A carta 3 do banco é {0}." .format(carta3b))
                    if baralho52[f] == 'A':
                        valor3b = 1
                    elif baralho52[f] == 10:
                        valor3b = 0
                    elif baralho52[f] == 'J':
                        valor3b = 0
                    elif baralho52[f] == 'Q':
                        valor3b = 0
                    elif baralho52[f] == 'K':
                        valor3b = 0
                    else:
                        valor3b = baralho52[f]
                    print("O seu valor é {0} ." .format(valor3b))
                    somaban = valor1b + valor2b + valor3b
                    if somaban >= 20:
                        somaban -= 20
                    elif somaban >= 10:
                        somaban -= 10
        elif somaban == 3:
                if valor3jog == 0 or valor3jog == 1 or valor3jog == 2 or valor3jog == 3 or valor3jog == 4 or valor3jog == 5 or valor3jog == 6 or valor3jog == 7 or valor3jog == 9:
                    #REGRAS PADRÃO DE VALOR DE CARTA
                    f = random.randint(0,51)
                    carta3b = baralho52[f]
                    print("A carta 3 do banco é {0}." .format(carta3b))
                    if baralho52[f] == 'A':
                        valor3b = 1
                    elif baralho52[f] == 10:
                        valor3b = 0
                    elif baralho52[f] == 'J':
                        valor3b = 0
                    elif baralho52[f] == 'Q':
                        valor3b = 0
                    elif baralho52[f] == 'K':
                        valor3b = 0
                    else:
                        valor3b = baralho52[f]
                    print("O seu valor é {0} ." .format(valor3b))
                    somaban = valor1b + valor2b + valor3b
                    if somaban >= 20:
                        somaban -= 20
                    elif somaban >= 10:
                        somaban -= 10
        elif somaban == 4:
                if valor3jog == 2 or valor3jog == 3 or valor3jog == 4 or valor3jog == 5 or valor3jog == 6 or valor3jog == 7:
                    #REGRAS PADRÃO DE VALOR DE CARTA
                    f = random.randint(0,51)
                    carta3b = baralho52[f]
                    print("A carta 3 do banco é {0}." .format(carta3b))
                    if baralho52[f] == 'A':
                        valor3b = 1
                    elif baralho52[f] == 10:
                        valor3b = 0
                    elif baralho52[f] == 'J':
                        valor3b = 0
                    elif baralho52[f] == 'Q':
                        valor3b = 0
                    elif baralho52[f] == 'K':
                        valor3b = 0
                    else:
                        valor3b = baralho52[f]
                    print("O seu valor é {0} ." .format(valor3b))
                    somaban = valor1b + valor2b + valor3b
                    if somaban >= 20:
                        somaban -= 20
                    elif somaban >= 10:
                        somaban -= 10
        elif somaban == 5:
                if valor3jog == 4 or valor3jog == 5 or valor3jog == 6 or valor3jog == 7:
                    #REGRAS PADRÃO DE VALOR DE CARTA
                    f = random.randint(0,51)
                    carta3b = baralho52[f]
                    print("A carta 3 do banco é {0}." .format(carta3b))
                    if baralho52[f] == 'A':
                        valor3b = 1
                    elif baralho52[f] == 10:
                        valor3b = 0
                    elif baralho52[f] == 'J':
                        valor3b = 0
                    elif baralho52[f] == 'Q':
                        valor3b = 0
                    elif baralho52[f] == 'K':
                        valor3b = 0
                    else:
                        valor3b = baralho52[f]
                    print("O seu valor é {0} ." .format(valor3b))
                    somaban = valor1b + valor2b + valor3b
                    if somaban >= 20:
                        somaban -= 20
                    elif somaban >= 10:
                        somaban -= 10
        elif somaban >= 20:
            somaban -= 20
        elif somaban >= 10:
            somaban -= 10
        #resultado da partida
        contador = 0
        while contador<n:
            if somajog == somaban and apostado[contador] == "empate":
                fichas[contador] += apostas[contador]*8
                #comissão
                if quantosbara == 1:
                    fichas[contador] -= apostas[contador]*0.1575
                elif quantosbara == 6:
                    fichas[contador] -= apostas[contador]*0.1444
                elif quantosbara == 8:
                    fichas[contador] -= apostas[contador]*0.1436
                else:
                    fichas[contador] -= apostas[contador]*0.1575 #o jogo escolhe 1 aralho caso a pessoa entrar com um num diferente das opções
                fichas[contador] = int(fichas[contador])
                print("Seu saldo de fichas é:")
                print(fichas[contador])
                print( "Empate! Você ganhou, jogador {0}!".format(contador+1))
            elif somajog == somaban and apostado[contador] != "empate":
                fichas[contador] -= apostas[contador]
                fichas[contador] = int(fichas[contador])
                print("Seu saldo de fichas é:")
                print(fichas[contador])
                print( "Empate! Você perdeu, jogador {0}!".format(contador+1))
            elif somajog > somaban and apostado[contador] == "jogador":
                fichas[contador] += apostas[contador]
                #comissão
                if quantosbara == 1:
                    fichas[contador] -= apostas[contador]*0.0129
                elif quantosbara == 6:
                    fichas[contador] -= apostas[contador]*0.0124
                elif quantosbara == 8:
                    fichas[contador] -= apostas[contador]*0.0124
                else:
                    fichas[contador] -= apostas[contador]*0.0129 #o jogo escolhe 1 aralho caso a pessoa entrar com um num diferente das opções
                fichas[contador] = int(fichas[contador])
                print("Seu saldo de fichas é:")
                print(fichas[contador])
                print( "O jogador venceu! Você ganhou, jogador {0}!".format(contador+1))
            elif somajog > somaban and apostado[contador] != "jogador":
                fichas[contador] -= apostas[contador]
                fichas[contador] = int(fichas[contador])
                print("Seu saldo de fichas é:")
                print(fichas[contador])
                print( "O jogador venceu! Você perdeu, jogador {0}!".format(contador+1))
            elif somaban > somajog and apostado[contador] == "banco":
                fichas[contador] += apostas[contador]*0.95
                #comissão
                if quantosbara == 1:
                    fichas[contador] -= apostas[contador]*0.0101
                elif quantosbara == 6:
                    fichas[contador] -= apostas[contador]*0.0106
                elif quantosbara == 8:
                    fichas[contador] -= apostas[contador]*0.0106
                else:
                    fichas[contador] -= apostas[contador]*0.0101 #o jogo escolhe 1 aralho caso a pessoa entrar com um num diferente das opções
                fichas[contador] = int(fichas[contador])
                print("Seu saldo de fichas é:")
                print(fichas[contador])
                print( "O banco venceu! Você ganhou, jogador {0}!".format(contador+1))
            elif somaban > somajog and apostado[contador] != "banco":
                fichas[contador] -= apostas[contador]
                print("Seu saldo de fichas é:")
                fichas[contador] = int(fichas[contador])
                print(fichas[contador])
                print( "O banco venceu! Você perdeu, jogador {0}!".format(contador+1))
            contador += 1
    #verifica se alguem zerou as fichas
    if 0 in fichas:
            valido_para_jogar = False
    percorrer = 0
    while percorrer<len(fichas):
        if fichas[percorrer] <= 0:
            fichas[percorrer] = 0
            valido_para_jogar = False
            break
        percorrer += 1
    #pergunta se quer continuar jogando ou não:
    if valido_para_jogar != False:
        continuar = input("Continuar o jogo? (sim ou não)")
        if continuar == "não":
            valido_para_jogar = False




    
