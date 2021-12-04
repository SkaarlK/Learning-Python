velocidade = int(input("A que velocidade você estava?: "))
if velocidade > 80:
    velocidade -= 80
    velocidade *= 5
    print("Você ultrapassou o limite de velocidade e foi multado em: R$" + str(velocidade))
elif velocidade <= 80:
    print("Tudo certo.")
