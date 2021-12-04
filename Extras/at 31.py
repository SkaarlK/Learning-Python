#Dados três valores A, B e C, em que A e B são números reais e C é um caractere,
#pede-se para imprimir o resultado da operação de A por B se C for um símbolo de
#operador aritmético; caso contrário deve ser impressa uma mensagem de operador
#não definido. Tratar erro de divisão por zero.

a = float(input("Insira o número A: "))
b = float(input("Insira o número B: "))
c = str(input("Insira o operador C \n+\n-\n*\n/\n-> "))
if (ord(c) != 43 and ord(c) != 45 and ord(c) != 42 and ord(c) != 47):
	print("\nOperador inválido.")
else:
	if(c == '/' and b == 0):
		print("\nNão é possível dividir por 0.")
		exit()
	print("\nResultado da operação é: ")
	if c == '+':
		print(str(a+b))
	elif c == '-':
		print(str(a-b))
	elif c == '*':
		print(str(a*b))
	elif c == '/':
		print(str(a/b))