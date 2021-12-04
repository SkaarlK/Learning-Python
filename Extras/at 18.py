#Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem 
#informando "maior de idade" e "menor de idade" para cada pessoa. Considere a 
#idade a partir de 18 anos como maior de idade.

pessoas = []
for i in range(75):
	pessoas.append(int(input("Insira a idade: ")))
	if pessoas[i] < 18:
		print("Menor de idade.")
	else:
		print("Maior de idade.")