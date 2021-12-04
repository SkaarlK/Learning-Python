#Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584
#funcionários de acordo com os seguintes critérios:
#a) 50% para aqueles que ganham menos do que três salários mínimos;
#b) 20% para aqueles que ganham entre três até dez salários mínimos;
#c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
#d) 10% para os demais funcionários.
#Leia o nome do funcionário, seu salário e o valor do salário mínimo. Calcule o seu
#novo salário reajustado. Escrever o nome do funcionário, o reajuste e seu novo
#salário. Calcule quanto à empresa vai aumentar sua folha de pagamento.
funcionarios = []; salarioMinimo = float(input("Qual o salário mínimo vigente?: R$")); folha = 0
class Funcionario:
	nome = str
	salario = float
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario
	def setAumento(self, valor):
		self.salario += salario * valor
		return salario * valor

for i in range(1, 585):
	nome = str(input("\n[" + str(i) +  "] Qual o nome do funcionário?: "))
	salario = float(input("E o salário dele?: R$"))
	funcionarios.append(Funcionario(nome,salario))

for j in funcionarios:
	aumento = float
	if j.salario < 3 * salarioMinimo:
		aumento = j.setAumento(0.5)
		folha += aumento
	elif j.salario > 3 * salarioMinimo and j.salario <= 10 * salarioMinimo:
		folha += (j.setAumento(0.2))
	elif j.salario > 10 * salarioMinimo and j.salario <= 20 * salarioMinimo:
		aumento = (j.setAumento(0.15))
		folha += aumento
	else:
		aumento = (j.setAumento(0.1))
		folha += aumento
	print("\n" + j.nome + " recebeu um aumento de: R$%.2f" % aumento)
print("\nA folha de pagamento aumentou em: R$%.2f" % folha)