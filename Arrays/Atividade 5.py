ultimo = 10
A = list(range(1, ultimo + 1))

while True:
	print("\nExistem %d clientes na fila 1" % len(A))
	print("Fila 1: ", A)
	print("Digite A para realizar o atendimento de um cliente na fila 1.")
	print("Digite F para adicionar um cliente ao fim da fila 1, ")
	print("Ou insira S para sair do programa.")
	operacao = input("Operação (F, A ou S): ").upper()
	operacao = list(operacao)

	while operacao != ['S'] and len(operacao) > 0:
		if 'A' in operacao:
			if len(A) > 0:
				atendido = A.pop(0)
				print("Cliente %d atendido" % atendido)
			else:
				print("Fila vazia! Ninguém para atender.")
			for j in range(len(operacao)):
				if operacao[j] == 'A':
					operacao.remove('A')
					break
		elif "F" in operacao:
			ultimo += 1 #incrementa o ticket do novo cliente
			A.append(ultimo)
			for j in range(len(operacao)):
				if operacao[j] == 'F':
					operacao.remove('F')
					break
		else:
			print("Operação inválida! Digite apenas F, A ou S!")
	if len(operacao) > 0:
		if operacao[0] == "S":
			exit()