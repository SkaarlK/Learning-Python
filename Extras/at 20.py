#calcule e exiba o valor do desconto e a ser pago pelo cliente.
#  Até 2000 - 12%
# acima de 2000 - 7%. O sistema
#deverá perguntar se deseja continuar calculando desconto até que a resposta seja:
#\u201c(N) Não\u201d . Informar total de carros com ano até 2000 e total geral.
juros = float; count = {'at':0, 'ac':0}; valorCarro = 0; valorDesconto = 0; valorTotal = 0;
while True:
	escolha = input("\n'n': Sair \nInsira o ano do carro: ")
	if escolha.lower() == 'n':
		print("Quantia de carros até 2000 foi de: %d" % count['at'])
		print("E o total geral: %d" % (count['at'] + count['ac']))
		exit()
	else:
		valorCarro = float(input("\nqual o valor do carro?: "))
		if int(escolha) > 2000:
			juros = 7/100
			count['ac'] += 1
		else:
			juros = 12/100
			count['at'] += 1
		valorDesconto += valorCarro * juros
		valorTotal = valorCarro - valorDesconto
	print("\nVocê recebeu um desconto de: " + str(valorDesconto))
	print("Totalizando: " + str(valorTotal))