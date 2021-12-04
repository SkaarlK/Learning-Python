#Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e 
#se ela é homem ou mulher. No final informe total de homens e de mulheres.
pessoas = []; contagem = {"homens": 0, "mulheres": 0}
class Pessoa:
	def __init__(self, nome, sexo):
		self.nome = nome
		self.sexo = sexo
for i in range(56):
	pessoas.append(Pessoa( str(input("Insira o nome da pessoa: ")), str(input("Insira o sexo da pessoa 'F' ou 'M': ")) ))
for j in range(len(pessoas)):
	if pessoas[j].sexo.lower() == 'm':
		contagem["homens"] += 1
	elif pessoas[j].sexo.lower() == 'f':
		contagem["mulheres"] += 1
	else:
		print(pessoas[j].nome + "possuí o sexo inserido errado: '%s' e não será considerado na contagem." % pessoas[j].sexo)
print("No total houveram " + str(contagem["homens"]) + " homem(ns) e " + str(contagem["mulheres"]) + " mulher(es)" )