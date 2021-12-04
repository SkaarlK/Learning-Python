distancia = int(input("Insira a distância a ser percorrida: "))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print("O preço da passagem ficou em: R$" + str(passagem))