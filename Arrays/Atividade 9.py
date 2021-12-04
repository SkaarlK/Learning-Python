#Modifique o programa 6.23 para pesquisar dois valores. Em vez de apenas p, leia
#outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi
#encontrado primeiro.

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0

while x < len(L):
	for i in L:
		if i == p:
			print("P: %d encontrado primeiro na posição %d da lista: " % (p, x) + str(L))
			exit()
		elif i == v:
			print("V: %d encontrado primeiro na posição %d da lista: " % (v, x) + str(L))
			exit()
	x += 1
print("%d não encontrado na lista: " % p + str(L))