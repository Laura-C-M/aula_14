from time import sleep
jogar = input("Queres jogar ao Quem quer ser milionário? O jogo baseia-se em 12 perguntas cada uma valendo \n"
              "100.000 euros o teu objetivo é chegar ao 1.000.000. Mas se errares perdes todo o valor antes ganho.\n"
              " Responde a cada uma das perguntas com sim ou não")
if jogar == "sim":
    print("Vamos começar!")
else:
    print("Talvez pra a próxima!")
    exit()
dinheiro=0
tempo_pergunta=15
if dinheiro == 1000000:
    print("Já chegaste a 1.000.000 de euros ganhaste!")
    exit()
while tempo_pergunta > 0:
    p1 = str(input("Existem pastéis de nata em Portugal?"))
    if p1 == "sim":
        dinheiro+=100000
        print(f"Acertaste!Tens {dinheiro}€.")
        break
    elif p1 != "sim":
        dinheiro==0
        print(f"Erraste! Ficas com {dinheiro}€.")
        break
while tempo_pergunta > 0:
    p2 = str(input("Lisboa é a capital de Portugal?"))
    if p2== "sim":
        dinheiro+=100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p2 != "sim":
        dinheiro-=dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p3 = str(input("A Ponte 25 de Abril fica em Portugal?"))
    if p3== "sim":
        dinheiro+=100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p3 != "sim":
        dinheiro-=dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p4 = str(input("Portugal faz parte da União Europeia?"))
    if p4 == "sim":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p4 != "sim":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p5 = str(input("O Algarve é uma região no norte de Portugal?"))
    if p5 == "não":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p5 != "não":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p6 = str(input("O rio Tejo passa por Lisboa?"))
    if p6 == "sim":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p6 != "sim":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p7 = str(input("A Torre de Belém está localizada no Porto?"))
    if p7 == "não":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p7 != "não":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p8 = str(input("O rio Zêzere passa por Lisboa?"))
    if p8 == "não":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p8 != "não":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p9 = str(input("O Fado é um estilo de música tradicional de Portugal?"))
    if p9 == "sim":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p9 != "sim":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p10 = str(input("Em Portugal falam inglês?"))
    if p10 == "não":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p10 != "não":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p11 = str(input("Portugal é conhecido pela produção de vinho do Porto?"))
    if p11 == "sim":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p11 != "sim":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
while tempo_pergunta > 0:
    p12 = str(input("Portugal tem uma fronteira terrestre com a Espanha?"))
    if p12 == "sim":
        dinheiro += 100000
        print(f"Acertaste!Tens {dinheiro}.")
        break
    elif p12 != "sim":
        dinheiro -= dinheiro
        print(f"Erraste! Ficas com {dinheiro}.")
        break
if dinheiro < 1000000:
    print("Não chegaste a 1 milhão de euros, perdeste")
if dinheiro > 1000000:
    print("Chegaste a 1 milhão de euros, ganhaste!")