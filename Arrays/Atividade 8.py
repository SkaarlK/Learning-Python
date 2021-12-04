#Modifique o programa 6.23 de forma a realizar a mesma tarefa, mas sem utilizar a
#variável achou. Dica: observe a condição de saída do while.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0

while x < len(L):
	if L[x] == p:
		print("%d encontrado na posição %d da lista: " % (p, x) + str(L))
		exit()
	x += 1
print("%d não encontrado na lista: " % p + str(L))
	