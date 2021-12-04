it = (int(input("Insira o número de números que deseja inserir: ")))
for i in range(it):
	num = int(input("\nInsira um número... "))
	if num < 0:
		print("NEGATIVO")
	elif num == 0:
		print("ZERO")
	else:
		print("POSITIVO")