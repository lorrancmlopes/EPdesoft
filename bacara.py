import random
#definindo o baralho
baralho52 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#Fichas inicias
fichas = 100
#inicializar banco, jogador e aposta
banco = 0
jogador = 0
somajog = 0
somaban = 0


print("Você possui {0} fichas para apostar." .format(fichas))
aposta = int(input("Quantas fichas quer apostar? "))
#implementando mais barahos
quantosbara = int(input("Deseja jogar com 6 ou 8 baralhos?"))
if quantosbara == 1:
    baralho52 = baralho52
elif quantosbara == 6:
    baralho52 = baralho52*6
elif quantosbara == 8:
    baralho52 = baralho52*8
else:
    print("Não entendi, prosseguiremos com 1 baralho.")
apostado = input("Aposta no banco, no jogador, ou empate?")
#limitando a aposta ao numero de fichas disponiveis
if aposta<= fichas:
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
    if somajog <= 5:
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
        if somajog >= 10:
            somajog -= 10

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
    if somaban <= 5:
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
        if somaban >= 10:
            somaban -= 10

    elif somaban >= 10:
        somaban -= 10

    def resultado (somajogador, somabanco, fic, apost):
        if somajogador == somabanco and apostado == "empate":
            fic += apost*8
            fic = int(fic)
            print("Seu saldo de fichas é:")
            print(fic)
            return "Empate! Você ganhou!"
        elif somajogador == somabanco and apostado != "empate":
            fic -= apost
            fic = int(fic)
            print("Seu saldo de fichas é:")
            print(fic)
            return "Empate! Você perdeu!"
        elif somajogador > somabanco and apostado == "jogador":
            fic += apost
            fic = int(fic)
            print("Seu saldo de fichas é:")
            print(fic)
            return "O jogador venceu! Você ganhou!"
        elif somajogador > somabanco and apostado != "jogador":
            fic -= apost
            fic = int(fic)
            print("Seu saldo de fichas é:")
            print(fic)
            return "O jogador venceu! Você perdeu!"
        elif somabanco > somajogador and apostado == "banco":
            fic += apost*0.95
            fic = int(fic)
            print("Seu saldo de fichas é:")
            print(fic)
            return "O banco venceu! Você ganhou!"
        elif somabanco > somajogador and apostado != "banco":
            fic -= apost
            print("Seu saldo de fichas é:")
            fic = int(fic)
            print(fic)
            return "O banco venceu! Você perdeu!"

    print(resultado(somajog, somaban, fichas, aposta))

else:
    print("Aposta inválida.")




    
