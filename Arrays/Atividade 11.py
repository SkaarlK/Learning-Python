#Modifique o programa 6.15 usando for. Explique por que nem todos os while podem
#ser transformados em for.

## Pois o For tem iterações contadas, sendo inicio e fim bem definidos.
## Diferente do while True que vai rodar pra sempre sem um break explicito.

L = []

while True:
	n = int(input("Digite um número (0 para sair): "))
	if n == 0:
		break
	L.append(n)

for i in range(len(L)):
	print(L[i])

