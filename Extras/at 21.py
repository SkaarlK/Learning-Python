#Escrever um algoritmo que leia os dados de N pessoas (nome, sexo, idade e saúde)
#e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os
#totais.
pessoas = []; dados = {'homens': 0, 'mulheres': 0, 'apto': 0, 'inapto': 0}
class Pessoa:
	nome = str
	sexo = str
	idade = int
	saude = str
	def __init__(self, nome, sexo, idade, saude):
		self.nome = nome
		self.sexo = sexo
		self.idade = idade
		self.saude = saude
	def avaliar(self):
		if (self.idade < 18):
			return False
		elif (self.saude.lower() != 'apto'):
			return False
		return True
for i in range(int(input("Quantas pessoas deseja validar?: "))):
	pessoa = Pessoa(str(input("\nInsira o nome: ")), str(input("Insira o sexo: ")), int(input("Insira a idade: ")), str(input("Resultado de aptidão física/mental ('apto'/'inapto'): ")))
	if (pessoa.saude.lower() == 'apto', 'inapto' and pessoa.sexo.lower() == 'm', 'f'):
		pessoas.append(pessoa)
		if pessoa.saude.lower() == 'apto':
			dados['apto'] += 1
		else:
			dados['inapto'] += 1
		if pessoa.sexo.lower() == 'm':
			dados['homens'] += 1
		else:
			dados['mulheres'] += 1
		if (pessoa.avaliar() == True):
			print('\nVocê pode se alistar.')
		else:
			print('\nVocê NÃO pode se alistar.')
print('\nTotal de validados: ' + str(len(pessoas)))
print('Relação Homens/Mulheres: ' + str(dados['homens']) + " / " + str(dados['mulheres']))
print('Relação Aptos/Inaptos: ' + str(dados['apto']) + " / " + str(dados['inapto']))